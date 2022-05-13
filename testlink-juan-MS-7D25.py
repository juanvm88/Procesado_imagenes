#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri May  6 15:03:31 2022

@author: juan
"""
import matplotlib as mpl
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from pandas import DataFrame, Series  
import pims
import trackpy as tp

#todo=pd.read_csv('/home/juan/Desktop/dataloc.csv')
#lo hago para los 1000 primeros frames

df=pd.read_csv('/home/juan/Desktop/dataloc.csv',nrows=5703103)

N=10
Nframe=max(df.frame)

for i in range(N):
  sub=df[df['frame']<=(i+1)*(Nframe/N)+10]
  sub=sub[sub['frame']>i*(Nframe/N)]
  
  linked=tp.link(sub,2,memory=3)
  linked_filter=tp.filter_stubs(linked,threshold=75)
  
  linked.to_csv(f'datalink_{i}.csv')
  linked_filter.to_csv(f'datalink_filter_{i}.csv')

    
    
