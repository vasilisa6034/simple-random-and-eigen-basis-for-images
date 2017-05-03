# -*- coding: utf-8 -*-
"""
Created on Tue May 02 10:33:39 2017

@author: temp
"""

import os
from scipy.misc import imresize, imread
import numpy as np

faces  = []
root = r'\' #database folder
folders = os.listdir(root)
for folder in folders:
    files = os.listdir(root + os.sep + folder)
    for filee in files:
        im = imread(root + os.sep + folder + os.sep + filee, flatten= True)
        im = imresize(im, (50,50))
        faces.append(im)
faces = np.array(faces).swapaxes(0,1).swapaxes(1,2)
                
import pickle
with open('referenceImages.dat','a+') as f:
    pickle.dump(faces,f) 
