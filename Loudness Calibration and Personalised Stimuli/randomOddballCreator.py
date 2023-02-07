import random
from random import choice
import librosa
import soundfile as sf
import numpy as np
import os


#RUN gainApplyer AFTER(?)

stimuliPath = "C:/Users/cjwin/OneDrive - Queen Mary, University of London/Documents/Music Interestingness in the Brain/Paradigm newest 07-02-23/Stimuli/"

def createOddball(signalCopy, start):
        sigPreOddball = signalCopy[:start]
        sigPostOddball = signalCopy[start+12000:] #Accounts for time oddball plays.
        
        firstPart = signalCopy[start:start+3000]
        firstPart = librosa.effects.pitch_shift(firstPart, sr, 8)
        
        secondPart = signalCopy[start+3000:start+6000]
        secondPart = librosa.effects.pitch_shift(firstPart, sr, -8)
        
        oddball = np.concatenate((firstPart, secondPart, firstPart, secondPart))
        
        return oddball

#Function to add random oddballs: #NEED TO ADJUST THIS SO IT'S NOT JUST CREATING ONE!
def addOddballs(signalCopy):
    numberOddballs = random.randint(1, 3) #From uniform dist.
    
    for i in range(numberOddballs): #Be careful as i can go from 0 to 2.
        
        if i == 0:
            start = random.randint(0, 649500) #Accounting for time oddball might play at end
            oddball1 = createOddball(signalCopy, start)
            
        if i == 1:            
            start2 = random.choice([j for j in range(0,649500) if j not in range(start, start+12000)])
            oddball2 = createOddball(signalCopy, start2)
            
        if i == 2:
            start3 = choice([j for j in range(0,649500) if j not in range(start, start+12000) or range(start2, start2+12000)])
            oddball3 = createOddball(signalCopy, start3)
     
        
        augmentedSignalCopy = np.concatenate((sigPreOddball, oddball, sigPostOddball))
        #Better to swap in the oddballs at their start points?
        
    return augmentedSignalCopy
        

for file in os.scandir(stimuliPath):
    if file.name[:3] == "Set": #Because of naming convention used, this will ignore trigs etc.
        signal, sr = librosa.load(file)
        signalCopy = signal
        augmentedSignalCopy = addOddballs(signalCopy)

        augmented_thing = np.concatenate((signal, augmentedSignalCopy))
        
        sf.write(str(file.name) + "with oddball.wav", augmented_thing, sr)