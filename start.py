#sample file
import pandas as pd
import numpy as np
import scipy
import sklearn
import itertools
import math

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

#select only those rows where engine is on
Igni = df1['IgniStat'] == 1
An = df1['an1']>3500

df1=df1[Igni & An]
#print(df1)

#only edited values
#df1.to_csv('Compactor_modified.csv')

#method to find vectors
def latlong_to_3d(latr, lonr):
    """Convert a point given latitude and longitude in radians to 3-dimensional space, assuming a sphere radius of one."""
    return np.array((
        math.cos(latr) * math.cos(lonr),
        math.cos(latr) * math.sin(lonr),
        math.sin(latr)
    ))

def angle_between_vectors_degrees(u, v):
    """Return the angle between two vectors in any dimension space,in degrees."""
    return np.degrees(
        math.acos(np.dot(u, v) / (np.linalg.norm(u) * np.linalg.norm(v))))

# The points in tuple latitude/longitude degrees space
A = (12.92473, 77.6183)
B = (12.92512, 77.61923)
C = (12.92541, 77.61985)

# Convert the points to numpy latitude/longitude radians space
a = np.radians(np.array(A))
b = np.radians(np.array(B))
c = np.radians(np.array(C))

# Vectors in latitude/longitude space
avec = a - b
cvec = c - b

# Adjust vectors for changed longitude scale at given latitude into 2D space
lat = b[0]
avec[1] *= math.cos(lat)
cvec[1] *= math.cos(lat)

a=angle_between_vectors_degrees(avec,cvec)
print(a)

# The points in 3D space
a3 = latlong_to_3d(*a)
b3 = latlong_to_3d(*b)
c3 = latlong_to_3d(*c)

# Vectors in 3D space
a3vec = a3 - b3
c3vec = c3 - b3

# Find the angle between the vectors in 2D space
angle3deg = angle_between_vectors_degrees(a3vec, c3vec)


# Print the results
print('\nThe angle ABC in 2D space in degrees:', angle2deg)
print('\nThe angle ABC in 3D space in degrees:', angle3deg)