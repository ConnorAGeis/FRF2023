#!/usr/bin/env python
# coding: utf-8

# In[5]:


### Collect 1 

import pandas as pd
import matplotlib.pyplot as plt

input_csv = r'/media/frfuser/FRF_ConnorG/KevinMartinsMiniArgusTest/1663005397544g/CamBob_B_Output/timeshift/tabular_data/corr_coeff_timeshift_1663005397544.csv'

data = pd.read_csv(input_csv)
title = 'Correlation Score: Collects That Fall Within Benchmark Image'
plt = data.plot.scatter(x= 'Duration (min)', y = 'Correlation Value', c = 'Majority in/out 10min@2hz Timex', title = title, colormap = 'viridis', ylim = (0.93,1), s=42)
#plt.savefig('/media/frfuser/FRF_ConnorG/KevinMartinsMiniArgusTest/1663005397544g/CamBob_B_Output/timeshift/B_img_correlation_inOut.png', bbox_inches = 'tight')


# In[30]:


### Collect 2 

import pandas as pd

input_csv = r'/media/frfuser/FRF_ConnorG/KevinMartinsMiniArgusTest/1663080831409g/CamBob_B_Output/timeshift/tabular_data/corr_coeff_timeshift_1663080831409.csv'

data = pd.read_csv(input_csv)
title = 'Correlation Score: Highlighting Collects That Fall Within Benchmark Image'
ax1 = data.plot.scatter(x= 'Duration (min)', y = 'Correlation Value', c = 'Majority in/out 10min@2hz Timex', title = title, colormap = 'viridis', ylim = (0.93,1), s=42)
#ax1 = data.plot.scatter(x= 'Duration (min)', y = 'Correlation Value', c = 'Majority in/out 10min@2hz Timex')
#ax1.sort_values('Duration (min)', inplace=True)


# In[31]:


### Collect 3

import pandas as pd

input_csv = r'/media/frfuser/FRF_ConnorG/KevinMartinsMiniArgusTest/1663869541385/CamBob_B_Output/timeshift/tabular_data/corr_coeff_timeshift_1663869541385.csv'

data = pd.read_csv(input_csv)
title = 'Correlation Score: Highlighting Collects That Fall Within Benchmark Image'
ax1 = data.plot.scatter(x= 'Duration (min)', y = 'Correlation Value', c = 'Majority in/out 10min@2hz Timex', title = title, colormap = 'viridis', ylim = (0.93,1), s=42)
#ax1 = data.plot.scatter(x= 'Duration (min)', y = 'Correlation Value', c = 'Majority in/out 10min@2hz Timex')
#ax1.sort_values('Duration (min)', inplace=True)


# In[32]:


### Collect 4 

import pandas as pd

input_csv = r'/media/frfuser/FRF_ConnorG/KevinMartinsMiniArgusTest/1663948741409/CamBob_B_Output/timeshift/tabular_data/corr_coeff_timeshift_1663948741409.csv'

data = pd.read_csv(input_csv)
title = 'Correlation Score: Highlighting Collects That Fall Within Benchmark Image'
ax1 = data.plot.scatter(x= 'Duration (min)', y = 'Correlation Value', c = 'Majority in/out 10min@2hz Timex', title = title, colormap = 'viridis', ylim = (0.93,1), s=42)
#ax1 = data.plot.scatter(x= 'Duration (min)', y = 'Correlation Value', c = 'Majority in/out 10min@2hz Timex')
#ax1.sort_values('Duration (min)', inplace=True)


# In[33]:


### Collect 5 

import pandas as pd

input_csv = r'/media/frfuser/FRF_ConnorG/KevinMartinsMiniArgusTest/1664117941403/CamBob_B_Output/timeshift/tabular_data/corr_coeff_timeshift_1664117941403.csv'

data = pd.read_csv(input_csv)
title = 'Correlation Score: Highlighting Collects That Fall Within Benchmark Image'
ax1 = data.plot.scatter(x= 'Duration (min)', y = 'Correlation Value', c = 'Majority in/out 10min@2hz Timex', title = title, colormap = 'viridis', ylim = (0.93,1), s=42)
#ax1 = data.plot.scatter(x= 'Duration (min)', y = 'Correlation Value', c = 'Majority in/out 10min@2hz Timex')
#ax1.sort_values('Duration (min)', inplace=True)


# In[34]:


### Collect 6 

import pandas as pd

input_csv = r'/media/frfuser/FRF_ConnorG/KevinMartinsMiniArgusTest/1664395141403/CamBob_B_Output/timeshift/tabular_data/corr_coeff_timeshift_1664395141403.csv'

data = pd.read_csv(input_csv)
title = 'Correlation Score: Highlighting Collects That Fall Within Benchmark Image'
ax1 = data.plot.scatter(x= 'Duration (min)', y = 'Correlation Value', c = 'Majority in/out 10min@2hz Timex', title = title, colormap = 'viridis', ylim = (0.93,1), s=42)
#ax1 = data.plot.scatter(x= 'Duration (min)', y = 'Correlation Value', c = 'Majority in/out 10min@2hz Timex')
#ax1.sort_values('Duration (min)', inplace=True)


# In[ ]:




