# -*- coding: utf-8 -*-
"""
@author: jradavenport

Goal: make map of radio stations based on genre
"""

from mpl_toolkits.basemap import Basemap, cm
import numpy as np
import matplotlib.pyplot as plt


stype, s_id = np.loadtxt("nielsen_stations.csv", delimiter=',', usecols=(0,1),unpack=True,dtype='string',skiprows=1)
stype_uniq = np.unique(stype)

''' 
what i could do...

read FM_service_contour_current.txt in w/ just that ID column
test = np.loadtxt("FM_service_contour_current.txt",delimiter='|',usecols=(2,),unpack=True, dtype='string')

and then read it again making a giant list of strings

then for ID matches, split the strings for matching rows and make the plots

but... whatever
'''

for n in range(0,len(stype_uniq)):
    print(stype_uniq[n])
    
    plt.figure(figsize=(26,16))
    m = Basemap(width=6000000,height=3500000,
                resolution='l',projection='stere',\
                lat_ts=50,lat_0=39,lon_0=-99.)
    m.drawcoastlines(linewidth=1.25)
    m.drawstates()
    m.drawcountries()

    myfile = open("FM_service_contour_current.txt", "r")
    
    while True:
        theline = myfile.readline()
        if len(theline) == 0:
            break
        
        xbig = []
        ybig = []
        
        clist = theline.split("|")
        s_id_n = clist[2][0:4]

        indx = np.where((s_id_n == s_id))        
        
        if (sum(s_id_n == s_id) > 0): # if there is a match
            if (stype_uniq[n] == stype[indx]): # if it's the right genre
                for i in range(4,len(clist)-1):
                    xt,yt = clist[i].split(',')
                    xbig.append(xt)
                    ybig.append(yt)
                xnew,ynew = m(np.array(ybig,dtype='float'),np.array(xbig,dtype='float'))
                plt.fill(xnew,ynew,'b',alpha=0.1,rasterized=True,
                         linewidth=None,closed=True)
         
    #plt.xlim((-128,-69))
    #plt.ylim((25,55))
    plt.suptitle(stype_uniq[n],fontsize=48)
    #plt.axis('off')
    plt.savefig(str(n)+'_map.png',dpi=250)
    plt.close()
    
    myfile.close()
 


