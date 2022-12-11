# CS492_Fall_customVTON
This is a result of Team15's CS492 Final project custom VTON.

![image](https://user-images.githubusercontent.com/71695489/206888247-ae48f9ef-2794-4f85-b37e-0748e5bafa28.png)

<br/>

This project is composed of 2 sub tasks. And we left our results in ```results.zip```

1. People & Clothes Segmentation.

2. Virtual Try-On segmented image and produced virtually tried-on image.

<br/>

## People & Clothes Segmentation.

- official paper: [SEMANTIC IMAGE SEGMENTATION WITH DEEP CONVOLUTIONAL NETS AND FULLY CONNECTED CRFS](https://arxiv.org/pdf/1412.7062.pdf)

- official gitHub: [DeepLab-V1 PyTorch](https://github.com/wangleihitcs/DeepLab-V1-PyTorch)

- installed conda environment yml: [segmentation env yml](https://github.com/KAIST16-Ryu/CS492_Fall_customVTON/blob/master/DeepLab-V1-PyTorch/seg.yml)

- Here below the execution guide for Segmentation

  1. ```python main.py --type=test```
  2. segmentation image results will be saved in ```'./exp/labels/clothes/crop/'```
<br/>

## Virtual Try-On segmented image and produced virtually tried-on image.

- official paper: [Parser-Free Virtual Try-on via Distilling Appearance Flows, CVPR 2021](https://arxiv.org/pdf/2103.04559.pdf)

- official gitHub: [PF-AFN gitHub](https://github.com/geyuying/PF-AFN)

- download pre-trained warp_model: [warp_model](https://drive.google.com/file/d/1kA1lnG1xZLxJk8Qw9vqb-Iomf0H_XDZs/view?usp=share_link)

- download pre-trained gen_model: [gen_model](https://drive.google.com/file/d/1FWMH9RBDZgmnLfqDoYeyAAi-XaNTKkLw/view?usp=share_link)

- installed conda environment yml: [VTON env yml](https://github.com/KAIST16-Ryu/CS492_Fall_customVTON/blob/master/PF-AFN/VTON.yml)

- Here below the execution guide for VTON

  1. cd PF-AFN_test
  2. download "pre-trained warp model" and "pre-trained gen model" in ```/PF-AFN/PF-AFN_test/checkpoints/``` from the above link.
  3. Prepare a dataset for each "Clothes Images", "Clothes Segmentation Map" and "Person Images" in each ```/PF-AFN/PF-AFN_test/dataset/test-clothes```, ```/PF-AFN/PF-AFN_test/dataset/test-edge``` and ```/PF-AFN/PF-AFN_test/dataset/test_img```.
  4. We create "create_demo_text.py" in ```/PF-AFN/PF-AFN_test/dataset/``` and it will produce "demo.txt", which will be used for inference.
  5. Place "demo.txt" in ```/PF-AFN/PF-AFN_test/```
  6. Execute ```$ test.sh``` with individual arguments.
