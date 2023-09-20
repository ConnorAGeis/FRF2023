#!/usr/bin/env python
# coding: utf-8

# In[5]:


### Folder2_1.5min

import os
import numpy as np
import cv2

# Argus Timex. Path. 10mins, 2Hz, Indices = (30,1230)
img1 = r'/media/frfuser/FRF_ConnorG/KevinMartinsMiniArgusTest/1663080831409g/CamBob_B_Output/timeshift_90s_analysis/b_5th_90.tiff'
img1 = cv2.imread(img1)

# Subsampled Timex. Path. Indices = ()
img2 = r'/media/frfuser/FRF_ConnorG/KevinMartinsMiniArgusTest/1663080831409g/CamBob_B_Output/timeshift_90s_analysis/B_10min_2hz_test.tiff'
img2 = cv2.imread(img2)

#1.5min
np.corrcoef(img1.flatten(), img2.flatten())


# In[ ]:


### Folder2_1.5min

0.965844

0.9667746

0.96459826

0.95737068

0.96405653


# In[12]:


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

time = pd.Series([1.5, 1.5, 1.5, 1.5, 1.5, 1.5])
corrCoef = pd.Series([0.96584519, 0.965844, 0.9667746, 0.96459826, 0.95737068, 0.96405653])

time1 = pd.Series([1.5, 3.0, 4.5, 6.0, 7.5, 9.0, 15.0])
corrCoef1 = pd.Series([0.96584519, 0.96787936, 0.96808663, 0.96856852, 0.96865045, 0.9685248, 0.96729304])

#for timeE, corrCoefE in zip(time, corrCoef):
    #plt.scatter(timeE, corrCoefE)

plt.scatter(time, corrCoef) 
plt.scatter(time1, corrCoef1)
#plt.plot(np.unique(time), np.poly1d(np.polyfit(time, corrCoef, 1))(np.unique(time)), color = 'green')

plt.title("Timex Sensitivity Analysis: Image Correlation of Various Sampling Schemes")
plt.xlabel("Sample Interval (s)")
plt.ylabel("Pearson Correlation Coefficient")

plt.savefig('/media/frfuser/FRF_ConnorG/KevinMartinsMiniArgusTest/1663080831409g/CamBob_B_Output/img_correlation/B_img_correlation_timeshift.tiff', bbox_inches = 'tight')


# In[8]:


import pandas as pd
import numpy as np
import matplotlib.pyplot as pt

time = pd.Series([1.5, 1.5, 1.5, 1.5, 1.5, 1.5])
corrCoef = pd.Series([0.96584519, 0.965844, 0.9667746, 0.96459826, 0.95737068, 0.96405653])

time = pd.Series([1.5, 3.0, 4.5, 6.0, 7.5, 9.0, 15.0]) 
corrCoef = pd.Series([0.96584519, 0.96787936, 0.96808663, 0.96856852, 0.96865045, 0.9685248, 0.96729304])


pt.scatter(time, corrCoef)
#pt.plot(np.unique(time), np.poly1d(np.polyfit(time, corrCoef, 1))(np.unique(time)), color = 'green')

pt.title("Timex Sensitivity Analysis: Image Correlation of Various Sampling Schemes")
pt.xlabel("Sample Interval (s)")
pt.ylabel("Pearson Correlation Coefficient")

pt.savefig('/media/frfuser/FRF_ConnorG/KevinMartinsMiniArgusTest/1663080831409g/CamBob_B_Output/img_correlation/B_img_correlation_timeshift.tiff', bbox_inches = 'tight')


# In[10]:


### Folder5_1.5min

import os
import numpy as np
import cv2

# Argus Timex. Path. 10mins, 2Hz, Indices = (30,1230)
img1 = r'/media/frfuser/FRF_ConnorG/KevinMartinsMiniArgusTest/1664117941403/CamBob_B_Output/timeshift_90s_analysis/B_10min_2hz_test.tiff'
img1 = cv2.imread(img1)

# Subsampled Timex. Path. Indices = ()
img2 = r'/media/frfuser/FRF_ConnorG/KevinMartinsMiniArgusTest/1664117941403/CamBob_B_Output/timeshift_90s_analysis/b_1st_90.tiff'
img2 = cv2.imread(img2)

#1.5min
np.corrcoef(img1.flatten(), img2.flatten())


# In[ ]:


### Folder5_1.5min

0.93805873

0.94594935

0.94781696

0.94576693

0.94509025


# In[13]:


import pandas as pd
import numpy as np
import matplotlib.pyplot as pt

time = pd.Series([1.5, 1.5, 1.5, 1.5, 1.5, 1.5])
corrCoef = pd.Series([0.93115025, 0.93805873, 0.94594935, 0.94781696, 0.94576693, 0.94509025])

time1 = pd.Series([1.5, 3.0, 4.5, 6.0, 7.5, 9.0, 15.0])
corrCoef1 = pd.Series([0.93115025, 0.94629724, 0.95099441, 0.95211558, 0.95210522, 0.95168365, 0.9490276])


plt.scatter(time, corrCoef) 
plt.scatter(time1, corrCoef1)
#pt.plot(np.unique(time), np.poly1d(np.polyfit(time, corrCoef, 1))(np.unique(time)), color = 'green')

pt.title("Timex Sensitivity Analysis: Image Correlation of Various Sampling Schemes")
pt.xlabel("Sample Interval (s)")
pt.ylabel("Pearson Correlation Coefficient")

pt.savefig('/media/frfuser/FRF_ConnorG/KevinMartinsMiniArgusTest/1664117941403/CamBob_B_Output/img_correlation/B_img_correlation_timeshift.tiff', bbox_inches = 'tight')


# In[ ]:




