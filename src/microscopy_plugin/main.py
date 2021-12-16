import numpy as np
import os
import glob
import re
import shutil

import tkinter as tk
from tkinter import filedialog
from tkinter import simpledialog
from prompt_toolkit import prompt

'''
path_original_file = askdirectory(title='Select the folder where the ClearScope acquisition data are stored') # shows dialog box and return the path
path_save_copy = askdirectory(title='Select the folder where to copy the portion of the ClearScope data') # shows dialog box and return the path
'''

'''
#Selection ClearScope Folder

path_original_file = filedialog.askdirectory(title='Select the folder where the ClearScope acquisition data are stored') # shows dialog box and return the path

#path_original_file = 'Y:/Alice/9007_CBT_PNP_LIGHTSHEET/CLEARSCOPE/Stitch_test_20211126/0001'
directories = glob.glob(path_original_file + "/*c") # the directories we are intrested in finish with a c for channel in ClearScope notation
newPath = directories[0]
newPath = newPath.replace("\\", "/")
directories2 = glob.glob(newPath + "/*c.tif") # the directories we are intrested in finish with a c for channel in ClearScope notation


n_tiles = len(directories)
n_slices = len(directories2)

print('There are "{}" tiles and "{}" slices per tiles.'.format(n_tiles,n_slices))

print("Original string : " + path_original_file)

num = re.findall(r'\d+', path_original_file)

print(num)

'''
#Build TeraStitcher architecture

origin = np.array([7.2,15.4,14.4])  # Units: mm
displacement = np.array([100.,100.]) # Units: um
voxelSize = np.array([0.8,0.8,1.])  # Units: um
tiling = np.array([5,5])  # Units: uniteless
conversionFactor = 10000   # Units: tenth um / mm

pathNewfolder = filedialog.askdirectory(title='Select the folder where to build the Tera Stitcher data architecture',initialdir = 'C:/Users/vgaillet/test_conversion') # shows dialog box and return the path

#pathNewfolder = 'C:/Users/vgaillet/test_conversion'
nameNewFolder = simpledialog.askstring(title="Test",
                                  prompt="Enter the folder name?:")
#Combine path
pathNewDir = pathNewfolder + "/" + nameNewFolder
dirs = os.listdir(pathNewfolder)

rangeLoop = len(dirs)

#Check that the name of the new directory is not already being used

isAlreadyPresent = False
if rangeLoop > 0:
    for ind in range(rangeLoop):
        if nameNewFolder == dirs[ind]:
            isAlreadyPresent = True

if isAlreadyPresent is False:
    os.makedirs(pathNewDir)
    for ind1 in range(tiling[0]):
        textVert = str(int(origin[0] * conversionFactor) + int(displacement[0]) * 10 * ind1)
        textVert = textVert.rjust(6, '0')
        os.makedirs(pathNewDir + '/' + textVert)
        for ind2 in range(tiling[1]):
            textHorz = str(int(origin[1] * conversionFactor) + int(displacement[1]) * 10 * ind2)
            textHorz = textHorz.rjust(6, '0')
            os.makedirs(pathNewDir + '/' + textVert + '/' + textVert + '_' + textHorz)
else:
    #print('The directory named "' + nameNewFolder + '" is already used.')
    print('The directory named "{}" is already used.'.format(nameNewFolder))
