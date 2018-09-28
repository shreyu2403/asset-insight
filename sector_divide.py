import pandas as pd
import numpy as np
import scipy
import sklearn
import itertools

import matplotlib.pyplot as plt
#read csv file
df=pd.read_csv("Raw_data_compactor.csv")

#to set max no of rows
pd.options.display.max_rows = 100

min_lat=df['fltLatitude'].min()
max_lat=df['fltLatitude'].max()
min_lon=df['fltLongitude'].min()
max_lon=df['fltLongitude'].max()

plt.rc('figure', figsize = (14, 7))
# Font size to 14
plt.rc('font', size = 14)
# Do not display top and right frame lines
plt.rc('axes.spines', top = True, right = True)
# Remove grid lines
plt.rc('axes', grid = True)
# Set backgound color to white
plt.rc('axes', facecolor = 'white')

def scatterplot(x_data, y_data, x_label, y_label, title):

    # Create the plot object
    _, ax = plt.subplots()

    # Plot the data, set the size (s), color and transparency (alpha)
    # of the points
    ax.scatter(x_data, y_data, s = 30, color = '#539caf', alpha = 0.75)

    # Label the axes and provide a title
    ax.set_title(title)
    ax.set_xlabel(x_label)
    ax.set_ylabel(y_label)

# Call the function to create plot
scatterplot(x_data = df['fltLatitude']
            , y_data = df['fltLongitude']
            , x_label = 'Latitude'
            , y_label = 'Longitude'
            , title = 'PLOT')

plt.show()
