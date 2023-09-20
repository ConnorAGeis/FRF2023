#!/usr/bin/env python
# coding: utf-8

# In[1]:


import os
import cv2
import numpy as np

imageFolder = r'/media/frfuser/FRF_ConnorG/KevinMartinsMiniArgusTest/1663080831409g/CamBob_B_Output/brightest'
outImage = r'/media/frfuser/FRF_ConnorG/KevinMartinsMiniArgusTest/1663005397544g/CamBob_B_Output/brightest/brightest_9.0min_6s.tiff'

imageLocs = os.listdir(imageFolder)

fileList = []

for i in imageLocs[0:1080:12]:
    imgName = os.path.join(imageFolder, i)
    fileList.append(imgName)

emptyTemplate = cv2.imread(fileList[0])
grayscale = cv2.cvtColor(emptyTemplate, cv2.COLOR_BGR2GRAY)
brightest = np.empty_like(grayscale, dtype = np.uint8)

for i in fileList:
    img = cv2.imread(i)
    img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    img = np.asarray(img)
    img = img.astype(np.uint8)
    brightest = np.dstack((img, brightest))

brightest = np.amax(brightest, axis = 2).astype(np.uint8)

cv2.imwrite(outImage, brightest)

print("done")


# In[ ]:


media/frfuser/FRF_ConnorG/KevinMartinsMiniArgusTest/1663005397544g()
media/frfuser/FRF_ConnorG/KevinMartinsMiniArgusTest/1663080831409g()
media/frfuser/FRF_ConnorG/KevinMartinsMiniArgusTest/1663869541385()
media/frfuser/FRF_ConnorG/KevinMartinsMiniArgusTest/1663948741409()
media/frfuser/FRF_ConnorG/KevinMartinsMiniArgusTest/1664117941403()
media/frfuser/FRF_ConnorG/KevinMartinsMiniArgusTest/1664395141403()


# In[ ]:




