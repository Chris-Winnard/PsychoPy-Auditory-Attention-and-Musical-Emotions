import os
import argparse
import glob
import soundfile as sf
from utils.SerialTriggerEncoder import SerialTriggerEncoder


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

def create_folder(folder):
    full_path = os.path.abspath(folder)
    os.makedirs(full_path, exist_ok=True)
    
    
    
    
#################################################################################################################################################    
#Set up binary for part start and end trigs, and fn to generate:    https://stackoverflow.com/questions/16926130/convert-to-binary-and-keep-leading-zeros
P1 = 0b00
P2 = 0b01
P3 = 0b11

part_subTrigs = [P1, P2, P3]

def single_part_trig(part, triggerEnc, location, partTrigNumber):
    part = 'P' + str(part+1)
    
    #
    trig_filename = os.path.join(newPath, part + '_' + location + '_trigger.wav')
    trig_metafilename = os.path.join(newPath, part + '_' + location + '_trigger.txt')            
    triggerEncoder.resetTrigger()      
        
    triggerEncoder.encode(partTrigNumber, 0.0)
    event_metafile = open(trig_metafilename, 'w')
    event_metafile.write("{}\t{}\n".format(partTrigNumber, 0)) #position in millisecond
    triggerEncoder.generateTrigger(trig_filename, 1.0)
    event_metafile.close()

def part_trigs(part, triggerEnc):
    
    partTrigNumber_start = part_subTrigs[part] + 0b0
    
    partTrigNumber_end = part_subTrigs[part] + 0b1
    
    single_part_trig(part, triggerEnc, "start", partTrigNumber_start)
    
    single_part_trig(part, triggerEnc, "end", partTrigNumber_end)

    
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
            
    stream_binary_thisValue = 0b0  #To verify that it is the start/end of a single-stream trial
    
    trialTrig_start = set_binary_thisValue + inst_binary_thisValue + stream_binary_thisValue + 0b0
    trialTrig_end =  set_binary_thisValue + inst_binary_thisValue + stream_binary_thisValue + 0b1
    return trialTrig_start, trialTrig_end

########################################################################################################################################################
"""Use the above to generate trigs:"""
    
#Trial trigs:    
if __name__ == '__main__':
    parser = argparse.ArgumentParser(prog='generate_trig')
    parser.add_argument("--in_folder", type=str, required=True, help="input folder containing target and non-target sounds.")
    parser.add_argument("--out_folder", type=str, required=True, help="output folder")
    parser.add_argument("--sr", type=int, default=22050, help="sampling rate. Default value is 22050.")
    parser.add_argument("--channels", type=int, default=1, help="number of output channels. Default value is 1.")
    parser.add_argument("--triggerClk", type=float, default=10.0, help="Clock rate of trigger. Default value is 10.0 Hz.")
    args = parser.parse_args()

    in_folder = os.path.abspath(args.in_folder)
    out_folder = os.path.abspath(args.out_folder)
    sr = args.sr
    ch = args.channels
    clkSerial = args.triggerClk
    if not os.path.exists(out_folder):
        os.makedirs(out_folder)
    
    file_list = getFileList(in_folder)
    file_list = [x for x in file_list if 'with Gain Applied' in x] #ONLY single-stream stuff- triggers for oddball test mixes dealt with on a per-
    #participant basis, as they must correspond to the individual oddball files
    
    triggerEncoder = SerialTriggerEncoder(sr, clkSerial)
    print('file_list', file_list)
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
            trig_metafilename = os.path.join(out_folder,'trigger_' + name + '.txt')            
            triggerEncoder.resetTrigger()            
            
            [TRIAL_START_CODE, TRIAL_END_CODE] = trial_trigs(name)
            triggerEncoder.encode(TRIAL_START_CODE, 0.0)
            event_metafile = open(trig_metafilename, 'w')
            event_metafile.write("{}\t{}\n".format(TRIAL_START_CODE, 0)) # start trig position in millisecond
            #
            triggerEncoder.encode(TRIAL_END_CODE, file_len)
            event_metafile.write("{}\t{}\n".format(TRIAL_END_CODE, round(file_len*1000))) # end trig position in millisecond
            triggerEncoder.generateTrigger(trig_filename, file_len+1.0) #shorter?
            event_metafile.close()
    
    #Part trigs:
    newPath = os.getcwd()
    for j in range(0, 3): #Parts 1-3
        part_trigs(j, triggerEncoder) #Reusing triggerEncoder from before