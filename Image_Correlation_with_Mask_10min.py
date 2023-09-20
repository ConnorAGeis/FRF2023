#!/usr/bin/env python
# coding: utf-8

# Scenario 1 

# In[8]:


### Scenario 1 

import cv2
import numpy as np

#downsampledMask
downsampledTimex = r'/media/frfuser/FRF_ConnorG/KevinMartinsMiniArgusTest/1663005397544g/CamBob_B_Output/timex_oblique/B_90x_10s_15.0min.tiff'

image = cv2.imread(downsampledTimex, 0)

mask = np.zeros(image.shape[:2], np.uint8)
mask[250:1500, 0:4096] = 255
img1 = cv2.bitwise_and(image,image,mask=mask)

######################################################

#benchmarkMask
benchmark = r'/media/frfuser/FRF_ConnorG/KevinMartinsMiniArgusTest/1663005397544g/CamBob_B_Output/img_correlation/B_10min_2hz_test.tiff'

image = cv2.imread(benchmark, 0)

mask = np.zeros(image.shape[:2], np.uint8)
mask[250:1500, 0:4096] = 255
img2 = cv2.bitwise_and(image,image,mask=mask)

np.corrcoef(img1.flatten(), img2.flatten())


# In[ ]:


### Scenario 1 Outputs 


#1.5min
array([[1.        , 0.99847014],
       [0.99847014, 1.        ]])

#3.0min
array([[1.        , 0.99907881],
       [0.99907881, 1.        ]])

#4.5min
array([[1.       , 0.9994322],
       [0.9994322, 1.       ]])

#6.0min
array([[1.        , 0.99965587],
       [0.99965587, 1.        ]])

#7.5min
array([[1.        , 0.99981985],
       [0.99981985, 1.        ]])

#9.0min
array([[1.        , 0.99989891],
       [0.99989891, 1.        ]])

#15.0min
array([[1.        , 0.99970435],
       [0.99970435, 1.        ]])


# In[47]:


import pandas as pd
import numpy as np
import matplotlib.pyplot as pt

time = pd.Series([1.5, 3.0, 4.5, 6.0, 7.5, 9.0, 15.0])
corrCoef = pd.Series([0.99847014, 0.99907881, 0.9994322, 0.99965587, 0.99981985, 0.99989891, 0.99970435])

pt.scatter(time, corrCoef)
pt.plot(np.unique(time), np.poly1d(np.polyfit(time, corrCoef, 1))(np.unique(time)), color = 'green')

pt.title("Timex Sensitivity Analysis: Image Correlation of Various Sampling Schemes")
pt.xlabel("Sample Duration (min)")
pt.ylabel("Pearson Correlation Coefficient")

pt.savefig('/media/frfuser/FRF_ConnorG/KevinMartinsMiniArgusTest/1663005397544g/CamBob_B_Output/img_correlation/B_img_correlation_10min_mask.tiff', bbox_inches = 'tight')


# Scenario 2 

# In[18]:


### Scenario 2

import cv2
import numpy as np

#downsampledMask
downsampledTimex = r'/media/frfuser/FRF_ConnorG/KevinMartinsMiniArgusTest/1663080831409g/CamBob_B_Output/timex_oblique/B_90x_5s_7.5min.tiff'

image = cv2.imread(downsampledTimex, 0)

mask = np.zeros(image.shape[:2], np.uint8)
mask[250:1500, 0:4096] = 255
img1 = cv2.bitwise_and(image,image,mask=mask)

######################################################

#benchmarkMask
benchmark = r'/media/frfuser/FRF_ConnorG/KevinMartinsMiniArgusTest/1663080831409g/CamBob_B_Output/img_correlation/B_10min_2hz_test.tiff'

image = cv2.imread(benchmark, 0)

mask = np.zeros(image.shape[:2], np.uint8)
mask[250:1500, 0:4096] = 255
img2 = cv2.bitwise_and(image,image,mask=mask)

np.corrcoef(img1.flatten(), img2.flatten())


# In[ ]:


### Scenario 2 Outputs 


#1.5min
array([[1.        , 0.99741013],
       [0.99741013, 1.        ]])

