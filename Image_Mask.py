#!/usr/bin/env python
# coding: utf-8

# In[1]:


### Modify to make rectangle mask and apply to code above. Working Rectangle coordinates input below

import cv2
import numpy as np

#Name File as Variable
image = r'/media/frfuser/FRF_ConnorG/KevinMartinsMiniArgusTest/1663005397544g/CamBob_B_Output/img_correlation/B_10min_2hz.tiff'

#Read Image
image = cv2.imread(image, 0)

#Apply Mask
mask = np.zeros(image.shape[:2], np.uint8)
mask[250:1500, 0:4096] = 255
image = cv2.bitwise_and(image,image,mask=mask)


###Save Example
outImage = r"/media/frfuser/FRF_ConnorG/KevinMartinsMiniArgusTest/1663005397544g/CamBob_B_Output/img_correlation/B_10min_2hz_mask_example.tiff"
cv2.imwrite(outImage, image)


#Custom Window Size
cv2.namedWindow("test", cv2.WINDOW_KEEPRATIO)
cv2.imshow("test", image)
cv2.resizeWindow("test", 1000, 1365)
cv2.waitKey(0)
cv2.destroyAllWindows()


# In[ ]:




