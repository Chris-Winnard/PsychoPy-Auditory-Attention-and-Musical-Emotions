#Calibration software, created with help from ChatGPT. At the end we run 'randomOddballCreator.py' to add
#oddballs to MS stimuli. Then we run 'personalisedStimuliMixer.py' to implement gains/do mixing.


#NOTE: TRIGGER FILES MUST BE GENERATED BEFOREHAND (FOR RANDOM SET OF STIMULI + ODDBALL MIXES- DOESN'T MATTER
#AS FILENAMES THE SAME REGARDLESS OF PARTICIPANT).

#PART 1: MULTI-STREAM GAINS: 

import pathlib
from psychopy import core, gui
from pyo import *
import time
import ctypes  #For dialogue boxes without option to cancel.

#from constants import *


SOUNDCARD_DEVICE_NAME = 'DAC8PRO'

OUT_CHANNELS = 2

volume_level = 0.025

volume_ratio = [1, 1]

spk_volume = [x * volume_level for x in volume_ratio]
 

s = Server(nchnls=OUT_CHANNELS, duplex=0)

devices = pa_get_output_devices()

for name in devices[0]:

    if SOUNDCARD_DEVICE_NAME in name:

        soundcard_idx = devices[1][devices[0].index(name)]

        print('sound card: ', name)

        s.setOutputDevice(soundcard_idx)

        break

 

s = s.boot()

#s.start()

expName = 'Loudness Calibration'  # from the Builder filename that created this script
expInfo = {'Participant': ''}
dlg = gui.DlgFromDict(dictionary=expInfo, sortKeys=False, title=expName)
if dlg.OK == False:
    core.quit()  # user pressed cancel

#Navigate into Data folder, and find the subfolder for the participant:
currentFolderPath = pathlib.Path(__file__).parent.resolve()
upperFolderPath = currentFolderPath.parent.resolve()
dataPath = str(upperFolderPath) + "/Data/"
participantFolderPath = dataPath + expInfo['Participant'] #Needs to be an existing folder with oddball files prepped

#Find which stimuli are assigned to this participant. Use the practice stimuli for this.

megasetAssignmentFile = dataPath + "Megaset Assignment.txt"

with open(megasetAssignmentFile, 'r') as f:
    lines = f.readlines()
    for line in lines:
        if "Megaset A" in line and expInfo['Participant'] in line:
            vibrPiece = "Set4-Vibr.wav"
            harmPiece = "Set4-Harm.wav"
            keybPiece = "Set4-Keyb.wav"
        elif "Megaset B" in line and expInfo['Participant'] in line:
            vibrPiece = "Set1-Vibr.wav"
            harmPiece = "Set1-Harm.wav"
            keybPiece = "Set1-Keyb.wav"
    f.close
    
    
# Start server
s.boot()

# Load the audio files
vibraphone = SfPlayer(vibrPiece, loop=True, mul=0.5)
harmonica = SfPlayer(harmPiece, loop=True, mul=0.5)
piano = SfPlayer(keybPiece, loop=True, mul=0.5)

# Create panner for each sound
vibraphone_pan = Pan(vibraphone, outs=2, pan=0)
harmonica_pan = Pan(harmonica, outs=2, pan=0.5)
piano_pan = Pan(piano, outs=2, pan=1)

start_time = time.time()

while True:
    # Create a GUI to get loudness values from the user for each audio stream
    dlg = gui.Dlg(title="Loudness Adjustment")
    dlg.addText("Please adjust the loudness of the instruments, so that you can hear them and pay "
                 + "attention to all three comfortably. The gains do not need to add up to 1.")
    dlg.addField("Vibraphone Loudness:", initial=vibraphone.mul)
    dlg.addField("Harmonica Loudness:", initial=harmonica.mul)
    dlg.addField("Piano Loudness:", initial=piano.mul)
    dlg.show()
    if dlg.OK:
        vibraphone_loudness = dlg.data[0]
        harmonica_loudness = dlg.data[1]
        piano_loudness = dlg.data[2]
    else:
        core.quit()

    # Update the loudness of each audio stream
    vibraphone.mul = vibraphone_loudness
    harmonica.mul = harmonica_loudness
    piano.mul = piano_loudness

    # Connect the panners to the server
    vibraphone_pan.out()
    harmonica_pan.out()
    piano_pan.out()

    # Start the server
    s.start()

    # Wait until 10 seconds pass
    core.wait(10)
    
    # Stop the server
    s.stop()

    # Ask user if they are happy with the loudness gains:
    dlg = gui.Dlg(title="Loudness Adjustment")
    dlg.addField("Are you happy with the gains?", choices=["No", "Yes"]) #No by default- acquiescence control.
    dlg.show()
    
    if dlg.OK and dlg.data[0] == "Yes":
       
        #Save the results:        
        gains = ["Vibraphone: ", vibraphone_loudness, " Harmonica: ", harmonica_loudness, " Piano: ", piano_loudness]        
        #Create a new file in the appropriate location. If there's already a file there of the same name, it's wiped:
        File = (participantFolderPath + "\Multi-stream Gains.txt")
        #Open, write to file, and close.
        with open(File, 'w') as f:
            for x in gains:
                f.write("%s" % x )
            f.close
        ctypes.windll.user32.MessageBoxW(0, "Your settings have been saved.", "Success!")        
        break

