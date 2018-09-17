import pandas as pd
import numpy as np
import scipy
import sklearn
import itertools

import matplotlib
matplotlib.use('agg')
import matplotlib.pyplot as plt
#read csv file
df1=pd.read_csv("Raw_data_compactor.csv")

#to set max no of rows
pd.options.display.max_rows = 200
#view data head and tail wise
#print(df1.head(5))
#print(df1.tail(3))

#obtain col name
#print(df1.columns)

#quick summary
#print(df1.describe)

#selecting partial data
#print(df1.loc[0:7,['CorrTime','fltLongitude','fltLatitude']])

#to drop missing data
#df.dropna(how=’any’) or df.dropna(how=’all’)

#to calulate distace between two lat_long:

import geopy.distance
from geopy.distance import geodesic
from geopy.distance import lonlat, distance

df1['lat_long'] = [', '.join(str(x) for x in y) for y in map(tuple, df1[['fltLatitude', 'fltLongitude']].values)]

distance=[]
coords_vals = df1['lat_long'].values
coords_vals_temp= df1.loc[1:,'lat_long'].values

#finding distance
for i in range(0,len(coords_vals)-1): 
    distance.append(geodesic(coords_vals[i], coords_vals_temp[i]).km)
distance.append('0')    
df1['distances'] = distance

#finding diff between each lat and long
df1['Diff_lat'] = df1['fltLatitude'] - df1['fltLatitude'].shift(1)
df1['Diff_long'] = df1['fltLongitude'] - df1['fltLongitude'].shift(1)
#print(df1)
#select only those rows where engine is on
Igni = df1['IgniStat'] == 1
An = df1['an1']>3500

df1=df1[Igni & An]
#want to find out vectors
#df1['vect']=[df1['fltLatitude']-df1['fltLatitude'].shift(1),df1['fltLongitude']-df1['fltLongitude'].shift(1)]
#print(df1)

#to plot
#fig=plt.figure()
#ax = fig.add_subplot(1,1,1)
#Variable
#ax.boxplot(df1['distances'])
#plt.show()

#df1.to_csv('Comapctor_modified.csv')