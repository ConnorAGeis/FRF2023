#!/usr/bin/env python
# coding: utf-8

# In[5]:


import os
import cv2
import numpy as np

imageFolder = r'/media/frfuser/FRF_ConnorG/KevinMartinsMiniArgusTest/1664117941403/CamBob_B'
outImage = r'/media/frfuser/FRF_ConnorG/KevinMartinsMiniArgusTest/1664117941403/CamBob_B_Output/timeshift/4.5min/b_5th_4.5min.tiff'

imageLocs = os.listdir(imageFolder)

bimages = []
gimages = []
rimages = []

for i in imageLocs[::]:
    img = cv2.imread(os.path.join(imageFolder, i))
    b,g,r = cv2.split(img)
    bimages.append(b)
    gimages.append(g)
    rimages.append(r)

bavg = np.mean(bimages, axis=0).astype(np.uint8)
gavg = np.mean(gimages, axis=0).astype(np.uint8)
ravg = np.mean(rimages, axis=0).astype(np.uint8)
merged = cv2.merge([bavg, gavg, ravg])


cv2.imwrite(outImage, merged)


# In[ ]:




