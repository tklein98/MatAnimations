# import numpy as np


# # print(np.random.uniform(0, 1, (50, 2))[:,1])

# # print(np.arange(0, 1, 1/(10+1))[1:])
# # print(np.arange(0, 1, 1/(5+1))[1:])

# horizontal = np.arange(0, 1, 1/(10+1))[1:]
# vertical = np.arange(0, 1, 1/(5+1))[1:]

# arr = np.empty((0,2), float)

# for j in range(5):
#     temp_v = vertical[j]
#     for i in range(10):
#         temp_h = horizontal[i]
#         arr = np.append(arr, np.array([[temp_h,temp_v]]), axis=0)


# print(arr)
import pandas as pd
import numpy as np


# starting_points = {}

# starting_points['1'] = [165, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
# starting_points['2'] = [163, 167, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
# starting_points['3'] = [160, 164, 168, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
# starting_points['4'] = [158, 162, 166, 170, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
# starting_points['5'] = [157, 161, 165, 169, 173, 0, 0, 0, 0, 0, 0, 0, 0, 0]
# starting_points['6'] = [154, 158, 162, 166, 170, 174, 0, 0, 0, 0, 0, 0, 0, 0]
# starting_points['7'] = [152, 156, 160, 164, 168, 172, 176, 0, 0, 0, 0, 0, 0, 0]
# starting_points['8'] = [248, 252, 256, 260, 68, 72, 76, 80, 0, 0, 0, 0, 0, 0]
# starting_points['9'] = [247, 251, 255, 259, 263, 69, 73, 77, 81, 0, 0, 0, 0, 0]
# starting_points['10'] = [247, 251, 255, 259, 263, 67, 71, 75, 79, 83, 0, 0, 0, 0]
# starting_points['11'] = [244, 248, 252, 256, 260, 264, 66, 70, 74, 78, 82, 0, 0, 0]
# starting_points['12'] = [244, 248, 252, 256, 260, 264, 64, 68, 72, 76, 80, 84, 0, 0]
# starting_points['13'] = [242, 246, 250, 254, 258, 262, 266, 64, 68, 72, 76, 80, 84, 0]
# starting_points['14'] = [242, 246, 250, 254, 258, 262, 266, 62, 66, 70, 74, 78, 82, 86]


# (pd.DataFrame.from_dict(data=starting_points)).to_csv('starting_points.csv', header=True)

# df = pd.read_csv('dict_file2.csv')

# print(df.head())


character_pixels = {}

character_pixels['A'] = [0, 2, 30, 32, 60, 61, 62, 90, 92, 120, 121, 122]
character_pixels['B'] = [0, 1, 30, 32, 60, 61, 90, 92, 120, 121]
character_pixels['C'] = [1, 2, 30, 60, 90, 121, 122]
character_pixels['D'] = [0, 1, 30, 32, 60, 62, 90, 92, 120, 121]
character_pixels['E'] = [0, 1, 2, 30, 60, 61, 90, 120, 121, 122]
character_pixels['F'] = [0, 30, 60, 61, 90, 120, 121, 122]
character_pixels['G'] = [1, 2, 30, 32, 60, 62, 90, 121, 122]
character_pixels['H'] = [0, 2, 30, 32, 60, 61, 62, 90, 92, 120, 122]
character_pixels['I'] = [0, 1, 2, 31, 61, 91, 120, 121, 122]
character_pixels['J'] = [0, 1, 2, 30, 32, 62, 92, 122]
character_pixels['K'] = [0, 2, 30, 32, 60, 61, 90, 92, 120, 122]
character_pixels['L'] = [0, 1, 2, 30, 60, 90, 120]
character_pixels['M'] = [0, 2, 30, 32, 60, 62, 90, 91, 92, 120, 122]
character_pixels['N'] = [0, 2, 30, 32, 60, 62, 90, 92, 120, 121, 122]
character_pixels['O'] = [0, 1, 2, 30, 32, 60, 62, 90, 92, 120, 121, 122]
character_pixels['P'] = [0, 30, 60, 61, 62, 90, 92, 120, 121, 122]
character_pixels['Q'] = [2, 30, 31, 60, 62, 90, 92, 120, 121, 122]
character_pixels['R'] = [0, 2, 30, 32, 60, 61, 90, 92, 120, 121]
character_pixels['S'] = [0, 1, 32, 61, 90, 121, 122]
character_pixels['T'] = [1, 31, 61, 91, 120, 121, 122]
character_pixels['U'] = [0, 1, 2, 30, 32, 60, 62, 90, 92, 120, 122]
character_pixels['V'] = [0, 1, 30, 32, 60, 62, 90, 92, 120, 122]
character_pixels['W'] = [0, 2, 30, 31, 32, 60, 62, 90, 92, 120, 122]
character_pixels['X'] = [0, 2, 30, 32, 61, 90, 92, 120, 122]
character_pixels['Y'] = [1, 31, 60, 61, 62, 90, 92, 120, 122]
character_pixels['Z'] = [0, 1, 2, 30, 61, 92, 120, 121, 122]
character_pixels['a'] = [0, 2, 30, 32, 60, 61, 62, 90, 92, 120, 121, 122]
character_pixels['b'] = [0, 2, 30, 32, 60, 61, 62, 90, 92, 120, 121, 122]
character_pixels['c'] = [0, 2, 30, 32, 60, 61, 62, 90, 92, 120, 121, 122]
character_pixels['d'] = [0, 2, 30, 32, 60, 61, 62, 90, 92, 120, 121, 122]
character_pixels['e'] = [0, 2, 30, 32, 60, 61, 62, 90, 92, 120, 121, 122]


df = pd.DataFrame.from_dict(character_pixels, orient='index').T

print(df)
(df).to_csv('capital_letters.csv', header=True)
