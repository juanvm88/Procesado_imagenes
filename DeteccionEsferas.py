# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
import matplotlib as mpl
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from pandas import DataFrame, Series  
import pims
import trackpy as tp

def createCircularMask(h, w, center=None, radius=None):
    """
    Creates an OpenCV circular mask
        
    Parameters
    ----------
    h : int
    Height of the image for which the mask is going to be used
    w : int
    Width of the image for which the mask is going to be used
    center : tuple or list, optional
    Pair of coordinates for the mask's central point. If not specified uses: [w/2, h/2]
    radius : float, optional
    Value of the mask radius. If not specified uses max possible value
    
    Returns
    -------
    mask : array
    Mask for using with the image (array of True/False values)
    """
    
    if center is None: # use the middle of the image
        center = [int(w/2), int(h/2)]
    if radius is None: # use the smallest distance between the center and image walls
        radius = min(center[0], center[1], w-center[0], h-center[1])
    
    Y, X = np.ogrid[:h, :w]
    dist_from_center = np.sqrt((X - center[0])**2 + (Y-center[1])**2)
    
    mask = dist_from_center <= radius
    
    return mask

@pims.pipeline
def maskImage(img, mask):
    """ 
    Masks an input image
      
    Parameters
    ----------
    img : array
    Input image
    mask : array
    True/False array with same shape as input image 
    
    Returns
    -------
    masked_img : array
    output masked image
        
    """
    masked_img = img.copy()
    masked_img[~mask] = 0
    
    return masked_img

frames=pims.open('/home/juan/Desktop/21549_1_6.cine')
#/run/user/1000/gvfs/tesla/homes/Lab/thin_layer/tests/Test1
#frames=pims.open('C:/ProgramData/Phantom/Snapshots/Test1/Calibration01/21549/21549_0001.tif')

w,h=frames[0].shape
#plt.imshow(frames[0],cmap='gray')

mascara=createCircularMask(w,h,center=(409,399),radius=388);
imagen=maskImage(frames, mascara);
#plt.figure()
#plt.imshow(imagen[0],cmap='gray')
#f=tp.locate(imagen[0],5,minmass=85,separation=4)
#plt.figure()
#tp.annotate(f,imagen[0])
#plt.figure()
#plt.plot(f['mass'],'.')



#with pd.ExcelWriter('dataloc.xlsx',engine='openpyxl',mode='a',if_sheet_exists='overlay') as writer:

for i in range(frames.shape[0]):
    if i==0:
        f=tp.locate(imagen[i],5,minmass=85,separation=4)
        f.to_csv('dataloc.csv',mode='a',index=False,header=True,columns=('x','y','frame'))
    else:
        leng=f.shape[0]
        f=tp.locate(imagen[i],5,minmass=85,separation=4)
        f.to_csv('dataloc.csv',mode='a',index=False,header=False,columns=('x','y','frame'))        
 


