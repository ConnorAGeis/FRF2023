#!/usr/bin/env python
# coding: utf-8

# In[7]:


### Scenario 1 

import os
import numpy as np
import cv2

# Argus Timex. Path. 10mins, 2Hz, Indices = (30,1230)
img1 = r'/media/frfuser/FRF_ConnorG/KevinMartinsMiniArgusTest/1663005397544g/CamBob_B_Output/img_correlation/B_15min_2hz_test.tiff'
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
array([[1.       , 0.9531156],
       [0.9531156, 1.       ]])

#3.0min
array([[1.        , 0.95514557],
       [0.95514557, 1.        ]])

#4.5min
array([[1.       , 0.9556738],
       [0.9556738, 1.       ]])

#6.0min
array([[1.        , 0.95675336],
       [0.95675336, 1.        ]])

#7.5min
array([[1.        , 0.95757231],
       [0.95757231, 1.        ]])

#9.0min
array([[1.        , 0.95816116],
       [0.95816116, 1.        ]])

#15.0min
array([[1.        , 0.95903652],
       [0.95903652, 1.        ]])


# In[45]:


### Scenario 1 

import pandas as pd
import numpy as np
import matplotlib.pyplot as pt

time = pd.Series([1.5, 3.0, 4.5, 6.0, 7.5, 9.0, 15.0])
corrCoef = pd.Series([0.9531156, 0.95514557, 0.9556738, 0.95675336, 0.95757231, 0.95816116, 0.95903652])

pt.scatter(time, corrCoef)
pt.plot(np.unique(time), np.poly1d(np.polyfit(time, corrCoef, 1))(np.unique(time)), color = 'green')

pt.title("Timex Sensitivity Analysis: Image Correlation of Various Sampling Schemes")
pt.xlabel("Sample Interval (s)")
pt.ylabel("Pearson Correlation Coefficient")

pt.savefig('/media/frfuser/FRF_ConnorG/KevinMartinsMiniArgusTest/1663005397544g/CamBob_B_Output/img_correlation/B_img_correlation_15min.tiff', bbox_inches = 'tight')


# In[53]:


### Scenario 2

import os
import numpy as np
import cv2

# Argus Timex. Path. 10mins, 2Hz, Indices = (30,1230)
img1 = r'/media/frfuser/FRF_ConnorG/KevinMartinsMiniArgusTest/1663080831409g/CamBob_B_Output/img_correlation/B_15min_2hz_test.tiff'
img1 = cv2.imread(img1)

# Subsampled Timex. Path. Indices = ()
img2 = r'/media/frfuser/FRF_ConnorG/KevinMartinsMiniArgusTest/1663080831409g/CamBob_B_Output/timex_oblique/B_90x_10s_15.0min.tiff'
img2 = cv2.imread(img2)

#1.5min
np.corrcoef(img1.flatten(), img2.flatten())


# In[ ]:


### Scenario 2


#1.5min
array([[1.        , 0.96452748],
       [0.96452748, 1.        ]])

#3.0min
array([[1.       , 0.9666439],
       [0.9666439, 1.       ]])

#4.5min
array([[1.        , 0.96688742],
       [0.96688742, 1.        ]])

#6.0min
array([[1.        , 0.96768263],
       [0.96768263, 1.        ]])

#7.5min
array([[1.        , 0.96786106],
       [0.96786106, 1.        ]])

#9.0min
array([[1.        , 0.96778953],
       [0.96778953, 1.        ]])

#15.0min
array([[1.        , 0.96760704],
       [0.96760704, 1.        ]])


# In[46]:


### Scenario 2 

import pandas as pd
import numpy as np
import matplotlib.pyplot as pt

time = pd.Series([1.5, 3.0, 4.5, 6.0, 7.5, 9.0, 15.0])
corrCoef = pd.Series([0.96452748, 0.9666439, 0.96688742, 0.96768263, 0.96786106, 0.96778953, 0.96760704])

pt.scatter(time, corrCoef)
pt.plot(np.unique(time), np.poly1d(np.polyfit(time, corrCoef, 1))(np.unique(time)), color = 'green')

pt.title("Timex Sensitivity Analysis: Image Correlation of Various Sampling Schemes")
pt.xlabel("Sample Interval (s)")
pt.ylabel("Pearson Correlation Coefficient")

pt.savefig('/media/frfuser/FRF_ConnorG/KevinMartinsMiniArgusTest/1663080831409g/CamBob_B_Output/img_correlation/B_img_correlation_15min.tiff', bbox_inches = 'tight')


# In[22]:


### Scenario 3

import os
import numpy as np
import cv2

# Argus Timex. Path. 10mins, 2Hz, Indices = (30,1230)
img1 = r'/media/frfuser/FRF_ConnorG/KevinMartinsMiniArgusTest/1663869541385/CamBob_B_Output/img_correlation/B_15min_2hz_test.tiff'
img1 = cv2.imread(img1)

# Subsampled Timex. Path. Indices = ()
img2 = r'/media/frfuser/FRF_ConnorG/KevinMartinsMiniArgusTest/1663869541385/CamBob_B_Output/timex_oblique/B_90x_10s_15.0min.tiff'
img2 = cv2.imread(img2)

#1.5min
np.corrcoef(img1.flatten(), img2.flatten())


# In[ ]:


### Scenario 3


#1.5min
array([[1.        , 0.94758303],
       [0.94758303, 1.        ]])

#3.0min
array([[1.        , 0.95333017],
       [0.95333017, 1.        ]])

#4.5min
array([[1.        , 0.95408802],
       [0.95408802, 1.        ]])

#6.0min
array([[1.        , 0.95498537],
       [0.95498537, 1.        ]])

