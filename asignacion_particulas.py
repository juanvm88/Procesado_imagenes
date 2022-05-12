#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed May 11 14:49:49 2022

@author: juan
"""

import matplotlib as mpl
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from pandas import DataFrame, Series  
import pims
import trackpy as tp

#crear diccionarios para comparar los valores y asignar la misma partícula
#a la misma posición en dos listas diferentes para un mismo frame

datos0=pd.read_csv('datalink_0.csv')
datos1=pd.read_csv('datalink_1.csv')

sub105=datos0[datos0['frame']==105]
sub105=sub105.rename_axis('index').reset_index()
sub105_bis=datos1[datos1['frame']==105]
sub105_bis=sub105_bis.rename_axis('index').reset_index()

pos0=(sub105.x[0],sub105.y[0])
dic105={pos0:sub105.particle[0]}
pos0_bis=(sub105_bis.x[0],sub105_bis.y[0])
dic105_bis={pos0_bis:sub105_bis.particle[0]}
