#!/usr/bin/env python
# coding: utf-8

# In[4]:


### Crops all images in a folder to spec. 

import cv2
import numpy as np
import os

imageFolder = r'/media/frfuser/FRF_ConnorG/KevinMartinsMiniArgusTest/1664117941403/CamBob_B_Output/timeshift/4.5min'

fileList = []

for image in os.listdir(imageFolder):
    imgName = os.path.join(imageFolder, image)
    fileList.append(imgName)

for i in fileList:
    image = cv2.imread(i, 0)
    newImage = image[250:1500, 0:4096]
    cv2.imwrite(i, newImage)

print('complete')


# In[ ]:




