import pathlib
import random
from random import choice
import librosa
import soundfile as sf
import numpy as np
import os
import re
import glob
from itertools import chain

#Find the stimuli path:
currentFolderPath = pathlib.Path(__file__).parent.resolve()
upperFolderPath = currentFolderPath.parent.resolve()
stimuliPath = str(upperFolderPath) + "/Stimuli"

#Find correct output path:
dataPath = str(upperFolderPath) + "/Data/"
participantPath = max(glob.glob(os.path.join(dataPath, '*/')), key=os.path.getmtime) #Last updated
#subfolder in Data folder. Because we run randomOddballCreator IMMEDIATELY after participant's
#folder is created, this will be the output path for them.

File = (participantPath + "\Oddball Start Times.txt")
with open(File, 'a') as f: #Create the file now to prevent any confusion later, because oddballsForbidden needs to read from it.
    f.close

"""Timings: one data point = 4.5e-05 (the same for all pieces to the 20th decimal). So, we don't need to
normalise w.r.t piece length. Use 2205 = 0.1s. To ensure pieces are exactly 30s each, we remove any excess data
points."""

tenthSec = 2205
oddballSegmentLength = 1808
oddballLength = 6*oddballSegmentLength

#Function to create an oddball for given signal, starting at a given point in that signal:
def createOddball(signalCopy, start):    
    
    firstPart = signalCopy[start:start+oddballSegmentLength]
    firstPart = librosa.effects.pitch_shift(firstPart, sr, 0.95, bins_per_octave=12)
    
    secondPart = signalCopy[start+oddballSegmentLength:start+2*oddballSegmentLength]
    secondPart = librosa.effects.pitch_shift(secondPart, sr, -0.95, bins_per_octave=12)
    
    thirdPart = signalCopy[start+2*oddballSegmentLength:start+3*oddballSegmentLength]
    thirdPart = librosa.effects.pitch_shift(thirdPart, sr, 0.95, bins_per_octave=12)
    
    fourthPart = signalCopy[start+3*oddballSegmentLength:start+4*oddballSegmentLength]
    fourthPart = librosa.effects.pitch_shift(fourthPart, sr, -0.95, bins_per_octave=12)
    
    fifthPart = signalCopy[start+4*oddballSegmentLength:start+5*oddballSegmentLength]
    fifthPart = librosa.effects.pitch_shift(fifthPart, sr, 0.95, bins_per_octave=12)
    
    sixthPart = signalCopy[start+5*oddballSegmentLength:start+6*oddballSegmentLength]
    sixthPart = librosa.effects.pitch_shift(sixthPart, sr, -0.95, bins_per_octave=12)
    
    oddball = np.concatenate((firstPart, secondPart, thirdPart, fourthPart, fifthPart, sixthPart))    
    
    return oddball

#Function to add random oddballs:
def addOddballs(signalCopy, forbiddenOddballPeriods_Starts):
    numberOddballs = random.randint(1, 3) #From uniform dist.
    startTimes = np.zeros(numberOddballs)
    
    excludedStartTimes = []
    
    #Create chain for excluded ranges. NOTE: can't save a chain to use a second time. Hence, have to keep "re-chaining" x2 etc.
    if len(forbiddenOddballPeriods_Starts) >= 1:
        x1 = range(forbiddenOddballPeriods_Starts[0] - 2*oddballLength, forbiddenOddballPeriods_Starts[0] + 2*oddballLength)
        
        if len(forbiddenOddballPeriods_Starts) >= 2:
            x2 = range(forbiddenOddballPeriods_Starts[1] - 2*oddballLength, forbiddenOddballPeriods_Starts[1] + 2*oddballLength)
            excludedStartTimes = chain(x1, x2)
            
            if len(forbiddenOddballPeriods_Starts) >= 3:
                x3 = range(forbiddenOddballPeriods_Starts[2] - 2*oddballLength, forbiddenOddballPeriods_Starts[2] + 2*oddballLength)
                excludedStartTimes = chain(x1, x2, x3)
                
                if len(forbiddenOddballPeriods_Starts) >= 4:
                    x4 = range(forbiddenOddballPeriods_Starts[3] - 2*oddballLength, forbiddenOddballPeriods_Starts[3] + 2*oddballLength)
                    excludedStartTimes = chain(x1, x2, x3, x4)
                    
                    if len(forbiddenOddballPeriods_Starts) >= 5:
                        x5 = range(forbiddenOddballPeriods_Starts[4] - 2*oddballLength, forbiddenOddballPeriods_Starts[4] + 2*oddballLength)
                        excludedStartTimes = chain(x1, x2, x3, x4, x5)
                        
                        if len(forbiddenOddballPeriods_Starts) == 6:
                            x6 = range(forbiddenOddballPeriods_Starts[5] - 2*oddballLength, forbiddenOddballPeriods_Starts[5] + 2*oddballLength)
                            excludedStartTimes = chain(x1, x2, x3, x4, x5, x6)

    for i in range(numberOddballs):
        
    #NOTE: We use a grace period at start, and accounting for time oddball might play at end. Also a grace period of +/- one oddball length either side - so you can't have two
    #simultaneously, or even one straight after another. forbiddenOddballPeriods_Starts added in to implement this between streams.

        if i == 0:
            start1 = choice([j for j in possibleStartTimes if j not in excludedStartTimes])
            startTimes[i] = start1
            oddball1 = createOddball(signalCopy, start1)
            signalCopy[start1:start1+oddballLength] = oddball1 #Insert the oddball.

        if i == 1:            
            start2 = choice([j for j in possibleStartTimes if j not in excludedStartTimes])
            startTimes[i] = start2
            oddball2 = createOddball(signalCopy, start2)
            signalCopy[start2:start2+oddballLength] = oddball2
            
        if i == 2:
            start3 = choice([j for j in possibleStartTimes if j not in excludedStartTimes])
            startTimes[i] = start3
            oddball3 = createOddball(signalCopy, start3)
            signalCopy[start3:start3+oddballLength] = oddball3
            
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

for file in os.scandir(stimuliPath):
    currentFilename = file.name #Easiest to keep it as a string variable
    if currentFilename[:3] == "Set": #Because of naming convention used, this will ignore trigs etc.
        signal, sr = librosa.load(file)
        signal = signal[0:661500] #Removing any excess points, so pieces are EXACTLY 30s long.
            
        #Fastest to consider grace periods here.
        
        adaptedSignalStart = oddballLength #Grace period at the start, length of one oddball. No oddballs in this grace period.
        
        #Calculate when the signal ends, and also calculate the "adapted end"- so that an oddball
        #doesn't start at the last half-second or anything like that:
        signalEnd = len(signal)
        adaptedSignalEnd = signalEnd - oddballLength
        
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
        attendedInst = "Harm"
        oddballFileWriter(currentFilename, signal, attendedInst)
        attendedInst = "Keyb"
        oddballFileWriter(currentFilename, signal, attendedInst)