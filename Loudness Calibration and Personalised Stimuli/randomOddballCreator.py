import random
import librosa
import soundfile as sf
import numpy as np
import os


#RUN gainApplyer AFTER(?)

stimuliPath = "C:/Users/cjwin/OneDrive - Queen Mary, University of London/Documents/Music Interestingness in the Brain/Paradigm newest 07-02-23/PsychoPy-Auditory-Attention-and-Musical-Emotions-main/Stimuli/"

#Function to add random oddballs: #NEED TO ADJUST THIS SO IT'S NOT JUST CREATING ONE!
def addOddballs(signalCopy):
    numberOddballs = random.randint(1, 3) #From uniform dist.
    
    for i in range(numberOddballs):
        start = random.randint(0, 649500) #Accounting for time oddball might play at end
        
        sigPreOddball = signalCopy[:start]
        sigPostOddball = signalCopy[start+12000:] #Accounts for time oddball plays.
        
        firstPart = signalCopy[start:start+3000]
        firstPart = librosa.effects.pitch_shift(firstPart, sr, 8)
        
        secondPart = signalCopy[start+3000:start+6000]
        secondPart = librosa.effects.pitch_shift(firstPart, sr, -8)
        
        oddball = np.concatenate((firstPart, secondPart, firstPart, secondPart))
        
        augmentedSignalCopy = np.concatenate((sigPreOddball, oddball, sigPostOddball))
        
    return augmentedSignalCopy
        

for file in os.scandir(stimuliPath):
    if file.name[:3] == "Set": #Because of naming convention used, this will ignore trigs etc.
        signal, sr = librosa.load(file)
        signalCopy = signal
        augmentedSignalCopy = addOddballs(signalCopy)

        augmented_thing = np.concatenate((signal, augmentedSignalCopy))
        
        sf.write(str(file.name) + "with oddball.wav", augmented_thing, sr)