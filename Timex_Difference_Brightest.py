#!/usr/bin/env python
# coding: utf-8

# In[6]:


import os
import cv2
import numpy as np



### Out Images

outImage_15min = r'/media/frfuser/FRF_ConnorG/KevinMartinsMiniArgusTest/1663005397544g/CamBob_B_Output/brightest_Dif/B_Timex_15min_brightest_dif.tiff'

outImage_90s = r'/media/frfuser/FRF_ConnorG/KevinMartinsMiniArgusTest/1663005397544g/CamBob_B_Output/brightest_Dif/B_Timex_90s_brightest_dif.tiff'

outImage_dif = r'/media/frfuser/FRF_ConnorG/KevinMartinsMiniArgusTest/1663005397544g/CamBob_B_Output/brightest_Dif/brightest_dif.tiff'

### Load Images

Timex_15min = cv2.imread('/media/frfuser/FRF_ConnorG/KevinMartinsMiniArgusTest/1663005397544g/CamBob_B_Output/brightest/brightest_15.0min_10s.tiff')

Timex_90s = cv2.imread('/media/frfuser/FRF_ConnorG/KevinMartinsMiniArgusTest/1663005397544g/CamBob_B_Output/brightest/brightest_1.5min_1s.tiff')

### Convert to Grayscale

grayscale_15min = cv2.cvtColor(Timex_15min, cv2.COLOR_BGR2GRAY)

grayscale_90s = cv2.cvtColor(Timex_90s, cv2.COLOR_BGR2GRAY)

### Compute Difference

difference = cv2.subtract(grayscale_15min, grayscale_90s)

### Colormask Red

ret, mask = cv2.threshold(difference, 0, 255,cv2.THRESH_BINARY_INV |cv2.THRESH_OTSU)
difference[mask != 255] 

### Add Mask to Images

Timex_15min[mask != 255] = [0, 0, 255]

Timex_90s[mask != 255] = [0, 0, 255]

### Store Images

cv2.imwrite(outImage_15min, Timex_15min)
cv2.imwrite(outImage_90s, Timex_90s)
cv2.imwrite(outImage_dif, difference)

print("complete")


# In[ ]:


media/frfuser/FRF_ConnorG/KevinMartinsMiniArgusTest/1663005397544g()

media/frfuser/FRF_ConnorG/KevinMartinsMiniArgusTest/1663080831409g()

media/frfuser/FRF_ConnorG/KevinMartinsMiniArgusTest/1663869541385()

media/frfuser/FRF_ConnorG/KevinMartinsMiniArgusTest/1663948741409()

media/frfuser/FRF_ConnorG/KevinMartinsMiniArgusTest/1664117941403()

media/frfuser/FRF_ConnorG/KevinMartinsMiniArgusTest/1664395141403()

