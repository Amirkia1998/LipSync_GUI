# Audio-driven Talking Head Generation and Evaluation

Official codebase for the [Paper](https://link.springer.com/chapter/10.1007/978-3-031-65282-0_10):

**"Can One Model Fit All? An Exploration of Wav2Lip’s Lip-Syncing Generalizability Across Culturally Distinct Languages"**
, presented at [ICCSA2024](https://iccsa.org/).

:movie_camera: Watch the presentation [here]().

## Content
### Lip Synchronization

Lip synchronization (LipSync) is a cutting-edge technology capable of generating highly realistic talking head videos by aligning lip movements precisely with spoken audio. 
You can use the ```lipsync_gui.py``` script to generate lip-synced videos for any face and language. (can be used without GPU :fire:)

![GUI](https://i.imghippo.com/files/MF2tm1722159355.jpg)

### Face-to-Face Translation
SOON!

### Evaluation
Evaluate the quality of lip synchronization with this [Colab notebook]() in the ```evaluation``` folder. It computes LipSync Error Distance **(LSE-D)** and LipSync Error Confidence **(LSE-C)** values. These metrics are specifically designed to quantitatively assess lip synchronization accuracy. 

[![Open In Collab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/Naereen/badges)

## Quick Start
To generate LipSynced videos, follow these steps: 

1. Create conda environment and install packages:
```
conda env create -f environment.yml
conda activate LipSync_GUI
```
2. Download the weights for the pre-trained face detection model  from this [link](link)  and place it in ```wav2Lip\face_detection\detection\sfd``` folder. 

3. Download the weights for the LipSync models ([Wav2Lip]() and [Wav2Lip_gan]())    and place it in the ```wav2Lip\checkpoints```.

4. Run ```app\lipsync_gui.py``` and use the Gradio app to generate videos.

Tips: 
- For initial testing, you can use the input audio and faces saved in the ```resources``` directory.
- The generated videos are saved in the ```app\results``` by default.

## Examples
<video src="https://youtu.be/eleObbZVk6k" width="500">

## Acknowledgments
We extend our sincere gratitude to authors of this [paper](https://dl.acm.org/doi/10.1145/3394171.3413532) for their pioneering research.

## Citation :page_with_curl: 
Rafiei Oskooei, A., Yahsi, E., Sungur, M., S. Aktas, M. (2024). Can One Model Fit All? An Exploration of Wav2Lip’s Lip-Syncing Generalizability Across Culturally Distinct Languages. Computational Science and Its Applications – ICCSA 2024 Workshops. ICCSA 2024. Lecture Notes in Computer Science, vol 14819. Springer, Cham. https://doi.org/10.1007/978-3-031-65282-0_10

