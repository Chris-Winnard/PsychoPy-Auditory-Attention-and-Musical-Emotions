import os
import sys
import argparse
import glob
import soundfile as sf
from utils.SerialTriggerEncoder import SerialTriggerEncoder

PART_START_CODE = 0b1110
PART_END_CODE = 0b1111
TRIAL_START_CODE = 0b1000
TRIAL_END_CODE = 0b1001

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

if __name__ == '__main__':
    parser = argparse.ArgumentParser(prog='generate_trig')
    parser.add_argument("--in_folder", type=str, required=True, help="input folder containing target and non-target sounds.")
    parser.add_argument("--out_folder", type=str, required=True, help="output folder")
    parser.add_argument("--sr", type=int, default=48000, help="sampling rate. Default value is 48000.")
    parser.add_argument("--channels", type=int, default=1, help="number of output channels. Default value is 1.")
    parser.add_argument("--triggerClk", type=float, default=8.0, help="Clock rate of trigger. Default value is 8.0 Hz.")
    args = parser.parse_args()

    in_folder = os.path.abspath(args.in_folder)
    out_folder = os.path.abspath(args.out_folder)
    sr = args.sr
    ch = args.channels
    clkSerial = args.triggerClk

    if not os.path.exists(out_folder):
        os.makedirs(out_folder)
    
    file_list = getFileList(in_folder)
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
            
            if "Oddball Test Mix" in name: #FOR PART 2 STIMULI- THE STIMULUS IS PLAYED, THEN THERE IS A 5S PAUSE, THEN THE 2ND LOOPING STARTS. WE 
            #ONLY CARE ABOUT THE LATTER.
                endOfFirstStimPlay = (file_len-5)/2 #Time when the stimulus stops playing (1st loop) in seconds
                startOfSecondStimPlay = endOfFirstStimPlay + 5 #Time when the stimulus starts playing (2nd loop) in seconds#
                event_metafile = open(trig_metafilename, 'w')
                event_metafile.write("{}\t{}\n".format(TRIAL_START_CODE, startOfSecondStimPlay*1000)) # start trig position in millisecond
                #
                triggerEncoder.encode(TRIAL_END_CODE, file_len)
                event_metafile.write("{}\t{}\n".format(TRIAL_END_CODE, round(file_len*1000))) # end trig position in milisecond
                triggerEncoder.generateTrigger(trig_filename, file_len+1.0)
                event_metafile.close()
            else:                      
                trig_filename = os.path.join(out_folder, 'trigger_' + name + '.wav')
                trig_metafilename = os.path.join(out_folder,'trigger_' + name + '.txt')
                triggerEncoder.resetTrigger()
                triggerEncoder.encode(TRIAL_START_CODE, 0.0)
                event_metafile = open(trig_metafilename, 'w')
                event_metafile.write("{}\t{}\n".format(TRIAL_START_CODE, 0)) # start trig position in millisecond
                #
                triggerEncoder.encode(TRIAL_END_CODE, file_len)
                event_metafile.write("{}\t{}\n".format(TRIAL_END_CODE, round(file_len*1000))) # end trig position in milisecond
                triggerEncoder.generateTrigger(trig_filename, file_len+1.0)
                event_metafile.close()
