#!/usr/bin/env python
# coding: utf-8

# In[23]:


### Collect 1 

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

input_csv = r'/media/frfuser/FRF_ConnorG/KevinMartinsMiniArgusTest/1663005397544g/CamBob_B_Output/timeshift/tabular_data/corr_coeff_timeshift_1663005397544_revise.csv'

data = pd.read_csv(input_csv)
title = 'Correlation Score: Collects That Fall Within Benchmark Image'
fig = sns.lmplot(data = data, x = 'Duration (min)', y = 'Correlation Value', hue = 'Majority in/out 10min@2hz Timex', palette = 'viridis_r').set(title = title)
plt.ylim(.93, 1)
#plt.savefig('/media/frfuser/FRF_ConnorG/KevinMartinsMiniArgusTest/1663005397544g/CamBob_B_Output/timeshift/B_img_correlation_inOut_SB.png', bbox_inches = 'tight')


# In[17]:


### Collect 2 

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

input_csv = r'/media/frfuser/FRF_ConnorG/KevinMartinsMiniArgusTest/1663080831409g/CamBob_B_Output/timeshift/tabular_data/corr_coeff_timeshift_1663080831409_revise.csv'

data = pd.read_csv(input_csv)
title = 'Correlation Score: Collects That Fall Within Benchmark Image'
fig = sns.lmplot(data = data, x = 'Duration (min)', y = 'Correlation Value', hue = 'Majority in/out 10min@2hz Timex').set(title = title)
plt.ylim(.93, 1)
plt.savefig('/media/frfuser/FRF_ConnorG/KevinMartinsMiniArgusTest/1663080831409g/CamBob_B_Output/timeshift/B_img_correlation_inOut_SB.png', bbox_inches = 'tight')


# In[16]:


### Collect 3 

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

input_csv = r'/media/frfuser/FRF_ConnorG/KevinMartinsMiniArgusTest/1663869541385/CamBob_B_Output/timeshift/tabular_data/corr_coeff_timeshift_1663869541385_revise.csv'

data = pd.read_csv(input_csv)
title = 'Correlation Score: Collects That Fall Within Benchmark Image'
fig = sns.lmplot(data = data, x = 'Duration (min)', y = 'Correlation Value', hue = 'Majority in/out 10min@2hz Timex').set(title = title)
plt.ylim(.93, 1)
plt.savefig('/media/frfuser/FRF_ConnorG/KevinMartinsMiniArgusTest/1663869541385/CamBob_B_Output/timeshift/B_img_correlation_inOut_SB.png', bbox_inches = 'tight')


# In[15]:


### Collect 4 

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

input_csv = r'/media/frfuser/FRF_ConnorG/KevinMartinsMiniArgusTest/1663948741409/CamBob_B_Output/timeshift/tabular_data/corr_coeff_timeshift_1663948741409_revise.csv'

data = pd.read_csv(input_csv)
title = 'Correlation Score: Collects That Fall Within Benchmark Image'
fig = sns.lmplot(data = data, x = 'Duration (min)', y = 'Correlation Value', hue = 'Majority in/out 10min@2hz Timex').set(title = title)
plt.ylim(.93, 1)
plt.savefig('/media/frfuser/FRF_ConnorG/KevinMartinsMiniArgusTest/1663948741409/CamBob_B_Output/timeshift/B_img_correlation_inOut_SB.png', bbox_inches = 'tight')


# In[14]:


### Collect 5 

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

input_csv = r'/media/frfuser/FRF_ConnorG/KevinMartinsMiniArgusTest/1664117941403/CamBob_B_Output/timeshift/tabular_data/corr_coeff_timeshift_1664117941403_revise.csv'

data = pd.read_csv(input_csv)
title = 'Correlation Score: Collects That Fall Within Benchmark Image'
fig = sns.lmplot(data = data, x = 'Duration (min)', y = 'Correlation Value', hue = 'Majority in/out 10min@2hz Timex').set(title = title)
plt.ylim(.93, 1)
plt.savefig('/media/frfuser/FRF_ConnorG/KevinMartinsMiniArgusTest/1664117941403/CamBob_B_Output/timeshift/B_img_correlation_inOut_SB.png', bbox_inches = 'tight')


# In[13]:


### Collect 6 

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

input_csv = r'/media/frfuser/FRF_ConnorG/KevinMartinsMiniArgusTest/1664395141403/CamBob_B_Output/timeshift/tabular_data/corr_coeff_timeshift_1664395141403_revise.csv'

data = pd.read_csv(input_csv)
title = 'Correlation Score: Collects That Fall Within Benchmark Image'
fig = sns.lmplot(data = data, x = 'Duration (min)', y = 'Correlation Value', hue = 'Majority in/out 10min@2hz Timex').set(title = title)
plt.ylim(.93, 1)
plt.savefig('/media/frfuser/FRF_ConnorG/KevinMartinsMiniArgusTest/1664395141403/CamBob_B_Output/timeshift/B_img_correlation_inOut_SB.png', bbox_inches = 'tight')


# In[ ]:




