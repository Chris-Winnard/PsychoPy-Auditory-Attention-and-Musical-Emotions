import os
import argparse
import glob
import soundfile as sf
from utils.SerialTriggerEncoder import SerialTriggerEncoder
import re
import pathlib

#Find the personalised stimuli path:
currentFolderPath = pathlib.Path(__file__).parent.resolve() #Current folder path
upperFolderPath = currentFolderPath.parent.resolve() #Path for next level up.
dataPath = str(upperFolderPath) + "/Data"

sub_paths = list() # Collect all files in sub directories
for root, dirs, files in os.walk(dataPath):
    sub_paths += [os.path.join(root,i) for i in files]
    
participantLastStimFile = max(sub_paths,key=os.path.getmtime) #Participant stimuli file that was just created- the most recently updated file
#in "Data" folder
participantPath = pathlib.Path(participantLastStimFile).parent.resolve() #Subfolder where that file is located, i.e participant's folder
participantPath = str(participantPath)

##################################################################################################################################################
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
clkSerial = 8.0 #Clock rate of trigger. Default value is 8.0 Hz.")

#First, let's read and convert the start time data. This will also be useful for part 4.
startTimesFile = participantPath + "\Oddball Start Times.txt"
startTimesData = open(startTimesFile, 'r')
lines = startTimesData.readlines()
startTimesData.close()

if not os.path.exists(out_folder):
    os.makedirs(out_folder)
  
file_list = getFileList(participantPath)
file_list = [x for x in file_list if 'Oddball Test Mix' in x]
print(file_list)
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