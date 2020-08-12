# SmartSwitch

This repository contains the source code and data for Stream Fingerprinting using nerual networks. The attack is an encrypted traffic analysis attack that allows a passive adversary to infer which YouTube video a user watchers by sniffing encrypted traffic between a user and the server. 

**The dataset and code are for research purposes only**. The results of this study are published in the following paper: 

Haipeng Li, Ben Niu, Boyang Wang, *“SmartSwitch: Efficient Traffic Obfuscation against Stream Fingerprinting,”* 16th EAI International Conference on Security and Privacy in Communication Networks (**SecureComm 2020**), October, 2020.  

## Content

The `video_collection` directory contains the code to automatically collect stream traffic between user and stream provider (e.g. Youtube). 

The `feature_selection` directory contains the code for feature selection. We have two different catogeries of selection methods, Mutual Information based methods and SW-PFI, which is proposed in our paper.

The `defense` directory contains the defense code for generating obfuscated stream traffic.

## Dataset

The original traffic data (i.e., non-defended traffic data), defended data and the list of YouTube videos we used in this study can be found below: 

https://mailuc-my.sharepoint.com/:f:/g/personal/wang2ba_ucmail_uc_edu/EoTxR4S42eJDk0_tbmLyLbQBRYT2zoeWSIc3ISUPSN1THg?e=kYE8rP


## Citation

When reporting results that use the dataset or code in this repository, please cite:

Haipeng Li, Ben Niu, Boyang Wang, *“SmartSwitch: Efficient Traffic Obfuscation against Stream Fingerprinting,”* 16th EAI International Conference on Security and Privacy in Communication Networks (**SecureComm 2020**), October, 2020. 


## Contacts

Haipeng Li, li2hp@mail.uc.edu, University of Cincinnati

Boyang Wang, boyang.wang@uc.edu, University of Cincinnati
