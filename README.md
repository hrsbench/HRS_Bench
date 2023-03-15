# HRS-Bench: Holistic, Reliable and Scalable Benchmark for Text-to-Image Models
This is the official implementation for our paper

[**"HRS-Bench: Holistic, Reliable and Scalable Benchmark for Text-to-Image Models"**](https://hrsbench.github.io/)

:satellite: [![Website](https://img.shields.io/badge/Project-Website-87CEEB)](https://hrsbench.github.io/) &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp;
:book: [![paper](https://img.shields.io/badge/arXiv-Paper-<COLOR>.svg)](https://hrsbench.github.io/index.html) &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp;
:clapper: [![video](https://img.shields.io/badge/Video-Presentation-F9D371)](https://hrsbench.github.io/index.html)

## :loudspeaker: News
* **(March 8, 2023):** HRS-Bench is submitted to ICCV 2023.

## :books: Synopsis

* Holistic skills evaluation. Rather than focus on isolated metrics such as accuracy, we measure 13 skills, which could be categorized into five critical skills; accuracy, robustness, generalization, fairness, and bias.
<p align="center">
  <img src="Figures/intro_Img.png" width="75%"/>
</p>

* Broad scenarios coverage. HRS-Bench covers 50 applications, e.g., fashion, animals, transportation, food, and clothes.
<p align="center">
  <img src="Figures/intro_Img.png" width="75%"/>
</p>

* Standardization. We propose a unified benchmark, where we fairly evaluate the existing models across a wide range of metrics.
<p align="center">
  <img src="Figures/intro_Img.png" width="75%"/>
</p>

## :pushpin: Covered Models
* [Stable-Diffusion V1](https://github.com/CompVis/stable-diffusion)
* [Stable-Diffusion V2](https://github.com/Stability-AI/stablediffusion)
* [DALL.E V2](https://openai.com/product/dall-e-2)
* [Structure-Difussion](https://github.com/weixi-feng/Structured-Diffusion-Guidance)
* [CogView V2](https://github.com/THUDM/CogView2)
* [Glide](https://github.com/openai/glide-text2im)
* [Paella](https://github.com/dome272/Paella)
* [minDALL-E](https://github.com/kakaobrain/minDALL-E)
* [DALLEMini](https://github.com/borisdayma/dalle-mini)

## :fire: Qualitative results
<p align="center">
  <img src="Figures/lar_arch.jpg" width="75%"/>
</p>


## :pushpin: Prerequisites
* Python >= 3.7
* Pytorch >= 1.7.0
* Install other common packages (numpy, [pytorch_transformers](https://pypi.org/project/pytorch-transformers/), etc.)


## :pushpin: Data
### :point_right: HRS-Bench
* First, download our prompts that covers the 13 skills from [here](https://drive.google.com/drive/folders/1AlA259sXi-3ZJD7RFaL2bGDwJXLImJrx).
* Each skill has its own CSV file that contains the prompt and the GT that will be used during the evaluation phase. 

## :pushpin: Evaluation


## :bouquet: Credits
The project is inspired from the great language benchmark [HELM](https://crfm.stanford.edu/helm/v0.1.0/?).

## :telephone: Contact us

## :mailbox_with_mail: Citation

Please consider citing our paper if you find it useful.
```

```
