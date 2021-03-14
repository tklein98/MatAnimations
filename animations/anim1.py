import numpy as np
import time
import pandas as pd

starting_points = pd.read_csv('data/starting_points.csv')
capital_letters = pd.read_csv('data/capital_letters.csv')
capital_letters_len = capital_letters.count()

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
def anim2(frame_number, rain_drops, n_drops, scat, arr, input_array, pause=1):
    # reset color fills
    rain_drops['fill'][:, 0] = 0.0
    rain_drops['fill'][:, 1] = 0.0
    rain_drops['fill'][:, 2] = 0.0
    rain_drops['fill'][:, 3] = 1

    # TODO: Maybe change the colors of the frame every time?

    rain_drops = rain_drops
    n_drops = n_drops
    scat = scat
    current_index = frame_number % n_drops
    arr = arr
    input_array = input_array
    index_array = current_index % len(input_array)
    input_word = input_array[index_array]

    # Setting grid positions
    rain_drops['position'] = arr

    # setting frame color
    rain_drops['frame'][:, 0] = 0.5
    rain_drops['frame'][:, 1] = 0.5
    rain_drops['frame'][:, 2] = 0.5
    rain_drops['frame'][:, 3] = 1

    # Size of raindrops in grid
    rain_drops['size'][:] = 500

    # Retrieving the list of starting points (bottom left corner of input word)
    word_points = starting_points[f'{len(input_word)}']

    # iterate through every character of the given word
    for count, character in enumerate(input_word):
        start_pixel_location = word_points[count]
        char_locations = capital_letters[f'{character}']

        # create each letter based on its pixel locations
        for pixel_locations in char_locations[:int(capital_letters_len[f'{character}'])]:

            rain_drops['fill'][start_pixel_location + int(pixel_locations), 0] = 0.0
            rain_drops['fill'][start_pixel_location + int(pixel_locations), 1] = 1.0
            rain_drops['fill'][start_pixel_location + int(pixel_locations), 2] = 0.0
            rain_drops['fill'][start_pixel_location + int(pixel_locations), 3] = 1

    scat.set_edgecolors(rain_drops['frame'])
    scat.set_sizes(rain_drops['size'])
    scat.set_offsets(rain_drops['position'])
    scat.set_facecolors(rain_drops['fill'])

    time.sleep(pause)

# TODO: Make filling process more pythonic
def fill_pixels(r, g, b, t, pixel_location, rain_drops):
    rain_drops['fill'][pixel_location, 0] = 0.0
    rain_drops['fill'][pixel_location, 1] = 0.8
    rain_drops['fill'][pixel_location, 2] = 0.0
    rain_drops['fill'][pixel_location, 3] = 1




