gainPath = "C:/Users/cjwin/OneDrive - Queen Mary, University of London/Documents/Music Interestingness in the Brain\Paradigm newest 07-02-23\PsychoPy-Auditory-Attention-and-Musical-Emotions-main/Loudness Calibration/"
gainPath = "C:/Users/cjwin/OneDrive - Queen Mary, University of London/Documents/Music Interestingness in the Brain\Paradigm newest 07-02-23\PsychoPy-Auditory-Attention-and-Musical-Emotions-main/Loudness Calibration/"

stimuliPath = "C:/Users/cjwin/OneDrive - Queen Mary, University of London/Documents/Music Interestingness in the Brain/Paradigm newest 07-02-23/PsychoPy-Auditory-Attention-and-Musical-Emotions-main/Stimuli"


#Single stimuli:
for file in os.scandir(stimuliPath):
    if file.name[:3] == "Set": #Because of naming convention used, this will ignore trigs etc.
        signal, sr = librosa.load(file)
        signalCopy = signal
        augmentedSignalCopy = addOddballs(signalCopy)

        augmented_thing = np.concatenate((signal, augmentedSignalCopy))
        
    if file.name[5:9] == "Keyb":
       signal = signal*
       
       sf.write(str(file.name) + " with gain applied.wav", signal, sr)
       #make sure writing to their folder..
       
    elif file.name[5:9] == "Vibr":
    
    sf.write(str(file.name) + " with gain applied.wav", signal, sr)
        
    elif file.name[5:9] == "Harm":
    
    sf.write(str(file.name) + " with gain applied.wav", signal, sr)


augmented_signal = signal*gain

#Multi-stream: stimuli:
    
for stimuli in stimuliPath:
    if ... name contains Keyb and .wav:
        
    elif... name contains Vibr and .wav:
    
    else:
        
        #remember to mix them..
        
        #Create new folder w/ stimuli specifically for the participant