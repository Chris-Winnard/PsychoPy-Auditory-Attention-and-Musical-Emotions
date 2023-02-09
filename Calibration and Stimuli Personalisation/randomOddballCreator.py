import pathlib
import random
from random import choice
import librosa
import soundfile as sf
import numpy as np
import os
import glob

#Find the stimuli path:
currentFolderPath = pathlib.Path(__file__).parent.resolve()
upperFolderPath = currentFolderPath.parent.resolve()
stimuliPath = str(upperFolderPath) + "/Stimuli"

#Find correct output path:
dataPath = str(upperFolderPath) + "/Data"
participantPath = max(glob.glob(os.path.join(dataPath, '*/')), key=os.path.getmtime) #Last updated
#subfolder in Data folder. Because we run randomOddballCreator IMMEDIATELY after participant's
#folder is created, this will be the output path for them.

"""Timings: one data point = 4.5e-05 (the same for all pieces to the 20th decimal). So, we don't need to
normalise w.r.t piece length. Use 2205 = 0.1s. To ensure pieces are exactly 30s each, we remove any excess data
points."""

tenthSec = 2205
fifthSec = 2*tenthSec
oddballLength = 3*fifthSec

#Function to create an oddball for given signal, starting at a given point in that signal:
def createOddball(signalCopy, start):        
        firstPart = signalCopy[start:start+tenthSec]
        firstPart = librosa.effects.pitch_shift(firstPart, sr, 1, bins_per_octave=12)
        
        secondPart = signalCopy[start+tenthSec:start+fifthSec]
        secondPart = librosa.effects.pitch_shift(secondPart, sr, -1, bins_per_octave=12)
        
        thirdPart = signalCopy[start+fifthSec:start+3*tenthSec]
        thirdPart = librosa.effects.pitch_shift(thirdPart, sr, -1, bins_per_octave=12)
        
        fourthPart = signalCopy[start+3*tenthSec:start+2*fifthSec]
        fourthPart = librosa.effects.pitch_shift(fourthPart, sr, -1, bins_per_octave=12)
        
        fifthPart = signalCopy[start+2*fifthSec:start+5*tenthSec]
        fifthPart = librosa.effects.pitch_shift(fifthPart, sr, -1, bins_per_octave=12)
        
        sixthPart = signalCopy[start+5*tenthSec:start+3*fifthSec]
        sixthPart = librosa.effects.pitch_shift(sixthPart, sr, -1, bins_per_octave=12)
        
        oddball = np.concatenate((firstPart, secondPart, thirdPart, fourthPart, fifthPart, sixthPart))      
        
        return oddball

#Function to add random oddballs:
def addOddballs(signalCopy):
    numberOddballs = random.randint(1, 3) #From uniform dist.
    
    for i in range(numberOddballs):
        
    #NOTE: We use a grace period of +/- one oddball length either side. So you can't have two simultaneously, or even one straight after
    #another.
    
        if i == 0:
            start = random.randint(0, adaptedSignalEnd) #Accounting for time oddball might play at end
            oddball1 = createOddball(signalCopy, start)
            signalCopy[start:start+oddballLength] = oddball1 #Insert the oddball.

        if i == 1:            
            start2 = random.choice([j for j in range(0, adaptedSignalEnd) if j not in range(start-oddballLength, start+2*oddballLength)])
            oddball2 = createOddball(signalCopy, start2)
            signalCopy[start2:start2+oddballLength] = oddball2
            
        if i == 2:
            start3 = choice([j for j in range(0, adaptedSignalEnd) if j not in range(start-oddballLength, start+2*oddballLength) or range(start2-oddballLength, start2+2*oddballLength)])
            oddball3 = createOddball(signalCopy, start3)
            signalCopy[start3:start3+oddballLength] = oddball3
    
    return signalCopy

def oddballFileWriter(signal, attendedInst):
        pause = np.zeros(110250)
        augmentedSignalCopy = addOddballs(signal)

        oddballStimulusFull = np.concatenate((signal, pause, augmentedSignalCopy))
        sf.write(participantPath + "/" + str(file.name)[:-4] + " oddball test-" + attendedInst + " attended.wav", oddballStimulusFull, sr)

for file in os.scandir(stimuliPath):
    if file.name[:3] == "Set": #Because of naming convention used, this will ignore trigs etc.
        signal, sr = librosa.load(file)
        signal = signal[0:661500] #Removing any excess points, so pieces are EXACTLY 30s long.
        
        #Calculate when the signal ends, and also calculate the "adapted end"- so that an oddball
        #doesn't start at the last half-second or anything like that:
        signalEnd = len(signal)
        adaptedSignalEnd = signalEnd - oddballLength
        
        #Have multiple versions, all with random oddballs. This means that e.g for Set1 mix with Vibr attended
        #there will be different vibraphone oddballs to Set1 mix with Keyb attended
        attendedInst = "Vibr"
        oddballFileWriter(signal, attendedInst)
        attendedInst = "Keyb"
        oddballFileWriter(signal, attendedInst)
        
        if int(file.name[3]) > 4: #For sets with harmonica pieces.
            attendedInst = "Harm"
            oddballFileWriter(signal, attendedInst)