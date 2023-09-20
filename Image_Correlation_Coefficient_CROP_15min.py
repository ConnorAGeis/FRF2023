#!/usr/bin/env python
# coding: utf-8

# In[10]:


### Scenario 1 

import os
import numpy as np
import cv2

# Argus Timex. Path. 10mins, 2Hz, Indices = (30,1230)
img1 = r'/media/frfuser/FRF_ConnorG/KevinMartinsMiniArgusTest/1663005397544g/CamBob_B_Output/cRop/B_15min_2hz.tiff'
img1 = cv2.imread(img1)

# Subsampled Timex. Path. Indices = ()
img2 = r'/media/frfuser/FRF_ConnorG/KevinMartinsMiniArgusTest/1663005397544g/CamBob_B_Output/cRop/B_90x_6s_9.0min.tiff'
img2 = cv2.imread(img2)

#1.5min
np.corrcoef(img1.flatten(), img2.flatten())

#3.0min



#4.5min



#6.0min



#7.5min



#9.0min



#15.0min


# In[ ]:


### Scenario 1


#1.5min
array([[1.       , 0.9807294],
       [0.9807294, 1.       ]])

#3.0min
array([[1.        , 0.98745765],
       [0.98745765, 1.        ]])

#4.5min
array([[1.        , 0.98892482],
       [0.98892482, 1.        ]])

#6.0min
array([[1.        , 0.99166956],
       [0.99166956, 1.        ]])

#7.5min
array([[1.        , 0.99438544],
       [0.99438544, 1.        ]])

#9.0min
array([[1.        , 0.99574409],
       [0.99574409, 1.        ]])

#15.0min
array([[1.        , 0.99836963],
       [0.99836963, 1.        ]])


# In[11]:


import pandas as pd
import numpy as np
import matplotlib.pyplot as pt

time = pd.Series([1.5, 3.0, 4.5, 6.0, 7.5, 9.0, 15.0])
corrCoef = pd.Series([0.9807294, 0.98745765, 0.98892482, 0.99166956, 0.99438544, 0.99574409, 0.99836963])

pt.scatter(time, corrCoef)
pt.plot(np.unique(time), np.poly1d(np.polyfit(time, corrCoef, 1))(np.unique(time)), color = 'green')

pt.title("Timex Sensitivity Analysis: Image Correlation of Various Sampling Schemes")
pt.xlabel("Sample Duration (s)")
pt.ylabel("Pearson Correlation Coefficient")

pt.savefig('/media/frfuser/FRF_ConnorG/KevinMartinsMiniArgusTest/1663005397544g/CamBob_B_Output/img_correlation/B_img_correlation_crop_15min.tiff', bbox_inches = 'tight')


# In[18]:


### Scenario 2

import os
import numpy as np
import cv2

# Argus Timex. Path. 10mins, 2Hz, Indices = (30,1230)
img1 = r'/media/frfuser/FRF_ConnorG/KevinMartinsMiniArgusTest/1663080831409g/CamBob_B_Output/cRop/B_15min_2hz.tiff'
img1 = cv2.imread(img1)

# Subsampled Timex. Path. Indices = ()
img2 = r'/media/frfuser/FRF_ConnorG/KevinMartinsMiniArgusTest/1663080831409g/CamBob_B_Output/cRop/B_90x_10s_15.0min.tiff'
img2 = cv2.imread(img2)

#1.5min
np.corrcoef(img1.flatten(), img2.flatten())


# In[ ]:


### Scenario 2


#1.5min
array([[1.        , 0.98343227],
       [0.98343227, 1.        ]])

#3.0min
array([[1.        , 0.98863581],
       [0.98863581, 1.        ]])

#4.5min
array([[1.        , 0.98910536],
       [0.98910536, 1.        ]])

#6.0min
array([[1.        , 0.99385831],
       [0.99385831, 1.        ]])

#7.5min
array([[1.        , 0.99557041],
       [0.99557041, 1.        ]])

#9.0min
array([[1.        , 0.99583854],
       [0.99583854, 1.        ]])

#15.0min
array([[1.        , 0.99802967],
       [0.99802967, 1.        ]])


# In[19]:


import pandas as pd
import numpy as np
import matplotlib.pyplot as pt

time = pd.Series([1.5, 3.0, 4.5, 6.0, 7.5, 9.0, 15.0])
corrCoef = pd.Series([0.98343227, 0.98863581, 0.98910536, 0.99385831, 0.99557041, 0.99583854, 0.99802967])

pt.scatter(time, corrCoef)
pt.plot(np.unique(time), np.poly1d(np.polyfit(time, corrCoef, 1))(np.unique(time)), color = 'green')

pt.title("Timex Sensitivity Analysis: Image Correlation of Various Sampling Schemes")
pt.xlabel("Sample Duration (min)")
pt.ylabel("Pearson Correlation Coefficient")

pt.savefig('/media/frfuser/FRF_ConnorG/KevinMartinsMiniArgusTest/1663080831409g/CamBob_B_Output/img_correlation/B_img_correlation_crop_15min.tiff', bbox_inches = 'tight')


# In[26]:


### Scenario 3

import os
import numpy as np
import cv2

# Argus Timex. Path. 10mins, 2Hz, Indices = (30,1230)
img1 = r'/media/frfuser/FRF_ConnorG/KevinMartinsMiniArgusTest/1663869541385/CamBob_B_Output/cRop/B_15min_2hz.tiff'
img1 = cv2.imread(img1)

# Subsampled Timex. Path. Indices = ()
img2 = r'/media/frfuser/FRF_ConnorG/KevinMartinsMiniArgusTest/1663869541385/CamBob_B_Output/cRop/B_90x_10s_15.0min.tiff'
img2 = cv2.imread(img2)

#1.5min
np.corrcoef(img1.flatten(), img2.flatten())


# In[ ]:


### Scenario 3


#1.5min
array([[1.        , 0.98247026],
       [0.98247026, 1.        ]])

#3.0min
array([[1.        , 0.99646118],
       [0.99646118, 1.        ]])

#4.5min
array([[1.       , 0.9972726],
       [0.9972726, 1.       ]])

#6.0min
array([[1.        , 0.99737253],
       [0.99737253, 1.        ]])

#7.5min
array([[1.        , 0.99824067],
       [0.99824067, 1.        ]])

#9.0min
array([[1.        , 0.99824226],
       [0.99824226, 1.        ]])

#15.0min
array([[1.        , 0.99824849],
       [0.99824849, 1.        ]])


# In[27]:


import pandas as pd
import numpy as np
import matplotlib.pyplot as pt

time = pd.Series([1.5, 3.0, 4.5, 6.0, 7.5, 9.0, 15.0])
corrCoef = pd.Series([0.98247026, 0.99646118, 0.9972726, 0.99737253, 0.99824067, 0.99824226, 0.99824849])

pt.scatter(time, corrCoef)
pt.plot(np.unique(time), np.poly1d(np.polyfit(time, corrCoef, 1))(np.unique(time)), color = 'green')

pt.title("Timex Sensitivity Analysis: Image Correlation of Various Sampling Schemes")
pt.xlabel("Sample Duration (min)")
pt.ylabel("Pearson Correlation Coefficient")

pt.savefig('/media/frfuser/FRF_ConnorG/KevinMartinsMiniArgusTest/1663869541385/CamBob_B_Output/img_correlation/B_img_correlation_crop_15min.tiff', bbox_inches = 'tight')



# In[34]:


### Scenario 4

import os
import numpy as np
import cv2

# Argus Timex. Path. 10mins, 2Hz, Indices = (30,1230)
img1 = r'/media/frfuser/FRF_ConnorG/KevinMartinsMiniArgusTest/1663948741409/CamBob_B_Output/cRop/B_15min_2hz.tiff'
img1 = cv2.imread(img1)

# Subsampled Timex. Path. Indices = ()
img2 = r'/media/frfuser/FRF_ConnorG/KevinMartinsMiniArgusTest/1663948741409/CamBob_B_Output/cRop/B_90x_10s_15.0min.tiff'
img2 = cv2.imread(img2)

#1.5min
np.corrcoef(img1.flatten(), img2.flatten())


# In[ ]:


### Scenario 4


#1.5min
array([[1.        , 0.97835833],
       [0.97835833, 1.        ]])

#3.0min
array([[1.        , 0.98920683],
       [0.98920683, 1.        ]])

#4.5min
array([[1.        , 0.99040534],
       [0.99040534, 1.        ]])

#6.0min
array([[1.        , 0.99380566],
       [0.99380566, 1.        ]])

#7.5min
array([[1.        , 0.99545742],
       [0.99545742, 1.        ]])

#9.0min
array([[1.        , 0.99661618],
       [0.99661618, 1.        ]])

#15.0min
array([[1.        , 0.99794546],
       [0.99794546, 1.        ]])


# In[36]:


import pandas as pd
import numpy as np
import matplotlib.pyplot as pt

time = pd.Series([1.5, 3.0, 4.5, 6.0, 7.5, 9.0, 15.0])
corrCoef = pd.Series([0.97835833, 0.98920683, 0.99040534, 0.99380566, 0.99545742, 0.99661618, 0.99794546])

pt.scatter(time, corrCoef)
pt.plot(np.unique(time), np.poly1d(np.polyfit(time, corrCoef, 1))(np.unique(time)), color = 'green')

pt.title("Timex Sensitivity Analysis: Image Correlation of Various Sampling Schemes")
pt.xlabel("Sample Duration (min)")
pt.ylabel("Pearson Correlation Coefficient")

pt.savefig('/media/frfuser/FRF_ConnorG/KevinMartinsMiniArgusTest/1663948741409/CamBob_B_Output/img_correlation/B_img_correlation_crop_15min.tiff', bbox_inches = 'tight')


# In[52]:


### Scenario 5

import os
import numpy as np
import cv2

# Argus Timex. Path. 10mins, 2Hz, Indices = (30,1230)
img1 = r'/media/frfuser/FRF_ConnorG/KevinMartinsMiniArgusTest/1664117941403/CamBob_B_Output/cRop/B_15min_2hz.tiff'
img1 = cv2.imread(img1)

# Subsampled Timex. Path. Indices = ()
img2 = r'/media/frfuser/FRF_ConnorG/KevinMartinsMiniArgusTest/1664117941403/CamBob_B_Output/cRop/B_90x_10s_15.0min.tiff'
img2 = cv2.imread(img2)

#1.5min
np.corrcoef(img1.flatten(), img2.flatten())


# In[ ]:


### Scenario 5


#1.5min
array([[1.        , 0.94108007],
       [0.94108007, 1.        ]])

#3.0min
array([[1.        , 0.96947447],
       [0.96947447, 1.        ]])

#4.5min
array([[1.        , 0.98600082],
       [0.98600082, 1.        ]])

#6.0min
array([[1.        , 0.99259571],
       [0.99259571, 1.        ]])

#7.5min
array([[1.        , 0.99479129],
       [0.99479129, 1.        ]])

#9.0min
array([[1.       , 0.9962139],
       [0.9962139, 1.       ]])

#15.0min
array([[1.        , 0.99878122],
       [0.99878122, 1.        ]])


# In[53]:


import pandas as pd
import numpy as np
import matplotlib.pyplot as pt

time = pd.Series([1.5, 3.0, 4.5, 6.0, 7.5, 9.0, 15.0])
corrCoef = pd.Series([0.94108007, 0.96947447, 0.98600082, 0.99259571, 0.99479129, 0.9962139, 0.99878122])

pt.scatter(time, corrCoef)
pt.plot(np.unique(time), np.poly1d(np.polyfit(time, corrCoef, 1))(np.unique(time)), color = 'green')

pt.title("Timex Sensitivity Analysis: Image Correlation of Various Sampling Schemes")
pt.xlabel("Sample Duration (min)")
pt.ylabel("Pearson Correlation Coefficient")

pt.savefig('/media/frfuser/FRF_ConnorG/KevinMartinsMiniArgusTest/1664117941403/CamBob_B_Output/img_correlation/B_img_correlation_crop_15min.tiff', bbox_inches = 'tight')


# In[60]:


### Scenario 6

import os
import numpy as np
import cv2

# Argus Timex. Path. 10mins, 2Hz, Indices = (30,1230)
img1 = r'/media/frfuser/FRF_ConnorG/KevinMartinsMiniArgusTest/1664395141403/CamBob_B_Output/cRop/B_15min_2hz.tiff'
img1 = cv2.imread(img1)

# Subsampled Timex. Path. Indices = ()
img2 = r'/media/frfuser/FRF_ConnorG/KevinMartinsMiniArgusTest/1664395141403/CamBob_B_Output/cRop/B_90x_10s_15.0min.tiff'
img2 = cv2.imread(img2)

#1.5min
np.corrcoef(img1.flatten(), img2.flatten())


# In[ ]:


### Scenario 6


#1.5min
array([[1.        , 0.99144156],
       [0.99144156, 1.        ]])

#3.0min
array([[1.        , 0.99429286],
       [0.99429286, 1.        ]])

#4.5min
array([[1.        , 0.99575178],
       [0.99575178, 1.        ]])

#6.0min
array([[1.        , 0.99653336],
       [0.99653336, 1.        ]])

#7.5min
array([[1.        , 0.99687352],
       [0.99687352, 1.        ]])

#9.0min
array([[1.        , 0.99763619],
       [0.99763619, 1.        ]])

#15.0min
array([[1.        , 0.99829377],
       [0.99829377, 1.        ]])


# In[61]:


import pandas as pd
import numpy as np
import matplotlib.pyplot as pt

time = pd.Series([1.5, 3.0, 4.5, 6.0, 7.5, 9.0, 15.0])
corrCoef = pd.Series([0.99144156, 0.99429286, 0.99575178, 0.99653336, 0.99687352, 0.99763619, 0.99829377])

pt.scatter(time, corrCoef)
pt.plot(np.unique(time), np.poly1d(np.polyfit(time, corrCoef, 1))(np.unique(time)), color = 'green')

pt.title("Timex Sensitivity Analysis: Image Correlation of Various Sampling Schemes")
pt.xlabel("Sample Duration (min)")
pt.ylabel("Pearson Correlation Coefficient")

pt.savefig('/media/frfuser/FRF_ConnorG/KevinMartinsMiniArgusTest/1664395141403/CamBob_B_Output/img_correlation/B_img_correlation_crop_15min.tiff', bbox_inches = 'tight')


# In[ ]:




