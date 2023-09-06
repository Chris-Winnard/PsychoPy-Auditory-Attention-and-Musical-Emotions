import pathlib
import glob
import os
import soundfile as sf
import librosa
import numpy as np
from numpy.random import default_rng
from pydub import AudioSegment
import re
import xlsxwriter
import argparse
from utils.SerialTriggerEncoder import SerialTriggerEncoder


#Find participant full path just from their ID
participantID = "P01"

#Find the stimuli path:
currentFolderPath = pathlib.Path(__file__).parent.resolve()
upperFolderPath = currentFolderPath.parent.resolve()

#Create output path:
dataPath = str(upperFolderPath) + "/Data/"


groupAssignmentFile = dataPath + "/Participant Groups.txt" #Needed for taking collecting stimuli, and saving to right place:
with open(groupAssignmentFile, 'r') as f:
    lines = f.readlines()
    for line in lines:
        if "Group A1" in line and participantID in line:
            participantPath = str(upperFolderPath) + "/Data/Group A1/" + participantID + "/"
        elif "Group A2" in line and participantID in line:
            participantPath = str(upperFolderPath) + "/Data/Group A2/" + participantID + "/"
            
        elif "Group B1" in line and participantID in line:
            participantPath = str(upperFolderPath) + "/Data/Group B1/" + participantID + "/"
        elif "Group B2" in line and participantID in line:
            participantPath = str(upperFolderPath) + "/Data/Group B2/" + participantID + "/"
    f.close

################################################################################################################################################ 
#The functions to mix stimuli, write lists, and make P2 trial triggers respectively:
    
"""Note: to ensure pieces are exactly 30s, we remove any excess data points."""

def StimMixer(participantPath):
    #Find the stimuli/demo stimuli paths:
    calibrationStimPrepPath = pathlib.Path(__file__).parent.resolve() #Where this file is located
    upperFolderPath = calibrationStimPrepPath.parent.resolve() #Path for next level up
    stimuliPath = str(upperFolderPath) + "/Stimuli"
    oddballDemosPath = str(upperFolderPath) + "/Oddball Demos"


    oddballDemosOutputPath = participantPath + "/Oddball Demos" 
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
    
    #Change back to the original path to prevent any possible later confusion
    os.chdir(calibrationStimPrepPath)
    return

def ListMaker(participantPath):
    #Navigating the files, and also specifying which set is the practice set:
        
    #Find the personalised stimuli path:
    calibrationStimPrepPath = pathlib.Path(__file__).parent.resolve() #Where this file is located = pathlib.Path(__file__).parent.resolve() #Current folder path
    upperFolderPath = calibrationStimPrepPath.parent.resolve() #Where this file is located.parent.resolve() #Path for next level up.
    dataPath = str(upperFolderPath) + "/Data"
    
    
    semimegasetFile = str(upperFolderPath) + "/Data/Semimegasets.txt"
    
    #Also, change to the participant path so that this .xlsx list is saved there:
    os.chdir(participantPath)
    
    #When we write the stimuli filenames, we will also need to include the location relative to the PsychoPy
    #paradigm scripts. This does NOT apply for trigger files, which are in a single general folder.
    participantName = os.path.split(os.getcwd())[1]
    
    if "Group A1" in participantPath:
        group = "Group A1"
        semimegaset = "Semimegaset A1"
        practiceSetPrimary = "Set04"
        practiceSetSecondary = "Set01"
    elif "Group A2" in participantPath:
        group = "Group A2"
        semimegaset = "Semimegaset A2"
        practiceSetPrimary = "Set04"
        practiceSetSecondary = "Set01"
    elif "Group B1" in participantPath:
        group = "Group B1"
        semimegaset = "Semimegaset B1"
        practiceSetPrimary = "Set01"
        practiceSetSecondary = "Set04"
    elif "Group B2" in participantPath:
        group = "Group B2"
        semimegaset = "Semimegaset B2"
        practiceSetPrimary = "Set01"
        practiceSetSecondary = "Set04"
      
    ##############################################################################################################
    ##############################################################################################################
    #PART 1: CREATING LIST OF STIMULI AND TRIGGER FILES. EXCLUDE PRACTICE TRIAL MATERIALS AND ODDBALL TEST
    #MATERIALS
    
    workbook = xlsxwriter.Workbook('stimuliList.xlsx')
    worksheet = workbook.add_worksheet()
    
    #First column- names of stimuli files, and second column- names of trigger files:
     
    worksheet.write('A1', 'stimuli_0')
    worksheet.write('B1', 'trigger')
    worksheet.write('C1', 'music_attended')
    
    #Need to get attendance data for part 3:
    with open(semimegasetFile, 'r') as f:
        lines = f.readlines()
        i=-1
        for line in lines:
            i+=1
            if semimegaset in line:
                attendedFiles = line + lines[i+1] #It will span two lines.
        f.close
        
    i = 2 #Index for row in sheet. 
    for file in os.scandir(participantPath):
        stimCell = "A" + str(i)
        trigCell = "B" + str(i)
        attdCell = "C" + str(i)
        if practiceSetPrimary not in file.name and practiceSetSecondary not in file.name:
            if ".wav" in file.name and "Oddball" not in file.name: #Only audio, and no oddball files. 
                stimPath = participantPath + str(file.name)
                worksheet.write(stimCell, stimPath)
                
                trigFilename = "trigger_" + str(file.name)
                trigFolderPlusFilename = "Trigger Files/" + trigFilename #Here we need to specify the folder
    #from main folder where the scripts are)   
                worksheet.write(trigCell, trigFolderPlusFilename)
                
                if file.name[3:10] in attendedFiles:
                    musicAttended = "Yes"
                else:
                    musicAttended = "No"
                
                worksheet.write(attdCell, musicAttended)
                i+=1
    
    # Close the xlsx file
    workbook.close()
    
    
    
    ##############################################################################################################
    ##############################################################################################################
    #PART 2: CREATING LIST OF STIMULI AND TRIGGER FILES FOR PRACTICE TRIALS. EXCLUDE MATERIALS FOR MAIN TRIALS AND
    #ODDBALL TEST MATERIALS. This is EXACTLY the same as above, just the list has a different name, and we ONLY
    #input practiceSet data to the lists. Since we're done with the above, here we can reuse i, j variables.
    
    workbook = xlsxwriter.Workbook('practiceStimuliList.xlsx')
    worksheet = workbook.add_worksheet()
    
    #First column- names of stimuli files, and second column- names of trigger files:
     
    worksheet.write('A1', 'stimuli_0')
    worksheet.write('B1', 'trigger')
    worksheet.write('C1', 'music_attended')
    i = 2 #Index for row in sheet.
    
    for file in os.scandir(participantPath):
        stimCell = "A" + str(i)
        trigCell = "B" + str(i)    
        attdCell = "C" + str(i)
        if practiceSetPrimary in file.name:
            if ".wav" in file.name and "Oddball" not in file.name: #Only audio, and no oddball files. 
                stimPath = participantPath + str(file.name)
                worksheet.write(stimCell, stimPath)
                
                trigFilename = "trigger_" + str(file.name)
                trigFolderPlusFilename = "Trigger Files/" + trigFilename
                worksheet.write(trigCell, trigFolderPlusFilename)
                if file.name[3:10] in attendedFiles:
                    musicAttended = "Yes"
                else:
                    musicAttended = "No"
    
                worksheet.write(attdCell, musicAttended)
                i+=1
    
    # Close the xlsx file
    workbook.close()
    
    
    
    ##############################################################################################################
    ##############################################################################################################
    #PART 3: CREATING LIST OF STIMULI AND TRIGGER FILES FOR ODDBALL TRIALS. EXCLUDE MATERIALS FOR PRACTICE TRIALS
    #AND SINGLE-STREAM WORK. Since we're done with the above, here we can reuse i, j variables.
    
    #First, let's read and convert the start time data. This will also be useful for part 4.
    startTimesFile = participantPath + "\Oddball Start Times.txt"
    startTimesData = open(startTimesFile, 'r')
    lines = startTimesData.readlines()
    startTimesData.close()
    
    workbook = xlsxwriter.Workbook('oddballStimuliList.xlsx')
    worksheet = workbook.add_worksheet()
    
     
    worksheet.write('A1', 'stimuli_0')
    worksheet.write('B1', 'attendedInst')
    worksheet.write('C1', 'trigger')
    worksheet.write('D1', 'attendedOddballs')
    i = 2 #Index for row in sheet.
    
    for file in os.scandir(participantPath):
        stimCell = "A" + str(i)
        attCell = "B" + str(i)
        trigCell = "C" + str(i)
        oddCell = "D" + str(i)
        if practiceSetPrimary not in file.name and practiceSetSecondary not in file.name:
            if ".wav" in file.name and "Oddball Test Mix" in file.name: #Only audio, only oddball files.
                if "Keyb Attended" in file.name:
                    attendedInst = "Keyb"
                elif "Vibr Attended" in file.name:
                    attendedInst = "Vibr"
                else:
                    attendedInst = "Harm"
                    
                stimPath = participantPath + str(file.name)
                worksheet.write(stimCell, stimPath)
                worksheet.write(attCell, str(attendedInst))
                
                trigFilename = "trigger_" + str(file.name)
                trigFolderPlusFilename = participantPath + "P2 Trigger Files/" + trigFilename
                worksheet.write(trigCell, trigFolderPlusFilename)
        
                for line in lines:
                    if file.name[0:5] in line and line.count(attendedInst) ==2: #E.g "Set03 Vibr stream for Vibr Attended"...
                        oddballStartTimes = re.findall("\d+\.\d+", line) 
                        numOddballs = len(oddballStartTimes)
                        worksheet.write(oddCell, str(numOddballs))
                i+=1
    
    workbook.close()
    
    ##############################################################################################################
    ##############################################################################################################
    #PART 4: CREATING LIST OF STIMULI AND TRIGGER FILES FOR ODDBALL PRACTICE TRIALS. EXCLUDE MATERIALS FOR ALL OTHER
    #TRIALS. Since we're done with the above, here we can reuse i/j/k variables.
    
    workbook = xlsxwriter.Workbook('practiceOddballStimuliList.xlsx')
    worksheet = workbook.add_worksheet()
    
    #First two columns: names of stimuli files and attended instruments. Also add 4th- attended oddballs:
     
    worksheet.write('A1', 'stimuli_0')
    worksheet.write('B1', 'attendedInst')
    worksheet.write('C1', 'trigger')
    worksheet.write('D1', 'attendedOddballs')
    i = 2 #Index for row in sheet.
    
    
    for file in os.scandir(participantPath):
        stimCell = "A" + str(i)
        attCell = "B" + str(i)
        trigCell = "C" + str(i)
        oddCell = "D" + str(i)
        if practiceSetPrimary in file.name or practiceSetSecondary in file.name:
            if ".wav" in file.name and "Oddball Test Mix" in file.name: #Only audio, only oddball files.
                if "Keyb Attended" in file.name:
                    attendedInst = "Keyb"
                elif "Vibr Attended" in file.name:
                    attendedInst = "Vibr"
                else:
                    attendedInst = "Harm"
                    
                stimPath = participantPath + str(file.name)
                worksheet.write(stimCell, stimPath)
                worksheet.write(attCell, str(attendedInst))
                
                trigFilename = "trigger_" + str(file.name)
                trigFolderPlusFilename = participantPath + "P2 Trigger Files/" + trigFilename
                worksheet.write(trigCell, trigFolderPlusFilename)
                
                for line in lines:
                    if file.name[0:5] in line and line.count(attendedInst) ==2:
                        oddballStartTimes = re.findall("\d+\.\d+", line)
                        numOddballs = len(oddballStartTimes)
                        worksheet.write(oddCell, str(numOddballs))
                i+=1
    
    
    workbook.close()
    
    #For parts 3 and 4 need to keep eye on how trigger filenames dealt with... not an issue if we
    #run generate_trig.py before doing ANY of this, for some generic versions of the files/mixes.
    
    os.chdir(calibrationStimPrepPath)
    
    return

