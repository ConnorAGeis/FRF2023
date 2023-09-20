#!/usr/bin/env python
# coding: utf-8

# In[14]:


### Scenario 1 

import os
import numpy as np
import cv2

# Argus Timex. Path. 10mins, 2Hz, Indices = (30,1230)
img1 = r'/media/frfuser/FRF_ConnorG/KevinMartinsMiniArgusTest/1663005397544g/CamBob_B_Output/img_correlation/B_10min_2hz_test.tiff'
img1 = cv2.imread(img1)

# Subsampled Timex. Path. Indices = ()
img2 = r'/media/frfuser/FRF_ConnorG/KevinMartinsMiniArgusTest/1663005397544g/CamBob_B_Output/timex_oblique/B_90x_10s_15.0min.tiff'
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
array([[1.        , 0.95347989],
       [0.95347989, 1.        ]])

#3.0min
array([[1.        , 0.95553379],
       [0.95553379, 1.        ]])

#4.5min
array([[1.        , 0.95641236],
       [0.95641236, 1.        ]])

#6.0min
array([[1.        , 0.95754348],
       [0.95754348, 1.        ]])

#7.5min
array([[1.        , 0.95827148],
       [0.95827148, 1.        ]])

#9.0min
array([[1.        , 0.95880825],
       [0.95880825, 1.        ]])

#15.0min
array([[1.        , 0.95872108],
       [0.95872108, 1.        ]])


# In[75]:


import pandas as pd
import numpy as np
import matplotlib.pyplot as pt

time = pd.Series([1.5, 3.0, 4.5, 6.0, 7.5, 9.0, 15.0])
corrCoef = pd.Series([0.95347989, 0.95553379, 0.95641236, 0.95754348, 0.95827148, 0.95880825, 0.95872108])

pt.scatter(time, corrCoef)
pt.plot(np.unique(time), np.poly1d(np.polyfit(time, corrCoef, 1))(np.unique(time)), color = 'green')

pt.title("Timex Sensitivity Analysis: Image Correlation of Various Sampling Schemes")
pt.xlabel("Sample Interval (s)")
pt.ylabel("Pearson Correlation Coefficient")

pt.savefig('/media/frfuser/FRF_ConnorG/KevinMartinsMiniArgusTest/1663005397544g/CamBob_B_Output/img_correlation/B_img_correlation.tiff', bbox_inches = 'tight')


# In[98]:


### Scenario 2

import os
import numpy as np
import cv2

# Argus Timex. Path. 10mins, 2Hz, Indices = (30,1230)
img1 = r'/media/frfuser/FRF_ConnorG/KevinMartinsMiniArgusTest/1663080831409g/CamBob_B_Output/img_correlation/B_10min_2hz_test.tiff'
img1 = cv2.imread(img1)

# Subsampled Timex. Path. Indices = ()
img2 = r'/media/frfuser/FRF_ConnorG/KevinMartinsMiniArgusTest/1663080831409g/CamBob_B_Output/timex_oblique/B_90x_10s_15.0min.tiff'
img2 = cv2.imread(img2)

#1.5min
np.corrcoef(img1.flatten(), img2.flatten())


# In[ ]:


### Scenario 2


#1.5min
array([[1.        , 0.96584519],
       [0.96584519, 1.        ]])

#3.0min
array([[1.       , 0.96787936],
       [0.9666439, 1.       ]])

#4.5min
array([[1.        , 0.96808663],
       [0.96787936, 1.        ]])

#6.0min
array([[1.        , 0.96856852],
       [0.96856852, 1.        ]])

#7.5min
array([[1.        , 0.96865045],
       [0.96865045, 1.        ]])

#9.0min
array([[1.       , 0.9685248],
       [0.9685248, 1.       ]])

#15.0min
array([[1.        , 0.96729304],
       [0.96729304, 1.        ]])


# In[2]:


import pandas as pd
import numpy as np
import matplotlib.pyplot as pt

time = pd.Series([1.5, 3.0, 4.5, 6.0, 7.5, 9.0, 15.0])
corrCoef = pd.Series([0.96584519, 0.96787936, 0.96808663, 0.96856852, 0.96865045, 0.9685248, 0.96729304])

pt.scatter(time, corrCoef)
pt.plot(np.unique(time), np.poly1d(np.polyfit(time, corrCoef, 1))(np.unique(time)), color = 'green')

pt.title("Timex Sensitivity Analysis: Image Correlation of Various Sampling Schemes")
pt.xlabel("Sample Duration (min)")
pt.ylabel("Pearson Correlation Coefficient")

pt.savefig('/media/frfuser/FRF_ConnorG/KevinMartinsMiniArgusTest/1663080831409g/CamBob_B_Output/img_correlation/B_img_correlation.tiff', bbox_inches = 'tight')


# In[2]:


### Scenario 3

