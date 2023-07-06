import pathlib
import glob
import os
import soundfile as sf
import librosa
import numpy as np
from pydub import AudioSegment


"""Note: to ensure pieces are exactly 30s, we remove any excess data points."""

#Find the stimuli/demo stimuli paths:
calibrationStimPrepPath = pathlib.Path(__file__).parent.resolve() #Where this file is located
upperFolderPath = calibrationStimPrepPath.parent.resolve() #Path for next level up
stimuliPath = str(upperFolderPath) + "/Stimuli"
oddballDemosPath = str(upperFolderPath) + "/Oddball Demos"

#Find correct path for the gain files, and for outputs:
dataPath = str(upperFolderPath) + "/Data"

sub_paths = list() # Collect all files in sub directories
for root, dirs, files in os.walk(dataPath):
    sub_paths += [os.path.join(root,i) for i in files]

participantCalibrationFile = max(sub_paths,key=os.path.getmtime) #Participant single-stream calibration file- the most recently updated file
#in "Data" folder
participantPath = pathlib.Path(participantCalibrationFile).parent.resolve() #Subfolder where that file is located, i.e participant's folder
participantPath = str(participantPath)

oddballDemosOutputPath = str(participantPath) + "/Oddball Demos" 
os.mkdir(oddballDemosOutputPath)

#Change to the participant path, to access gain files and output the adjusted stimuli:
os.chdir(participantPath)

spatialisationSettingsFile = open("Spatialisation Settings.txt")
spatialisationSettingsData = spatialisationSettingsFile.read()
spatialisationSettings = spatialisationSettingsData.split(" ")
spatialisationSettingsFile.close()

vibrPan = float(spatialisationSettings[1])
harmPan = float(spatialisationSettings[3])
keybPan = float(spatialisationSettings[5])

##############################################################################################################
##############################################################################################################
#Find which stimuli are assigned to this participant:

if "Group A1" in participantPath or "Group A2" in participantPath:
    thisParticipantStimuliPath = stimuliPath + "\Megaset A"
    demoSet = "Set04"
elif "Group B1" in participantPath or "Group B2" in participantPath:
    thisParticipantStimuliPath = stimuliPath + "\Megaset B"
    demoSet = "Set01"
    
########################################################################################################################################################
#Single stream:
    
ssGainsFile = open("Single-stream Gains.txt")
ssGainsData = ssGainsFile.read()
ssGains = ssGainsData.split(" ")
ssGainsFile.close()

ssVibrGainLinear = float(ssGains[1])
ssVibrGain = 20*np.log10(ssVibrGainLinear)

ssHarmGainLinear = float(ssGains[3])
ssHarmGain = 20*np.log10(ssHarmGainLinear)

ssKeybGainLinear = float(ssGains[5])
ssKeybGain = 20*np.log10(ssKeybGainLinear)


#Single stimuli:
for file in os.scandir(thisParticipantStimuliPath):
    if file.name[:3] == "Set": #Because of naming convention used, this will ignore trigs etc.
        signal = AudioSegment.from_wav(file)
        signal = signal[0:661500]
        signalCopy = signal
        
        if file.name[6:10] == "Vibr":
           signal = signal.apply_gain(ssVibrGain)
           signal = signal.pan(vibrPan)
           outputPathPlusName = participantPath + "/" + str(file.name)[:-4] + " with Gain Applied.wav"
           signal = signal.set_frame_rate(22050) #Downsample, for consistency with multistream files and everything else
           signal.export(outputPathPlusName, format="wav")
           
        elif file.name[6:10] == "Harm":
            signal = signal.apply_gain(ssHarmGain)
            signal = signal.pan(harmPan)
            outputPathPlusName = participantPath + "/" + str(file.name)[:-4] + " with Gain Applied.wav"
            signal = signal.set_frame_rate(22050)
            signal.export(outputPathPlusName, format="wav")
            
        elif file.name[6:10] == "Keyb":
            signal = signal.apply_gain(ssKeybGain)
            signal = signal.pan(keybPan)
            outputPathPlusName = participantPath + "/" + str(file.name)[:-4] + " with Gain Applied.wav"
            signal = signal.set_frame_rate(22050)
            signal.export(outputPathPlusName, format="wav")

