#!/usr/bin/env python
# coding: utf-8

# In[12]:


### Scenario 1 

import os
import numpy as np
import cv2

# Argus Timex. Path. 10mins, 2Hz, Indices = (30,1230)
img1 = r'/media/frfuser/FRF_ConnorG/KevinMartinsMiniArgusTest/1663005397544g/CamBob_B_Output/cRop/B_10min_2hz.tiff'
img1 = cv2.imread(img1)

# Subsampled Timex. Path. Indices = ()
img2 = r'/media/frfuser/FRF_ConnorG/KevinMartinsMiniArgusTest/1663005397544g/CamBob_B_Output/cRop/B_90x_4s_6.0min.tiff'
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
array([[1.        , 0.98208944],
       [0.98208944, 1.        ]])

#3.0min
array([[1.        , 0.98884687],
       [0.98884687, 1.        ]])

#4.5min
array([[1.        , 0.99250863],
       [0.99250863, 1.        ]])

#6.0min
array([[1.        , 0.99548605],
       [0.99548605, 1.        ]])

#7.5min
array([[1.        , 0.99760517],
       [0.99760517, 1.        ]])

#9.0min
array([[1.        , 0.99865503],
       [0.99865503, 1.        ]])

#15.0min
array([[1.        , 0.99603855],
       [0.99603855, 1.        ]])


# In[13]:


import pandas as pd
import numpy as np
import matplotlib.pyplot as pt

time = pd.Series([1.5, 3.0, 4.5, 6.0, 7.5, 9.0, 15.0])
corrCoef = pd.Series([0.98208944, 0.98884687, 0.99250863, 0.99548605, 0.99760517, 0.99865503, 0.99603855])

pt.scatter(time, corrCoef)
pt.plot(np.unique(time), np.poly1d(np.polyfit(time, corrCoef, 1))(np.unique(time)), color = 'green')

pt.title("Timex Sensitivity Analysis: Image Correlation of Various Sampling Schemes")
pt.xlabel("Sample Duration (s)")
pt.ylabel("Pearson Correlation Coefficient")

pt.savefig('/media/frfuser/FRF_ConnorG/KevinMartinsMiniArgusTest/1663005397544g/CamBob_B_Output/img_correlation/B_img_correlation_crop.tiff', bbox_inches = 'tight')


# In[20]:


### Scenario 2

import os
import numpy as np
import cv2

# Argus Timex. Path. 10mins, 2Hz, Indices = (30,1230)
img1 = r'/media/frfuser/FRF_ConnorG/KevinMartinsMiniArgusTest/1663080831409g/CamBob_B_Output/cRop/B_10min_2hz.tiff'
img1 = cv2.imread(img1)

# Subsampled Timex. Path. Indices = ()
img2 = r'/media/frfuser/FRF_ConnorG/KevinMartinsMiniArgusTest/1663080831409g/CamBob_B_Output/cRop/B_90x_10s_15.0min.tiff'
img2 = cv2.imread(img2)

#1.5min
np.corrcoef(img1.flatten(), img2.flatten())


# In[ ]:


### Scenario 2


#1.5min
array([[1.        , 0.98624003],
       [0.98624003, 1.        ]])

#3.0min
array([[1.        , 0.99131786],
       [0.99131786, 1.        ]])

#4.5min
array([[1.        , 0.99167292],
       [0.99167292, 1.        ]])

#6.0min
array([[1.        , 0.99582331],
       [0.99582331, 1.        ]])

#7.5min
array([[1.       , 0.9973299],
       [0.9973299, 1.       ]])

#9.0min
array([[1.        , 0.99760003],
       [0.99760003, 1.        ]])

#15.0min
array([[1.        , 0.99678246],
       [0.99678246, 1.        ]])


# In[21]:


import pandas as pd
import numpy as np
import matplotlib.pyplot as pt

time = pd.Series([1.5, 3.0, 4.5, 6.0, 7.5, 9.0, 15.0])
corrCoef = pd.Series([0.98624003, 0.99131786, 0.99167292, 0.99582331, 0.9973299, 0.99760003, 0.99678246])

pt.scatter(time, corrCoef)
pt.plot(np.unique(time), np.poly1d(np.polyfit(time, corrCoef, 1))(np.unique(time)), color = 'green')

pt.title("Timex Sensitivity Analysis: Image Correlation of Various Sampling Schemes")
pt.xlabel("Sample Duration (min)")
pt.ylabel("Pearson Correlation Coefficient")

pt.savefig('/media/frfuser/FRF_ConnorG/KevinMartinsMiniArgusTest/1663080831409g/CamBob_B_Output/img_correlation/B_img_correlation_crop.tiff', bbox_inches = 'tight')


# In[32]:


### Scenario 3

import os
import numpy as np
import cv2

