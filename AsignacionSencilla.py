#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri May 13 12:22:23 2022

@author: juan
"""

import matplotlib as mpl
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from pandas import DataFrame, Series  
import pims
import trackpy as tp

df=pd.read_csv('/home/juan/Desktop/dataloc.csv',nrows=5703103)
datos0=pd.read_csv('datalink_0.csv')
datos1=pd.read_csv('datalink_1.csv')

N=10
Nframe=max(df.frame)

#part=1000
t=round((Nframe/N)+5)



#con el código interno del bucle 
#en df1 se busca la posición que 
#ocupa la particula part en el frame t

#luego se busca esa misma posición en el df2
#a partir de esa posición se busca el índice y a qué partícula corresponde
#el último paso sería asignar a esa partícula el mismo nombre que en el primer df1
for part in datos0.particle:
    if part in datos0.particle:
        a=datos0[datos0.particle==part][datos0.frame==t].x.values[0]

        b=np.where(datos1.x.values==a)[0][0]

        c=datos1.at[b,'particle']

        datos1.loc[datos1['particle']==c,'particle']=part




#sin embargo no funciona bien aún porque hay posiciones que no existen en el df2
#porque han podido ser filtradas al no ser trayectorias completas en el linkado