import os
import numpy as np
import cv2

# Argus Timex. Path. 10mins, 2Hz, Indices = (30,1230)
img1 = r'/media/frfuser/FRF_ConnorG/KevinMartinsMiniArgusTest/1664117941403/CamBob_B_Output/timeshift_90s_analysis/B_10min_2hz_test.tiff'
img1 = cv2.imread(img1)

# Subsampled Timex. Path. Indices = ()
img2 = r'/media/frfuser/FRF_ConnorG/KevinMartinsMiniArgusTest/1664117941403/CamBob_B_Output/timeshift_90s_analysis/b_2nd_90.tiff'
img2 = cv2.imread(img2)

#1.5min
np.corrcoef(img1.flatten(), img2.flatten())


# In[ ]:


### Scenario 3


#1.5min
array([[1.        , 0.93805873],
       [0.93805873, 1.        ]])

#3.0min
array([[1.        , 0.94594935],
       [0.94594935, 1.        ]])

#4.5min
array([[1.        , 0.95559601],
       [0.95559601, 1.        ]])

#6.0min
array([[1.        , 0.95641847],
       [0.95641847, 1.        ]])

#7.5min
array([[1.        , 0.95680502],
       [0.95680502, 1.        ]])

#9.0min
array([[1.        , 0.95690172],
       [0.95690172, 1.        ]])

#15.0min
array([[1.        , 0.95603108],
       [0.95603108, 1.        ]])


# In[87]:


import pandas as pd
import numpy as np
import matplotlib.pyplot as pt

time = pd.Series([1.5, 3.0, 4.5, 6.0, 7.5, 9.0, 15.0])
corrCoef = pd.Series([0.94963067, 0.95480452, 0.95559601, 0.95641847, 0.95680502, 0.95690172, 0.95603108])

pt.scatter(time, corrCoef)
pt.plot(np.unique(time), np.poly1d(np.polyfit(time, corrCoef, 1))(np.unique(time)), color = 'green')

pt.title("Timex Sensitivity Analysis: Image Correlation of Various Sampling Schemes")
pt.xlabel("Sample Interval (s)")
pt.ylabel("Pearson Correlation Coefficient")

pt.savefig('/media/frfuser/FRF_ConnorG/KevinMartinsMiniArgusTest/1663869541385/CamBob_B_Output/img_correlation/B_img_correlation.tiff', bbox_inches = 'tight')



# In[38]:


### Scenario 4

import os
import numpy as np
import cv2

# Argus Timex. Path. 10mins, 2Hz, Indices = (30,1230)
img1 = r'/media/frfuser/FRF_ConnorG/KevinMartinsMiniArgusTest/1663948741409/CamBob_B_Output/img_correlation/B_10min_2hz_test.tiff'
img1 = cv2.imread(img1)

# Subsampled Timex. Path. Indices = ()
img2 = r'/media/frfuser/FRF_ConnorG/KevinMartinsMiniArgusTest/1663948741409/CamBob_B_Output/timex_oblique/B_90x_10s_15.0min.tiff'
img2 = cv2.imread(img2)

#1.5min
np.corrcoef(img1.flatten(), img2.flatten())


# In[ ]:


### Scenario 4


#1.5min
array([[1.        , 0.93642403],
       [0.93642403, 1.        ]])

#3.0min
array([[1.        , 0.93863762],
       [0.93863762, 1.        ]])

#4.5min
array([[1.        , 0.94183601],
       [0.94183601, 1.        ]])

#6.0min
array([[1.        , 0.94288619],
       [0.94288619, 1.        ]])

#7.5min
array([[1.        , 0.94354752],
       [0.94354752, 1.        ]])

#9.0min
array([[1.        , 0.94395261],
       [0.94395261, 1.        ]])

#15.0min
array([[1.        , 0.94205275],
       [0.94205275, 1.        ]])


# In[88]:


import pandas as pd
import numpy as np
import matplotlib.pyplot as pt

time = pd.Series([1.5, 3.0, 4.5, 6.0, 7.5, 9.0, 15.0])
corrCoef = pd.Series([0.93642403, 0.93863762, 0.94183601, 0.94288619, 0.94354752, 0.94395261, 0.94205275])

pt.scatter(time, corrCoef)
pt.plot(np.unique(time), np.poly1d(np.polyfit(time, corrCoef, 1))(np.unique(time)), color = 'green')

pt.title("Timex Sensitivity Analysis: Image Correlation of Various Sampling Schemes")
pt.xlabel("Sample Interval (s)")
pt.ylabel("Pearson Correlation Coefficient")

pt.savefig('/media/frfuser/FRF_ConnorG/KevinMartinsMiniArgusTest/1663948741409/CamBob_B_Output/img_correlation/B_img_correlation.tiff', bbox_inches = 'tight')


# In[45]:


### Scenario 5

import os
import numpy as np
import cv2

# Argus Timex. Path. 10mins, 2Hz, Indices = (30,1230)
img1 = r'/media/frfuser/FRF_ConnorG/KevinMartinsMiniArgusTest/1664117941403/CamBob_B_Output/img_correlation/B_10min_2hz_test.tiff'
img1 = cv2.imread(img1)

# Subsampled Timex. Path. Indices = ()
img2 = r'/media/frfuser/FRF_ConnorG/KevinMartinsMiniArgusTest/1664117941403/CamBob_B_Output/timex_oblique/B_90x_10s_15.0min.tiff'
img2 = cv2.imread(img2)

#1.5min
np.corrcoef(img1.flatten(), img2.flatten())


# In[ ]:


### Scenario 5


#1.5min
array([[1.        , 0.93115025],
       [0.93115025, 1.        ]])

#3.0min
array([[1.        , 0.94629724],
       [0.94629724, 1.        ]])

#4.5min
array([[1.        , 0.95099441],
       [0.95099441, 1.        ]])

#6.0min
array([[1.        , 0.95211558],
       [0.95211558, 1.        ]])

#7.5min
array([[1.        , 0.95210522],
       [0.95210522, 1.        ]])

#9.0min
array([[1.        , 0.95168365],
       [0.95168365, 1.        ]])

#15.0min
array([[1.       , 0.9490276],
       [0.9490276, 1.       ]])



# In[1]:


import pandas as pd
import numpy as np
import matplotlib.pyplot as pt

time = pd.Series([1.5, 3.0, 4.5, 6.0, 7.5, 9.0, 15.0])
corrCoef = pd.Series([0.93115025, 0.94629724, 0.95099441, 0.95211558, 0.95210522, 0.95168365, 0.9490276])

pt.scatter(time, corrCoef)
pt.plot(np.unique(time), np.poly1d(np.polyfit(time, corrCoef, 1))(np.unique(time)), color = 'green')

pt.title("Timex Sensitivity Analysis: Image Correlation of Various Sampling Schemes")
pt.xlabel("Sample Duration (min)")
pt.ylabel("Pearson Correlation Coefficient")

pt.savefig('/media/frfuser/FRF_ConnorG/KevinMartinsMiniArgusTest/1664117941403/CamBob_B_Output/img_correlation/B_img_correlation.tiff', bbox_inches = 'tight')


# In[54]:


### Scenario 6

import os
import numpy as np
import cv2

# Argus Timex. Path. 10mins, 2Hz, Indices = (30,1230)
img1 = r'/media/frfuser/FRF_ConnorG/KevinMartinsMiniArgusTest/1664395141403/CamBob_B_Output/img_correlation/B_10min_2hz_test.tiff'
img1 = cv2.imread(img1)

# Subsampled Timex. Path. Indices = ()
img2 = r'/media/frfuser/FRF_ConnorG/KevinMartinsMiniArgusTest/1664395141403/CamBob_B_Output/timex_oblique/B_90x_10s_15.0min.tiff'
img2 = cv2.imread(img2)

#1.5min
np.corrcoef(img1.flatten(), img2.flatten())


# In[ ]:


### Scenario 6


#1.5min
array([[1.        , 0.93176331],
       [0.93176331, 1.        ]])

#3.0min
array([[1.        , 0.93460576],
       [0.93460576, 1.        ]])

#4.5min
array([[1.        , 0.93640438],
       [0.93640438, 1.        ]])

#6.0min
array([[1.        , 0.93758644],
       [0.93758644, 1.        ]])

#7.5min
array([[1.        , 0.93836047],
       [0.93836047, 1.        ]])

#9.0min
array([[1.        , 0.93897589],
       [0.93897589, 1.        ]])

#15.0min
array([[1.        , 0.93862836],
       [0.93862836, 1.        ]])


# In[2]:


import pandas as pd
import numpy as np
import matplotlib.pyplot as pt

time = pd.Series([1.5, 3.0, 4.5, 6.0, 7.5, 9.0, 15.0])
corrCoef = pd.Series([0.93176331, 0.93460576, 0.93640438, 0.93758644, 0.93836047, 0.93897589, 0.93862836])

pt.scatter(time, corrCoef)
pt.plot(np.unique(time), np.poly1d(np.polyfit(time, corrCoef, 1))(np.unique(time)), color = 'green')

pt.title("Timex Sensitivity Analysis: Image Correlation of Various Sampling Schemes")
pt.xlabel("Sample Interval (s)")
pt.ylabel("Pearson Correlation Coefficient")

pt.savefig('/media/frfuser/FRF_ConnorG/KevinMartinsMiniArgusTest/1664395141403/CamBob_B_Output/img_correlation/B_img_correlation.tiff', bbox_inches = 'tight')


# In[ ]:




