#!/usr/bin/env python
# coding: utf-8

# In[1]:


### Examine OG Dataset

import xarray as xr

fn = r'/home/frfuser/Downloads/FRF_geomorphology_DEMs_surveyDEM_20230323.nc'
DS = xr.open_dataset(fn)

DS


# In[1]:


### Dune Lidar ArcGIS Pre Processing Code 

### Part 1 of 2 
### Part 1: Xarray Code 
### Part 2: NCO on Linux device. ncremap

### This version requires downloading a copy of the Dune Lidar data
### from thredds. Can be improved by using OpenDAP to pull data remotely, and by constructing 
### path variables rather than using absolute paths, but it is sufficient for testing. The code 
### outputs a temporary nc dataset that can be ingested into the NCO command line executable
### ncremap. 

### Import xarray to use it on netcdf datasets

import xarray as xr

### Create variable to represent file. Use absolute filepath in side parentheses. 
### filename = r'absolutePath'

filename = r'/home/frfuser/Downloads/FRF-geomorphology_DEMs_duneLidarDEM_202106.nc'

### Use open_dataset method. Be sure to set your dataset equal to a new variable. I use DS

DS = xr.open_dataset(filename)

### You can call your DS to read dims, coordinate variables, variables, attribution, etc... 
### Just type in your variable name and hit run

DS

### This is how you call a variable. Drill down into the dataset and access
### your variables by using DS.variables['variable name goes here'][:]
### The colon in square brackets calls all variable values 

lat = DS.variables['latitude'][:]
lon = DS.variables['longitude'][:]

### Now that your variables are loaded. We will do a dimension swap. This line of
### of code below swaps variables into the dimension spot on the header metadata. 
### This redefines how the space-time cube will orient itself when placed into a program
### like Arc Pro. What we are doing is making a dictionary to make the swap. 

### A dictionary is used to store data values in key:value pairs
### Using swap_dims, the dictionary will swap the key for the value. Use the variables 
### you created with the code above to make the swap and rewrite the new dataset

DS = DS.swap_dims({"xFRF":"lon", "yFRF":"lat"})

### Arc Pro needs to see lat/lon, or easting/northing in the coordinate variable position
### set_coords elevates a variable to the coordinate variable position
### Note: Units of measurement must be ... for Arc Pro to read it

DS = DS.set_coords(("latitude", "longitude"))

### Drop variables if you want. Make a list of variables to drop and erase them from the
### dataset using the drop_vars method

vars2drop = ["xFRF", "yFRF", "assessmentPlanesOffset", "rmsReflectorError", "translationSigma", "rotationSigma", "coregQCFlag", "coregAlgorithmFlag"]
DS = DS.drop_vars(vars2drop)

### Call your variables and the desired attribute to edit. Here we will change the units of 
### latitude and longitude from meters to degrees. May require some experimentation as I am 
### not sure if the dataset is in lat/lon or easting/northing. Note: The units used below 
### are one of a few conventions that ESRI will recognize. 

#DS.lon.attrs["units"] = "degrees_east"
#DS.lat.attrs["units"] = "degrees_north"

#DS['lon']attrs["units"] = "degrees_east"
#DS['lat']attrs["units"] = "degrees_north"

### Call DS to look over the data

DS

### Save to file. 

DS.to_netcdf('/home/frfuser/Downloads/FRF-geomorphology_DEMs_duneLidarDEM_202106_temp.nc')

### The new file is ready for NCO ncremap. This can be run from the linux 
### command line or using pynco, which will call the command line executable from an 
### IDE or another cell in this jupyter notebook. 

print('complete')


# In[ ]:


assessmentPlanesOffset  (time) float64 ...
    rmsReflectorError       (time) float64 ...
    translationSigma        (time, errorDimensions) float64 ...
    rotationSigma           (time, errorDimensions) float64 ...
    coregQCFlag             (time) float64 ...
    coregAlgorithmFlag 

