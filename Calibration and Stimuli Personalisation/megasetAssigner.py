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
megasetA_participants = megasetA_participants.tolist() #Convert to list

megasetB_participants = np.setdiff1d(allParticipants, megasetA_participants)
megasetB_participants = megasetB_participants.tolist()

for i in range(0, len(megasetA_participants)):
    x = megasetA_participants[i]
    if x < 10:
        x = "P0" + str(x)
    else:
        x = "P" + str(x)
    megasetA_participants[i] = x
    
for i in range(0, len(megasetB_participants)):
    x = megasetB_participants[i]
    if x < 10:
        x = "P0" + str(x)
    else:
        x = "P" + str(x)
    megasetB_participants[i] = x

#Find the data path:
currentFolderPath = pathlib.Path(__file__).parent.resolve()
upperFolderPath = currentFolderPath.parent.resolve()
dataPath = str(upperFolderPath) + "/Data/"
File = (dataPath + "\Megaset Assignment.txt")

#Set it up so that we can assign new participants without contradicting what was already written:
    
def intersection(lst1, lst2):
    lst3 = [value for value in lst1 if value in lst2]
    return lst3

with open(File,"r+") as f:     
    
    words = [line.split(' ') for line in f.readlines()]
    for word in words:
        word = word.rstrip("\"")
    print(words)
    print(megasetA_participants)
    A_alreadyAssigned = intersection(words, megasetA_participants)
    megasetA_participants = set(megasetA_participants) - set(A_alreadyAssigned)
    megasetA_participants = str(megasetA_participants)
    megasetA_participants = megasetA_participants.rstrip(",")
        
    B_alreadyAssigned = intersection(words, megasetB_participants)
    megasetB_participants = set(megasetB_participants) - set(B_alreadyAssigned)
    megasetB_participants = str(megasetB_participants)
    megasetB_participants = megasetB_participants.rstrip(",")
    f.close()

#Finally, write to file:
with open(File,"a") as f:    
    f.write("Participants assigned Megaset A: ")
    f.write(str(megasetA_participants))
    f.write("\n")
    f.write("Participants assigned Megaset B: ")
    f.write(str(megasetB_participants))   
    f.write("\n")
    f.close