###################################################################################################
#Multi-stream: Use oddball versions!

msGainsFile = open("Multi-stream Gains.txt")
msGainsData = msGainsFile.read()
msGains = msGainsData.split(" ")
msGainsFile.close()

msVibrGainLinear = float(msGains[1])
msVibrGain = 20*np.log10(msVibrGainLinear)
msHarmGainLinear = float(msGains[3])
msHarmGain = 20*np.log10(msHarmGainLinear)
msKeybGainLinear = float(msGains[5])
msKeybGain = 20*np.log10(msKeybGainLinear)

def mixer(attendedInst): 
    VibrDone = False
    HarmDone = False #Hippocrates approves. 
    KeybDone = False
    for file in os.scandir(participantPath):  
        for i in range(1, 13):
            
            if i < 10:
                string_I = "0" + str(i)
            else:
                string_I = str(i)
            
            if "Set" + string_I in file.name and attendedInst in file.name: #Only oddball versions. This will also ignore triggers etc.
                signal = AudioSegment.from_wav(file)
                signal = signal[0:1433250] #Remove any excess points - should be 1 min 5s exactly.
                if file.name[6:10] == "Vibr":
                   VibrSignal = signal.pan(-1).apply_gain(msVibrGain) #Pan and apply gain.
                   VibrDone = True
                   os.remove(file) #Delete single streams after use
                   
                elif file.name[6:10] == "Harm":
                   HarmSignal = signal.pan(harmPan).apply_gain(msHarmGain)
                   HarmDone = True
                   os.remove(file)
                    
                elif file.name[6:10] == "Keyb":
                    KeybSignal = signal.pan(1).apply_gain(msKeybGain)
                    KeybDone = True
                    os.remove(file)
                            
                if KeybDone == True and HarmDone == True and VibrDone == True:
                    outputPathPlusName = participantPath + "/Set" + string_I + "-Oddball Test Mix - " + attendedInst + ".wav"
                    oddballStimMix = VibrSignal.overlay(HarmSignal).overlay(KeybSignal) #All 3 overlaid together (panned in above steps)
                    oddballStimMix.export(outputPathPlusName, format="wav")

#Oddball demos- these will use the MS weightings and even come from the same directions, but only one instrument will be heard at a time:

def demoMixer():
    VibrDone = False
    HarmDone = False
    KeybDone = False
        
    for file in os.scandir(oddballDemosPath): 
        if demoSet in file.name:
            signal = AudioSegment.from_wav(file)
            
            if "Vibr" in file.name:
               oddballDemo = signal.pan(-1).apply_gain(msVibrGain) #Pan and apply gain. 
               attendedInst = "Vibr Attended"
               VibrDone = True
               
            elif "Harm" in file.name:
               oddballDemo = signal.pan(harmPan).apply_gain(msHarmGain)
               attendedInst = "Harm Attended"
               HarmDone = True
                
            elif "Keyb" in file.name:
                oddballDemo = signal.pan(1).apply_gain(msKeybGain)
                attendedInst = "Keyb Attended"
                KeybDone = True
                        
            if KeybDone == True or HarmDone == True or VibrDone == True: #Only want ONE.
                outputPathPlusName = oddballDemosOutputPath + "/" + demoSet + "-Oddball Demo for " + attendedInst[:5] + ".wav"
                oddballDemo.export(outputPathPlusName, format="wav")

#Run both functions, for all attended conditions:
demoMixer()
attendedInst = "Vibr Attended"
mixer(attendedInst)

attendedInst = "Harm Attended"
mixer(attendedInst)

attendedInst = "Keyb Attended"
mixer(attendedInst)

#Change back to the original path. This prevents confusion when later scripts are run.
os.chdir(calibrationStimPrepPath)