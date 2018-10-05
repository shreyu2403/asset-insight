import pandas as pd
import numpy as np
import scipy
import sklearn
import itertools

import matplotlib.pyplot as plt
from matplotlib import colors as mcolors
#read csv file
df=pd.read_csv("Compactor_modified1.csv")

#to set max no of rows
pd.options.display.max_rows = 100

plt.rc('figure', figsize = (14, 7))
# Font size to 14
plt.rc('font', size = 14)
# Do not display top and right frame lines
plt.rc('axes.spines', top = True, right = True)
# Remove grid lines
plt.rc('axes', grid = True)
# Set backgound color to white
plt.rc('axes', facecolor = 'white')

# Call the function to create plot

#df.loc[(df.speed < 0.25) , ['fltLatitude','fltLongitude']].plot.scatter( x ='fltLatitude',y ='fltLongitude',s = 30, color = 'salmon', alpha = 0.75)
#plt.show()

#boxvector
#for point in df['lat_long']:
#    a=0
#    b=0
#    for i in self.boxvector:
#        if point[0] < i:
#            a=self.boxvector.index(i)-1
#            break

#   for i in self.boxvector:
#        if point[1] < i:
#            b=self.boxvector.index(i)-1
#            break

#    farray[a][b]+=1
min_lat=df['fltLatitude'].min()
max_lat=df['fltLatitude'].max()
min_lon=df['fltLongitude'].min()
max_lon=df['fltLongitude'].max()



gridyy=np.linspace(min_lat,max_lat,5)
gridyx=np.linspace(min_lon,max_lon,5)

lat = df.loc[(df.speed > 0.25),'fltLatitude'].values
lon = df.loc[(df.speed > 0.25),'fltLongitude'].values
print(lat,lon)
grid, _, _ = np.histogram2d( lon,lat , bins=[gridyx, gridyy])
plt.pcolormesh(gridyx,gridyy , grid)
plt.colorbar()
#df.loc[(df.speed > 0.25) , ['fltLatitude','fltLongitude']].plot.scatter( x ='fltLatitude',y ='fltLongitude',s = 30, color = '#539caf', alpha = 0.75)

plt.show()



