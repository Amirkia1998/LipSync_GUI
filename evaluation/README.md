# LipSync Accuracy Evaluation
Using this notebook you can calculate LipSync Error Distance (LSE-D) and LipSync Error Confidence (LSE-C) scores for LipSynced videos.

## To run the notebook in Google colab: 
[![Open In Collab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/drive/1x8edclm-3N9_asqqPqz3E1uoSibqXDsB?usp=sharing)
1.   Put your LipSynced videos in your the ```videos``` folder
2.   Run the notebook cells 
3.   The results will appear in the ```all_scores.txt``` file



## To run in your local:


1.   Download  ```syncnet_python``` folder 
2.   Download the model weights by running ```download_model.sh``` file
3. Install the dependencies ```!pip install -r requirements.txt```
4.   Run the following commands to update the libraries
```
!pip install scenedetect==0.6.1
!pip install python_speech_features
``` 
5. Run ```!sh calculate_scores_real_videos.sh {path_to_videos}/``` to calculate the scores
6. The results will appear in the ```all_scores.txt``` file

### Acknowledgment
Thanks to authors of [this paper](https://link.springer.com/chapter/10.1007/978-3-319-54427-4_19) for their groundbreaking work.