#3.0min
array([[1.        , 0.99842578],
       [0.99842578, 1.        ]])

#4.5min
array([[1.        , 0.99848707],
       [0.99848707, 1.        ]])

#6.0min
array([[1.        , 0.99937566],
       [0.99937566, 1.        ]])

#7.5min
array([[1.        , 0.99959848],
       [0.99959848, 1.        ]])

#9.0min
array([[1.       , 0.9996424],
       [0.9996424, 1.       ]])

#15.0min
array([[1.        , 0.99955094],
       [0.99955094, 1.        ]])


# In[48]:


import pandas as pd
import numpy as np
import matplotlib.pyplot as pt

time = pd.Series([1.5, 3.0, 4.5, 6.0, 7.5, 9.0, 15.0])
corrCoef = pd.Series([0.99741013, 0.99842578, 0.99848707, 0.99937566, 0.99959848, 0.9996424, 0.99955094])

pt.scatter(time, corrCoef)
pt.plot(np.unique(time), np.poly1d(np.polyfit(time, corrCoef, 1))(np.unique(time)), color = 'green')

pt.title("Timex Sensitivity Analysis: Image Correlation of Various Sampling Schemes")
pt.xlabel("Sample Duration (min)")
pt.ylabel("Pearson Correlation Coefficient")

pt.savefig('/media/frfuser/FRF_ConnorG/KevinMartinsMiniArgusTest/1663080831409g/CamBob_B_Output/img_correlation/B_img_correlation_10min_mask.tiff', bbox_inches = 'tight')


# Scenario 3 

# In[25]:


### Scenario 3

import cv2
import numpy as np

#downsampledMask
downsampledTimex = r'/media/frfuser/FRF_ConnorG/KevinMartinsMiniArgusTest/1663869541385/CamBob_B_Output/timex_oblique/B_90x_10s_15.0min.tiff'

image = cv2.imread(downsampledTimex, 0)

mask = np.zeros(image.shape[:2], np.uint8)
mask[250:1500, 0:4096] = 255
img1 = cv2.bitwise_and(image,image,mask=mask)

######################################################

#benchmarkMask
benchmark = r'/media/frfuser/FRF_ConnorG/KevinMartinsMiniArgusTest/1663869541385/CamBob_B_Output/img_correlation/B_10min_2hz_test.tiff'

image = cv2.imread(benchmark, 0)

mask = np.zeros(image.shape[:2], np.uint8)
mask[250:1500, 0:4096] = 255
img2 = cv2.bitwise_and(image,image,mask=mask)

np.corrcoef(img1.flatten(), img2.flatten())


# In[ ]:


### Scenario 3 Outputs 


#1.5min
array([[1.        , 0.99682524],
       [0.99682524, 1.        ]])

#3.0min
array([[1.        , 0.99937836],
       [0.99937836, 1.        ]])

#4.5min
array([[1.        , 0.99958945],
       [0.99958945, 1.        ]])

#6.0min
array([[1.        , 0.99964134],
       [0.99964134, 1.        ]])

#7.5min
array([[1.       , 0.9997606],
       [0.9997606, 1.       ]])

#9.0min
array([[1.        , 0.99974671],
       [0.99974671, 1.        ]])

#15.0min
array([[1.        , 0.99956697],
       [0.99956697, 1.        ]])


# In[49]:


import pandas as pd
import numpy as np
import matplotlib.pyplot as pt

time = pd.Series([1.5, 3.0, 4.5, 6.0, 7.5, 9.0, 15.0])
corrCoef = pd.Series([0.99682524, 0.99937836, 0.99958945, 0.99964134, 0.9997606, 0.99974671, 0.99956697])

pt.scatter(time, corrCoef)
pt.plot(np.unique(time), np.poly1d(np.polyfit(time, corrCoef, 1))(np.unique(time)), color = 'green')

pt.title("Timex Sensitivity Analysis: Image Correlation of Various Sampling Schemes")
pt.xlabel("Sample Duration (min)")
pt.ylabel("Pearson Correlation Coefficient")

pt.savefig('/media/frfuser/FRF_ConnorG/KevinMartinsMiniArgusTest/1663869541385/CamBob_B_Output/img_correlation/B_img_correlation_10min_mask.tiff', bbox_inches = 'tight')



