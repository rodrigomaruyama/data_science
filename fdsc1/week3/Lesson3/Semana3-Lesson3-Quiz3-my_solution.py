import numpy as np

ridership = np.array([
    [   0,    0,    2,    5,    0],
    [1478, 3877, 3674, 2328, 2539],
    [1613, 4088, 3991, 6461, 2691],
    [1560, 3392, 3826, 4787, 2613],
    [1608, 4802, 3932, 4477, 2705],
    [1576, 3933, 3909, 4979, 2685],
    [  95,  229,  255,  496,  201],
    [   2,    0,    1,   27,    0],
    [1438, 3785, 3589, 4174, 2215],
    [1342, 4043, 4009, 4665, 3033]
])


def mean_riders_for_max_station(ridership):
    dimensions = ridership.shape
    days = dimensions[0]
    stations = dimensions[1]
    for i in range(stations):
        maximum_riders = 0
        if ridership[0,i] > maximum_riders:
            maximum_riders = ridership[0,i]
            maximum_riders_station = i
    riders = float(0)
    for j in range(days):
        riders += ridership[j, maximum_riders_station]
    mean_for_max = riders/(days)
    overall = float(0)
    for k in range(days):
        for l in range(stations):
            overall += ridership[k,l]
    overall_mean = overall/(days*stations)

    return (overall_mean, mean_for_max)

print mean_riders_for_max_station(ridership)
