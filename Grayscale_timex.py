#!/usr/bin/env python
# coding: utf-8

# In[7]:


import os
import cv2
import numpy as np

#imageFolder = r"/media/frfuser/FRF_ConnorG/KevinMartinsMiniArgusTest/1663005397544g/CamBob_B"
imageFolder = r'/media/frfuser/FRF_ConnorG/KevinMartinsMiniArgusTest/1663005397544g/CamBob_B'
outImage = r"/media/frfuser/FRF_ConnorG/KevinMartinsMiniArgusTest/1663005397544g/CamBob_B_Output/img_correlation/B_10min_2hz.tiff"

imageLocs = os.listdir(imageFolder)

fileList = []

for i in imageLocs[1:1200:]:
    imgName = os.path.join(imageFolder, i)
    fileList.append(imgName)

emptyTemplate = cv2.imread(fileList[0])
grayscale = cv2.cvtColor(emptyTemplate, cv2.COLOR_BGR2GRAY)
empty = np.empty_like(grayscale, dtype = np.float32)

for i in fileList:
    img = cv2.imread(i)
    grayscaleArray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    grayscaleArrayFloat = grayscaleArray.astype(np.float32)
    empty = np.add(empty, grayscaleArrayFloat)

grayscaleAvg = (empty / len(fileList)).astype(np.uint8)

cv2.imwrite(outImage, grayscaleAvg)

print('complete')


# In[ ]:


import os
import cv2
import numpy as np

imageFolder = r'/media/frfuser/FRF_ConnorG/KevinMartinsMiniArgusTest/1663005397544g/CamBob_B'
outImage = r'/media/frfuser/FRF_ConnorG/KevinMartinsMiniArgusTest/1663005397544g/CamBob_B_Output/img_correlation/B_10min_2hz.tiff'

imageLocs = os.listdir(imageFolder)

fileList = []

for i in imageLocs[0:1200:]:
    imgName = os.path.join(imageFolder, i)
    fileList.append(imgName)

emptyTemplate = cv2.imread(fileList[0])
grayscale = cv2.cvtColor(emptyTemplate, cv2.COLOR_BGR2GRAY)
empty = np.empty_like(grayscale, dtype = np.float32)

for i in fileList:
    
    img = cv2.imread()
    grayscaleArray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    grayscaleArrayFloat = grayscaleArray.astype(np.float32)
    empty = np.add(empty, grayscaleArrayFloat)

    
grayscaleAvg = (empty / len(fileList)).astype(np.uint8)

cv2.imwrite(outImage, grayscaleAvg)

print('complete')


# In[ ]:


import os
import cv2
import numpy as np

imageFolder = r'/media/frfuser/FRF_ConnorG/KevinMartinsMiniArgusTest/1663005397544g/CamBob_B'
outImage = r'/media/frfuser/FRF_ConnorG/KevinMartinsMiniArgusTest/1663005397544g/CamBob_B_Output/img_correlation/B_10min_2hz.tiff'

imageLocs = os.listdir(imageFolder)

fileList = []

for i in imageLocs[0:1200:]:
    imgName = os.path.join(imageFolder, i)
    fileList.append(imgName)
    
#print(fileList)

emptyTemplate = cv2.imread(fileList[0])
grayscale = cv2.cvtColor(emptyTemplate, cv2.COLOR_BGR2GRAY)
empty = np.empty_like(grayscale, dtype = np.float32)

for i in imageFolder[0:1200:]:
    img = cv2.imread(str(i))
    grayscaleArray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    grayscaleArrayFloat = grayscaleArray.astype(np.float32)
    empty = np.add(empty, grayscaleArrayFloat)
    
grayscaleAvg = (empty / len(fileList)).astype(np.uint8)

cv2.imwrite(outImage, grayscaleAvg)

print('complete')


# In[ ]:


import os
import cv2
import numpy as np

imageFolder = r'/media/frfuser/FRF_ConnorG/KevinMartinsMiniArgusTest/1663005397544g/CamBob_B'
outImage = r'/media/frfuser/FRF_ConnorG/KevinMartinsMiniArgusTest/1663005397544g/CamBob_B_Output/img_correlation/B_10min_2hz.tiff'

imageLocs = os.listdir(imageFolder)

fileList = []

for i in imageLocs[0:1200:]:
    imgName = os.path.join(imageFolder, i)
    fileList.append(imgName)
    
#print(fileList)

emptyTemplate = cv2.imread(fileList[0])
grayscale = cv2.cvtColor(emptyTemplate, cv2.COLOR_BGR2GRAY)
empty = np.empty_like(grayscale, dtype = np.float32)

for i in imageFolder[0:1200:]:
    #img = cv2.imread(str(i))
    img = cv2.imread(i)
    print(img.type)


# In[ ]:


import cv2
import glob
import os
import numpy as np 


imageFolder = r'/media/frfuser/FRF_ConnorG/KevinMartinsMiniArgusTest/1663005397544g/CamBob_B'
outImage = r'/media/frfuser/FRF_ConnorG/KevinMartinsMiniArgusTest/1663005397544g/CamBob_B_Output/img_correlation/B_10min_2hz.tiff'

imageLocs = os.listdir(imageFolder)

fileList = []

for i in imageLocs[0:1200:]:
    imgName = os.path.join(imageFolder, i)
    fileList.append(imgName)

emptyTemplate = cv2.imread(fileList[0])
grayscale = cv2.cvtColor(emptyTemplate, cv2.COLOR_BGR2GRAY)
empty = np.empty_like(grayscale, dtype = np.float32)


images = [cv2.imread(image) for image in glob.glob("/media/frfuser/FRF_ConnorG/KevinMartinsMiniArgusTest/1663005397544g/CamBob_B/*.tiff")]

for image in images:
    grayscaleArray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    grayscaleArrayFloat = grayscaleArray.astype(np.float32)
    empty = np.add(empty, grayscaleArrayFloat)
    
grayscaleAvg = (empty / len(fileList)).astype(np.uint8)

cv2.imwrite(outImage, grayscaleAvg)

print('complete')


# In[5]:


import os
import cv2
import numpy as np

imageFolder = r'/media/frfuser/FRF_ConnorG/KevinMartinsMiniArgusTest/1663005397544g/CamBob_B'
outImage = r'/media/frfuser/FRF_ConnorG/KevinMartinsMiniArgusTest/1663005397544g/CamBob_B_Output/img_correlation/B_10min_2hz.tiff'

imageLocs = os.listdir(imageFolder)

fileList = []

for i in imageLocs[0:1200:]:
    imgName = os.path.join(imageFolder, i)
    fileList.append(imgName)
    
print(fileList)


# In[ ]:




