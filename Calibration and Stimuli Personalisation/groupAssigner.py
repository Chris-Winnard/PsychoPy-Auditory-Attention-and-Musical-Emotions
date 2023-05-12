import numpy as np
import pathlib
from numpy.random import default_rng
rng = default_rng() 
import os

#Find the data path:
currentFolderPath = pathlib.Path(__file__).parent.resolve()
upperFolderPath = currentFolderPath.parent.resolve()
dataPath = str(upperFolderPath) + "/Data/"
MegasetFile = (dataPath + "\Megaset Assignment.txt")

ParticipantGroupFile = (dataPath + "\Participant Groups.txt")

megasetA_participants = []
megasetB_participants = []

with open(MegasetFile, "r") as f:     
    
    lines = f.readlines() 
    for line in lines:
        
        if "Megaset A" in line:
            words = line.rstrip("]\n")
            words = words.split(" ")
            for x in words:
                if len(x)  == 3:
                    if x[0] == "P":
                        megasetA_participants.append(x)
            
        elif "Megaset B" in line:
            words = line.rstrip("]\n")
            words = words.split(" ")
            for x in words:
                if len(x)  == 3:
                    if x[0] == "P":
                        megasetB_participants.append(x)
    f.close

#Split participants listening to Megaset A into two groups, A1 and A2:
half_megasetA_participants = round(len(megasetA_participants)/2)
A1_participants = rng.choice(megasetA_participants, size=half_megasetA_participants, replace=False)
A2_participants = np.setdiff1d(megasetA_participants, A1_participants)
A1_participants = A1_participants.tolist() #Convert to lists
A2_participants = A2_participants.tolist()

#Same for Megaset B:
half_megasetB_participants = round(len(megasetB_participants)/2)
B1_participants = rng.choice(megasetB_participants, size=half_megasetB_participants, replace=False)
B2_participants = np.setdiff1d(megasetB_participants, B1_participants)
B1_participants = B1_participants.tolist() #Convert to lists
B2_participants = B2_participants.tolist()

#Set it up so that we can assign new participants without contradicting what was already written:
A1_alreadyAssigned = []
A2_alreadyAssigned = []
B1_alreadyAssigned = []
B2_alreadyAssigned = []

with open(ParticipantGroupFile,"r") as f:     
    
    lines = f.readlines()
    for line in lines:
        if "Group A1" in line:
            A1_original = line.rstrip("\n")
            
        if "Group A2" in line:
            A2_original = line.rstrip("\n")
        
        if "Group B1" in line:
            B1_original = line.rstrip("\n")
        
        if "Group B2" in line:
            B2_original = line
            
        words = line.rstrip("\n")
        words = words.rsplit(" ")
        
        for word in A1_participants:
            if word in words:
                A1_alreadyAssigned.append(word)
        
        for word in A2_participants:
            if word in words:
                A2_alreadyAssigned.append(word)
        
        for word in B1_participants:
            if word in words:
                B1_alreadyAssigned.append(word)
        
        for word in B2_participants:
            if word in words:
                B2_alreadyAssigned.append(word)

    A1_participants_new = set(A1_participants) - set(A1_alreadyAssigned)
    A1_participants_new = " ".join(str(x) for x in A1_participants_new) #String format
    A1_participants_updated = A1_original + " " + A1_participants_new
    
    A2_participants_new = set(A2_participants) - set(A2_alreadyAssigned)
    A2_participants_new = " ".join(str(x) for x in A2_participants_new)
    A2_participants_updated = A2_original + " " + A2_participants_new

    B1_participants_new = set(B1_participants) - set(B1_alreadyAssigned)
    B1_participants_new = " ".join(str(x) for x in B1_participants_new)
    B1_participants_updated = B1_original + " " + B1_participants_new
    
    B2_participants_new = set(B2_participants) - set(B2_alreadyAssigned)
    B2_participants_new = " ".join(str(x) for x in B2_participants_new)
    B2_participants_updated = B2_original + " " + B2_participants_new
    
    f.close()

#Finally, write to file:
with open(ParticipantGroupFile, "w") as f:    
    f.write(str(A1_participants_updated))
    f.write("\n")
    f.write(str(A2_participants_updated))  
    f.write("\n")
    f.write(str(B1_participants_updated))
    f.write("\n")
    f.write(str(B2_participants_updated))  
    f.close