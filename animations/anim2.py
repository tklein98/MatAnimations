import numpy as np
import time
import pandas as pd
import random

dict_columns = np.zeros(30)
def moving_vertical(frame_number, rain_drops, n_drops, scat, arr):
    rain_drops = rain_drops
    n_drops = n_drops
    linewidth = 4000
    scat = scat
    index_control = 30
    current_index = frame_number % index_control
    arr = arr
    start = np.arange(0,450,30)

    rain_drops['position'] = arr

    #Updating fill
    rain_drops['fill'] = (0,
                                         0,
                                         0,
                                         0)
    # Updating frame
    rain_drops['frame'] = (1,
                                          1,
                                          1,
                                          0.1)

    rain_drops['size'] = 1200
    
    rain_drops['fill'][current_index] = (0,1,0,1)
    
    column_indexes = []
    for i in range(random.randrange(0,15)):
        index = np.random.randint(0,14)
        rain_drops['fill'][start[index]] = (0,1,0,1)
        column_indexes.append(start[index])
    
    # TODO: Create an object that memorizes all newly created column sequences and passes it on to the next columnd (+1) There are 30 columns in total 
    # dict_columns[current_index] = column_indexes
    
    time.sleep(0.1)

    scat.set_edgecolors(rain_drops['frame'])
    scat.set_sizes(rain_drops['size'])
    scat.set_offsets(rain_drops['position'])
    scat.set_facecolors(rain_drops['fill'])