# DeepLab-V1-PyTorch

Code for ICLR 2015 deeplab-v1 paper ["Semantic Image Segmentation with Deep Convolutional Nets and Fully Connected CRFs"](http://arxiv.org/pdf/1412.7062.pdf), backbone is deeplab-largeFOV.

## Config
- Check seg.yml for conda environment.


```
## Usage
### Train
```
python main.py --type=train
```
### Test
without CRF
```
python main.py --type=test
```

with CRF
```
python main.py --type=test --use_crf
```

### Evaluate
```
python evalate.py
```

## References
1. Liang-Chieh Chen*, George Papandreou*, Iasonas Kokkinos, Kevin Murphy, and Alan L. Yuille. (*equal contribution). Semantic Image Segmentation with Deep Convolutional Nets and Fully Connected CRFs. ICLR,
2015.<br>
[Project](http://liangchiehchen.com/projects/DeepLab.html) /
[Code](https://bitbucket.org/aquariusjay/deeplab-public-ver2) / [arXiv
paper](http://arxiv.org/pdf/1412.7062.pdf)

2. [deeplab-v2-pytorch](https://github.com/kazuto1011/deeplab-pytorch)
