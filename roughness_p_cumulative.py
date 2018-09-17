# -*- coding: utf-8 -*-
"""
Created on Fri Jun  8 10:52:45 2018

@author: user
"""


import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from scipy.optimize import curve_fit


    
#####READ TXT FILE############    

#Obtain data from gwyddion
#You can download Gwyddion software from: http://gwyddion.net
#In Gwyddion get an AFM image and extract the 2D Fourier ressonance contribution and get only the noise from the measurement
#This noise is translated into roughness. Take a slice of the roughness plot and save it into a file

df=pd.read_csv('C:\\Users\\user\\Documents\\birmingham\\MT_Measurement techniques\\AFM\\AFM measurements\\AFM DATA\\AFM_PG_06_22_18\\1 region 20x20um2\\roughness_nh.csv',sep=';',header=None)

n_parts=df.shape[1]

#Load all the values for the roughness

for i in range(n_parts//2):
    xData = df.iloc[:,i*2]
    yData = df.iloc[:,i*2+1]
    xData = np.nan_to_num(xData)
    yData = np.nan_to_num(yData)

    xAll = np.concatenate([xData for i in range(n_parts//2)])
    yAll = np.concatenate([yData for i in range(n_parts//2)])
    yAll2 = yAll
    yAll2 = yAll2.astype('float')
    yAll2[yAll2 == 0] = 'nan'
  
#Present the roughness in hexagonal bins with respective average and std of all the measurements  
  
plt.hexbin(xAll, yAll, gridsize = 30)
plt.ylim([-0.000000002, 0.000000002])
plt.yticks(np.arange(-0.000000002, 0.000000002, 0.0000000005))
cb = plt.colorbar()
cb.set_label('counts in bin')
plt.show()
print(np.nanmean(yAll2),np.nanstd(yAll2))
 
