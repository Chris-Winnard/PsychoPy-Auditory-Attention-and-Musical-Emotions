import os
import soundfile as sf
import librosa



stimuliPath = "C:/Users/cjwin/OneDrive - Queen Mary, University of London/Documents/Music Interestingness in the Brain/Paradigm newest 07-02-23/Stimuli"

########################################################################################################################################################
#Single stream:
    
#Read single-stream gains:
ssGainsFile = open("Single-stream Gains for Chris.txt") #need to edit so it's gains for that person..
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
        signalCopy = signal
        
        if file.name[5:9] == "Vibr":
           signal = signal*ssVibrGain
           
           sf.write(str(file.name) + " with gain applied.wav", signal, sr)
           #make sure writing to their folder..
           
        elif file.name[5:9] == "Harm":
            signal = signal*ssHarmGain
        
            sf.write(str(file.name) + " with gain applied.wav", signal, sr)
            
        elif file.name[5:9] == "Keyb":
            signal = signal*ssKeybGain
            sf.write(str(file.name) + " with gain applied.wav", signal, sr)

###################################################################################################
#Multi-stream:

#Read multi-stream gains:
msGainsFile = open("Multi-stream Gains for Chris.txt") #need to edit so it's gains for that person..
msGainsData = msGainsFile.read()
msGains = msGainsData.split(" ")
msGainsFile.close()

msVibrGain = float(msGains[1])
msKeybGain = float(msGains[3])
#msKeybGain = float(msGains[5]) #Later adapt all of this to include harmonica.

for file in os.scandir(stimuliPath):
    for i in range(1, 7): #Because of naming convention used, this will ignore trigs etc.
        if file.name[3] == str(i):
            signal, sr = librosa.load(file)
            signalCopy = signal      
        
            if file.name[5:9] == "Vibr":
               VibrSignal = signal*msVibrGain
                
            elif file.name[5:9] == "Keyb":
                KeybSignal = signal*msKeybGain

        # Use zip to get item pairs
            merged = zip(VibrSignal, KeybSignal) #right way round?
            
            # Print out the merged list
            print(merged)
            sf.write("Weighted Mix.wav", list(merged), sr)
            i = 0
            j = 0
        
        #remember to mix them.. do I literally just concatenate the two lists/arrays (one 
        #left, one right)?
        
        #Create new folder w/ stimuli specifically for the participant