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

with open(MegasetFile, "r") as f:     
    
    lines = f.readlines()
    
    for line in lines:
        
        if "Megaset A" in line:
            words = line.rstrip("]\n")
            words = words.split(" ")
            megasetA_participants = [int(x) for x in words if x.isnumeric()==1]
            
        elif "Megaset B" in line:
            words = line.rstrip("]\n")
            words = words.split(" ")
            megasetB_participants = [int(x) for x in words if x.isnumeric()==1]
            
    f.close

#Split participants listening to Megaset A into two groups, A1 and A2:
half_megasetA_participants = round(len(megasetA_participants)/2)
GroupA1_participants = rng.choice(megasetA_participants, size=half_megasetA_participants, replace=False)
GroupA2_participants = np.setdiff1d(megasetA_participants, GroupA1_participants)

#Same for Megaset B:
half_megasetB_participants = round(len(megasetB_participants)/2)
GroupB1_participants = rng.choice(megasetB_participants, size=half_megasetB_participants, replace=False)
GroupB2_participants = np.setdiff1d(megasetB_participants, GroupB1_participants)

#Set it up so that we can assign new participants without rewriting:
if os.path.getsize(ParticipantGroupFile) != 0:
    maxAlreadyAssigned = 0
    
    with open(ParticipantGroupFile, "r") as f:     
        
        lines = f.readlines()
        for line in lines:
            words = line.rstrip("]\n")
            words = words.split(" ")
            maxAlreadyAssigned_thisGroup = max(int(x) for x in words if x.isnumeric()==1)
            if maxAlreadyAssigned_thisGroup > maxAlreadyAssigned:
                maxAlreadyAssigned = maxAlreadyAssigned_thisGroup
        
        for line in lines:
            if "Group A1" in line:
                words = line.rstrip("]\n")
                words = words.split(" ")
                GroupA1_participantsAlreadyAssigned = [int(x) for x in words if x.isnumeric()==1]
                new_GroupA1_participants = np.array([x for x in GroupA1_participants if x > maxAlreadyAssigned], dtype=np.int)
                GroupA1_participants = np.concatenate([GroupA1_participantsAlreadyAssigned, GroupA1_participants])
                
            elif "Group A2" in line:
                words = line.rstrip("]\n")
                words = words.split(" ")
                GroupA2_participantsAlreadyAssigned = [int(x) for x in words if x.isnumeric()==1]
                new_GroupA2_participants = np.array([x for x in GroupA2_participants if x > maxAlreadyAssigned], dtype=np.int)
                GroupA2_participants = np.concatenate([GroupA2_participantsAlreadyAssigned, new_GroupA2_participants])
                
            elif "Group B1" in line:
                words = line.rstrip("]\n")
                words = words.split(" ")
                GroupB1_participantsAlreadyAssigned = [int(x) for x in words if x.isnumeric()==1]
                new_GroupB1_participants = np.array([x for x in GroupB1_participants if x > maxAlreadyAssigned], dtype=np.int)
                GroupB1_participants = np.concatenate([GroupB1_participantsAlreadyAssigned, GroupB1_participants])
            
            elif "Group B2" in line:
                words = line.rstrip("]\n")
                words = words.split(" ")
                GroupB2_participantsAlreadyAssigned = [int(x) for x in words if x.isnumeric()==1]
                GroupB2_participants = np.array([x for x in GroupB2_participants if x > maxAlreadyAssigned], dtype=np.int)
                GroupB2_participants = np.concatenate([GroupB2_participantsAlreadyAssigned, GroupB2_participants])

#Finally, write to file:
with open(ParticipantGroupFile, 'w') as f:
        f.write("Participant groups:\n")
        f.write("Group A1: ")
        f.write(str(GroupA1_participants))
        f.write("\n")
        f.write("Group A2: ")
        f.write(str(GroupA2_participants))
        f.write("\n")
        f.write("Group B1: ")
        f.write(str(GroupB1_participants))
        f.write("\n")
        f.write("Group B2: ")
        f.write(str(GroupB2_participants))   
        f.write("\n")
        f.write("Remember to add in leading zeros for single-digit numbers.")
        f.close
    
print("Remember to add in leading zeros for single-digit numbers.")