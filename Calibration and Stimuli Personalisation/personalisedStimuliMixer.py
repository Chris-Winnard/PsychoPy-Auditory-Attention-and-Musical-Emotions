import pathlib
import glob
import os
import soundfile as sf
import librosa
import numpy as np
from pydub import AudioSegment

"""Note: to ensure pieces are exactly 30s each, we remove any excess data points."""

#Find the stimuli path:
calibrationStimPrepPath = pathlib.Path(__file__).parent.resolve() #Where this file is located
upperFolderPath = calibrationStimPrepPath.parent.resolve() #Path for next level up
stimuliPath = str(upperFolderPath) + "/Stimuli"

#Find correct path for the gain files, and for outputs:
dataPath = str(upperFolderPath) + "/Data"
participantPath = max(glob.glob(os.path.join(dataPath, '*/')), key=os.path.getmtime) #Last updated
#subfolder in Data folder. Because we run this and randomOddballCreator IMMEDIATELY after participant's
#folder is created, this will be the output path for them.

#Change to the participant path, to access gain files and output the adjusted stimuli:
os.chdir(participantPath)

########################################################################################################################################################
#Single stream:
    
#Read single-stream gains:
ssGainsFile = open("Single-stream Gains.txt")
ssGainsData = ssGainsFile.read()
ssGains = ssGainsData.split(" ")
ssGainsFile.close()

ssVibrGain = float(ssGains[1])
ssHarmGain = float(ssGains[3])
ssKeybGain = float(ssGains[5])


#Single stimuli:
for file in os.scandir(stimuliPath):
    if file.name[:3] == "Set": #Because of naming convention used, this will ignore trigs etc.
        signal, sr = librosa.load(file)
        signal = signal[0:661500]
        signalCopy = signal
        
        if file.name[5:9] == "Vibr":
           signal = signal*ssVibrGain
           
           sf.write(str(file.name)[:-4] + " with Gain Applied.wav", signal, sr)
           #make sure writing to their folder..
           
        elif file.name[5:9] == "Harm":
            signal = signal*ssHarmGain
        
            sf.write(str(file.name)[:-4] + " with Gain Applied.wav", signal, sr)
            
        elif file.name[5:9] == "Keyb":
            signal = signal*ssKeybGain
            sf.write(str(file.name)[:-4] + " with Gain Applied.wav", signal, sr)

###################################################################################################
#Multi-stream: Use oddball versions!

#Read multi-stream gains:
msGainsFile = open("Multi-stream Gains.txt")
msGainsData = msGainsFile.read()
msGains = msGainsData.split(" ")
msGainsFile.close()

msVibrGain = float(msGains[1])
msHarmGain = float(msGains[3])
msKeybGain = float(msGains[5])

def mixer(attendedInst):
    VibrDone = False
    HarmDone = False #Hippocrates approves. 
    KeybDone = False
    for file in os.scandir(participantPath):  
        for i in range(1, 8):
            if file.name[3] == str(i) and attendedInst in file.name: #Only oddball versions. This will also ignore triggers etc.
                signal = AudioSegment.from_wav(file)
                signal = signal[0:1433250] #Remove any excess points - should be 1 min 5s exactly.
                
                if file.name[5:9] == "Vibr":
                   VibrSignal = signal.pan(-1).apply_gain(msVibrGain) #Pan and apply gain.
                 #  VibrSignal = signal*msVibrGain
                   VibrDone = True
                   os.remove(file) #Delete single streams when they're no longer needed.
                   
                elif file.name[5:9] == "Harm":
                   HarmSignal = signal.pan(0).apply_gain(msHarmGain)
                   HarmDone = True
                   os.remove(file) #Delete single streams when they're no longer needed.
                    
                elif file.name[5:9] == "Keyb":
                    KeybSignal = signal.pan(1).apply_gain(msKeybGain)
                    KeybDone = True
                    os.remove(file) #Delete single streams when they're no longer needed.
                            
                if KeybDone == True and HarmDone == True and VibrDone == True:
                    outputPathPlusName = participantPath + "/Set" + str(i) + "-Oddball Test Mix - " + attendedInst + ".wav"
                    oddballStimMix = VibrSignal.overlay(HarmSignal).overlay(KeybSignal) #All 3 overlaid together (panned in above steps)
                    oddballStimMix.export(outputPathPlusName, format="wav")

attendedInst = "Vibr Attended"
mixer(attendedInst)

attendedInst = "Harm Attended"
mixer(attendedInst)

attendedInst = "Keyb Attended"
mixer(attendedInst)


#Change back to the original path. This prevents confusion when later scripts are run.
os.chdir(calibrationStimPrepPath)