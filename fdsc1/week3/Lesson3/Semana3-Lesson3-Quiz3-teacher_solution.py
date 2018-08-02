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
    maximum_riders_station = ridership[0, :].argmax()
    mean_for_max = ridership[ :,maximum_riders_station].mean()
    overall_mean = ridership.mean()
    return (overall_mean, mean_for_max)

print mean_riders_for_max_station(ridership)
