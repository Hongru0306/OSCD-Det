# OSCD
Official implementation of our paper.


## 1. Proposed Modules
- The implementation of the proposed modules is in [`modules.py`](./modules.py).  
- Model configurations are located in the [`configs/`](./configs/) directory.

## 2. Data and Pretrained Weights
Relevant datasets and pretrained model checkpoints can be accessed from our [Google Drive](./) *(link to be updated after acceptance)*.

## 3. Implement
### 3.1 Environment Setup
```
pip install -r requirements.txt
```

### 3.2 Train
```
python train.py --epoch 400 --batch 16
```

### 3.3 Val
```
python val.py
```
### 3.4 System
```
python system.py --source 'stream' --strain True --save './results'
```

# Note
All relevant source will be released after acceptance.
