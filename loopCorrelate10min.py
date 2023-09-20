#!/usr/bin/env python
# coding: utf-8

# In[42]:


### Run code for each folder and copy and paste output into corresponding .txt file

import sys
import os
import numpy as np
import cv2

# Argus Timex. Path. 10mins, 2Hz, Indices = (30,1230)
img1 = r'/media/frfuser/FRF_ConnorG/KevinMartinsMiniArgusTest/1664395141403/CamBob_B_Output/timeshift/B_10min_2hz.tiff'
img1 = cv2.imread(img1)

# Subsampled Timex. Path. Indices = ()
imageFolder = r'/media/frfuser/FRF_ConnorG/KevinMartinsMiniArgusTest/1664395141403/CamBob_B_Output/timeshift/15.0min'

fileList = []

for image in os.listdir(imageFolder):
    imgName = os.path.join(imageFolder, image)
    fileList.append(imgName)

for i in fileList:
    img2 = cv2.imread(i)
    corr = np.corrcoef(img1.flatten(), img2.flatten())
    #sys.stdout = open('/media/frfuser/FRF_ConnorG/KevinMartinsMiniArgusTest/1663005397544g/CamBob_B_Output/timeshift/3.0min/corrOutput.txt', 'w')
    print(corr)


# In[ ]:


### Scenario 2

import os
import numpy as np
import cv2

# Argus Timex. Path. 10mins, 2Hz, Indices = (30,1230)
img1 = r'/media/frfuser/FRF_ConnorG/KevinMartinsMiniArgusTest/1663005397544g/CamBob_B_Output/timeshift/B_10min_2hz.tiff'
img1 = cv2.imread(img1)


img2 = r'/media/frfuser/FRF_ConnorG/KevinMartinsMiniArgusTest/1663005397544g/CamBob_B_Output/timeshift/1.5min/b_1st_90.tiff'
img2 = cv2.imread(img2)

#1.5min
np.corrcoef(img1.flatten(), img2.flatten())


# In[ ]:




