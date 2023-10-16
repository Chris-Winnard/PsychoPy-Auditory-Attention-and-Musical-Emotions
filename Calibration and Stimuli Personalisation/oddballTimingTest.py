#Code to read through oddball start times list and check they are not too close.

import pathlib
import glob
import os
import soundfile as sf
import numpy as np
import math
from pydub import AudioSegment
import re
import xlsxwriter
from utils.SerialTriggerEncoder import SerialTriggerEncoder


#Find participant full path just from their ID
participantID = "P03"

idealOB_segmentLength = 1808*0.1/2205
idealOB_length = 6*idealOB_segmentLength
StrictTolerance = idealOB_length
LaxTolerance= 1+StrictTolerance

#Find the stimuli path:
currentFolderPath = pathlib.Path(__file__).parent.resolve()
upperFolderPath = currentFolderPath.parent.resolve()

#Create output path:
dataPath = str(upperFolderPath) + "/Data/"
TriggerConfigFile = r"C:\Users\cjwin\OneDrive - Queen Mary, University of London\Documents\Music Interestingness in the Brain\Par 22-9-23\Trigger Generation (Not Inc P2 Trial Trigs)\Trigger Config.xlsx"


groupAssignmentFile = dataPath + "/Participant Groups.txt" #Needed for taking collecting stimuli, and saving to right place:
with open(groupAssignmentFile, 'r') as f:
    lines = f.readlines()
    for line in lines:
        if "Group A1" in line and participantID in line:
            participantPath = str(upperFolderPath) + "/Data/Group A1/" + participantID + "/"
        elif "Group A2" in line and participantID in line:
            participantPath = str(upperFolderPath) + "/Data/Group A2/" + participantID + "/"
            
        elif "Group B1" in line and participantID in line:
            participantPath = str(upperFolderPath) + "/Data/Group B1/" + participantID + "/"
        elif "Group B2" in line and participantID in line:
            participantPath = str(upperFolderPath) + "/Data/Group B2/" + participantID + "/"
    f.close

##########################################################################################################################    
#Let's read and convert the start time data
startTimesFile = participantPath + "\Oddball Start Times.txt"
startTimesData = open(startTimesFile, 'r')
lines = startTimesData.readlines()
startTimesData.close()

def checkTrigTimes(participantPath):
        
    #################################################################################################################################################

    def oddballTrigs(filename):
        
        #Include times of start/end/oddballs in the metafile? At v least, have the order correct in metafile? <<Is it possible that the audio oddballs
        #themselves aren't playing in right order? E.g, all 149 ones going before 150 ones in audio file???
        attendedInst = filename[-17:-13]
        
        thisMixVibr = filename[0:6] + "Vibr Oddball Test-" + filename[-17:] #E.g, Set01-Oddball Test Mix-Harm Attended.wav -> Set01-Vibr Oddball Test-Harm Attended.wav
        thisMixHarm = filename[0:6] + "Harm Oddball Test-" + filename[-17:] #E.g, Set01-Oddball Test Mix-Harm Attended.wav -> Set01-Harm Oddball Test-Harm Attended.wav
        thisMixKeyb = filename[0:6] + "Keyb Oddball Test-" + filename[-17:] 
        
        linesReadFrom = 0        
        for line in lines:
            if thisMixVibr in line:
                vibrOddballStartTimes = re.findall("\d+\.\d+", line) 
                linesReadFrom += 1
            elif thisMixHarm in line:
                harmOddballStartTimes = re.findall("\d+\.\d+", line)
                linesReadFrom += 1
            elif thisMixKeyb in line:
                keybOddballStartTimes = re.findall("\d+\.\d+", line)
                linesReadFrom += 1
            
            if linesReadFrom == 3:
                break
        
        allOBTimes = vibrOddballStartTimes + harmOddballStartTimes + keybOddballStartTimes
        
        return allOBTimes
        
    ########################################################################################################################################################
    minorProblems = 0
    majorProblems = 0
    
    for file in os.scandir(participantPath):
     if "Oddball Test Mix" in file.name:
        name = file.name
        oddballTimes = oddballTrigs(name)
        for i in range(len(oddballTimes)):
            for j in range(i, len(oddballTimes)):
                if i != j:
                    time1 = float(oddballTimes[i])
                    time2 = float(oddballTimes[j])
                    testBool_LAX = math.isclose(time1, time2,abs_tol = LaxTolerance)
                    testBool_STRICT = math.isclose(time1, time2,abs_tol = StrictTolerance)
                    
                    if testBool_LAX == True and testBool_STRICT == False:
                        print("Warning - found two oddballs within one second plus an oddball length of each other. They are NOT likely to be"
                              + " directly overlapping.")
         
                        print("These are in file: " + name)
                        print("\n")
                        minorProblems += 1
                        
                    if testBool_STRICT == True:
                        print("Warning - found two oddballs LIKELY TO BE DIRECTLY OVERLAPPING.")
                        print("These are in file: " + name)
                        print("\n")
                        majorProblems += 1
            
    return minorProblems, majorProblems

#################################################################################################################################################

minorProblems, majorProblems = checkTrigTimes(participantPath)
print(minorProblems)
print(majorProblems)