#7.5min
array([[1.        , 0.95565582],
       [0.95565582, 1.        ]])

#9.0min
array([[1.        , 0.95600242],
       [0.95600242, 1.        ]])

#15.0min
array([[1.        , 0.95671865],
       [0.95671865, 1.        ]])


# In[ ]:


### Scenario 3

import pandas as pd
import numpy as np
import matplotlib.pyplot as pt

time = pd.Series([1.5, 3.0, 4.5, 6.0, 7.5, 9.0, 15.0])
corrCoef = pd.Series([0.94758303, 0.95333017, 0.95408802, 0.95498537, 0.95565582, 0.95600242, 0.95671865])

pt.scatter(time, corrCoef)
pt.plot(np.unique(time), np.poly1d(np.polyfit(time, corrCoef, 1))(np.unique(time)), color = 'green')

pt.title("Timex Sensitivity Analysis: Image Correlation of Various Sampling Schemes")
pt.xlabel("Sample Interval (s)")
pt.ylabel("Pearson Correlation Coefficient")

pt.savefig('/media/frfuser/FRF_ConnorG/KevinMartinsMiniArgusTest/1663869541385/CamBob_B_Output/img_correlation/B_img_correlation.tiff', bbox_inches = 'tight')


# In[29]:


### Scenario 4

import os
import numpy as np
import cv2

# Argus Timex. Path. 10mins, 2Hz, Indices = (30,1230)
img1 = r'/media/frfuser/FRF_ConnorG/KevinMartinsMiniArgusTest/1663948741409/CamBob_B_Output/img_correlation/B_15min_2hz_test.tiff'
img1 = cv2.imread(img1)

# Subsampled Timex. Path. Indices = ()
img2 = r'/media/frfuser/FRF_ConnorG/KevinMartinsMiniArgusTest/1663948741409/CamBob_B_Output/timex_oblique/B_90x_10s_15.0min.tiff'
img2 = cv2.imread(img2)

#1.5min
np.corrcoef(img1.flatten(), img2.flatten())


# In[ ]:


### Scenario 4


#1.5min
array([[1.        , 0.93499571],
       [0.93499571, 1.        ]])

#3.0min
array([[1.        , 0.93704674],
       [0.93704674, 1.        ]])

#4.5min
array([[1.        , 0.93982338],
       [0.93982338, 1.        ]])

#6.0min
array([[1.        , 0.94110004],
       [0.94110004, 1.        ]])

#7.5min
array([[1.        , 0.94190777],
       [0.94190777, 1.        ]])

#9.0min
array([[1.        , 0.94257631],
       [0.94257631, 1.        ]])

#15.0min
array([[1.        , 0.94247763],
       [0.94247763, 1.        ]])


# In[ ]:


### Scenario 4

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


# In[36]:


### Scenario 5

import os
import numpy as np
import cv2

# Argus Timex. Path. 10mins, 2Hz, Indices = (30,1230)
img1 = r'/media/frfuser/FRF_ConnorG/KevinMartinsMiniArgusTest/1664117941403/CamBob_B_Output/img_correlation/B_15min_2hz_test.tiff'
img1 = cv2.imread(img1)

# Subsampled Timex. Path. Indices = ()
img2 = r'/media/frfuser/FRF_ConnorG/KevinMartinsMiniArgusTest/1664117941403/CamBob_B_Output/timex_oblique/B_90x_10s_15.0min.tiff'
img2 = cv2.imread(img2)

#1.5min
np.corrcoef(img1.flatten(), img2.flatten())


# In[ ]:


### Scenario 5


#1.5min
array([[1.        , 0.92468187],
       [0.92468187, 1.        ]])

#3.0min
array([[1.       , 0.9416543],
       [0.9416543, 1.       ]])

#4.5min
array([[1.        , 0.94740537],
       [0.94740537, 1.        ]])

#6.0min
array([[1.        , 0.94920805],
       [0.94920805, 1.        ]])
#7.5min
array([[1.        , 0.94960246],
       [0.94960246, 1.        ]])

#9.0min
array([[1.        , 0.94963354],
       [0.94963354, 1.        ]])

#15.0min
array([[1.        , 0.94881849],
       [0.94881849, 1.        ]])



# In[ ]:


### Scenario 5

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


# In[44]:


### Scenario 6

import os
import numpy as np
import cv2

# Argus Timex. Path. 10mins, 2Hz, Indices = (30,1230)
img1 = r'/media/frfuser/FRF_ConnorG/KevinMartinsMiniArgusTest/1664395141403/CamBob_B_Output/img_correlation/B_15min_2hz_test.tiff'
img1 = cv2.imread(img1)

# Subsampled Timex. Path. Indices = ()
img2 = r'/media/frfuser/FRF_ConnorG/KevinMartinsMiniArgusTest/1664395141403/CamBob_B_Output/timex_oblique/B_90x_10s_15.0min.tiff'
img2 = cv2.imread(img2)

#1.5min
np.corrcoef(img1.flatten(), img2.flatten())


# In[ ]:


### Scenario 6


#1.5min
array([[1.       , 0.9295607],
       [0.9295607, 1.       ]])

#3.0min
array([[1.        , 0.93249189],
       [0.93249189, 1.        ]])

#4.5min
array([[1.        , 0.93434996],
       [0.93434996, 1.        ]])

#6.0min
array([[1.        , 0.93569801],
       [0.93569801, 1.        ]])

#7.5min
array([[1.        , 0.93671419],
       [0.93671419, 1.        ]])

#9.0min
array([[1.        , 0.93773475],
       [0.93773475, 1.        ]])

#15.0min
array([[1.        , 0.93956158],
       [0.93956158, 1.        ]])


# In[ ]:


### Scenario 6 

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

