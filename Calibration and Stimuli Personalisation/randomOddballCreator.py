import pathlib
import random
from random import choice
import librosa
import soundfile as sf
import numpy as np
import os
import re
from itertools import chain

#Find the stimuli path:
currentFolderPath = pathlib.Path(__file__).parent.resolve()
upperFolderPath = currentFolderPath.parent.resolve()
stimuliPath = str(upperFolderPath) + "/Stimuli"

#Create output path:
dataPath = str(upperFolderPath) + "/Data/"
participantPath = str(upperFolderPath) + "/Data/" + "/4" #- assigned to megaset B
os.mkdir(participantPath)
File = (participantPath + "\Oddball Start Times.txt")
with open(File, 'a') as f: #Create the file now to prevent any confusion later, because oddballsForbidden needs to read from it.
    f.close


#Find which stimuli are assigned to this participant:

megasetAssignmentFile = dataPath + "/Megaset Assignment.txt"

participantName = os.path.split(participantPath)[1]

with open(megasetAssignmentFile, 'r') as f:
    lines = f.readlines()
    for line in lines:
        if "Megaset A" in line and participantName in line:
            thisParticipantStimuliPath = stimuliPath + "\Megaset A"
        elif "Megaset B" in line and participantName in line:
            thisParticipantStimuliPath = stimuliPath + "\Megaset B"
    f.close
    

"""Timings: one data point = 4.5e-05 (the same for all pieces to the 20th decimal). So, we don't need to
normalise w.r.t piece length. Use 2205 = 0.1s. To ensure pieces are exactly 30s each, we remove any excess data
points."""

tenthSec = 2205
idealOB_segmentLength = 1808
idealOB_length = 6*idealOB_segmentLength
OB_lengthTolerance = 0.001 #E.g, 0.05 is 5% tolerance

#Function to create an oddball for given signal, starting at a given point in that signal:
def createOddball(signalCopy, start, actualOB_length):    
    
    actualOB_segmentLength = round(actualOB_length/6)
    
    firstPart = signalCopy[start:start+actualOB_segmentLength]
    firstPart = librosa.effects.pitch_shift(firstPart, sr, 0.95, bins_per_octave=12)
    
    secondPart = signalCopy[start+actualOB_segmentLength:start+2*actualOB_segmentLength]
    secondPart = librosa.effects.pitch_shift(secondPart, sr, -0.95, bins_per_octave=12)
    
    thirdPart = signalCopy[start+2*actualOB_segmentLength:start+3*actualOB_segmentLength]
    thirdPart = librosa.effects.pitch_shift(thirdPart, sr, 0.95, bins_per_octave=12)
    
    fourthPart = signalCopy[start+3*actualOB_segmentLength:start+4*actualOB_segmentLength]
    fourthPart = librosa.effects.pitch_shift(fourthPart, sr, -0.95, bins_per_octave=12)
    
    fifthPart = signalCopy[start+4*actualOB_segmentLength:start+5*actualOB_segmentLength]
    fifthPart = librosa.effects.pitch_shift(fifthPart, sr, 0.95, bins_per_octave=12)
    
    sixthPart = signalCopy[start+5*actualOB_segmentLength:start+actualOB_length] #Notice we don't use "6*actualOB_segmentLength"- avoid rounding problems
    sixthPart = librosa.effects.pitch_shift(sixthPart, sr, -0.95, bins_per_octave=12)
    
    oddball = np.concatenate((firstPart, secondPart, thirdPart, fourthPart, fifthPart, sixthPart))    
    
    return oddball

