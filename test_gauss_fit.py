import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from scipy.optimize import curve_fit



##############################
########DEFINITIONS###########
##############################
#define gaussian distribution

def gaus(x,a,x0,sigma,y0):
    return y0+a*exp(-(x-x0)**2/(2*sigma**2))

##############################
#########CODE#################
##############################
    
#####READ TXT FILE############    
#read data file

df=pd.read_csv('C:\\Users\\user\\Documents\\birmingham\\MT_Measurement techniques\\AFM\\AFM measurements\\AFM DATA\\AFM_PG_06_22_18\\1 region 20x20um2\\nn_real_nh.csv',sep=';',header=None)
n_parts=df.shape[1]


for i in range(n_parts//2):
    try:
#get x and y values from data file, in this case we are finding the distance between the nearest neighbours. when we want to find the distance between the nearest neightbours
# we have the plot shapes like and "U" so to be possible to fit a gaussian we inver the y axis thus we have the minus sign in the y axis.
# If we want to find the size of the pillar the data points will be an inverted "U" so it would be easy to fit with just a Gaussian fit and the y values would not have the negative sign.

        xData = df.iloc[:,i*2]
        yData = -df.iloc[:,i*2+1]
        xData = np.nan_to_num(xData)
        yData = np.nan_to_num(yData)
        
        meanx = np.average(xData)                   #note this correction
        sigmax = np.std(xData)      #note this correction
        meany = np.average(yData)                   #note this correction
        sigmay = np.std(yData)  

#Gaussian fitting and plotting of the fit with respective data points.
        popt,pcov = curve_fit(gaus , xData , yData, p0=[max(yData),meanx,sigmax,meany])
        plt.plot(xData,yData,'b+:',label='data')
        plt.plot(xData,gaus(xData,*popt),'ro:',label='fit')
        plt.figure()
        plt.legend()
        print('Fitted parameters: a,x0,sigma,y0 {}'.format(popt))
        print(i)
        
#The values will be written in a folder in the respective order: A , X0, Sigma and y0
#We define the height of the pillar as height = |y0-a| and the size(=Diameter) of the pillar as Diameter=2*FWHM. Where the FWHM~2.35*sigma 

        df2 = pd.DataFrame({'a':pd.Series(popt[0]) ,'x0': pd.Series(popt[1]) ,'sigma': pd.Series(popt[2]) ,'y0': pd.Series(popt[3])})
        df2.to_csv('C:\\Users\\user\\Documents\\birmingham\\MT_Measurement techniques\\AFM\\AFM measurements\\AFM DATA\\AFM_PG_06_22_18\\1 region 20x20um2\\nn_nh_dist.csv' , header = None , mode='a' , index=False, sep='\t')

       

    except:
        pass
   
    



#####References####
#https://bitbucket.org/zunzuncode/ramanspectroscopyfit    #lorentzian fit
#https://github.com/btjones-me/raman_spectroscopy/blob/master/Raman%20Spectroscopy/PythonCode/raman_analysis_clean.py     #peak fit
#http://scipy.github.io/devdocs/generated/scipy.signal.savgol_filter.html   #scipy.signal.savgol_filter
#https://gist.github.com/perimosocordiae/efabc30c4b2c9afd8a83    #asl
