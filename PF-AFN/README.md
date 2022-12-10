# Parser-Free Virtual Try-on via Distilling Appearance Flows, CVPR 2021
Official code for CVPR 2021 paper 'Parser-Free Virtual Try-on via Distilling Appearance Flows'


**The training code has been released.**

![image](https://github.com/geyuying/PF-AFN/blob/main/show/compare_both.jpg?raw=true)

[[Paper]](https://openaccess.thecvf.com/content/CVPR2021/papers/Ge_Parser-Free_Virtual_Try-On_via_Distilling_Appearance_Flows_CVPR_2021_paper.pdf)       [[Supplementary Material]](https://github.com/geyuying/PF-AFN/blob/main/PFAFN_supp.pdf)

[[Checkpoints for Test]](https://drive.google.com/file/d/1_a0AiN8Y_d_9TNDhHIcRlERz3zptyYWV/view?usp=sharing)

[[Training_Data]](https://drive.google.com/file/d/1Uc0DTTkSfCPXDhd4CMx2TQlzlC6bDolK/view?usp=sharing)
[[Test_Data]](https://drive.google.com/file/d/1Y7uV0gomwWyxCvvH8TIbY7D9cTAUy6om/view?usp=sharing)

[[VGG_Model]](https://drive.google.com/file/d/1Mw24L52FfOT9xXm3I1GL8btn7vttsHd9/view?usp=sharing)

## Our Environment
check VTON.yml for installed module.

RTX 2080 Ti GPU for test

## Run the demo
1. cd PF-AFN_test
2. First, you need to download the checkpoints from [checkpoints](https://drive.google.com/file/d/1_a0AiN8Y_d_9TNDhHIcRlERz3zptyYWV/view?usp=sharing) and put the folder "PFAFN" under the folder "checkpoints". The folder "checkpoints/PFAFN" shold contain "warp_model_final.pth" and "gen_model_final.pth". 
3. The "dataset" folder contains the demo images for test, where the "test_img" folder contains the person images, the "test_clothes" folder contains the clothes images, and the "test_edge" folder contains edges extracted from the clothes images with the built-in function in python (We saved the extracted edges from the clothes images for convenience). 'demo.txt' records the test pairs. 
4. During test, a person image, a clothes image and its extracted edge are fed into the network to generate the try-on image. **No human parsing results or human pose estimation results are needed for test.**
5. To test with the saved model, run **test.sh** and the results will be saved in the folder "results".
6. **To reproduce our results from the saved model, your test environment should be the same as our test environment, especifically for the version of cupy.** 


## Citation
If our code is helpful to your work, please cite:
```
@article{ge2021parser,
  title={Parser-Free Virtual Try-on via Distilling Appearance Flows},
  author={Ge, Yuying and Song, Yibing and Zhang, Ruimao and Ge, Chongjian and Liu, Wei and Luo, Ping},
  journal={arXiv preprint arXiv:2103.04559},
  year={2021}
}
```
```
@inproceedings{han2019clothflow,
  title={Clothflow: A flow-based model for clothed person generation},
  author={Han, Xintong and Hu, Xiaojun and Huang, Weilin and Scott, Matthew R},
  booktitle={Proceedings of the IEEE/CVF International Conference on Computer Vision},
  pages={10471--10480},
  year={2019}
}
```