# Argus Timex. Path. 10mins, 2Hz, Indices = (30,1230)
img1 = r'/media/frfuser/FRF_ConnorG/KevinMartinsMiniArgusTest/1663869541385/CamBob_B_Output/cRop/B_10min_2hz.tiff'
img1 = cv2.imread(img1)

# Subsampled Timex. Path. Indices = ()
img2 = r'/media/frfuser/FRF_ConnorG/KevinMartinsMiniArgusTest/1663869541385/CamBob_B_Output/cRop/B_90x_6s_9.0min.tiff'
img2 = cv2.imread(img2)

#1.5min
np.corrcoef(img1.flatten(), img2.flatten())


# In[ ]:


### Scenario 3


#1.5min
array([[1.        , 0.98410366],
       [0.98410366, 1.        ]])

#3.0min
array([[1.       , 0.9968692],
       [0.9968692, 1.       ]])

#4.5min
array([[1.        , 0.99792396],
       [0.99792396, 1.        ]])

#6.0min
array([[1.        , 0.99818618],
       [0.99818618, 1.        ]])

#7.5min
array([[1.        , 0.99879409],
       [0.99879409, 1.        ]])

#9.0min
array([[1.        , 0.99873107],
       [0.99873107, 1.        ]])

#15.0min
array([[1.        , 0.99780688],
       [0.99780688, 1.        ]])


# In[33]:


import pandas as pd
import numpy as np
import matplotlib.pyplot as pt

time = pd.Series([1.5, 3.0, 4.5, 6.0, 7.5, 9.0, 15.0])
corrCoef = pd.Series([0.98410366, 0.9968692, 0.99792396, 0.99818618, 0.99879409, 0.99873107, 0.99780688])

pt.scatter(time, corrCoef)
pt.plot(np.unique(time), np.poly1d(np.polyfit(time, corrCoef, 1))(np.unique(time)), color = 'green')

pt.title("Timex Sensitivity Analysis: Image Correlation of Various Sampling Schemes")
pt.xlabel("Sample Duration (min)")
pt.ylabel("Pearson Correlation Coefficient")

pt.savefig('/media/frfuser/FRF_ConnorG/KevinMartinsMiniArgusTest/1663869541385/CamBob_B_Output/img_correlation/B_img_correlation_crop.tiff', bbox_inches = 'tight')



# In[41]:


### Scenario 4

import os
import numpy as np
import cv2

# Argus Timex. Path. 10mins, 2Hz, Indices = (30,1230)
img1 = r'/media/frfuser/FRF_ConnorG/KevinMartinsMiniArgusTest/1663948741409/CamBob_B_Output/cRop/B_10min_2hz.tiff'
img1 = cv2.imread(img1)

# Subsampled Timex. Path. Indices = ()
img2 = r'/media/frfuser/FRF_ConnorG/KevinMartinsMiniArgusTest/1663948741409/CamBob_B_Output/cRop/B_90x_10s_15.0min.tiff'
img2 = cv2.imread(img2)

#1.5min
np.corrcoef(img1.flatten(), img2.flatten())


# In[ ]:


### Scenario 4


#1.5min
array([[1.        , 0.97963646],
       [0.97963646, 1.        ]])

#3.0min
array([[1.        , 0.99048652],
       [0.99048652, 1.        ]])

#4.5min
array([[1.       , 0.9922619],
       [0.9922619, 1.       ]])

#6.0min
array([[1.        , 0.99541227],
       [0.99541227, 1.        ]])

#7.5min
array([[1.        , 0.99718035],
       [0.99718035, 1.        ]])

#9.0min
array([[1.        , 0.99814253],
       [0.99814253, 1.        ]])

#15.0min
array([[1.       , 0.9964454],
       [0.9964454, 1.       ]])


# In[42]:


import pandas as pd
import numpy as np
import matplotlib.pyplot as pt

time = pd.Series([1.5, 3.0, 4.5, 6.0, 7.5, 9.0, 15.0])
corrCoef = pd.Series([0.97963646, 0.99048652, 0.9922619, 0.99541227, 0.99718035, 0.99814253, 0.9964454])

pt.scatter(time, corrCoef)
pt.plot(np.unique(time), np.poly1d(np.polyfit(time, corrCoef, 1))(np.unique(time)), color = 'green')

pt.title("Timex Sensitivity Analysis: Image Correlation of Various Sampling Schemes")
pt.xlabel("Sample Duration (min)")
pt.ylabel("Pearson Correlation Coefficient")

pt.savefig('/media/frfuser/FRF_ConnorG/KevinMartinsMiniArgusTest/1663948741409/CamBob_B_Output/img_correlation/B_img_correlation_crop.tiff', bbox_inches = 'tight')


# In[49]:


### Scenario 5