def Part2TrialTrigMaker(participantPath):
    
    def getFileList(in_path):
        filepaths = []
        if os.path.isfile(in_path):
            filepaths.append(in_path)
        elif os.path.isdir(in_path):
            for filename in glob.glob(in_path + '/**/*.*', recursive=True):
                filepaths.append(filename)
        else:
            print("Path is invalid: " + in_path)
            return None
        return filepaths
        
    #################################################################################################################################################
    #Binary for trial start and end trigs, and fn to gen:
        
    set_binary_values = [0b0000, 0b0001, 0b0010, 0b0011, 0b0100, 0b0101, 0b0110, 0b0111, 0b1000, 0b1001, 0b1010, 0b1011] #Remember that Set01 corresponds to 0000, etc.
    inst_binary_values = [0b00, 0b01, 0b11]
    
    def trial_trigs(filename): #Oddball ones- add in trigs at oddball start times? Although would this mean new trig files for EACH participant?
        for i in range(1, 13):
            if i < 10:
                string_I = "0" + str(i)
            else:
                string_I = str(i)
            
            if string_I in filename:
                set_binary_thisValue = set_binary_values[i-1]
        
        instruments = ["Vibr", "Harm", "Keyb"]
        
        for j in range(0, 3):
            if instruments[j] in filename:
                inst_binary_thisValue = inst_binary_values[j]
                
            stream_binary_thisValue = 0b1 #To verify that it is the start/end of a multi-stream trial
        
        trialTrig_start = set_binary_thisValue + inst_binary_thisValue + stream_binary_thisValue + 0b0
        trialTrig_end =  set_binary_thisValue + inst_binary_thisValue + stream_binary_thisValue + 0b1
        return trialTrig_start, trialTrig_end
    
    
    def oddballTrigs(filename):
        attendedInst = filename[-13:-9]
        
        thisMixVibr = filename[0:6] + "Vibr Oddball Test-" + filename[-13:] #E.g, Set01-Oddball Test Mix - Harm Attended.wav -> Set01-Vibr Oddball Test-Harm Attended.wav
        thisMixHarm = filename[0:6] + "Harm Oddball Test-" + filename[-13:] #E.g, Set01-Oddball Test Mix - Harm Attended.wav -> Set01-Harm Oddball Test-Harm Attended.wav
        thisMixKeyb = filename[0:6] + "Keyb Oddball Test-" + filename[-13:] 
        
        linesReadFrom = 0        
        for line in lines:
            if thisMixVibr in line:
                vibrOddballStartTimes = re.findall("\d+\.\d+", line) 
                linesReadFrom += 1
            elif thisMixHarm in line:
                harmOddballStartTimes = re.findall("\d+\.\d+", line)
                linesReadFrom += 1
            elif thisMixKeyb in line:
                keybOddballStartTimes = re.findall("\d+\.\d+", line)
                linesReadFrom += 1
            
            if linesReadFrom == 3:
                break
        #Trigs- 00 for vibr, 01 for harm, 11 for keyb. First two indicate inst to be attended, last two indicate oddball type. e.g, 0111 for keyb oddball
        #when harm attended
        
        if attendedInst == "Vibr":
            vibrOddballTrig = 0b0000
            harmOddballTrig = 0b0001
            keybOddballTrig = 0b0011
            
        elif attendedInst == "Harm":
            vibrOddballTrig = 0b0100
            harmOddballTrig = 0b0101
            keybOddballTrig = 0b0111
            
        elif attendedInst == "Keyb":
            vibrOddballTrig = 0b1100
            harmOddballTrig = 0b1101
            keybOddballTrig = 0b1111
            
        vibrOBtrigs = [vibrOddballTrig]*len(vibrOddballStartTimes)
        
        harmOBtrigs = [harmOddballTrig]*len(harmOddballStartTimes)
        
        keybOBtrigs = [keybOddballTrig]*len(keybOddballStartTimes)
        
        allOBtrigsAndTimes = [vibrOBtrigs + harmOBtrigs + keybOBtrigs, vibrOddballStartTimes + harmOddballStartTimes + keybOddballStartTimes]
        
        return allOBtrigsAndTimes
        
    ########################################################################################################################################################
    """Use the above to generate trigs:"""
      
    out_folder = participantPath + "/P2 Trigger Files"
    os.path.abspath(out_folder) #E.g "P04/P2 Trigger Files"
    sr = 22050 #sampling rate
    ch = 1 #channels
    clkSerial = 10.0 #Clock rate of trigger. Default value is 10.0 Hz.")
    
    #First, let's read and convert the start time data. This will also be useful for part 4.
    startTimesFile = participantPath + "\Oddball Start Times.txt"
    startTimesData = open(startTimesFile, 'r')
    lines = startTimesData.readlines()
    startTimesData.close()
    
    if not os.path.exists(out_folder):
        os.makedirs(out_folder)
      
    file_list = getFileList(participantPath)
    file_list = [x for x in file_list if 'Oddball Test Mix' in x]
    triggerEncoder = SerialTriggerEncoder(sr, clkSerial)
    #  print('file_list', file_list)
    for i in range(len(file_list)):    
        path, ext = os.path.splitext(file_list[i])
        if ext != ".wav":
            continue
        else:
            f = sf.SoundFile(file_list[i])
            data, sr = sf.read(file_list[i])
            file_len = f.frames/f.samplerate
            name = os.path.basename(path)
            trig_filename = os.path.join(out_folder, 'trigger_' + name + '.wav')     
            triggerEncoder.resetTrigger()            
              
            [TRIAL_START_CODE, TRIAL_END_CODE] = trial_trigs(name)
            triggerEncoder.encode(TRIAL_START_CODE, 0.0)
              
            oddballTrigsAndTimes = oddballTrigs(name)
            for x in range(len(oddballTrigsAndTimes[0])): #Number of columns, i.e total triggers
                triggerEncoder.encode(oddballTrigsAndTimes[0][x], float(oddballTrigsAndTimes[1][x]))
            
            triggerEncoder.encode(TRIAL_END_CODE, file_len)
            triggerEncoder.generateTrigger(trig_filename, file_len+1.0) #shorter?
            
    return

#################################################################################################################################################
StimMixer(participantPath) #Create stimuli with gains applied: both single-stream, and
#mixes of the oddball stimuli.

#Additional note: trigger files (EXCEPT FOR P2 TRIALS) have already been created. By the nature of gainApplier and randomOddballCreator,
#all pieces have the exact same lengths enforced, so can just use one start/end trigger pair for the Set1-Harm files
#(i.e not different versions of the triggers for different participants), etc.


ListMaker(participantPath) #Create lists of the stimuli and the trigger files that can be used in the scripts
#with minimal extra work.

Part2TrialTrigMaker(participantPath)  #Note that for P2 trigger files: for oddball tests the start trigger is at the v start of the audio file.