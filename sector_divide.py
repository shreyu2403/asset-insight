import pandas as pd
import numpy as np
import scipy
import sklearn
import itertools
import geohash
import matplotlib
matplotlib.use('agg')
import matplotlib.pyplot as plt
#read csv file
df=pd.read_csv("Raw_data_compactor.csv")

#to set max no of rows
pd.options.display.max_rows = 100

min_lat=df['fltLatitude'].min()
max_lat=df['fltLatitude'].max()
min_lon=df['fltLongitude'].min()
max_lon=df['fltLongitude'].max()