#Function to add random oddballs:
def addOddballs(signalCopy, forbiddenOddballPeriods_Starts):
    numberOddballs = random.randint(1, 3) #From uniform dist.
    startTimes = np.zeros(numberOddballs)
    
    excludedStartTimes = []
    
    #We set it up so that oddballs can't overlap (+/- 1 oddball length buffer period around existing start times). Also include a 1s grace period either side. This applies both WITHIN streams, and between them.
    
    #Create chain for excluded ranges. Turn chains into tuples so they can be reused.
    if len(forbiddenOddballPeriods_Starts) >= 1:
        excludedStartTimes = range(forbiddenOddballPeriods_Starts[0] -idealOB_length-10*tenthSec, forbiddenOddballPeriods_Starts[0] + idealOB_length+10*tenthSec)
        
        if len(forbiddenOddballPeriods_Starts) >= 2:
            x2 = range(forbiddenOddballPeriods_Starts[1] -idealOB_length-10*tenthSec, forbiddenOddballPeriods_Starts[1] + idealOB_length+10*tenthSec)
            excludedStartTimes = tuple(chain(excludedStartTimes, x2))
            
            if len(forbiddenOddballPeriods_Starts) >= 3:
                x3 = range(forbiddenOddballPeriods_Starts[2] - idealOB_length-10*tenthSec, forbiddenOddballPeriods_Starts[2] + idealOB_length+10*tenthSec)
                excludedStartTimes = tuple(chain(excludedStartTimes, x3))
                
                if len(forbiddenOddballPeriods_Starts) >= 4:
                    x4 = range(forbiddenOddballPeriods_Starts[3] - idealOB_length-10*tenthSec, forbiddenOddballPeriods_Starts[3] + idealOB_length+10*tenthSec)
                    excludedStartTimes = tuple(chain(excludedStartTimes, x4))
                    
                    if len(forbiddenOddballPeriods_Starts) >= 5:
                        x5 = range(forbiddenOddballPeriods_Starts[4] - idealOB_length-10*tenthSec, forbiddenOddballPeriods_Starts[4] + idealOB_length+10*tenthSec)
                        excludedStartTimes = tuple(chain(excludedStartTimes, x5))
                        
                        if len(forbiddenOddballPeriods_Starts) == 6:
                            x6 = range(forbiddenOddballPeriods_Starts[5] - idealOB_length-10*tenthSec, forbiddenOddballPeriods_Starts[5] + idealOB_length+10*tenthSec)
                            excludedStartTimes = tuple(chain(excludedStartTimes, x6))

    for i in range(numberOddballs):
        
    #NOTE: We use a grace period at start, and accounting for time oddball might play at end. Also a grace period of +/- one oddball length either side - so you can't have two
    #simultaneously, or even one straight after another. forbiddenOddballPeriods_Starts added in to implement this between streams.

        if i == 0:
            validOddball = False #We only want oddballs with a reasonable (mean) amplitude. Oddballs covering quiet periods may be too difficult to hear.
            #Also, oddball lengths must fall within certain tolerances
            
            while validOddball == False:
                start1 = choice([j for j in possibleStartTimes if j not in excludedStartTimes])
                
                #Find the zero crossing closest to start1 + an idealised oddball length:
                shiftedPossStartTimes = possibleStartTimes - start1
                end1Index = (np.abs(shiftedPossStartTimes - idealOB_length)).argmin()
                end1 = possibleStartTimes[end1Index]
                actualOB_length1 = round(end1 - start1)
                
                if np.abs(actualOB_length1 - idealOB_length) <= OB_lengthTolerance*idealOB_length: #Length tolerance
                    oddball1 = createOddball(signalCopy, start1, actualOB_length1)
                
                    if np.mean(abs(oddball1)) >= 7.5e-3: #Mean amplitude tolerance
                        validOddball = True
            
            startTimes[i] = start1
            signalCopy[start1:start1+actualOB_length1] = oddball1 #Insert the oddball.
            
            #Add oddball and the surrounding period to excludedStartTimes:
            x7 = range(start1-actualOB_length1-10*tenthSec, start1+actualOB_length1+10*tenthSec)
            excludedStartTimes = tuple(chain(excludedStartTimes, x7))

        if i == 1:      
            validOddball = False
            
            while validOddball == False:
                start2 = choice([j for j in possibleStartTimes if j not in excludedStartTimes])
                
                shiftedPossStartTimes = possibleStartTimes - start2
                end2Index = (np.abs(shiftedPossStartTimes - idealOB_length)).argmin()
                end2 = possibleStartTimes[end2Index]
                actualOB_length2 = round(end2 - start2)
                
                if np.abs(actualOB_length2 - idealOB_length) <= OB_lengthTolerance*idealOB_length:
                    oddball2 = createOddball(signalCopy, start2, actualOB_length2)
                
                    if np.mean(abs(oddball2)) >= 7.5e-3: #Mean amplitude tolerance
                        validOddball = True
            
            startTimes[i] = start2
            signalCopy[start2:start2+actualOB_length2] = oddball2
            
            x8 = range(start2-actualOB_length2-10*tenthSec, start2+actualOB_length2+10*tenthSec)
            excludedStartTimes = tuple(chain(excludedStartTimes, x8))
            
        if i == 2:
            validOddball = False
            
            while validOddball == False:
                start3 = choice([j for j in possibleStartTimes if j not in excludedStartTimes])
                
                shiftedPossStartTimes = possibleStartTimes - start3
                end3Index = (np.abs(shiftedPossStartTimes - idealOB_length)).argmin()
                end3 = possibleStartTimes[end3Index]
                actualOB_length3 = round(end3 - start3)
                
                if np.abs(actualOB_length3 - idealOB_length) <= OB_lengthTolerance*idealOB_length:
                    oddball3 = createOddball(signalCopy, start3, actualOB_length3)
                
                    if np.mean(abs(oddball3)) >= 7.5e-3: #Mean amplitude tolerance
                        validOddball = True
            
            startTimes[i] = start3
            signalCopy[start3:start3+actualOB_length3] = oddball3
            
    return signalCopy, startTimes

