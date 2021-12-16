import matplotlib.pyplot as plt
import numpy as np
import glob
import re
import os
from functionsConvertClearScope import convert_coord_cs_to_xy
from functionsConvertClearScope import convert_coord_xy_to_cs
from functionsConvertClearScope import getClearScopeRange
from functionsConvertClearScope import getClearScopeRange2

from tkinter import Tk
from tkinter.filedialog import askdirectory
'''
path_original_file = askdirectory(title='Select the folder where the ClearScope acquisition data are stored') # shows dialog box and return the path
path_save_copy = askdirectory(title='Select the folder where to copy the portion of the ClearScope data') # shows dialog box and return the path

files = glob.glob(path_original_file + '/*_00001*0c')
print(path_original_file)
'''
vector = np.arange(1,45)

#cx,cy = convert_coord_cs_to_xy(vector,13,17)

cs = convert_coord_xy_to_cs([2,2,2], [1,2,3], 13, 17)

dim_tiling_x = 13
dim_tiling_y = 17

range_x = [2,3]
range_y = [1,3]

#range_x = [2,3]
#range_y = [11,12]

test = getClearScopeRange(dim_tiling_x, dim_tiling_y, range_x, range_y)
test2 = getClearScopeRange2(dim_tiling_x, dim_tiling_y, range_x, range_y)



l = dim_tiling_x
sizeV = dim_tiling_x*dim_tiling_y

vector = np.arange(sizeV)
x = vector
y1 = np.absolute(np.mod(vector-l-1, 2*l)-l+0.5)+0.5
y2 = np.floor(vector / l) + 1

min_x = np.min(x)
max_x = np.max(x)

min_y = np.min(np.append(y1, y2))
max_y = np.max(np.append(y1, y2))

plt.plot(x, y1, 'ro', color='red')
plt.plot(x, y2, 'ro', color='blue')

#plt.axis(min_x, max_x, min_y, max_y)
plt.grid()
plt.show()
