# Awesome-Inpainting-Tech [![Awesome](https://cdn.rawgit.com/sindresorhus/awesome/d7305f38d29fed78fa85652e3a63e154dd8e8829/media/badge.svg)](https://github.com/sindresorhus/awesome)
A curated list of inpainting papers and resources, inspired by [awesome-computer-vision](https://github.com/jbhuang0604/awesome-computer-vision).


## Contents
 - [Image Inpainting](#image-inpainting)
 - [Video Inpainting](#video-inpainting)
 - [Challenge](#challenge)

![teaser](https://github.com/pathak22/context-encoder/blob/master/images/teaser.jpg "Sample inpainting results on held-out images")


## Image Inpainting 

### Classical methods (Non-learning based)
1. [Image inpainting](https://www.cse.unr.edu/~bebis/CS474/StudentPaperPresentations/imageinpainting.pdf). Bertalmio, M., Sapiro, G., Caselles, V., & Ballester, C. ```In SIGGRAPH 2000```
2. [Simultaneous structure and texture image inpainting](http://www.math.ucla.edu/~lvese/PAPERS/01217265.pdf). Bertalmio, M., Vese, L., Sapiro, G., & Osher, S. ```In TIP 2003```
3. [Region filling and object removal by exemplar-based image inpainting](http://www.irisa.fr/vista/Papers/2004_ip_criminisi.pdf). Criminisi, A., Pérez, P., & Toyama, K. ```In TIP 2004```
4. [Image completion with structure propagation](http://webee.technion.ac.il/cgm/Computer-Graphics-Multimedia/Undergraduate-Projects/2009/ImageCompletion/ImageCompletion_SIGGRAPH05.pdf). Sun, J., Yuan, L., Jia, J., & Shum, H. Y. ```In TOG 2005```
5. [Image completion using planar structure guidance](https://www.microsoft.com/en-us/research/wp-content/uploads/2017/01/structure_completion_small.pdf). Huang, J. B., Kang, S. B., Ahuja, N., & Kopf, J. ```In TOG 2014``` [[code]](https://github.com/jbhuang0604/StructCompletion) [[project]](https://sites.google.com/site/jbhuang0604/publications/struct_completion)
6. [PatchMatch: A randomized correspondence algorithm for structural image editing](https://gfx.cs.princeton.edu/pubs/Barnes_2009_PAR/patchmatch.pdf). Connelly Barnes, Eli Shechtman, Adam Finkelstein, Dan B Goldman. ```In TOG 2009```, [[project]](https://gfx.cs.princeton.edu/pubs/Barnes_2009_PAR/)

### Deep Architectures (Learning Based)
1. [Shepard convolutional neural networks](https://papers.nips.cc/paper/5774-shepard-convolutional-neural-networks.pdf). Ren, J. S., Xu, L., Yan, Q., & Sun, W. ```In NeurIPS 2015``` [[code]](https://github.com/jimmy-ren/vcnn_double-bladed/tree/master/applications/Shepard_CNN)
2. [Context encoders: Feature learning by inpainting](https://arxiv.org/abs/1604.07379). Pathak, D., Krahenbuhl, P., Donahue, J., Darrell, T., & Efros, A. A. ```In CVPR 2016```. [[code]](https://github.com/pathak22/context-encoder)
3. [Globally and locally consistent image completion](http://hi.cs.waseda.ac.jp/~iizuka/projects/completion/data/completion_sig2017.pdf). Iizuka, S., Simo-Serra, E., & Ishikawa, H. (2017). ```In TOG 2017``` [[code]](https://github.com/satoshiiizuka/siggraph2017_inpainting) [[project]](http://hi.cs.waseda.ac.jp/~iizuka/projects/completion/en/)
4. [High-resolution image inpainting using multi-scale neural patch synthesis](https://arxiv.org/abs/1611.09969). Yang, C., Lu, X., Lin, Z., Shechtman, E., Wang, O., & Li, H. ```In CVPR 2017``` [[code]](https://github.com/leehomyc/Faster-High-Res-Neural-Inpainting)
5. [Generative face completion](http://openaccess.thecvf.com/content_cvpr_2017/papers/Li_Generative_Face_Completion_CVPR_2017_paper.pdf). Li, Y., Liu, S., Yang, J., & Yang, M. H. ```In CVPR 2017``` [[code]](https://github.com/Yijunmaverick/GenerativeFaceCompletion)
6. [Semantic image inpainting with deep generative models](http://openaccess.thecvf.com/content_cvpr_2017/papers/Yeh_Semantic_Image_Inpainting_CVPR_2017_paper.pdf). Yeh, R. A., Chen, C., Yian Lim, T., Schwing, A. G., Hasegawa-Johnson, M., & Do, M. N. ```In CVPR 2017``` [[code]](https://github.com/moodoki/semantic_image_inpainting) [[project]](http://www.isle.illinois.edu/~yeh17/projects/semantic_inpaint/index.html)
7. [Generative image inpainting with contextual attention](https://arxiv.org/abs/1801.07892). Yu, J., Lin, Z., Yang, J., Shen, X., Lu, X., & Huang, T. S. ```In CVPR 2018```  [[code]](https://github.com/JiahuiYu/generative_inpainting) [[project]](http://jiahuiyu.com/deepfill/)
8. [Natural and effective obfuscation by head inpainting](http://openaccess.thecvf.com/content_cvpr_2018/papers/Sun_Natural_and_Effective_CVPR_2018_paper.pdf). Sun Qianru et al. ```In CVPR 2018```
9. [Eye in-painting with exemplar generative adversarial networks](http://openaccess.thecvf.com/content_cvpr_2018/papers/Dolhansky_Eye_In-Painting_With_CVPR_2018_paper.pdf). Dolhansky, B., & Canton Ferrer, C. ```In CVPR 2018``` [[project]](https://bdol.github.io/exemplar_gans/) [[code]](https://github.com/bdol/exemplar_gans)
10. [Uv-gan: Adversarial facial uv map completion for pose-invariant face recognition](http://openaccess.thecvf.com/content_cvpr_2018/papers/Deng_UV-GAN_Adversarial_Facial_CVPR_2018_paper.pdf). Deng, J., Cheng, S., Xue, N., Zhou, Y., & Zafeiriou, S. ```In CVPR 2018```
11. [Disentangling Structure and Aesthetics for Style-aware Image Completion](http://openaccess.thecvf.com/content_cvpr_2018/papers/Gilbert_Disentangling_Structure_and_CVPR_2018_paper.pdf). Gilbert, A., Collomosse, J., Jin, H., & Price, B. ```In CVPR 2018```
12. [Image inpainting for irregular holes using partial convolutions](https://arxiv.org/abs/1804.07723). Liu, G., Reda, F. A., Shih, K. J., Wang, T. C., Tao, A., & Catanzaro, B. ```In ECCV 2018``` [[project]](http://masc.cs.gmu.edu/wiki/partialconv)
13. [Contextual-based image inpainting: Infer, match, and translate](https://arxiv.org/abs/1711.08590). Song, Y., Yang, C., Lin, Z., Liu, X., Huang, Q., Li, H., & Jay Kuo, C. C. ```In ECCV 2018```
14. [Shift-net: Image inpainting via deep feature rearrangement](https://arxiv.org/abs/1801.09392v2). Yan, Z., Li, X., Li, M., Zuo, W., & Shan, S. ```In ECCV 2018``` [[code]](https://github.com/Zhaoyi-Yan/Shift-Net)
15. [Image Inpainting via Generative Multi-column Convolutional Neural Networks](https://arxiv.org/abs/1810.08771). Wang, Y., Tao, X., Qi, X., Shen, X., & Jia, J. ```In NeurIPS 2018``` [[code]](https://github.com/shepnerd/inpainting_gmcnn)
16.  [SPG-Net: Segmentation prediction and guidance network for image inpainting](https://arxiv.org/abs/1805.03356). Song, Y., Yang, C., Shen, Y., Wang, P., Huang, Q., & Kuo, C. C. J. ```In BMVC 2018```
17. [Structural inpainting](https://arxiv.org/abs/1803.10348). Vo, H. V., Duong, N. Q., & Pérez, P. ```In MM 2018``` 
18. [Semantic Image Inpainting with Progressive Generative Networks](https://dl.acm.org/citation.cfm?id=3240625). Zhang, H., Hu, Z., Luo, C., Zuo, W., & Wang, M. ```In MM 2018``` [[code]](https://github.com/crashmoon/Progressive-Generative-Networks)
19. [Face Completion with Semantic Knowledge and Collaborative Adversarial Learning](https://arxiv.org/pdf/1812.03252.pdf). Liao, H., Funka-Lea, G., Zheng, Y., Luo, J., & Zhou, S. K. ```In ACCV 2018```
20. [Edge-Aware Context Encoder for Image Inpainting](http://mirlab.org/conference_papers/International_Conference/ICASSP%202018/pdfs/0003156.pdf). Liao, L., Hu, R., Xiao, J., & Wang, Z. ```In ICASPP 2018```
21. [Faceshop: Deep sketch-based face image editing](https://arxiv.org/abs/1804.08972). Portenier, T., Hu, Q., Szabó, A., Bigdeli, S. A., Favaro, P., & Zwicker, M. ```In TOG 2018```
22. [High resolution face completion with multiple controllable attributes via fully end-to-end progressive generative adversarial networks](https://arxiv.org/pdf/1812.01458.pdf). Chen, Z., Nie, S., Wu, T., & Healey, C. G. ```In Arxiv 2018```
23. [On Hallucinating Context and Background Pixels from a Face Mask using Multi-scale GANs](https://arxiv.org/pdf/1811.07104.pdf). Banerjee, S., Scheirer, W. J., Bowyer, K. W., & Flynn, P. J. ```In Arxiv 2018```
24. [Pluralistic Image Completion](https://arxiv.org/abs/1903.04227). Zheng, C., Cham, T. J., & Cai, J. ```In CVPR 2019``` [[code]](https://github.com/lyndonzheng/Pluralistic-Inpainting) [[project]](http://www.chuanxiaz.com/publication/pluralistic/)
25. [Learning Pyramid-Context Encoder Network for High-Quality Image Inpainting](https://arxiv.org/abs/1904.07475). Zeng, Y., Fu, J., Chao, H., & Guo, B. ```In CVPR 2019``` [[code]](https://github.com/researchmm/PEN-Net-for-Inpainting)
26. [Foreground-aware Image Inpainting](https://arxiv.org/abs/1901.05945). Xiong, W., Lin, Z., Yang, J., Lu, X., Barnes, C., & Luo, J. ```In CVPR 2019```
27. [Deep Reinforcement Learning of Volume-guided Progressive View Inpainting for 3D Point Scene Completion from a Single Depth Image](https://arxiv.org/pdf/1903.04019.pdf). Han, X., Zhang, Z., Du, D., Yang, M., Yu, J., Pan, P., ... & Cui, S. ```In CVPR 2019```
28. [PEPSI: Fast Image Inpainting With Parallel Decoding Network. CVPR (pp. 11360-11368)](http://openaccess.thecvf.com/content_CVPR_2019/papers/Sagong_PEPSI__Fast_Image_Inpainting_With_Parallel_Decoding_Network_CVPR_2019_paper.pdf). Sagong, M. C., Shin, Y. G., Kim, S. W., Park, S., & Ko, S. J. ```In CVPR 2019```
29. [Coordinate-Based Texture Inpainting for Pose-Guided Human Image Generation](https://arxiv.org/abs/1811.11459). Grigorev, A., Sevastopolsky, A., Vakhitov, A., & Lempitsky, V. CVPR2019.
30. [Deep Inception Generative Network for Cognitive Image Inpainting](https://arxiv.org/pdf/1812.01458.pdf). Xiao, Q., Li, G., & Chen, Q. ```In Arxiv 2019```
31. [Detecting Overfitting of Deep Generative Networks via Latent Recovery](https://arxiv.org/pdf/1901.03396.pdf). Webster, R., Rabin, J., Simon, L., & Jurie, F. ```In Arxiv 2019```
32. [SC-FEGAN: Face Editing Generative Adversarial Network with User's Sketch and Color](https://arxiv.org/abs/1902.06838). Jo, Y., & Park, J. (2019). ```In Arxiv 2019``` [[code]](https://github.com/JoYoungjoo/SC-FEGAN)
33. [Deep Fusion Network for Image Completion](https://arxiv.org/abs/1904.08060). Hong, X., Xiong, P., Ji, R., & Fan, H. ```In Arxiv 2019``` [[code]](https://github.com/hughplay/DFNet)
34. [PEPSI++: Fast and Lightweight Network for Image Inpainting](https://arxiv.org/pdf/1905.09010.pdf). Shin, Y. G., Sagong, M. C., Yeo, Y. J., Kim, S. W., & Ko, S. J. ```In Arxiv 2019```
35. [Generative Image Inpainting with Submanifold Alignment](https://arxiv.org/abs/1908.00211) Ang Li, Jianzhong Qi, Rui Zhang, Xingjun Ma, Kotagiri Ramamohanarao. ```In IJCAI 2019```
36. [MUSICAL: Multi-Scale Image Contextual Attention Learning for Inpainting](https://www.ijcai.org/proceedings/2019/0520.pdf). Wang, N., Li, J., Zhang, L., & Du, B. ```In IJCAI 2019```
37. [Coarse-to-Fine Image Inpainting via Region-wise Convolutions and Non-Local Correlation](https://www.ijcai.org/proceedings/2019/0433.pdf). Ma, Y., Liu, X., Bai, S., Wang, L., He, D., & Liu, A. ```In IJCAI 2019```
38. [StructureFlow: Image Inpainting via Structure-aware Appearance Flow](https://arxiv.org/abs/1908.03852), Yurui Ren, Xiaoming Yu, Ruonan Zhang, Thomas H. Li, Shan Liu, Ge Li. ```In ICCV 2019``` [[code]](https://github.com/RenYurui/StructureFlow)
39. [Image Inpainting with Learnable Bidirectional Attention Maps](https://arxiv.org/abs/1909.00968), Chaohao Xie, Shaohui Liu, Chao Li, Ming-Ming Cheng, Wangmeng Zuo, Xiao Liu, Shilei Wen, Errui Ding. ```In ICCV 2019``` [[code]](https://github.com/Vious/LBAM_inpainting)
40. [Coherent Semantic Attention for Image Inpainting](https://arxiv.org/abs/1905.12384), Hongyu Liu, Bin Jiang, Yi Xiao, Chao Yang. ```In ICCV 2019``` [[code]](https://github.com/KumapowerLIU/CSA-inpainting)
41. [EdgeConnect: Generative Image Inpainting with Adversarial Edge Learning](http://arxiv.org/abs/1901.00212). Nazeri, K., Ng, E., Joseph, T., Qureshi, F., & Ebrahimi, M. ```In ICCVW 2019``` [[code]](https://github.com/knazeri/edge-connect)
42. [Free-form image inpainting with gated convolution](https://arxiv.org/abs/1806.03589). Yu, J., Lin, Z., Yang, J., Shen, X., Lu, X., & Huang, T. S. ```In ICCV 2019```  [[project]](http://jiahuiyu.com/deepfill2/)
43. [Region Normalization for Image Inpainting](https://arxiv.org/pdf/1911.10375.pdf). Tao et al. ```In AAAI 2020``` [[code]](https://github.com/geekyutao/RN)
44. [Learning to Incorporate Structure Knowledge for Image Inpainting](https://arxiv.org/abs/2002.04170), Yang et al. ```In AAAI 2020``` [[code]](https://github.com/YoungGod/sturcture-inpainting)
45. [Prior Guided GAN Based Semantic Inpainting](http://openaccess.thecvf.com/content_CVPR_2020/html/Lahiri_Prior_Guided_GAN_Based_Semantic_Inpainting_CVPR_2020_paper.html), Lahiri1 et al. ```In CVPR 2020```
46. [UCTGAN: Diverse Image Inpainting based on Unsupervised Cross-Space Translation](http://openaccess.thecvf.com/content_CVPR_2020/html/Zhao_UCTGAN_Diverse_Image_Inpainting_Based_on_Unsupervised_Cross-Space_Translation_CVPR_2020_paper.html), Zhao et al. ```In CVPR 2020```
47. [Recurrent Feature Reasoning for Image Inpainting](http://openaccess.thecvf.com/content_CVPR_2020/html/Li_Recurrent_Feature_Reasoning_for_Image_Inpainting_CVPR_2020_paper.html), Li et al. ```In CVPR 2020``` [[code]](https://github.com/jingyuanli001/)
48. [Contextual Residual Aggregation for Ultra High-Resolution Image Inpainting](http://openaccess.thecvf.com/content_CVPR_2020/html/Yi_Contextual_Residual_Aggregation_for_Ultra_High-Resolution_Image_Inpainting_CVPR_2020_paper.html), Yi et al., ```In CVPR 2020``` [[code]](https://github.com/Ascend-Huawei/Ascend-Canada/tree/master/Models/Research_HiFIll_Model)
49. [3D Photography using Context-aware Layered Depth Inpainting](http://openaccess.thecvf.com/content_CVPR_2020/papers/Shih_3D_Photography_Using_Context-Aware_Layered_Depth_Inpainting_CVPR_2020_paper.pdf), Shih et al. ```In CVPR 2020``` [[demo]](https://shihmengli.github.io/3D-Photo-Inpainting) [[code]](https://github.com/vt-vl-lab/3d-photo-inpainting)
50. [Rethinking Image Inpainting via a Mutual Encoder-Decoder with Feature Equalizations](https://arxiv.org/abs/2007.06929), Liu et al. ```In ECCV 2020``` [[code]](https://github.com/KumapowerLIU/Rethinking-Inpainting-MEDFE)
51. [Guidance and Evaluation: Semantic-Aware Image Inpainting for Mixed Scenes](https://arxiv.org/abs/2003.06877), Liao et al. ```In ECCV 2020``` 
52. [VCNet: A Robust Approach to Blind Image Inpainting](https://arxiv.org/abs/2003.06816), Wang et al. ```In ECCV2020``` [[code]](https://github.com/shepnerd/blindinpainting_vcnet)
53. [High-Resolution Image Inpainting with Iterative Confidence Feedback and Guided Upsampling](https://arxiv.org/abs/2005.11742), Zeng et al. ```In ECCV2020``` [[project]](https://zengxianyu.github.io/iic/)

## Video Inpainting 

### Classical methods (Non-learning based)

1. [Navier-stokes, fluid dynamics, and image and video inpainting](https://www.math.ucla.edu/~bertozzi/papers/cvpr01.pdf). Bertalmio, M., Bertozzi, A. L., & Sapiro, G. ```In CVPR 2001``` (Vol. 1, pp. I-I). IEEE.
2. [Video inpainting of occluding and occluded objects](http://kedarpatwardhan.org/Research/pdfs/VideoInpainting.pdf). Patwardhan, K. A., Sapiro, G., & Bertalmio, M. ```In ICIP 2005``` (Vol. 2, pp. II-69). IEEE.
3. [Full-frame video stabilization with motion inpainting](http://mmlab.ie.cuhk.edu.hk/archive/2006/01634345.pdf). Matsushita, Y., Ofek, E., Ge, W., Tang, X., & Shum, H. Y. ```In TPAMI 2006```, (7), 1150-1163. [[project]](https://docs.opencv.org/master/d5/d50/group__videostab.html)
4. [Video completion by motion field transfer](https://www.cs.cmu.edu/~siratori/pub/CVPR2006shiratori.pdf). Shiratori, T., Matsushita, Y., Tang, X., & Kang, S. B. (2006, June). ```In CVPR 2006``` (Vol. 1, pp. 411-418). [[project]](https://www.cs.cmu.edu/~siratori/MotionFieldTransfer/index.html)
5. [Space-time completion of video](http://www.wisdom.weizmann.ac.il/~vision/VideoCompletion/SpaceTimeCompletion.pdf). Wexler, Y., Shechtman, E., & Irani, M. ```In TPAMI 2007```, (3), 463-476. [[project]](http://www.wisdom.weizmann.ac.il/~vision/VideoCompletion.html)
6. [Video inpainting under constrained camera motion](http://kedarpatwardhan.org/Research/pdfs/kedar_tip07.pdf). Patwardhan, K. A., Sapiro, G., & Bertalmío, M. ```In TIP 2007```, 16(2), 545-553.
7. [How not to be seen—object removal from videos of crowded scenes](https://gvv.mpi-inf.mpg.de/projects/vidinp/granados12_vidinp.pdf). Granados, M., Tompkin, J., Kim, K., Grau, O., Kautz, J., & Theobalt, C. ```In Computer Graphics Forum 2012``` (Vol. 31, No. 2pt1, pp. 219-228). [[project]](https://gvv.mpi-inf.mpg.de/projects/vidinp/)
8. [Background inpainting for videos with dynamic objects and a free-moving camera](https://gvv.mpi-inf.mpg.de/projects/vidbginp/granados12b_vidbginp.pdf). Springer, Berlin, Heidelberg. Granados, M., Kim, K. I., Tompkin, J., Kautz, J., & Theobalt, C. ```In ECCV 2012```. [[project]](https://gvv.mpi-inf.mpg.de/projects/vidbginp/index.html)
9. [Video inpainting of complex scenes](https://perso.telecom-paristech.fr/gousseau/video_inpainting/Video_inpainting_complex_scenes.pdf). Newson, A., Almansa, A., Fradet, M., Gousseau, Y., & Pérez, P. ```In SIAM Journal on Imaging Sciences 2014```, 7(4), 1993-2019. [[project]](https://perso.telecom-paristech.fr/gousseau/video_inpainting/) 
10. [Video inpainting with short-term windows: application to object removal and error concealment](https://hal.inria.fr/hal-01204677/file/Ebdelli_videoInpainting_TIP2015.pdf). Ebdelli, M., Le Meur, O., & Guillemot, C. ```In TIP 2015```, 24(10), 3034-3047.
11. [Temporally coherent completion of dynamic video](https://www.microsoft.com/en-us/research/wp-content/uploads/2017/01/SigAsia_2016_VideoCompletion.pdf). Huang, J. B., Kang, S. B., Ahuja, N., & Kopf, J. ```In TOG 2016```. [[project]](https://filebox.ece.vt.edu/~jbhuang/project/vidcomp/index.html) [[code]](https://github.com/amjltc295/Temporally-Coherent-Completion-of-Dynamic-Video)

### Deep Architectures (Learning Based)
1. [Video inpainting by jointly learning temporal structure and spatial details](https://arxiv.org/abs/1806.08482). Wang, C., Huang, H., Han, X., & Wang, J. ```In AAAI 2019```
2. [Deep Flow-Guided Video Inpainting](https://arxiv.org/abs/1905.02884). Xu, R., Li, X., Zhou, B., & Loy, C. C. ```In CVPR 2019``` [[code]](https://github.com/nbei/Deep-Flow-Guided-Video-Inpainting) [[project]](https://nbei.github.io/video-inpainting.html)
3. [Deep Video Inpainting](https://arxiv.org/abs/1905.01639). Kim, D., Woo, S., Lee, J. Y., & Kweon, I. S. ```In CVPR 2019``` [[code]](https://github.com/mcahny/Deep-Video-Inpainting) [[project]](https://sites.google.com/view/deepvinet/)
4. [Deep Blind Video Decaptioning by Temporal Aggregation and Recurrence](http://openaccess.thecvf.com/content_CVPR_2019/papers/Kim_Deep_Blind_Video_Decaptioning_by_Temporal_Aggregation_and_Recurrence_CVPR_2019_paper.pdf). Kim, D., Woo, S., Lee, J. Y., & Kweon, I. S. ```In CVPR 2019``` [[project]](https://sites.google.com/view/bvdnet/)
5. [VORNet: Spatio-temporally Consistent Video Inpainting for Object Removal](https://arxiv.org/abs/1904.06726)
Ya-Liang Chang, Zhe Yu Liu, Winston Hsu. ```In CVPRW 2019``` [[code]](https://github.com/amjltc295/VORNet-Spatio-temporally-Consistent-Video-Inpainting-for-Object-Removal)
6. [Learnable Gated Temporal Shift Module for Deep Video Inpainting](https://arxiv.org/abs/1907.01131) Ya-Liang Chang, Zhe Yu Liu, Kuan-Ying Lee, Winston Hsu. ```In BMVC 2019``` [[code]](https://github.com/amjltc295/Free-Form-Video-Inpainting)
7. [Align-and-Attend Network for Globally and Locally Coherent Video Inpainting](https://arxiv.org/abs/1905.13066). Woo, S., Kim, D., Park, K., Lee, J. Y., & Kweon, I. S. ```In Arxiv 2019```
8. [Frame-Recurrent Video Inpainting by Robust Optical Flow Inference](https://arxiv.org/abs/1905.02882) Yifan Ding, Chuan Wang, Haibin Huang, Jiaming Liu, Jue Wang, Liqiang Wang. ```In Arxiv 2019``` 
9. [Free-form Video Inpainting with 3D Gated Convolution and Temporal PatchGAN](https://arxiv.org/abs/1904.10247) Ya-Liang Chang, Zhe Yu Liu, Kuan-Ying Lee, Winston Hsu. ```In ICCV 2019``` [[code]](https://github.com/amjltc295/Free-Form-Video-Inpainting)
10. [Onion-Peel Networks for Deep Video Completion](https://arxiv.org/abs/1908.08718), Seoung Wug Oh, Sungho Lee, Joon-Young Lee, Seon Joo Kim. ```In ICCV 2019``` [[project]](https://sites.google.com/view/seoungwugoh) [[code]](https://github.com/seoungwugoh/opn-demo)
11. [Copy-and-Paste Networks for Deep Video Inpainting](https://arxiv.org/pdf/1908.11587.pdf), Sunho Lee, Seoung Wug Oh, DaeYeun Won, Seon Joo Kim. ```In ICCV 2019``` [[code]](https://github.com/shleecs/Copy-and-Paste-Networks-for-Deep-Video-Inpainting)[[project]](https://sites.google.com/view/seoungwugoh)
12. [An Internal Learning Approach to Video Inpainting](https://arxiv.org/pdf/1909.07957.pdf) Haotian Zhang, Long Mai, Ning Xu, Zhaowen Wang, John Collomosse, Hailin Jin. ```In ICCV 2019``` [[project]](https://cs.stanford.edu/~haotianz/publications/video_inpainting/)
13. [Short-Term and Long-Term Context Aggregation Network for Video Inpainting](https://www.ecva.net/papers/eccv_2020/papers_ECCV/papers/123490698.pdf), Li et al. ```In ECCV2020``` 
14. [Proposal-based Video Completion](http://www.cs.utexas.edu/~grauman/papers/eccv2020-hu.pdf), Hu et al. ```In ECCV2020``` 
15. [DVI: Depth Guided Video Inpainting for Autonomous Driving](https://arxiv.org/pdf/2007.08854.pdf), Liao et al. ```In ECCV2020``` [[project]](https://github.com/ApolloScapeAuto/dataset-api/tree/master/inpainting)
16. [Learning Joint Spatial-Temporal Transformations for Video Inpainting](https://arxiv.org/abs/2007.10247), Zeng et al., ```In ECCV2020``` [[project]](https://github.com/researchmm/STTN)




## Challenge 

1. [Looking at People ECCV Satellite Challenge @ ECCV 2018](http://chalearnlap.cvc.uab.es/challenge/26/description/)
2. [ICME Grand Challenge Learning-Based Image Inpainting @ ICME 2019](https://icme19inpainting.github.io/)
3. [Image Inpainting Challenge - AIM Workshop and Challenges @ ECCV 2020](https://competitions.codalab.org/competitions/24675#learn_the_details-evaluation)
