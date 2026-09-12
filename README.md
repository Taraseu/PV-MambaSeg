# PV-MambaSeg
Official PyTorch implementation of PV-MambaSeg for photovoltaic cell defect segmentation (TII 2026)
> Ziai Zhou, Chaoyang Song, Xiaotong Kong, Shixiong Fang, Huimin Lu, Jinxia Zhang
> *IEEE Transactions on Industrial Informatics (TII)*
> DOI: [10.1109/TII.2026.3707683](https://doi.org/10.1109/TII.2026.3707683)

[![IEEE Paper](https://img.shields.io/badge/Paper‑IEEE‑0066cc)](https://ieeexplore.ieee.org/document/11606595)
[![License](https://img.shields.io/badge/License‑MIT‑green)](LICENSE)

## 📋 Abstract
Pixel‑level segmentation of diverse defects for photovoltaic (PV) modules is critical for intelligent operation and maintenance of large‑scale PV power plants. Existing approaches suffer two major bottlenecks:
1. Poor modeling capability for geometric‑complex, arbitrarily‑oriented defects and weak anti‑noise performance, resulting in discontinuous and inaccurate segmentation masks.
2. Heavy computational overhead and large memory footprint, limiting deployment on resource‑constrained edge devices.

To mitigate these issues, we propose **PV‑MambaSeg**, a lightweight Mamba‑based network for PV cell defect segmentation.
- **OLS (Omni‑Local Scan)**: A novel multi‑directional continuous scanning strategy with differentiated forward‑backward paths, capturing structural continuity for arbitrarily oriented PV defects and reducing feature redundancy.
- **GLVSS (Global‑Local Visual State Space)**: Fuses multi‑window global features and fine‑grained local features. Equipped with DWAG (Dual‑Window Aggregation Gate) and SE attention, it suppresses complex background noise and enhances tiny‑defect representation.

PV‑MambaSeg achieves state‑of‑the‑art segmentation performance with only **2.77 M parameters**, **0.78 GFLOPs**, and **548.04 FPS** inference speed.

![network_arch](figures/arch.png)
> Overall architecture of PV‑MambaSeg, including Mamba‑based SegMAN encoder, OLS block and GLVSS module.

## 📊 Main Experimental Results
### Quantitative results on UCF‑EL test set
| Model | mIoU | Params(M) | GFLOPs | FPS |
|:-----:|:----:|:---------:|:------:|:---:|
| PV‑MambaSeg (Ours) | **0.6181** | **2.77** | **0.78** | **548.04** |

Per‑class IoU on UCF‑EL:
Crack: 0.7844｜Contact: 0.4162｜Interconnect:0.1750｜Corrosion:0.7451｜Background:0.9696

Industrial simulation test set (defect‑normal ratio 1:10):
- MDR (Missed Detection Rate): **0.0000**
- FAR (False Alarm Rate): **0.0098**
- Precision:0.9091｜Recall:1.0000｜F1‑Score:**0.9524**

Qualitative comparison against SOTA methods:
![vis_compare](figures/visual_compare.png)

## 📚 Datasets
Experiments are conducted on two public PV electroluminescence defect segmentation datasets:
1. **UCF‑EL Dataset**
> J. Fioresi et al., "Automated defect detection and localization in photovoltaic cells using semantic segmentation of electroluminescence images," *IEEE J. Photovolt.*, 2022.
> Train / Val / Test = **8:1:1**

2. **PSCDE Dataset**
> P. Zhou et al., "SIIF: Semantic information interactive fusion network for photovoltaic defect segmentation," *Applied Energy*, 2024.
> Train / Val / Test = **4:2:4**

> Please download datasets from their official project pages. Arrange dataset folder following `datasets/README_dataset.md`.
> Private industrial test set in the paper is not publicly available.

## 🛠 Environment & Installation
### Requirements
- Python >= 3.9
- PyTorch >= 2.0
- torchvision
- mamba‑ssm
- opencv‑python
- timm
- numpy
- scipy
- einops

Install dependencies:
```bash
pip install -r requirements.txt
