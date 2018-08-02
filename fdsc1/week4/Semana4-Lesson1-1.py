# -*- coding: utf-8 -*-

import unicodecsv
import numpy as np
from datetime import datetime as dt
import matplotlib.pyplot as plt

with open('/home/maru/Documents/Udacity/Udacity-DataScienceI/Semana4/life-expectancy.csv') as f:
    for line in f:
        line_splited = line.split(',')
        if line_splited[0] == 'Country':
            year = line_splited
            year.remove('Country')
            # print len(year)
            # break
        if line_splited[0] != 'Country' and len(line_splited) == 205:
            country = line_splited
            country.remove(line_splited[0])
        plt.plot(country)
    plt.show()
