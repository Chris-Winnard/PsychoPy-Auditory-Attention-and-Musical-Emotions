import pathlib
import glob
import os
import soundfile as sf
import librosa
import numpy as np

"""Note: to ensure pieces are exactly 30s each, we remove any excess data points."""

#Find the stimuli path:
currentFolderPath = pathlib.Path(__file__).parent.resolve()
upperFolderPath = currentFolderPath.parent.resolve()
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
           
           sf.write(str(file.name)[:-4] + " with gain applied.wav", signal, sr)
           #make sure writing to their folder..
           
        elif file.name[5:9] == "Harm":
            signal = signal*ssHarmGain
        
            sf.write(str(file.name)[:-4] + " with gain applied.wav", signal, sr)
            
        elif file.name[5:9] == "Keyb":
            signal = signal*ssKeybGain
            sf.write(str(file.name)[:-4] + " with gain applied.wav", signal, sr)

###################################################################################################
#Multi-stream: Use oddball versions!

#Read multi-stream gains:
msGainsFile = open("Multi-stream Gains.txt")
msGainsData = msGainsFile.read()
msGains = msGainsData.split(" ")
msGainsFile.close()

msVibrGain = float(msGains[1])
msKeybGain = float(msGains[3])
#msKeybGain = float(msGains[5]) #Later adapt all of this to include harmonica.

for file in os.scandir(participantPath):  
    
    for i in range(1, 8): 
        attendedInst = "Vibr attended" #MUST include " attended"
        vibrDone = False
        keybDone = False
        for attendedInst in file.name:
            print(file.name)
            if file.name[3] == str(i): #Ignores other sets/attended instruments, trigers etc
                    signal, sr = librosa.load(file)
                    signal = signal[0:661500] #Remove any excess points
                    
                    if file.name[5:9] == "Vibr":
                       vibrSignal = signal*msVibrGain
                       vibrDone = True
                        
                    elif file.name[5:9] == "Keyb":
                        keybSignal = signal*msKeybGain
                        keybDone = True
                        
                    if keybDone == True and vibrDone == True: #If both signals are ready for mixing
                        print("done")
                        oddballStimMix = np.column_stack((vibrSignal, keybSignal)) #Mixing
                        sf.write(participantPath + "/" + str(file.name)[:-21] + "oddball test mix- " 
                                 + attendedInst + " attended.wav", oddballStimMix, sr)
                    
                    
        attendedInst = "Keyb attended" #MUST include " attended"            
        if file.name[3] == str(i) and attendedInst in file.name: #Ignores other sets/attended instruments, trigers etc
         signal, sr = librosa.load(file)
         signal = signal[0:661500] #Remove any excess points
         
         if file.name[5:9] == "Vibr":
            vibrSignal = signal*msVibrGain
            vibrDone = True
             
         elif file.name[5:9] == "Keyb":
             keybSignal = signal*msKeybGain
             keybDone = True
             
         if keybDone == True and vibrDone == True: #If both signals are ready for mixing
             print("done")
             oddballStimMix = np.column_stack((vibrSignal, keybSignal)) #Mixing
             sf.write(participantPath + "/" + str(file.name)[:-21] + "oddball test mix- " 
                      + attendedInst + " attended.wav", oddballStimMix, sr)
        
        attendedInst = "Vibr attended"   
        vibrDone = False
        keybDone = False
        mixer(attendedInst, vibrDone, keybDone)
        attendedInst = "Keyb attended"        
        vibrDone = False
        keybDone = False
        mixer(attendedInst, vibrDone, keybDone)
        if i > 4:
            attendedInst = "Harm attended"       
            vibrDone = False
            keybDone = False         
            if file.name[3] == str(i) and attendedInst in file.name: #Ignores other sets/attended instruments, trigers etc
             signal, sr = librosa.load(file)
             signal = signal[0:661500] #Remove any excess points
             
             if file.name[5:9] == "Vibr":
                vibrSignal = signal*msVibrGain
                vibrDone = True
                 
             elif file.name[5:9] == "Keyb":
                 keybSignal = signal*msKeybGain
                 keybDone = True
                 
             if keybDone == True and vibrDone == True: #If both signals are ready for mixing
                 print("done")
                 oddballStimMix = np.column_stack((vibrSignal, keybSignal)) #Mixing
                 sf.write(participantPath + "/" + str(file.name)[:-21] + "oddball test mix- " 
                          + attendedInst + " attended.wav", oddballStimMix, sr)
            
#for file in os.scandir(participantPath):     
 #   if "oddball test" in file.name and "mix" not in file.name:
  #      os.remove(file) #Delete the single streams when they're no longer needed.