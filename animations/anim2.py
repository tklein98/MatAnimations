import numpy as np
import time
import pandas as pd
import random

dict_columns = np.zeros(30)
memory = []
start_frame = 0
size = 1200

def moving_vertical(frame_number, rain_drops, n_drops, scat, arr):
    rain_drops = rain_drops
    n_drops = n_drops
    scat = scat
    index_control = 30
    current_index = frame_number % index_control
    arr = arr
    start = np.arange(0,450,30)
    global start_frame
    global size
    start_frame+=1

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
                                          0.2)

    rain_drops['size'] = size
    
    # TODO Change up sizes for more variation
    
    if start_frame>20 and size > 100 and start_frame<100:
        size -= 50
    elif size < 1500 and start_frame>100:
        size += 100
    
    column_indexes = []
    for i in range(random.randrange(0,15)):
        index = np.random.randint(0,15)
        column_indexes.append(start[index])
    memory.insert(0,column_indexes)

    # Delete last column when columns are full
    if len(memory)>index_control:
        del memory[-1] 
    new_memory = []
    new_memory.insert(0,column_indexes) 
    
    # Sweep to the Right 
    for count, pixels in enumerate(memory):
        new_list = [x+count for x in pixels]
        new_memory.append(new_list)
        
    # Sweep down
    # if start_frame > 50:
    #     for i in range(50):
    #         rain_drops['size'] = 1200/(i+1)
    #         time.sleep(0.1)
                        
    #         scat.set_edgecolors(rain_drops['frame'])
    #         scat.set_sizes(rain_drops['size'])
    #         scat.set_offsets(rain_drops['position'])
    #         scat.set_facecolors(rain_drops['fill'])

    # TODO: Create additional sweeps (left, up down)
    
    # Update all 450 pixel fills 
    for pixels in new_memory:
        rain_drops['fill'][pixels, 0] = 1/index_control*current_index
        rain_drops['fill'][pixels, 1] = 1/(current_index+1)
        rain_drops['fill'][pixels, 2] = 0.4
        rain_drops['fill'][pixels, 3] = 1 

    time.sleep(0.1)

    scat.set_edgecolors(rain_drops['frame'])
    scat.set_sizes(rain_drops['size'])
    scat.set_offsets(rain_drops['position'])
    scat.set_facecolors(rain_drops['fill'])