#!/usr/bin/env python
# coding: utf-8

# Examine OG Dataset. Import xarray and run code snippet to look at output. Review Diagnosis. Tutorial starts below code description. 

# In[3]:


import xarray as xr

fn = r'/home/frfuser/Downloads/FRF-geomorphology_DEMs_duneLidarDEM_202106.nc'
DS = xr.open_dataset(fn)

DS


# Dataset Diagnosis:
# 
# 1. Dimensions = time, and FRF coordinates. We want to keep each time slice but change the spatial dimensions of the dataset to something ArcGIS Pro can read, i.e. lat/lon. Notice how the dimensions define spatial foot print and temporal aspects of the variable of interest, elevation. 
# 
# 2. ArcGIS Pro also requires the coordinate variables to be lat/lon
# 
# 3. We can use the latitude and longitude variables to rewrite the header metadata using a few simple xarray commands, and make a new netcdf dataset. After rewriting the dataset with xarray, we can then use NCO to map our dataset to a grid created in ArcGIS Pro. 

# NCO Information:
# 
# Link: https://nco.sourceforge.net
# 
# "The NCO toolkit manipulates and analyzes data stored in netCDF-accessible formats, including DAP, HDF4, HDF5, and, most recently, Zarr. NCO exploits the geophysical expressivity and logic of many CF (Climate & Forecast) metadata conventions, the flexible description of physical dimensions translated by UDUnits, the network transparency of OPeNDAP, the storage capabilities (e.g., compression, chunking, groups) of HDF (the Hierarchical Data Format), many powerful mathematical and statistical algorithms of GSL (the GNU Scientific Library), and the lossy and lossless compression codecs provided by the CCR (Community Codec Repository). NCO is fast, powerful, and free."
# 
# NCO executables: https://nco.sourceforge.net/#Executables
# 
# ^ See Anaconda section for install 
# 
# NCO documentation: https://nco.sourceforge.net/nco.pdf
# 
# ^ See Section 4.12 - ncremap netCDF Remapper for command line executable to use on the output of this script.  
# 
# Note: This is already compiled and ready for use on this machine. 

# 
# 
# 
# 
# 
# 

# Dune Lidar ArcGIS Pre Processing Code 
# 
# Part 1 of 2 
# Part 1: Xarray Code 
# Part 2: NCO on Linux device. ncremap
# 
# This version requires downloading a copy of the Dune Lidar data
# from thredds. Can be improved by using OpenDAP to pull data remotely, and by constructing 
# path variables rather than using absolute paths, but it is sufficient for testing. The code 
# outputs a temporary nc dataset that can be ingested into the NCO command line executable
# ncremap. 
# 
# Import xarray to use it on netcdf datasets
# 

# In[4]:


import xarray as xr


# Create variable to represent file. Use absolute filepath in side parentheses. 
# filename = r'absolutePath'

# In[5]:


filename = r'/home/frfuser/Downloads/FRF-geomorphology_DEMs_duneLidarDEM_202106.nc'


# Use open_dataset method. Be sure to set your dataset equal to a new variable. I use DS.
# You can call your DS to read dims, coordinate variables, variables, attribution, etc... 
# Just type in your variable name and hit run. Calling DS pulls up the interactive xarray representation
# of the netcdf.

# In[6]:


DS = xr.open_dataset(filename)
DS


# This is how you call a variable. Drill down into the dataset and access
# your variables by using DS.variables['variable name goes here'][:]
# The colon in square brackets calls all variable values 

# In[7]:


lat = DS.variables['latitude'][:]
lon = DS.variables['longitude'][:]


# Now that your variables are loaded. We will do a dimension swap. This line of
# of code below swaps variables into the dimension spot on the header metadata. 
# This redefines how the space-time cube will orient itself when placed into a program
# like Arc Pro. What we are doing is making a dictionary to make the swap. 
# 
# A dictionary is used to store data values in key:value pairs
# Using swap_dims, the dictionary will swap the key for the value. Use the variables 
# you created with the code above to make the swap and rewrite the new dataset

# In[8]:


DS = DS.swap_dims({"xFRF":"lon", "yFRF":"lat"})


# Arc Pro needs to see lat/lon, or easting/northing in the coordinate variable position
# set_coords elevates a variable to the coordinate variable position
# Note: Units of measurement must be ... for Arc Pro to read it

# In[9]:


DS = DS.set_coords(("latitude", "longitude"))


# Drop variables if you want. Make a list of variables to drop and erase them from the
# dataset using the drop_vars method

# In[10]:


vars2drop = ["xFRF", "yFRF"]
DS = DS.drop_vars(vars2drop)


# Call your variables and the desired attribute to edit. Here we will change the units of 
# latitude and longitude from meters to degrees. May require some experimentation as I am 
# not sure if the dataset is in lat/lon or easting/northing. Note: The units used below 
# are one of a few conventions that ESRI will recognize. 

# In[11]:


DS.lon.attrs["units"] = "degrees_east"
DS.lat.attrs["units"] = "degrees_north"


# Call DS to look over the data

# In[12]:


DS


# Uncomment, input the file path and save to file.

# In[13]:


#DS.to_netcdf("")


# The new file is ready for NCO ncremap. This can be run from the linux 
# command line or using pynco. Pynco will call the desired command line executable from an 
# IDE or another cell in this jupyter notebook. 
# 
# https://pynco.readthedocs.io/en/stable/