import os
import numpy as np
import cv2

# Argus Timex. Path. 10mins, 2Hz, Indices = (30,1230)
img1 = r'/media/frfuser/FRF_ConnorG/KevinMartinsMiniArgusTest/1664117941403/CamBob_B_Output/cRop/B_10min_2hz.tiff'
img1 = cv2.imread(img1)

# Subsampled Timex. Path. Indices = ()
img2 = r'/media/frfuser/FRF_ConnorG/KevinMartinsMiniArgusTest/1664117941403/CamBob_B_Output/cRop/B_90x_10s_15.0min.tiff'
img2 = cv2.imread(img2)

#1.5min
np.corrcoef(img1.flatten(), img2.flatten())


# In[ ]:


### Scenario 5


#1.5min
array([[1.        , 0.94878105],
       [0.94878105, 1.        ]])

#3.0min
array([[1.        , 0.97537574],
       [0.97537574, 1.        ]])

#4.5min
array([[1.        , 0.99053317],
       [0.99053317, 1.        ]])

#6.0min
array([[1.        , 0.99605368],
       [0.99605368, 1.        ]])

#7.5min
array([[1.        , 0.99779918],
       [0.99779918, 1.        ]])

#9.0min
array([[1.        , 0.99861766],
       [0.99861766, 1.        ]])

#15.0min
array([[1.        , 0.99764515],
       [0.99764515, 1.        ]])


# In[50]:


import pandas as pd
import numpy as np
import matplotlib.pyplot as pt

time = pd.Series([1.5, 3.0, 4.5, 6.0, 7.5, 9.0, 15.0])
corrCoef = pd.Series([0.94878105, 0.97537574, 0.99053317, 0.99605368, 0.99779918, 0.99861766, 0.99764515])

pt.scatter(time, corrCoef)
pt.plot(np.unique(time), np.poly1d(np.polyfit(time, corrCoef, 1))(np.unique(time)), color = 'green')

pt.title("Timex Sensitivity Analysis: Image Correlation of Various Sampling Schemes")
pt.xlabel("Sample Duration (min)")
pt.ylabel("Pearson Correlation Coefficient")

pt.savefig('/media/frfuser/FRF_ConnorG/KevinMartinsMiniArgusTest/1664117941403/CamBob_B_Output/img_correlation/B_img_correlation_crop.tiff', bbox_inches = 'tight')


# In[57]:


### Scenario 6

import os
import numpy as np
import cv2

# Argus Timex. Path. 10mins, 2Hz, Indices = (30,1230)
img1 = r'/media/frfuser/FRF_ConnorG/KevinMartinsMiniArgusTest/1664395141403/CamBob_B_Output/cRop/B_10min_2hz.tiff'
img1 = cv2.imread(img1)

# Subsampled Timex. Path. Indices = ()
img2 = r'/media/frfuser/FRF_ConnorG/KevinMartinsMiniArgusTest/1664395141403/CamBob_B_Output/cRop/B_90x_10s_15.0min.tiff'
img2 = cv2.imread(img2)

#1.5min
np.corrcoef(img1.flatten(), img2.flatten())


# In[ ]:


### Scenario 6


#1.5min
array([[1.        , 0.99246375],
       [0.99246375, 1.        ]])

#3.0min
array([[1.        , 0.99534692],
       [0.99534692, 1.        ]])

#4.5min
array([[1.        , 0.99702329],
       [0.99702329, 1.        ]])

#6.0min
array([[1.        , 0.99774796],
       [0.99774796, 1.        ]])

#7.5min
array([[1.        , 0.99810725],
       [0.99810725, 1.        ]])

#9.0min
array([[1.       , 0.9986602],
       [0.9986602, 1.       ]])

#15.0min
array([[1.        , 0.99751978],
       [0.99751978, 1.        ]])


# In[59]:


import pandas as pd
import numpy as np
import matplotlib.pyplot as pt

time = pd.Series([1.5, 3.0, 4.5, 6.0, 7.5, 9.0, 15.0])
corrCoef = pd.Series([0.99246375, 0.99534692, 0.99702329, 0.99774796, 0.99810725, 0.9986602, 0.99751978])

pt.scatter(time, corrCoef)
pt.plot(np.unique(time), np.poly1d(np.polyfit(time, corrCoef, 1))(np.unique(time)), color = 'green')

pt.title("Timex Sensitivity Analysis: Image Correlation of Various Sampling Schemes")
pt.xlabel("Sample Duration (min)")
pt.ylabel("Pearson Correlation Coefficient")

pt.savefig('/media/frfuser/FRF_ConnorG/KevinMartinsMiniArgusTest/1664395141403/CamBob_B_Output/img_correlation/B_img_correlation_crop.tiff', bbox_inches = 'tight')


# In[ ]:




