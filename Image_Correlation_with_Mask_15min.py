#!/usr/bin/env python
# coding: utf-8

# Scenario 1 

# In[7]:


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
benchmark = r'/media/frfuser/FRF_ConnorG/KevinMartinsMiniArgusTest/1663005397544g/CamBob_B_Output/img_correlation/B_15min_2hz_test.tiff'

image = cv2.imread(benchmark, 0)

mask = np.zeros(image.shape[:2], np.uint8)
mask[250:1500, 0:4096] = 255
img2 = cv2.bitwise_and(image,image,mask=mask)

np.corrcoef(img1.flatten(), img2.flatten())


# In[ ]:


### Scenario 1 Outputs 


#1.5min
array([[1.        , 0.99834932],
       [0.99834932, 1.        ]])

#3.0min
array([[1.        , 0.99896109],
       [0.99896109, 1.        ]])

#4.5min
array([[1.        , 0.99916181],
       [0.99916181, 1.        ]])

#6.0min
array([[1.       , 0.9993666],
       [0.9993666, 1.       ]])

#7.5min
array([[1.        , 0.99957813],
       [0.99957813, 1.        ]])

#9.0min
array([[1.        , 0.99968043],
       [0.99968043, 1.        ]])

#15.0min
array([[1.       , 0.9998794],
       [0.9998794, 1.       ]])


# In[8]:


import pandas as pd
import numpy as np
import matplotlib.pyplot as pt

time = pd.Series([1.5, 3.0, 4.5, 6.0, 7.5, 9.0, 15.0])
corrCoef = pd.Series([0.99834932, 0.99896109, 0.99916181, 0.9993666, 0.99957813, 0.99968043, 0.9998794])

pt.scatter(time, corrCoef)
pt.plot(np.unique(time), np.poly1d(np.polyfit(time, corrCoef, 1))(np.unique(time)), color = 'green')

pt.title("Timex Sensitivity Analysis: Image Correlation of Various Sampling Schemes")
pt.xlabel("Sample Duration (min)")
pt.ylabel("Pearson Correlation Coefficient")

pt.savefig('/media/frfuser/FRF_ConnorG/KevinMartinsMiniArgusTest/1663005397544g/CamBob_B_Output/img_correlation/B_img_correlation_15min_mask.tiff', bbox_inches = 'tight')


# Scenario 2 

# In[15]:


### Scenario 2

import cv2
import numpy as np

#downsampledMask
downsampledTimex = r'/media/frfuser/FRF_ConnorG/KevinMartinsMiniArgusTest/1663080831409g/CamBob_B_Output/timex_oblique/B_90x_10s_15.0min.tiff'

image = cv2.imread(downsampledTimex, 0)

mask = np.zeros(image.shape[:2], np.uint8)
mask[250:1500, 0:4096] = 255
img1 = cv2.bitwise_and(image,image,mask=mask)

######################################################

#benchmarkMask
benchmark = r'/media/frfuser/FRF_ConnorG/KevinMartinsMiniArgusTest/1663080831409g/CamBob_B_Output/img_correlation/B_15min_2hz_test.tiff'

image = cv2.imread(benchmark, 0)

mask = np.zeros(image.shape[:2], np.uint8)
mask[250:1500, 0:4096] = 255
img2 = cv2.bitwise_and(image,image,mask=mask)

np.corrcoef(img1.flatten(), img2.flatten())


# In[ ]:


### Scenario 2 Outputs 


#1.5min
array([[1.        , 0.99685843],
       [0.99685843, 1.        ]])

#3.0min
array([[1.        , 0.99792787],
       [0.99792787, 1.        ]])

#4.5min
array([[1.        , 0.99800708],
       [0.99800708, 1.        ]])

#6.0min
array([[1.        , 0.99906032],
       [0.99906032, 1.        ]])

#7.5min
array([[1.        , 0.99931491],
       [0.99931491, 1.        ]])

#9.0min
array([[1.        , 0.99936214],
       [0.99936214, 1.        ]])

#15.0min
array([[1.        , 0.99972289],
       [0.99972289, 1.        ]])


# In[16]:


import pandas as pd
import numpy as np
import matplotlib.pyplot as pt

time = pd.Series([1.5, 3.0, 4.5, 6.0, 7.5, 9.0, 15.0])
corrCoef = pd.Series([0.99685843, 0.99792787, 0.99800708, 0.99906032, 0.99931491, 0.99936214, 0.99972289])

pt.scatter(time, corrCoef)
pt.plot(np.unique(time), np.poly1d(np.polyfit(time, corrCoef, 1))(np.unique(time)), color = 'green')

pt.title("Timex Sensitivity Analysis: Image Correlation of Various Sampling Schemes")
pt.xlabel("Sample Duration (min)")
pt.ylabel("Pearson Correlation Coefficient")

pt.savefig('/media/frfuser/FRF_ConnorG/KevinMartinsMiniArgusTest/1663080831409g/CamBob_B_Output/img_correlation/B_img_correlation_15min_mask.tiff', bbox_inches = 'tight')


# Scenario 3 

# In[23]:


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
benchmark = r'/media/frfuser/FRF_ConnorG/KevinMartinsMiniArgusTest/1663869541385/CamBob_B_Output/img_correlation/B_15min_2hz_test.tiff'

image = cv2.imread(benchmark, 0)

mask = np.zeros(image.shape[:2], np.uint8)
mask[250:1500, 0:4096] = 255
img2 = cv2.bitwise_and(image,image,mask=mask)

np.corrcoef(img1.flatten(), img2.flatten())


# In[ ]:


### Scenario 3 Outputs 


#1.5min
array([[1.        , 0.99650262],
       [0.99650262, 1.        ]])

#3.0min
array([[1.       , 0.9992968],
       [0.9992968, 1.       ]])

#4.5min
array([[1.        , 0.99946399],
       [0.99946399, 1.        ]])

#6.0min
array([[1.        , 0.99948072],
       [0.99948072, 1.        ]])

#7.5min
array([[1.        , 0.99964996],
       [0.99964996, 1.        ]])

#9.0min
array([[1.        , 0.99964791],
       [0.99964791, 1.        ]])

#15.0min
array([[1.        , 0.99965524],
       [0.99965524, 1.        ]])


# In[24]:


import pandas as pd
import numpy as np
import matplotlib.pyplot as pt

time = pd.Series([1.5, 3.0, 4.5, 6.0, 7.5, 9.0, 15.0])
corrCoef = pd.Series([0.99650262, 0.9992968, 0.99946399, 0.99948072, 0.99964996, 0.99964791, 0.99965524])

pt.scatter(time, corrCoef)
pt.plot(np.unique(time), np.poly1d(np.polyfit(time, corrCoef, 1))(np.unique(time)), color = 'green')

pt.title("Timex Sensitivity Analysis: Image Correlation of Various Sampling Schemes")
pt.xlabel("Sample Duration (min)")
pt.ylabel("Pearson Correlation Coefficient")

pt.savefig('/media/frfuser/FRF_ConnorG/KevinMartinsMiniArgusTest/1663869541385/CamBob_B_Output/img_correlation/B_img_correlation_15min_mask.tiff', bbox_inches = 'tight')



# Scenario 4 

# In[31]:


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
benchmark = r'/media/frfuser/FRF_ConnorG/KevinMartinsMiniArgusTest/1663948741409/CamBob_B_Output/img_correlation/B_15min_2hz_test.tiff'

image = cv2.imread(benchmark, 0)

mask = np.zeros(image.shape[:2], np.uint8)
mask[250:1500, 0:4096] = 255
img2 = cv2.bitwise_and(image,image,mask=mask)

np.corrcoef(img1.flatten(), img2.flatten())


# In[ ]:


### Scenario 4 Outputs 


#1.5min
array([[1.       , 0.9974121],
       [0.9974121, 1.       ]])

#3.0min
array([[1.        , 0.99870395],
       [0.99870395, 1.        ]])

#4.5min
array([[1.        , 0.99884147],
       [0.99884147, 1.        ]])

#6.0min
array([[1.        , 0.99925373],
       [0.99925373, 1.        ]])

#7.5min
array([[1.        , 0.99945295],
       [0.99945295, 1.        ]])

#9.0min
array([[1.        , 0.99959123],
       [0.99959123, 1.        ]])

#15.0min
array([[1.        , 0.99975107],
       [0.99975107, 1.        ]])


# In[33]:


import pandas as pd
import numpy as np
import matplotlib.pyplot as pt

time = pd.Series([1.5, 3.0, 4.5, 6.0, 7.5, 9.0, 15.0])
corrCoef = pd.Series([0.9974121, 0.99870395, 0.99884147, 0.99925373, 0.99945295, 0.99959123, 0.99975107])

pt.scatter(time, corrCoef)
pt.plot(np.unique(time), np.poly1d(np.polyfit(time, corrCoef, 1))(np.unique(time)), color = 'green')

pt.title("Timex Sensitivity Analysis: Image Correlation of Various Sampling Schemes")
pt.xlabel("Sample Duration (min)")
pt.ylabel("Pearson Correlation Coefficient")

pt.savefig('/media/frfuser/FRF_ConnorG/KevinMartinsMiniArgusTest/1663948741409/CamBob_B_Output/img_correlation/B_img_correlation_15min_mask.tiff', bbox_inches = 'tight')


# Scenario 5 

# In[40]:


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
benchmark = r'/media/frfuser/FRF_ConnorG/KevinMartinsMiniArgusTest/1664117941403/CamBob_B_Output/img_correlation/B_15min_2hz_test.tiff'

image = cv2.imread(benchmark, 0)

mask = np.zeros(image.shape[:2], np.uint8)
mask[250:1500, 0:4096] = 255
img2 = cv2.bitwise_and(image,image,mask=mask)

np.corrcoef(img1.flatten(), img2.flatten())


# In[ ]:


### Scenario 5 Outputs 


#1.5min
array([[1.        , 0.99108402],
       [0.99108402, 1.        ]])

#3.0min
array([[1.        , 0.99538378],
       [0.99538378, 1.        ]])

#4.5min
array([[1.        , 0.99788414],
       [0.99788414, 1.        ]])

#6.0min
array([[1.        , 0.99887915],
       [0.99887915, 1.        ]])

#7.5min
array([[1.        , 0.99921022],
       [0.99921022, 1.        ]])

#9.0min
array([[1.        , 0.99942662],
       [0.99942662, 1.        ]])

#15.0min
array([[1.        , 0.99981529],
       [0.99981529, 1.        ]])


# In[41]:


import pandas as pd
import numpy as np
import matplotlib.pyplot as pt

time = pd.Series([1.5, 3.0, 4.5, 6.0, 7.5, 9.0, 15.0])
corrCoef = pd.Series([0.99108402, 0.99538378, 0.99788414, 0.99887915, 0.99921022, 0.99942662, 0.99981529])

pt.scatter(time, corrCoef)
pt.plot(np.unique(time), np.poly1d(np.polyfit(time, corrCoef, 1))(np.unique(time)), color = 'green')

pt.title("Timex Sensitivity Analysis: Image Correlation of Various Sampling Schemes")
pt.xlabel("Sample Duration (min)")
pt.ylabel("Pearson Correlation Coefficient")

pt.savefig('/media/frfuser/FRF_ConnorG/KevinMartinsMiniArgusTest/1664117941403/CamBob_B_Output/img_correlation/B_img_correlation_15min_mask.tiff', bbox_inches = 'tight')


# Scenario 6 

# In[48]:


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
benchmark = r'/media/frfuser/FRF_ConnorG/KevinMartinsMiniArgusTest/1664395141403/CamBob_B_Output/img_correlation/B_15min_2hz_test.tiff'

image = cv2.imread(benchmark, 0)

mask = np.zeros(image.shape[:2], np.uint8)
mask[250:1500, 0:4096] = 255
img2 = cv2.bitwise_and(image,image,mask=mask)

np.corrcoef(img1.flatten(), img2.flatten())


# In[ ]:


### Scenario 6 Outputs 


#1.5min
array([[1.        , 0.99886375],
       [0.99886375, 1.        ]])

#3.0min
array([[1.        , 0.99924037],
       [0.99924037, 1.        ]])

#4.5min
array([[1.        , 0.99942681],
       [0.99942681, 1.        ]])

#6.0min
array([[1.        , 0.99952697],
       [0.99952697, 1.        ]])

#7.5min
array([[1.        , 0.99957482],
       [0.99957482, 1.        ]])

#9.0min
array([[1.        , 0.99968196],
       [0.99968196, 1.        ]])

#15.0min
array([[1.        , 0.99977269],
       [0.99977269, 1.        ]])


# In[49]:


import pandas as pd
import numpy as np
import matplotlib.pyplot as pt

time = pd.Series([1.5, 3.0, 4.5, 6.0, 7.5, 9.0, 15.0])
corrCoef = pd.Series([0.99886375, 0.99924037, 0.99942681, 0.99952697, 0.99957482, 0.99968196, 0.99977269])

pt.scatter(time, corrCoef)
pt.plot(np.unique(time), np.poly1d(np.polyfit(time, corrCoef, 1))(np.unique(time)), color = 'green')

pt.title("Timex Sensitivity Analysis: Image Correlation of Various Sampling Schemes")
pt.xlabel("Sample Duration (min)")
pt.ylabel("Pearson Correlation Coefficient")

pt.savefig('/media/frfuser/FRF_ConnorG/KevinMartinsMiniArgusTest/1664395141403/CamBob_B_Output/img_correlation/B_img_correlation_15min_mask.tiff', bbox_inches = 'tight')


# In[ ]:




