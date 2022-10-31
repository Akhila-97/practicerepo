# -*- coding: utf-8 -*-
"""
Created on Mon Oct 24 11:33:39 2022

@author: akhil
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

Barclays = pd.read_csv('BCS_ann.csv')
bp = pd.read_csv('BP_ann.csv')
tesco = pd.read_csv('TSCO_ann.csv')
voda = pd.read_csv('VOD_ann.csv')

barclays_data = [Barclays['ann_return'],'Barclays']
bp_data = [bp['ann_return'],'Bp']
tesco_data = [tesco['ann_return'],'tesco']
voda_data = [voda['ann_return'],'Voda']
data=[barclays_data[0],bp_data[0],tesco_data[0],voda_data[0]]
dataname = [barclays_data[1],bp_data[1],tesco_data[1],voda_data[1]]
print(dataname)
plt.figure()
plt.subplots_adjust(hspace=0.4, wspace=0.4)

for i in range (4) :
    
    plt.subplot(2, 2 , i+1)
    #plt.xlim(0,50)
    #plt.ylim(-50,50 )
    plt.hist(data[i])
    plt.xlabel(dataname[i])
    plt.ylabel('N')

plt.show()