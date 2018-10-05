import math
import numpy as np
import pandas as pd
import scipy
import sklearn

#read csv file
df1 = pd.read_csv("Raw_data_compactor.csv")

def angle_between_vectors_degrees(u, v):
    """Return the angle between two vectors in any dimension space,in degrees."""
    return np.degrees(math.acos(np.dot(u, v) / (np.linalg.norm(u) * np.linalg.norm(v))))

def angle_between_vectors_degrees_cross(u, v):
    """Return the angle between two vectors in any dimension space,in degrees."""
    return np.degrees(math.asin(np.cross(u, v) / (np.linalg.norm(u) * np.linalg.norm(v))))


lat_long_new=[]

# The points in tuple latitude/longitude degrees space
for i in np.array(df1[['fltLatitude','fltLongitude']]):
    lat_long_new.append(np.radians(np.array(i)))
vects=[]

# Vectors in latitude/longitude space
for i in range(0,len(lat_long_new)-1):
    vects.append(lat_long_new[i+1]-lat_long_new[i])

a=[]

a.append(0)
for i in range(0,len(vects)-1):
    a.append(angle_between_vectors_degrees(vects[i],vects[i+1]))
a.append(0)

df1['angles'] = a

#cross vproduct checking
#a_cross = []
#a_cross.append(0)
#for i in range(0, len(vects) - 1):
#    a_cross.append(angle_between_vectors_degrees(vects[i], vects[i + 1]))
#a_cross.append(0)

#df1['angles_cross']=a_cross

import dateutil
import geopy.distance
from geopy.distance import geodesic
from geopy.distance import lonlat, distance

df1['lat_long'] = [', '.join(str(x) for x in y) for y in map(tuple, df1[['fltLatitude', 'fltLongitude']].values)]

distance=[]
coords_vals = df1['lat_long'].values
coords_vals_temp= df1.loc[1:,'lat_long'].values

#finding distance
distance.append('0')
for i in range(0,len(coords_vals)-1): 
    distance.append(geodesic(coords_vals[i], coords_vals_temp[i]).km)
    
df1['distances'] = distance
df1.distances = df1.distances.astype(float).fillna(0.0)
#FINDING TIME DIFFERNCE
df1['CorrTime'] = pd.to_datetime(df1['CorrTime'])
delta = (df1['CorrTime']-df1['CorrTime'].shift()).fillna(0)
deltaT=[]
for i in delta:
    deltaT.append(i.total_seconds()/3600)

df1['deltaT']= deltaT
df1['speed']=df1['distances'].div(df1.deltaT, axis=0)

a_sum = 0.0
for i,row in df1.loc[df1['speed'].notnull(),:].iterrows():
    total=df1['angles'].sum()

print(total)

#df1.to_csv('Compactor_modified1.csv')
print("success")
