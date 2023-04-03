# -*- coding: utf-8 -*-
"""
Created on Wed Mar 29 14:36:42 2023

@author: cjwin
"""

import numpy as np
import pathlib
from numpy.random import default_rng
rng = default_rng() 

allParticipants = np.arange(1, 17) #16 participants

megasetA_participants = rng.choice(allParticipants, size=8, replace=False)

megasetB_participants = np.setdiff1d(allParticipants, megasetA_participants)

print(megasetA_participants)
print(megasetB_participants)

#Find the data path:
currentFolderPath = pathlib.Path(__file__).parent.resolve()
upperFolderPath = currentFolderPath.parent.resolve()
dataPath = str(upperFolderPath) + "/Data/"
File = (dataPath + "\Megaset Assignment.txt")
with open(File, 'a') as f:
    f.write("Participants assigned megaset A: ")
    f.write(str(megasetA_participants))
    f.write("\n")
    f.write("Participants assigned megaset B: ")
    f.write(str(megasetB_participants))
    f.close