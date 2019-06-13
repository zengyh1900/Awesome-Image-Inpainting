# Awesome-Image-Inpainting
A list of resources for Image Inpainting, inspired by [Awesome-deep-vision](https://github.com/kjw0612/awesome-deep-vision) and [Awesome Computer Vision](https://github.com/jbhuang0604/awesome-computer-vision) .

Please feel free to [pull requests](https://github.com/1900zyh/Awesome-Image-Inpainting/pulls) to add papers.

![teaser](https://github.com/pathak22/context-encoder/blob/master/images/teaser.jpg "Sample inpainting results on held-out images")





## Early methods (Non Learning Based)
[1] Bertalmio, M., Sapiro, G., Caselles, V., & Ballester, C. (2000, July). Image inpainting. In SIGGRAPH (pp. 417-424). [[paper]](http://www.dtic.upf.edu/~mbertalmio/bertalmi.pdf)  

[2] Bertalmio, M., Vese, L., Sapiro, G., & Osher, S. (2003). Simultaneous structure and texture image inpainting. TIP, 12(8), 882-889. [[paper]](http://www.math.ucla.edu/~lvese/PAPERS/01217265.pdf)

[3] Criminisi, A., Pérez, P., & Toyama, K. (2004). Region filling and object removal by exemplar-based image inpainting. TIP 13(9), 1200-1212. [[paper]](http://www.irisa.fr/vista/Papers/2004_ip_criminisi.pdf)

[4] Sun, J., Yuan, L., Jia, J., & Shum, H. Y. (2005, July). Image completion with structure propagation. ToG (Vol. 24, No. 3, pp. 861-868). [[paper]](http://webee.technion.ac.il/cgm/Computer-Graphics-Multimedia/Undergraduate-Projects/2009/ImageCompletion/ImageCompletion_SIGGRAPH05.pdf)

[5] Huang, J. B., Kang, S. B., Ahuja, N., & Kopf, J. (2014). Image completion using planar structure guidance. TOG, 33(4), 129. [[paper]](https://www.microsoft.com/en-us/research/wp-content/uploads/2017/01/structure_completion_small.pdf) [[code]](https://github.com/jbhuang0604/StructCompletion) [[project]](https://sites.google.com/site/jbhuang0604/publications/struct_completion)



## Deep Architectures (Learning Based)

### NeurIPS 2015
[1] Ren, J. S., Xu, L., Yan, Q., & Sun, W. (2015). Shepard convolutional neural networks. NeurIPS pp. 901-909). [[paper]](https://papers.nips.cc/paper/5774-shepard-convolutional-neural-networks.pdf) [[code]](https://github.com/jimmy-ren/vcnn_double-bladed/tree/master/applications/Shepard_CNN)


### CVPR 2016
[1] Pathak, D., Krahenbuhl, P., Donahue, J., Darrell, T., & Efros, A. A. (2016). Context encoders: Feature learning by inpainting. CVPR (pp. 2536-2544). [[paper]](https://arxiv.org/abs/1604.07379) [[code]](https://github.com/pathak22/context-encoder)


### Siggraph 2017
[1] Iizuka, S., Simo-Serra, E., & Ishikawa, H. (2017). Globally and locally consistent image completion. ToG, 36(4), 107. [[paper]](http://hi.cs.waseda.ac.jp/~iizuka/projects/completion/data/completion_sig2017.pdf) [[code]](https://github.com/satoshiiizuka/siggraph2017_inpainting) [[project]](http://hi.cs.waseda.ac.jp/~iizuka/projects/completion/en/)


### CVPR 2017
[1] Yang, C., Lu, X., Lin, Z., Shechtman, E., Wang, O., & Li, H. (2017). High-resolution image inpainting using multi-scale neural patch synthesis. CVPR (pp. 6721-6729). [[paper]](https://arxiv.org/abs/1611.09969) [[code]](https://github.com/leehomyc/Faster-High-Res-Neural-Inpainting)

[2]Li, Y., Liu, S., Yang, J., & Yang, M. H. (2017). Generative face completion. CVPR (pp. 3911-3919). [[paper]](http://openaccess.thecvf.com/content_cvpr_2017/papers/Li_Generative_Face_Completion_CVPR_2017_paper.pdf) [[code]](https://github.com/Yijunmaverick/GenerativeFaceCompletion)

[3] Yeh, R. A., Chen, C., Yian Lim, T., Schwing, A. G., Hasegawa-Johnson, M., & Do, M. N. (2017). Semantic image inpainting with deep generative models. CVPR (pp. 5485-5493). [[paper]](http://openaccess.thecvf.com/content_cvpr_2017/papers/Yeh_Semantic_Image_Inpainting_CVPR_2017_paper.pdf) [[code]](https://github.com/moodoki/semantic_image_inpainting) [[project]](http://www.isle.illinois.edu/~yeh17/projects/semantic_inpaint/index.html)


### CVPR 2018
[1] Jiahui Yu, Zhe Lin, Jimei Yang, Xiaohui Shen, Xin Lu, Thomas S. Huang, Generative Image Inpainting with Contextual Attention, CVPR, 2018. [[paper]](https://arxiv.org/abs/1801.07892) [[code]](https://github.com/JiahuiYu/generative_inpainting)  [[project]](http://jiahuiyu.com/deepfill/)

[2] Yu, J., Lin, Z., Yang, J., Shen, X., Lu, X., & Huang, T. S. (2018). Generative image inpainting with contextual attention. CVPR (pp. 5505-5514). [[paper]](http://openaccess.thecvf.com/content_cvpr_2018/papers/Sun_Natural_and_Effective_CVPR_2018_paper.pdf)

[3] Dolhansky, B., & Canton Ferrer, C. (2018). Eye in-painting with exemplar generative adversarial networks. CVPR (pp. 7902-7911). [[paper]](http://openaccess.thecvf.com/content_cvpr_2018/papers/Dolhansky_Eye_In-Painting_With_CVPR_2018_paper.pdf) [[project]](https://bdol.github.io/exemplar_gans/) [[code]](https://github.com/bdol/exemplar_gans)

[4] Deng, J., Cheng, S., Xue, N., Zhou, Y., & Zafeiriou, S. (2018). Uv-gan: Adversarial facial uv map completion for pose-invariant face recognition. CVPR (pp. 7093-7102). [[paper]](http://openaccess.thecvf.com/content_cvpr_2018/papers/Deng_UV-GAN_Adversarial_Facial_CVPR_2018_paper.pdf)

[5] Gilbert, A., Collomosse, J., Jin, H., & Price, B. (2018). Disentangling Structure and Aesthetics for Style-aware Image Completion. CVPR (pp. 1848-1856). [[paper]](http://openaccess.thecvf.com/content_cvpr_2018/papers/Gilbert_Disentangling_Structure_and_CVPR_2018_paper.pdf)


### ECCV 2018
[1] Liu, G., Reda, F. A., Shih, K. J., Wang, T. C., Tao, A., & Catanzaro, B. (2018). Image inpainting for irregular holes using partial convolutions. ECCV (pp. 85-100). [[paper]](https://arxiv.org/abs/1804.07723) [[project]](http://masc.cs.gmu.edu/wiki/partialconv)

[2] Song, Y., Yang, C., Lin, Z., Liu, X., Huang, Q., Li, H., & Jay Kuo, C. C. (2018). Contextual-based image inpainting: Infer, match, and translate. ECCV (pp. 3-19). [[paper]](https://arxiv.org/abs/1711.08590)

[3] Yan, Z., Li, X., Li, M., Zuo, W., & Shan, S. (2018). Shift-net: Image inpainting via deep feature rearrangement. ECCV (pp. 1-17). [[paper]](https://arxiv.org/abs/1801.09392v2) [[code]](https://github.com/Zhaoyi-Yan/Shift-Net)


### NeurIPS 2018
[1] Wang, Y., Tao, X., Qi, X., Shen, X., & Jia, J. (2018). Image Inpainting via Generative Multi-column Convolutional Neural Networks. NeurIPS (pp. 331-340). [[paper]](https://arxiv.org/abs/1810.08771) [[code]](https://github.com/shepnerd/inpainting_gmcnn)


### BMVC 2018
[1] Song, Y., Yang, C., Shen, Y., Wang, P., Huang, Q., & Kuo, C. C. J. (2018). SPG-Net: Segmentation prediction and guidance network for image inpainting. BMVC. [[paper]](https://arxiv.org/abs/1805.03356)


### MM 2018
[1] Vo, H. V., Duong, N. Q., & Pérez, P. (2018, October). Structural inpainting. MM (pp. 1948-1956). [[paper]](https://arxiv.org/abs/1803.10348)

[2] Zhang, H., Hu, Z., Luo, C., Zuo, W., & Wang, M. (2018, October). Semantic Image Inpainting with Progressive Generative Networks. MM (pp. 1939-1947). [[paper]](https://dl.acm.org/citation.cfm?id=3240625) [[code]](https://github.com/crashmoon/Progressive-Generative-Networks)


### ACCV 2018
[1] Liao, H., Funka-Lea, G., Zheng, Y., Luo, J., & Zhou, S. K. (2018). Face Completion with Semantic Knowledge and Collaborative Adversarial Learning. ACCV. [[paper]](https://arxiv.org/pdf/1812.03252.pdf)


### ICASSP 2018
[1] Liao, L., Hu, R., Xiao, J., & Wang, Z. (2018, April). Edge-Aware Context Encoder for Image Inpainting. ICASSP (pp. 3156-3160). [[paper]](http://mirlab.org/conference_papers/International_Conference/ICASSP%202018/pdfs/0003156.pdf)


### ACM Transactions on Graphics (TOG) 2018
[1] Portenier, T., Hu, Q., Szabó, A., Bigdeli, S. A., Favaro, P., & Zwicker, M. (2018). Faceshop: Deep sketch-based face image editing. TOG, 37(4), 99. [[paper]](https://arxiv.org/abs/1804.08972)


### Arxiv 2018
[1] Chen, Z., Nie, S., Wu, T., & Healey, C. G. (2018). High resolution face completion with multiple controllable attributes via fully end-to-end progressive generative adversarial networks. arXiv preprint arXiv:1801.07632. [[paper]](https://arxiv.org/pdf/1812.01458.pdf)

[2] Banerjee, S., Scheirer, W. J., Bowyer, K. W., & Flynn, P. J. (2018). On Hallucinating Context and Background Pixels from a Face Mask using Multi-scale GANs. arXiv preprint arXiv:1811.07104. [[paper]](https://arxiv.org/pdf/1811.07104.pdf)

[3] Yu, J., Lin, Z., Yang, J., Shen, X., Lu, X., & Huang, T. S. (2018). Free-form image inpainting with gated convolution. arXiv preprint arXiv:1806.03589. [[paper]](https://arxiv.org/abs/1806.03589) [[project]](http://jiahuiyu.com/deepfill2/)


### CVPR 2019
[1] Zheng, C., Cham, T. J., & Cai, J. (2019). Pluralistic Image Completion. CVPR. [[paper]](https://arxiv.org/abs/1903.04227) [[code]](https://github.com/lyndonzheng/Pluralistic-Inpainting) [[project]](http://www.chuanxiaz.com/publication/pluralistic/)

[2] Zeng, Y., Fu, J., Chao, H., & Guo, B. (2019). Learning Pyramid-Context Encoder Network for High-Quality Image Inpainting. CVPR. [[paper]](https://arxiv.org/abs/1904.07475) [[code]](https://github.com/researchmm/PEN-Net-for-Inpainting)

[3] Xiong, W., Lin, Z., Yang, J., Lu, X., Barnes, C., & Luo, J. (2019). Foreground-aware Image Inpainting. CVPR. [[paper]](https://arxiv.org/abs/1901.05945)

[4] Han, X., Zhang, Z., Du, D., Yang, M., Yu, J., Pan, P., ... & Cui, S. (2019). Deep Reinforcement Learning of Volume-guided Progressive View Inpainting for 3D Point Scene Completion from a Single Depth Image. CVPR. [[paper]](https://arxiv.org/pdf/1903.04019.pdf)

[5] Sagong, M. C., Shin, Y. G., Kim, S. W., Park, S., & Ko, S. J. (2019). PEPSI: Fast Image Inpainting With Parallel Decoding Network. CVPR (pp. 11360-11368). [[paper]](http://openaccess.thecvf.com/content_CVPR_2019/papers/Sagong_PEPSI__Fast_Image_Inpainting_With_Parallel_Decoding_Network_CVPR_2019_paper.pdf)

[6] Grigorev, A., Sevastopolsky, A., Vakhitov, A., & Lempitsky, V. (2019). Coordinate-Based Texture Inpainting for Pose-Guided Human Image Generation. CVPR (pp. 12135-12144). [[paper]](https://arxiv.org/abs/1811.11459)

[7] Xu, R., Li, X., Zhou, B., & Loy, C. C. (2019). Deep Flow-Guided Video Inpainting. CVPR. [[paper]](https://arxiv.org/abs/1905.02884)[[code]](https://github.com/nbei/Deep-Flow-Guided-Video-Inpainting)

[8] Kim, D., Woo, S., Lee, J. Y., & Kweon, I. S. (2019). Deep Video Inpainting. CVPR. [[paper]](https://arxiv.org/abs/1905.01639)[[code]](https://github.com/mcahny/Deep-Video-Inpainting)

[9] Kim, D., Woo, S., Lee, J. Y., & Kweon, I. S. (2019). Deep Blind Video Decaptioning by Temporal Aggregation and Recurrence. CVPR. [[paper]](http://openaccess.thecvf.com/content_CVPR_2019/papers/Kim_Deep_Blind_Video_Decaptioning_by_Temporal_Aggregation_and_Recurrence_CVPR_2019_paper.pdf)




### Arxiv 2019 
[1] Nazeri, K., Ng, E., Joseph, T., Qureshi, F., & Ebrahimi, M. (2019). EdgeConnect: Generative Image Inpainting with Adversarial Edge Learning. arXiv preprint arXiv:1901.00212. [[paper]](http://arxiv.org/abs/1901.00212) [[code]](https://github.com/knazeri/edge-connect)

[2] Xiao, Q., Li, G., & Chen, Q. (2018). Deep Inception Generative Network for Cognitive Image Inpainting. arXiv preprint arXiv:1812.01458. [[paper]]( https://arxiv.org/pdf/1812.01458.pdf)

[3] Webster, R., Rabin, J., Simon, L., & Jurie, F. (2019). Detecting Overfitting of Deep Generative Networks via Latent Recovery. arXiv preprint arXiv:1901.03396. [[paper]](https://arxiv.org/pdf/1901.03396.pdf)

[4] Jo, Y., & Park, J. (2019). SC-FEGAN: Face Editing Generative Adversarial Network with User's Sketch and Color. arXiv preprint arXiv:1902.06838. [[paper]](https://arxiv.org/abs/1902.06838) [[code]](https://github.com/JoYoungjoo/SC-FEGAN)

[5] Hong, X., Xiong, P., Ji, R., & Fan, H. (2019). Deep Fusion Network for Image Completion. arXiv preprint arXiv:1904.08060. [[paper]](https://arxiv.org/abs/1904.08060) [[code]](https://github.com/hughplay/DFNet)

[6] Shin, Y. G., Sagong, M. C., Yeo, Y. J., Kim, S. W., & Ko, S. J. (2019). PEPSI++: Fast and Lightweight Network for Image Inpainting. arXiv preprint arXiv:1905.09010. [[paper]](https://arxiv.org/pdf/1905.09010.pdf)

