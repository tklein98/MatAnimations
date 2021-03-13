import numpy as np
import time
def anim1(frame_number, rain_drops, n_drops, scat):
    rain_drops = rain_drops
    n_drops = n_drops
    scat = scat
    current_index = frame_number % n_drops

    # Updating size
    rain_drops['size'][current_index] = np.random.uniform(5, 30, 1) * \
    current_index**1.2

    # Updating position
    rain_drops['position'][current_index] = np.random.uniform(0, 1, 2)

    #Updating fill
    rain_drops['fill'][current_index] = (np.random.uniform(0.2, 1),
                                         np.random.uniform(0.6, 1),
                                         np.random.uniform(0, 0.4),
                                         1)
    # Updating frame
    rain_drops['frame'][current_index] = (np.random.uniform(0.2, 1),
                                          np.random.uniform(0.6, 1),
                                          np.random.uniform(0, 0.4),
                                          1)

    rain_drops['frame'][:, 3] -= 1.0/len(rain_drops)
    rain_drops['frame'][:, 3] = np.clip(rain_drops['frame'][:, 3], 0, 1)

    rain_drops['fill'][:, 3] -= 1.0/len(rain_drops)
    rain_drops['fill'][:, 3] = np.clip(rain_drops['fill'][:, 3], 0, 1)

    scat.set_edgecolors(rain_drops['frame'])
    scat.set_sizes(rain_drops['size'])
    scat.set_offsets(rain_drops['position'])
    scat.set_facecolors(rain_drops['fill'])

# Animation two
def anim2(frame_number, rain_drops, n_drops, scat):
    rain_drops = rain_drops
    n_drops = n_drops
    scat = scat
    current_index = frame_number % n_drops
    print('test')
    horizontal = 25
    vertical = n_drops/horizontal

    horizontal_coordinates = np.arange(0, 1, 1/(horizontal+1))[1:]
    vertical_coordinates = np.arange(0, 1, 1/(vertical+1))[1:]

    arr = np.empty((0,2), float)

    for j in range(int(vertical)):
        temp_v = vertical_coordinates[j]
        for i in range(int(horizontal)):
            temp_h = horizontal_coordinates[i]
            arr = np.append(arr, np.array([[temp_h,temp_v]]), axis=0)

    rain_drops['position'] = arr



    rain_drops['frame'][:, 0] = 0.5
    rain_drops['frame'][:, 1] = 0.0
    rain_drops['frame'][:, 2] = 0.0
    rain_drops['frame'][:, 3] = 1

    rain_drops['fill'][:25+current_index, 0] = 0.0
    rain_drops['fill'][:25+current_index, 1] = 0.8
    rain_drops['fill'][:25+current_index, 2] = 0.0
    rain_drops['fill'][:25+current_index, 3] = 1

    rain_drops['size'][:] = 250




    scat.set_edgecolors(rain_drops['frame'])
    scat.set_sizes(rain_drops['size'])
    scat.set_offsets(rain_drops['position'])
    scat.set_facecolors(rain_drops['fill'])

