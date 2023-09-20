#!/usr/bin/env python
# coding: utf-8

# In[73]:


### Modify to make rectangle mask and apply to code above. Working Rectangle coordinates input below

import cv2
import numpy as np

#Name File as Variable
image = r'/media/frfuser/FRF_ConnorG/KevinMartinsMiniArgusTest/1664117941403/CamBob_B_Output/timex_oblique/B_90x_5s_7.5min.tiff'

#Read Image
image = cv2.imread(image, 0)

#Apply Mask
image = image[250:1500, 0:4096]

###Save Example
outImage = r"/media/frfuser/FRF_ConnorG/KevinMartinsMiniArgusTest/1664117941403/CamBob_B_Output/cRop/B_90x_5s_7.5min.tiff"
cv2.imwrite(outImage, image)


#Custom Window Size
#cv2.namedWindow("test", cv2.WINDOW_KEEPRATIO)
#cv2.imshow("test", image)
#cv2.resizeWindow("test", 1000, 1365)
#cv2.waitKey(0)
#cv2.destroyAllWindows()


# In[ ]:





# In[ ]:




