import torch
from torch import nn, Tensor, LongTensor
from torch.nn import init
import torch.nn.functional as F
import torchvision


import math
import numpy as np
from einops import rearrange
from torch import Tensor
from typing import Tuple, Optional, List
from ..modules.conv import Conv, autopad

__all__ = ['PAP']



import torch
from torch import nn, Tensor, LongTensor
from torch.nn import init
import torch.nn.functional as F
import torchvision


import math
import numpy as np
from einops import rearrange
from torch import Tensor
from typing import Tuple, Optional, List
from ..modules.conv import Conv, autopad

__all__ = ['PAP']


class ABlock(nn.Module):
    def __init__(self, dim):
        super().__init__()
        self.conv0 = nn.Conv2d(dim, dim, 5, padding=2, groups=dim)
        self.conv_spatial = nn.Conv2d(dim, dim, 7, stride=1, padding=9, groups=dim, dilation=3)  # 
        self.conv1 = nn.Conv2d(dim, dim//2, 1)
        self.conv2 = nn.Conv2d(dim, dim//2, 1)
        self.conv_squeeze = nn.Conv2d(2, 2, 7, padding=3)
        self.conv = nn.Conv2d(dim//2, dim, 1)

    def forward(self, x):   
        attn1 = self.conv0(x)
        attn2 = self.conv_spatial(attn1)

        attn1 = self.conv1(attn1)
        attn2 = self.conv2(attn2)
        
        attn = torch.cat([attn1, attn2], dim=1)
        avg_attn = torch.mean(attn, dim=1, keepdim=True)
        max_attn, _ = torch.max(attn, dim=1, keepdim=True)
        agg = torch.cat([avg_attn, max_attn], dim=1)
        sig = self.conv_squeeze(agg).sigmoid()
        attn = attn1 * sig[:,0,:,:].unsqueeze(1) + attn2 * sig[:,1,:,:].unsqueeze(1)
        attn = self.conv(attn)
        return x * attn

class PAP(nn.Module):
    # PAP attn
    def __init__(self, channel=256):
        super().__init__()
        
        min_ch = channel // 2
        self.proj_1 = nn.Conv2d(channel, channel, 1)
        self.activation = nn.GELU()
        assert min_ch >= 8, f'channel must Greater than {16}, but {channel}'
        
        self.convs_lsk = ABlock(dim=min_ch)
        
        self.proj_2 = nn.Conv2d(min_ch, min_ch, 1)
        self.conv_1x1 = Conv(channel, channel, k=1)
        
    def forward(self, x):
        
        x = self.proj_1(x)
        _, c, _, _ = x.size()
        x_cheap, x_group = torch.split(x, [c // 2, c // 2], dim=1)
        shorcut = x_group.clone()
        
        x_group = self.activation(x_group)
        x_group = self.convs_lsk(x_group)
        x_group = self.proj_2(x_group)
        x_group += shorcut
        x = torch.cat([x_cheap, x_group], dim=1)
        
        x = self.conv_1x1(x)
        
        return x
