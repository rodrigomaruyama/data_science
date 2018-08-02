import pandas as pd
import numpy as np
from datetime import datetime

path = '/home/maru/Documents/Udacity/Udacity-DataScienceI/Semana3/Lesson3/'
nyc_weather = pd.read_csv(path + 'nyc-subway-weather.csv')

# print nyc_weathe

nyc_weather_array = np.array(nyc_weather)

dimensions = nyc_weather_array.shape
rows = dimensions[0]
columns = dimensions[1]
# print columns
# exit()

maximum_riders = 0
maximum_riders_station = ''
maximum_riders_station_total = 0
overall_max = 0
for i in range(rows):
    date_split = nyc_weather_array[i,1].split('-')
    date = date_split[0] + '-' + date_split[1] + '-' + '20' + date_split[2]
    entries = int(nyc_weather_array[i,3])
    # exits = int(nyc_weather_array[i,4])
    # entries_hourly = int(nyc_weather_array[i,4])
    # exits_hourly = int(nyc_weather_array[i,4])
    station = nyc_weather_array[i,11]
    overall_max += entries
    if date == '05-01-2011':
        if entries > maximum_riders:
            maximum_riders = entries
            maximum_riders_station = station
    if station == maximum_riders_station:
        maximum_riders_station_total +=entries
    # print date, entries, exits, entries_hourly, exits_hourly, station

# maximum_riders_station_mean = np.array(maximum_riders_station_mean)
mean_for_max = maximum_riders_station_total/31
overall_max_mean = overall_max/rows
how_big = maximum_riders_station_total/overall_max_mean
print station, mean_for_max, overall_max_mean, how_big
