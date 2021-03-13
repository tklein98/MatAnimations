import numpy as np


# print(np.random.uniform(0, 1, (50, 2))[:,1])

# print(np.arange(0, 1, 1/(10+1))[1:])
# print(np.arange(0, 1, 1/(5+1))[1:])

horizontal = np.arange(0, 1, 1/(10+1))[1:]
vertical = np.arange(0, 1, 1/(5+1))[1:]

arr = np.empty((0,2), float)

for j in range(5):
    temp_v = vertical[j]
    for i in range(10):
        temp_h = horizontal[i]
        arr = np.append(arr, np.array([[temp_h,temp_v]]), axis=0)


print(arr)
