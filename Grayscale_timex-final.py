#!/usr/bin/env python
# coding: utf-8

# In[27]:


### GOOD

import os
import cv2
import numpy as np

imageFolder = r'/media/frfuser/FRF_ConnorG/KevinMartinsMiniArgusTest/1663005397544g/CamBob_B'
outImage = r"/media/frfuser/FRF_ConnorG/KevinMartinsMiniArgusTest/1663005397544g/CamBob_B_Output/img_correlation/B_15min_2hz_test.tiff"

#imageLocs = os.listdir(imageFolder)[1000:2200]
imageLocs = os.listdir(imageFolder)[30:1830]

emptyTemplate = cv2.imread(os.path.join(imageFolder, imageLocs[0]))
grayscale = cv2.cvtColor(emptyTemplate, cv2.COLOR_BGR2GRAY)
empty = np.empty_like(grayscale, dtype = np.float32)

for image in imageLocs:
    img = cv2.imread(os.path.join(imageFolder, image))
    img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    grayscaleArrayFloat = img.astype(np.float32)
    empty = np.add(empty, grayscaleArrayFloat)

grayscaleAvg = (empty / len(imageLocs)).astype(np.uint8)

cv2.imwrite(outImage, grayscaleAvg)

print('complete')


# In[ ]:




