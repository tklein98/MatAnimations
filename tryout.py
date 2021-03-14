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


starting_points = {}

starting_points['1'] = [165, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
starting_points['2'] = [163, 167, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
starting_points['3'] = [160, 164, 168, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
starting_points['4'] = [158, 162, 166, 170, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
starting_points['5'] = [157, 161, 165, 169, 173, 0, 0, 0, 0, 0, 0, 0, 0, 0]
starting_points['6'] = [154, 158, 162, 166, 170, 174, 0, 0, 0, 0, 0, 0, 0, 0]
starting_points['7'] = [152, 156, 160, 164, 168, 172, 176, 0, 0, 0, 0, 0, 0, 0]
starting_points['8'] = [248, 252, 256, 260, 68, 72, 76, 80, 0, 0, 0, 0, 0, 0]
starting_points['9'] = [247, 251, 255, 259, 263, 69, 73, 77, 81, 0, 0, 0, 0, 0]
starting_points['10'] = [247, 251, 255, 259, 263, 67, 71, 75, 79, 83, 0, 0, 0, 0]
starting_points['11'] = [244, 248, 252, 256, 260, 264, 66, 70, 74, 78, 82, 0, 0, 0]
starting_points['12'] = [244, 248, 252, 256, 260, 264, 64, 68, 72, 76, 80, 84, 0, 0]
starting_points['13'] = [242, 246, 250, 254, 258, 262, 266, 64, 68, 72, 76, 80, 84, 0]
starting_points['14'] = [242, 246, 250, 254, 258, 262, 266, 62, 66, 70, 74, 78, 82, 86]


(pd.DataFrame.from_dict(data=starting_points)).to_csv('starting_points.csv', header=True)

# df = pd.read_csv('dict_file2.csv')

# print(df.head())