def oddballFileWriter(currentFilename, signal, attendedInst):
        pause = np.zeros(110250)
        forbiddenOddballPeriods_Starts = oddballsForbidden(currentFilename) #Prevents overlapping/consecutive oddballs BETWEEN STREAMS to avoid participant confusion.                
        augmentedSignalCopy, startTimes = addOddballs(signal, forbiddenOddballPeriods_Starts)

        #Create and write oddball file:
        oddballStimulusFull = np.concatenate((originalSignalCopy, pause, augmentedSignalCopy))
        sf.write(participantPath + "/" + str(currentFilename)[:-4] + " Oddball Test-" + attendedInst + " Attended.wav", oddballStimulusFull, sr)
        
        #Record when oddballs start:   
            
        startTimes = startTimes*30/661500 #Convert to seconds
        startTimes += 35 #Accounts for first playing and the 5s pause
        startTimes = str(startTimes)
        with open(File, 'a') as f:
            f.write("Oddball Start Times for \"" + str(currentFilename)[:-4] + " Oddball Test-" + attendedInst + " Attended.wav\": ")
            f.write(startTimes)
            f.write("\n")
            f.close


def oddballsForbidden(currentFilename):
    "Prevents overlapping/consecutive oddballs BETWEEN STREAMS, to avoid participant confusion."
    
    setNumber = currentFilename[3]
    forbiddenOddballPeriods_Starts = np.array([])
    
    with open(File, 'r') as f:
        lines = f.readlines(-8) #Read last 8 lines in the file.
        for line in lines:
            if "Set" + setNumber in line and attendedInst + " Attended" in line: #E.g Set4 Harm attended- should be up to two lines already written.
                forbiddenOddballPeriods_StartsOneInstrument = np.array([re.findall("\d+\.\d+", line)]) #E.g, start times for vibraphone oddballs
                forbiddenOddballPeriods_Starts = np.append(forbiddenOddballPeriods_Starts, forbiddenOddballPeriods_StartsOneInstrument) #For all other instruments in the set.
        f.close
        
    forbiddenOddballPeriods_Starts = forbiddenOddballPeriods_Starts.astype(np.float) #From strings to floats.

    #Convert start times back FROM seconds:
    forbiddenOddballPeriods_Starts -= 35 #Minus 35s
    forbiddenOddballPeriods_Starts = forbiddenOddballPeriods_Starts*661500/30
    forbiddenOddballPeriods_Starts = forbiddenOddballPeriods_Starts.astype(np.int) #Should already be integers (or very close with rounding errors), this just affirms the data type.
    return forbiddenOddballPeriods_Starts

for file in os.scandir(thisParticipantStimuliPath):
    currentFilename = file.name #Easiest to keep it as a string variable
    if currentFilename[:3] == "Set": #Because of naming convention used, this will ignore trigs etc.
        signal, sr = librosa.load(file)
        signal = signal[0:661500] #Removing any excess points, so pieces are EXACTLY 30s long.
            
        #Fastest to consider grace periods here.
        
        adaptedSignalStart = 6*tenthSec + idealOB_length #Grace period at the start. Length of fade-in (0.6s) + ideal oddball.
        
        #Calculate when the signal ends, and also calculate the "adapted end"- so that an oddball
        #must finish before the fade-out (must end before final 0.6s)
        signalEnd = len(signal)
        adaptedSignalEnd = signalEnd - 6*tenthSec - idealOB_length
        
        #Only want start times at zero crossings:
        crossingsBoolean = librosa.zero_crossings(signal) #Threshold OK?
        possibleStartTimes = np.array([])
        
        for i in range(adaptedSignalStart, adaptedSignalEnd): #Only in acceptable range...
            if crossingsBoolean[i] == True: #...and only zero-crossings
                possibleStartTimes = np.append(possibleStartTimes, i)
        possibleStartTimes = np.asarray(possibleStartTimes, 'int')
        
        originalSignalCopy = np.copy(signal) #Put this here- needed to add in non-oddball demos of files at start.
        
        #Have multiple versions, all with random oddballs. This means that e.g for Set1 mix with Vibr attended
        #there will be different vibraphone oddballs to Set1 mix with Keyb attended
        attendedInst = "Vibr"
        oddballFileWriter(currentFilename, signal, attendedInst)
        
        signal, sr = librosa.load(file)
        signal = signal[0:661500] #Removing any excess points, so pieces are EXACTLY 30s long.
        
        attendedInst = "Harm"
        oddballFileWriter(currentFilename, signal, attendedInst)
        
        signal, sr = librosa.load(file)
        signal = signal[0:661500] #Removing any excess points, so pieces are EXACTLY 30s long.
        attendedInst = "Keyb"
        oddballFileWriter(currentFilename, signal, attendedInst)