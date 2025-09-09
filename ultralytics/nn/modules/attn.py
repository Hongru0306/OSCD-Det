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



class PAP(nn.Module):
    # PAP attn
    # Relevant source will be released upon paper acceptance
    def __init__(self, channel=256):
        super().__init__()
        
        
    def forward(self, x):
        
        
        return x