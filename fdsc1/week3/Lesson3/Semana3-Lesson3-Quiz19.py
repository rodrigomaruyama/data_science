import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sns

filename = '/home/maru/Documents/Udacity/Udacity-DataScienceI/Semana3/Lesson3/nyc-subway-weather.csv'
subway_df = pd.read_csv(filename)

dispersion = subway_df.groupby('UNIT')['latitude', 'longitude', 'ENTRIESn_hourly'].sum().head()
area = dispersion['ENTRIESn_hourly']/100

plt.scatter(dispersion['latitude'], dispersion['longitude'], s=area)
plt.show()
