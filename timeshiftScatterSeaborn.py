#!/usr/bin/env python
# coding: utf-8

# In[27]:


### Collect 1 

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

input_csv = r'/media/frfuser/FRF_ConnorG/KevinMartinsMiniArgusTest/1663005397544g/CamBob_B_Output/timeshift/tabular_data/corr_coeff_timeshift_1663005397544.csv'

data = pd.read_csv(input_csv)
title = 'Correlation Score: Timeshift (1-5)'
fig = sns.lmplot(data = data, x = 'Duration (min)', y = 'Correlation Value', hue = 'Timeshift', palette = 'RdYlGn').set(title = title)
plt.ylim(.93, 1)
#plt.savefig('/media/frfuser/FRF_ConnorG/KevinMartinsMiniArgusTest/1663005397544g/CamBob_B_Output/timeshift/B_img_correlation_order_SB.png', bbox_inches = 'tight')


# In[11]:


### Collect 2 

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

input_csv = r'/media/frfuser/FRF_ConnorG/KevinMartinsMiniArgusTest/1663080831409g/CamBob_B_Output/timeshift/tabular_data/corr_coeff_timeshift_1663080831409.csv'

data = pd.read_csv(input_csv)
title = 'Correlation Score: Timeshift (1-5)'
fig = sns.lmplot(data = data, x = 'Duration (min)', y = 'Correlation Value', hue = 'Timeshift').set(title = title)
plt.ylim(.93, 1)
plt.savefig('/media/frfuser/FRF_ConnorG/KevinMartinsMiniArgusTest/1663080831409g/CamBob_B_Output/timeshift/B_img_correlation_order_SB.png', bbox_inches = 'tight')


# In[12]:


### Collect 3 

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

input_csv = r'/media/frfuser/FRF_ConnorG/KevinMartinsMiniArgusTest/1663869541385/CamBob_B_Output/timeshift/tabular_data/corr_coeff_timeshift_1663869541385.csv'

data = pd.read_csv(input_csv)
title = 'Correlation Score: Timeshift (1-5)'
fig = sns.lmplot(data = data, x = 'Duration (min)', y = 'Correlation Value', hue = 'Timeshift').set(title = title)
plt.ylim(.93, 1)
plt.savefig('/media/frfuser/FRF_ConnorG/KevinMartinsMiniArgusTest/1663869541385/CamBob_B_Output/timeshift/B_img_correlation_order_SB.png', bbox_inches = 'tight')


# In[13]:


### Collect 4 

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

input_csv = r'/media/frfuser/FRF_ConnorG/KevinMartinsMiniArgusTest/1663948741409/CamBob_B_Output/timeshift/tabular_data/corr_coeff_timeshift_1663948741409.csv'

data = pd.read_csv(input_csv)
title = 'Correlation Score: Highlighting Collects That Fall Within Benchmark Image'
fig = sns.lmplot(data = data, x = 'Duration (min)', y = 'Correlation Value', hue = 'Timeshift').set(title = title)
plt.ylim(.93, 1)
plt.savefig('/media/frfuser/FRF_ConnorG/KevinMartinsMiniArgusTest/1663948741409/CamBob_B_Output/timeshift/B_img_correlation_order_SB.png', bbox_inches = 'tight')


# In[14]:


### Collect 5 

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

input_csv = r'/media/frfuser/FRF_ConnorG/KevinMartinsMiniArgusTest/1664117941403/CamBob_B_Output/timeshift/tabular_data/corr_coeff_timeshift_1664117941403.csv'

data = pd.read_csv(input_csv)
title = 'Correlation Score: Timeshift (1-5)'
fig = sns.lmplot(data = data, x = 'Duration (min)', y = 'Correlation Value', hue = 'Timeshift').set(title = title)
plt.ylim(.93, 1)
plt.savefig('/media/frfuser/FRF_ConnorG/KevinMartinsMiniArgusTest/1664117941403/CamBob_B_Output/timeshift/B_img_correlation_order_SB.png', bbox_inches = 'tight')


# In[15]:


### Collect 6 

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

input_csv = r'/media/frfuser/FRF_ConnorG/KevinMartinsMiniArgusTest/1664395141403/CamBob_B_Output/timeshift/tabular_data/corr_coeff_timeshift_1664395141403.csv'

data = pd.read_csv(input_csv)
title = 'Correlation Score: Timeshift (1-5)'
fig = sns.lmplot(data = data, x = 'Duration (min)', y = 'Correlation Value', hue = 'Timeshift').set(title = title)
plt.ylim(.93, 1)
plt.savefig('/media/frfuser/FRF_ConnorG/KevinMartinsMiniArgusTest/1664395141403/CamBob_B_Output/timeshift/B_img_correlation_order_SB.png', bbox_inches = 'tight')


# In[ ]:




