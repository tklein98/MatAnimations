import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
import random

z = np.arange(0.066,1,0.066)

k = np.arange(0.1,1,0.09)

completex = np.array([])

for i in range(10):
    completex = np.append(completex,z)
    

completey = np.array([])

for i in k:
    full = np.full(15,i)
    completey = np.append(completey,full)

background_color = 'black'

fig = plt.figure(figsize=(12, 9))
ax = fig.add_axes([0, 0, 1, 1], frameon=False)
ax.set_xlim(0, 1), ax.set_xticks([])
ax.set_ylim(0, 1), ax.set_yticks([])
fig.set_facecolor(background_color)


shape1 = [0,1,16,31]
shape2 = [3,4,19]
shape3 = [9,10,24]
shape4 = [13,29]
shape5 = [21,22]
shape6 = [26,41]
shape7 = [33,47,48]
shape8 = [35,49,51]
shape9 = [37,38]
shape10 = [43,57]
shape11 = [45]
shape12 = [54,68]
shape13 = [59,73]
shape14 = [62,77,78,92]
shape15 = [65,80]
shape16 = [70,71,72]
shape17 = [75,90]
shape18 = [82,96,97,98,112]
shape19 = [84,85]
shape20 = [87,103]
shape21 = [94,108,109]
shape22 = [101,116,117]
shape23 = [104,119]
shape24 = [106]
shape25 = [114,130,144]
shape26 = [120,135,136]
shape27 = [122,137]
shape28 = [125,140]
shape29 = [128,142]
shape30 = [133,148]



shapes = [shape1] + [shape2] + [shape3]+ [shape4]+[shape5]+[shape6]+[shape7]+[shape8]+[shape9]+[shape10]+[shape11]+[shape12]\
+[shape13]+[shape14]+[shape15]+[shape16]+[shape17]+[shape18]+[shape19]+[shape20]+[shape21]+[shape22]+[shape23]+[shape24]+[shape25]+[shape26]+[shape27]+[shape28]+[shape29]+[shape30]


colors = np.full((150,3),[0.0,0.0,0.0])

r = 1
g = 1
b = 0

rs = 1.0
gs = 1.0
bs = 0.0

def iterate(frame_number):
    # for shape in shapes:
        
    r = random.random()
    g = random.random()
    b = random.random()
    

    colors[shapes[frame_number]] = [rs,gs,bs]
    
    if frame_number > 0:
        colors[shapes[frame_number-1]] = colors[shapes[frame_number-1]]/10
    scat.set_color(colors)
    
    print(colors)
    
    
    
plt.rcParams['axes.facecolor'] = 'black'
# plt.scatter(completex, completey, s= 80,color=colors, linewidths= 1, edgecolors= [0,0,0])

scat = ax.scatter(completex, completey, s= 500,color=colors, linewidths= 1, edgecolors= [0,0,0])


# figManager = plt.get_current_fig_manager()
# figManager.full_screen_toggle()


animation = FuncAnimation(fig, iterate, interval=250,frames=30,repeat=True)

plt.show()