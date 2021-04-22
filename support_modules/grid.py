import numpy as np


def return_grid(n_drops):
    horizontal = 30
    vertical = n_drops/horizontal
    horizontal_coordinates = np.arange(0, 1, 1/(horizontal+1))[1:]
    vertical_coordinates = np.arange(0, 1, 1/(vertical+1))[1:]

    arr = np.empty((0,2), float)
    for j in range(int(vertical)):
        temp_v = vertical_coordinates[j]
        for i in range(int(horizontal)):
            temp_h = horizontal_coordinates[i]
            arr = np.append(arr, np.array([[temp_h,temp_v]]), axis=0)

    return arr