# Scenario 4 

# In[32]:


### Scenario 4

import cv2
import numpy as np

#downsampledMask
downsampledTimex = r'/media/frfuser/FRF_ConnorG/KevinMartinsMiniArgusTest/1663948741409/CamBob_B_Output/timex_oblique/B_90x_10s_15.0min.tiff'

image = cv2.imread(downsampledTimex, 0)

mask = np.zeros(image.shape[:2], np.uint8)
mask[250:1500, 0:4096] = 255
img1 = cv2.bitwise_and(image,image,mask=mask)

######################################################

#benchmarkMask
benchmark = r'/media/frfuser/FRF_ConnorG/KevinMartinsMiniArgusTest/1663948741409/CamBob_B_Output/img_correlation/B_10min_2hz_test.tiff'

image = cv2.imread(benchmark, 0)

mask = np.zeros(image.shape[:2], np.uint8)
mask[250:1500, 0:4096] = 255
img2 = cv2.bitwise_and(image,image,mask=mask)

np.corrcoef(img1.flatten(), img2.flatten())


# In[ ]:


### Scenario 4 Outputs 


#1.5min
array([[1.        , 0.99755617],
       [0.99755617, 1.        ]])

#3.0min
array([[1.        , 0.99885254],
       [0.99885254, 1.        ]])

#4.5min
array([[1.        , 0.99905536],
       [0.99905536, 1.        ]])

#6.0min
array([[1.        , 0.99944236],
       [0.99944236, 1.        ]])

#7.5min
array([[1.        , 0.99965775],
       [0.99965775, 1.        ]])

#9.0min
array([[1.        , 0.99977522],
       [0.99977522, 1.        ]])

#15.0min
array([[1.        , 0.99956926],
       [0.99956926, 1.        ]])


# In[50]:


import pandas as pd
import numpy as np
import matplotlib.pyplot as pt

time = pd.Series([1.5, 3.0, 4.5, 6.0, 7.5, 9.0, 15.0])
corrCoef = pd.Series([0.99755617, 0.99885254, 0.99905536, 0.99944236, 0.99965775, 0.99977522, 0.99956926])

pt.scatter(time, corrCoef)
pt.plot(np.unique(time), np.poly1d(np.polyfit(time, corrCoef, 1))(np.unique(time)), color = 'green')

pt.title("Timex Sensitivity Analysis: Image Correlation of Various Sampling Schemes")
pt.xlabel("Sample Duration (min)")
pt.ylabel("Pearson Correlation Coefficient")

pt.savefig('/media/frfuser/FRF_ConnorG/KevinMartinsMiniArgusTest/1663948741409/CamBob_B_Output/img_correlation/B_img_correlation_10min_mask.tiff', bbox_inches = 'tight')


# Scenario 5 

# In[39]:


### Scenario 5

import cv2
import numpy as np

#downsampledMask
downsampledTimex = r'/media/frfuser/FRF_ConnorG/KevinMartinsMiniArgusTest/1664117941403/CamBob_B_Output/timex_oblique/B_90x_10s_15.0min.tiff'

image = cv2.imread(downsampledTimex, 0)

mask = np.zeros(image.shape[:2], np.uint8)
mask[250:1500, 0:4096] = 255
img1 = cv2.bitwise_and(image,image,mask=mask)

######################################################

#benchmarkMask
benchmark = r'/media/frfuser/FRF_ConnorG/KevinMartinsMiniArgusTest/1664117941403/CamBob_B_Output/img_correlation/B_10min_2hz_test.tiff'

image = cv2.imread(benchmark, 0)

mask = np.zeros(image.shape[:2], np.uint8)
mask[250:1500, 0:4096] = 255
img2 = cv2.bitwise_and(image,image,mask=mask)

np.corrcoef(img1.flatten(), img2.flatten())


# In[ ]:


### Scenario 5 Outputs 


#1.5min
array([[1.        , 0.99227889],
       [0.99227889, 1.        ]])

#3.0min
array([[1.        , 0.99629077],
       [0.99629077, 1.        ]])

