# SmartSwitch

This repository contains the source code and data for Stream Fingerprinting using nerual networks. The attack is an encrypted traffic analysis attack that allows a passive adversary to infer which YouTube video a user watches by sniffing encrypted traffic between a user and the server. 

**The dataset and code are for research purposes only**. The results of this study are published in the following paper: 

Haipeng Li, Ben Niu, Boyang Wang, *“SmartSwitch: Efficient Traffic Obfuscation against Stream Fingerprinting,”* 16th EAI International Conference on Security and Privacy in Communication Networks (**SecureComm 2020**), October, 2020.  

## Content

The `video_collection` directory contains the code to automatically collect stream traffic between user and stream provider (e.g. Youtube). 

The `feature_selection` directory contains the code for feature selection. We have two different catogeries of selection methods, Mutual Information based methods and SW-PFI, which is proposed in our paper.

The `defense` directory contains the defense code for generating obfuscated stream traffic.

## Dataset

We investigated 100 classes (i.e., Youtube videos) and 200 traffic traces per class in this research. The original traffic data (i.e., non-defended traffic data), defended data and the list of YouTube videos we used in this study can be found below (**last modified: Sept, 2021**): 

https://mailuc-my.sharepoint.com/:f:/g/personal/wang2ba_ucmail_uc_edu/EoTxR4S42eJDk0_tbmLyLbQBRYT2zoeWSIc3ISUPSN1THg?e=uErNwo

**Note:** the above link needs to be updated every 6 months due to certain settings of OneDrive. If you find the link is expired and you cannot access the data, please feel free to email us (boyang.wang@uc.edu). We will be update the link as soon as we can. Thanks! 

## Neural Networks

We leveraged a Convolutional Neural Network to infer which video it is based on the traffic pattern. The CNN includes 11 layers and achieved over 90% accuracy in the attack. Details of the structure and tuned hyperparameters can be found in our paper. 

## Citation

When reporting results that use the dataset or code in this repository, please cite:

Haipeng Li, Ben Niu, Boyang Wang, *“SmartSwitch: Efficient Traffic Obfuscation against Stream Fingerprinting,”* 16th EAI International Conference on Security and Privacy in Communication Networks (**SecureComm 2020**), October, 2020. 


## Contacts

Haipeng Li, li2hp@mail.uc.edu, University of Cincinnati

Boyang Wang, boyang.wang@uc.edu, University of Cincinnati