# Stop the server
s.stop()



#PART 2: DIFFERENT INSTRUMENTS PLAYING AT DIFFERENT TIMES

continue_adjusting = True

#New server:
s = Server(nchnls=OUT_CHANNELS, duplex=0)

devices = pa_get_output_devices()

for name in devices[0]:

    if SOUNDCARD_DEVICE_NAME in name:

        soundcard_idx = devices[1][devices[0].index(name)]

        print('sound card: ', name)

        s.setOutputDevice(soundcard_idx)

        break

 

s = s.boot()

#Set default gains. To avoid confusion, these are not necessarily the same as the .mul
#values which are actually used to control loudness. E.g, piano_loudness might be 1, but the
#piano output will be 0 whilst the vibraphone plays.
vibraphone_loudness = 0.5
harmonica_loudness = 0.5
piano_loudness = 0.5

# Reload the audio files, this time without panning
vibraphone = SfPlayer(vibrPiece, loop=True, mul=vibraphone_loudness)
harmonica = SfPlayer(harmPiece, loop=True, mul=harmonica_loudness)
piano = SfPlayer(keybPiece, loop=True, mul=piano_loudness)

while continue_adjusting:
    # Create a GUI to get the instrument selection from the user
    dlg = gui.Dlg(title="Single Instrument Calibration")
    dlg.addField("You will now need to adjust the instruments whilst they play one-at-a-time. You can\nswitch between"
                 + " them as you do this. Which instrument would you like to listen to first?",
                 choices=["Vibraphone", "Harmonica", "Piano"])
    dlg.show()
    if dlg.OK:
        selected_instrument = dlg.data[0]
    else:
        core.quit()

    # Mute the unselected instrument
    if selected_instrument == "Vibraphone":
        vibraphone.out()
        harmonica.mul = 0
        piano.mul= 0
    elif selected_instrument == "Harmonica":
        vibraphone.mul = 0
        harmonica.out()
        piano.mul = 0
    else:
        vibraphone.mul = 0
        harmonica.mul = 0
        piano.out()

    s.start()
    start_time = time.time()

    while True:
        # Create a GUI to get loudness values from the user
        dlg = gui.Dlg(title="Loudness Adjustment")
        dlg.addText("Now, please adjust the settings so that you can follow it comfortably and easily.")
        dlg.addField("Loudness:", initial=vibraphone_loudness if selected_instrument == "Vibraphone" else (harmonica_loudness if selected_instrument == "Harmonica" else piano_loudness))
        dlg.addField("Play next:", choices=["Vibraphone", "Harmonica", "Piano"])
        dlg.addField("Do you want to continue adjusting the instruments?", choices=["Yes", "No"]) #Yes by default- acquiescence control.
        dlg.show()
        if dlg.OK:
            loudness = dlg.data[0]
            new_selected_instrument = dlg.data[1]
            continue_adjusting = (dlg.data[2] == "Yes")
        else:
            core.quit()
            break
        
        # Update the loudness of the selected instrument
        if selected_instrument == "Vibraphone":
            vibraphone_loudness = loudness
        elif selected_instrument == "Harmonica":
            harmonica_loudness = loudness
        else:
            piano_loudness = loudness
       
        # Check what instrument the user has selected now. Make sure that it is not muted, and the other one is
        if new_selected_instrument == "Vibraphone":
            vibraphone.mul = vibraphone_loudness
            vibraphone.out()
            harmonica.mul = 0
            piano.mul = 0
        elif new_selected_instrument == "Harmonica":
            vibraphone.mul = 0
            harmonica.mul = harmonica_loudness
            harmonica.out()
            piano.mul = 0
        else:
            vibraphone.mul = 0
            harmonica.mul = 0
            piano.mul = piano_loudness
            piano.out()
        selected_instrument = new_selected_instrument
        
        if continue_adjusting == 0:           
            #Save the results:        
            gains = ["Vibraphone: ", vibraphone_loudness, " Harmonica: ", harmonica_loudness,
                     " Piano: ", piano_loudness]        
            #Create a new file in the appropriate location. If there's already a file there of the same name, it's wiped:
            File = (participantFolderPath + "\Single-stream Gains.txt")
            #Open, write to file, and close.
            with open(File, 'w') as f:
                for x in gains:
                    f.write("%s" % x )
                f.close
            break
        
s.stop()
s.shutdown()

ctypes.windll.user32.MessageBoxW(0, "Your settings have been saved.", "Success!")

##############################################################################################################
exec(open('personalisedStimuliMixer.py').read()) #Create stimuli with gains applied: both single-stream, and
#mixes of the oddball stimuli.

#Additional note: trigger files have already been created. By the nature of gainApplier and randomOddballCreator,
#all pieces have the exact same lengths enforced, so can just use one start/end trigger pair for the Set1-Harm files
#(i.e not different versions of the triggers for different participants), etc.

#Also note that for the trigger files: for oddball tests the start trigger is at the v start of the audio file.

exec(open('listMaker.py').read()) #Create lists of the stimuli and the trigger files that can be used in the scripts
#with minimal extra work.