#4.5min
array([[1.        , 0.99857537],
       [0.99857537, 1.        ]])

#6.0min
array([[1.        , 0.99940459],
       [0.99940459, 1.        ]])

#7.5min
array([[1.        , 0.99966612],
       [0.99966612, 1.        ]])

#9.0min
array([[1.        , 0.99979091],
       [0.99979091, 1.        ]])

#15.0min
array([[1.        , 0.99964341],
       [0.99964341, 1.        ]])


# In[51]:


import pandas as pd
import numpy as np
import matplotlib.pyplot as pt

time = pd.Series([1.5, 3.0, 4.5, 6.0, 7.5, 9.0, 15.0])
corrCoef = pd.Series([0.99227889, 0.99629077, 0.99857537, 0.99940459, 0.99966612, 0.99979091, 0.99964341])

pt.scatter(time, corrCoef)
pt.plot(np.unique(time), np.poly1d(np.polyfit(time, corrCoef, 1))(np.unique(time)), color = 'green')

pt.title("Timex Sensitivity Analysis: Image Correlation of Various Sampling Schemes")
pt.xlabel("Sample Duration (min)")
pt.ylabel("Pearson Correlation Coefficient")

pt.savefig('/media/frfuser/FRF_ConnorG/KevinMartinsMiniArgusTest/1664117941403/CamBob_B_Output/img_correlation/B_img_correlation_10min_mask.tiff', bbox_inches = 'tight')


# Scenario 6 

# In[46]:


### Scenario 6

import cv2
import numpy as np

#downsampledMask
downsampledTimex = r'/media/frfuser/FRF_ConnorG/KevinMartinsMiniArgusTest/1664395141403/CamBob_B_Output/timex_oblique/B_90x_10s_15.0min.tiff'

image = cv2.imread(downsampledTimex, 0)

mask = np.zeros(image.shape[:2], np.uint8)
mask[250:1500, 0:4096] = 255
img1 = cv2.bitwise_and(image,image,mask=mask)

######################################################

#benchmarkMask
benchmark = r'/media/frfuser/FRF_ConnorG/KevinMartinsMiniArgusTest/1664395141403/CamBob_B_Output/img_correlation/B_10min_2hz_test.tiff'

image = cv2.imread(benchmark, 0)

mask = np.zeros(image.shape[:2], np.uint8)
mask[250:1500, 0:4096] = 255
img2 = cv2.bitwise_and(image,image,mask=mask)

np.corrcoef(img1.flatten(), img2.flatten())


# In[ ]:


### Scenario 6 Outputs 


#1.5min
array([[1.        , 0.99901135],
       [0.99901135, 1.        ]])

#3.0min
array([[1.        , 0.99938951],
       [0.99938951, 1.        ]])

#4.5min
array([[1.        , 0.99960797],
       [0.99960797, 1.        ]])

#6.0min
array([[1.        , 0.99970127],
       [0.99970127, 1.        ]])

#7.5min
array([[1.        , 0.99974967],
       [0.99974967, 1.        ]])

#9.0min
array([[1.        , 0.99982407],
       [0.99982407, 1.        ]])

#15.0min
array([[1.        , 0.99967138],
       [0.99967138, 1.        ]])


# In[52]:


import pandas as pd
import numpy as np
import matplotlib.pyplot as pt

time = pd.Series([1.5, 3.0, 4.5, 6.0, 7.5, 9.0, 15.0])
corrCoef = pd.Series([0.99901135, 0.99938951, 0.99960797, 0.99970127, 0.99974967, 0.99982407, 0.99967138])

pt.scatter(time, corrCoef)
pt.plot(np.unique(time), np.poly1d(np.polyfit(time, corrCoef, 1))(np.unique(time)), color = 'green')

pt.title("Timex Sensitivity Analysis: Image Correlation of Various Sampling Schemes")
pt.xlabel("Sample Duration (min)")
pt.ylabel("Pearson Correlation Coefficient")

pt.savefig('/media/frfuser/FRF_ConnorG/KevinMartinsMiniArgusTest/1664395141403/CamBob_B_Output/img_correlation/B_img_correlation_10min_mask.tiff', bbox_inches = 'tight')


# In[ ]:




