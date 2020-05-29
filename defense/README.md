# Usage

`laplace_weith.py` is used to generate obfuscated dataset by using SmartSwich version of d*-privacy method. 

  The input includes: 
  
  `method` the feature selection method we want to use in SmartSwich.
  `b` the bin size.
  `r` the number of features we want to add higher noise
  `eps_heavy` the value of `epsilon` for relevant features.
  `eps_light` the value of `epsilon` for irrelevant features.
  
  When `eps_heavy` equals to `eps_light`, the SmartSwich version of d*-privacy method becomes the original d*-privacy method.
  
-```Python3 loadDriver.py [method] [b] [r] [eps_heavy] [eps_light]```-
