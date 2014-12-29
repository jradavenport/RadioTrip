# -*- coding: utf-8 -*-
"""
Created on Sat Sep 27 21:28:02 2014
@author: jradavenport

Goal: make map of all 27k FM radio transmitter coverages
"""

import numpy as np
import matplotlib.pyplot as plt


plt.figure(figsize=(50,40))

myfile = open("FM_service_contour_current.txt", "r")
#for k in range(10000):
while True:
    theline = myfile.readline()
    if len(theline) == 0:
        break
    
    xbig = []
    ybig = []
    
    clist = theline.split("|")
    for i in range(4,len(clist)-1):
        xt,yt = clist[i].split(',')
        xbig.append(xt)
        ybig.append(yt)
    
    # plot the line
    
    plt.fill(ybig,xbig,'b',alpha=0.05,rasterized=True,
             linewidth=None,closed=True)

plt.xlim((-180,-60))
plt.ylim((15,75))
plt.axis('off')
plt.savefig('fm_map.png',dpi=450)
myfile.close()



