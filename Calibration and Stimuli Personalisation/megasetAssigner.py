# -*- coding: utf-8 -*-
"""
Created on Wed Mar 29 14:36:42 2023

@author: cjwin
"""

import numpy as np
import pathlib
from numpy.random import default_rng
rng = default_rng() 
import os

allParticipants = np.arange(1, 17) #16 participants

halfParticipants = round(len(allParticipants)/2)

megasetA_participants = rng.choice(allParticipants, size=halfParticipants, replace=False)

megasetB_participants = np.setdiff1d(allParticipants, megasetA_participants)

print(megasetA_participants)
print(megasetB_participants)

#Find the data path:
currentFolderPath = pathlib.Path(__file__).parent.resolve()
upperFolderPath = currentFolderPath.parent.resolve()
dataPath = str(upperFolderPath) + "/Data/"
File = (dataPath + "\Megaset Assignment.txt")


#Set it up so that we can assign new participants without rewriting:
if os.path.getsize(File) != 0:
    maxAlreadyAssigned = 0
    
    with open(File, "r") as f:     
        
        lines = f.readlines()
        for line in lines:
            words = line.rstrip("]\n")
            words = words.split(" ")
            maxAlreadyAssigned_thisMegaset = max(int(x) for x in words if x.isnumeric()==1)
            if maxAlreadyAssigned_thisMegaset > maxAlreadyAssigned:
                maxAlreadyAssigned = maxAlreadyAssigned_thisMegaset
        print(maxAlreadyAssigned)
        
        for line in lines:
            if "Megaset A" in line:
                words = line.rstrip("]\n")
                words = words.split(" ")
                megaset_A_participantsAlreadyAssigned = [int(x) for x in words if x.isnumeric()==1]
                new_megasetA_participants = np.array([x for x in megasetB_participants if x > maxAlreadyAssigned], dtype=np.int)
                megasetA_participants = np.concatenate([megaset_A_participantsAlreadyAssigned, new_megasetA_participants])
                print(megasetA_participants)
                
            elif "Megaset B" in line:
                words = line.rstrip("]\n")
                words = words.split(" ")
                megaset_B_participantsAlreadyAssigned = [int(x) for x in words if x.isnumeric()==1]
                new_megasetB_participants = np.array([x for x in megasetB_participants if x > maxAlreadyAssigned], dtype=np.int)
                megasetB_participants = np.concatenate([megaset_B_participantsAlreadyAssigned, new_megasetB_participants])

#Finally, write to file:
with open(File, 'w') as f:
        f.write("Participants assigned Megaset A: ")
        f.write(str(megasetA_participants))
        f.write("\n")
        f.write("Participants assigned Megaset B: ")
        f.write(str(megasetB_participants))
        f.close
        