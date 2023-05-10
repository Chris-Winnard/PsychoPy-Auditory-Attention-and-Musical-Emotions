#Calibration software, created with help from ChatGPT. At the end we run 'randomOddballCreator.py' to add
#oddballs to MS stimuli. Then we run 'personalisedStimuliMixer.py' to implement gains/do mixing.


#NOTE: TRIGGER FILES MUST BE GENERATED BEFOREHAND (FOR RANDOM SET OF STIMULI + ODDBALL MIXES- DOESN'T MATTER
#AS FILENAMES THE SAME REGARDLESS OF PARTICIPANT).

import pathlib
from psychopy import core, gui, sound, visual
from pyo import *
import time
import ctypes  #For dialogue boxes without option to cancel.
from pydub import AudioSegment
import numpy as np
import os
import wx

expName = 'Loudness Calibration'  # from the Builder filename that created this script
expInfo = {'Participant': ''}
dlg = gui.DlgFromDict(dictionary=expInfo, sortKeys=False, title=expName)
if dlg.OK == False:
    core.quit()  # user pressed cancel

#Navigate into Data folder, and find the subfolder for the participant:
currentFolderPath = pathlib.Path(__file__).parent.resolve()
upperFolderPath = currentFolderPath.parent.resolve()
dataPath = str(upperFolderPath) + "/Data/"


groupAssignmentFile = dataPath + "Participant Groups.txt" #Needed for taking collecting stimuli, and saving to right place:
with open(groupAssignmentFile, 'r') as f:
    lines = f.readlines()
    for line in lines:
        if "Group A1" in line and expInfo['Participant'] in line:
            participantPath = dataPath + "Group A1/" + expInfo['Participant']
            vibrPiece = "Set01-Vibr.wav"
            harmPiece = "Set01-Harm.wav"
            keybPiece = "Set01-Keyb.wav"
        elif "Group A2" in line and expInfo['Participant'] in line:
            participantPath = dataPath + "Group A2/" + expInfo['Participant']
            vibrPiece = "Set01-Vibr.wav"
            harmPiece = "Set01-Harm.wav"
            keybPiece = "Set01-Keyb.wav"
            
        elif "Group B1" in line and expInfo['Participant'] in line:
            participantPath = dataPath + "Group B1/" + expInfo['Participant']
            vibrPiece = "Set04-Vibr.wav"
            harmPiece = "Set04-Harm.wav"
            keybPiece = "Set04-Keyb.wav"
        elif "Group B2" in line and participantNo in line:
            participantPath = dataPath + "Group B2/" + expInfo['Participant']
            vibrPiece = "Set04-Vibr.wav"
            harmPiece = "Set04-Harm.wav"
            keybPiece = "Set04-Keyb.wav"
    f.close
    
##########################################################################################################################################

#PART 1 - SPATIAL BALANCING:
SOUNDCARD_DEVICE_NAME = 'DAC8PRO'

OUT_CHANNELS = 2

volume_level = 0.05

volume_ratio = [1, 1, 5]

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

# Load the audio files
vibraphone = AudioSegment.from_wav(vibrPiece)
harmonica = AudioSegment.from_wav(harmPiece)
piano = AudioSegment.from_wav(keybPiece)

# To control for acquiescence, we randomise the initial settings.
[vibrPan, harmPan, keybPan] = np.random.uniform(-1, 1, 3)

#Set up loudness parameter, apply gain:
vibraphone_loudness = 0.5
vibraphone = vibraphone.apply_gain(20*np.log10(vibraphone_loudness))

harmonica_loudness = 0.5
harmonica = harmonica.apply_gain(20*np.log10(harmonica_loudness))

piano_loudness = 0.5
piano = piano.apply_gain(20*np.log10(piano_loudness))

current_instrument = "Vibraphone"
currentPan = vibrPan

# Create a GUI
dlg = gui.Dlg(title="Spatialisation")
dlg.addText("People can have slightly different perceptions of where the \"centre\" is when they hear music. We are going to run a test to tweak the audio settings to your ears.\n"
            "A vibraphone will play from a random direction, and you will need to adjust the balance so that you hear it as coming from the centre- you can adjust\n"
            + "as many times as needed. We will then repeat the test twice with other instruments.\n\nWhen you are ready to hear the music for the first time, press \"OK\".")
dlg.show()
if dlg.OK == False:
    core.quit()  # user pressed cancel

while True:
    if current_instrument == "Vibraphone":
        output = vibraphone.pan(currentPan)
    elif current_instrument == "Harmonica":
        output = harmonica.pan(currentPan)
    else:
        output = piano.pan(currentPan)

    output.export("Temp.wav", format="wav")
    
    #Create players for new mix:
    players = []
    for i in range(1, OUT_CHANNELS):
        if i < len(spk_volume):  # check if spk_volume has the correct number of elements
            player = sound.Sound("Temp.wav")
            player.setVolume(spk_volume[i])  # set the volume for the current speaker
        players.append(player)

    # Start the server
    s.start()
    for player in players:
        player.play()
        # Wait until 10 seconds pass
        core.wait(10)
        player.stop()
    
    # Stop the server
    s.stop()
    
    # Ask user if they are happy:
    dlg = gui.Dlg(title="Spatialisation")
    dlg.addField("Would you like to continue adjusting this instrument?", choices=["Yes", "No"])
    dlg.show()
    
    if dlg.OK and dlg.data[0] == "No" and current_instrument == "Vibraphone":
        dlg = gui.Dlg(title="Spatialisation")
        dlg.addText("We will now move on to the harmonica.")
        dlg.show()
        if dlg.OK == False:
            core.quit()  # user pressed cancel
        current_instrument = "Harmonica"
        currentPan = harmPan
        
    elif dlg.OK and dlg.data[0] == "No" and current_instrument == "Harmonica":
        dlg = gui.Dlg(title="Spatialisation")
        dlg.addText("We will now move on to the piano.")
        dlg.show()
        if dlg.OK == False:
            core.quit()  # user pressed cancel
        current_instrument = "Piano"
        currentPan = keybPan
        
    elif dlg.OK and dlg.data[0] == "No" and current_instrument == "Piano":
    
        #Save the results:        
        gains = ["Vibraphone: ", vibrPan, " Harmonica: ", harmPan, " Piano: ", keybPan]        
        #Create a new file in the appropriate location. If there's already a file there of the same name, it's wiped:
        File = (participantPath + "\Spatialisation Settings.txt")
        #Open, write to file, and close.
        with open(File, 'w') as f:
            for x in gains:
                f.write("%s" % x )
            f.close()
        ctypes.windll.user32.MessageBoxW(0, "Your settings have been saved.", "Success!")        
        break
    
    elif dlg.OK and dlg.data[0] == "Yes":
        dlg = gui.Dlg(title="Spatialisation")
        dlg.addText("On a scale of -90 (90 degrees to the left) to +90 (90 degrees to the right), please indicate how much you would like to change the direction.")        
        dlg.addField("Change: ")
        dlg.show()
        if dlg.OK:
            changeDegrees = float(dlg.data[0])
            currentPan += changeDegrees*(1/90)
            
            #If we get numbers out of the range (-1, 1), we loop back around from the other side:
            if currentPan < -1:
                diff = - 1 - currentPan
                currentPan = 1 - diff
            elif currentPan > 1:
                diff = currentPan - 1
                currentPan = 1 - diff
        else:
            core.quit()

# Stop the server
s.stop()
    
##########################################################################################################################################

#PART 2 - MULTI-STREAM GAINS:
SOUNDCARD_DEVICE_NAME = 'DAC8PRO'

OUT_CHANNELS = 2

volume_level = 0.05

volume_ratio = [1, 1, 5]

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

# Load the audio files
vibraphone = AudioSegment.from_wav(vibrPiece)
harmonica = AudioSegment.from_wav(harmPiece)
piano = AudioSegment.from_wav(keybPiece)

# Create panner for each sound
vibraphone = vibraphone.pan(-1)
harmonica = harmonica.pan(harmPan)
piano = piano.pan(1)

#Set up loudness parameter, apply gain:
vibraphone_loudness = 0.45
harmonica_loudness = 0.45
piano_loudness = 0.45
    

while True:
    # Create a GUI to get loudness values from the user for each audio stream
    dlg = gui.Dlg(title="Loudness Adjustment")
    dlg.addText("Please adjust the loudness of the instruments, so that you can hear them and pay "
                 + "attention to all three comfortably. The gains should be >0 but do not need to add up to 1.")
    dlg.addField("Vibraphone Loudness:", initial=vibraphone_loudness)
    dlg.addField("Harmonica Loudness:", initial=harmonica_loudness)
    dlg.addField("Piano Loudness:", initial=piano_loudness)
    dlg.show()
    if dlg.OK:
        vibraphone_loudness = dlg.data[0]
        harmonica_loudness = dlg.data[1]
        piano_loudness = dlg.data[2]
    else:
        core.quit()
    
    #Update:
    vibrOutput = vibraphone.apply_gain(20*np.log10(vibraphone_loudness)) #Apply gain- CONVERT TO DB!
    harmOutput = harmonica.apply_gain(20*np.log10(harmonica_loudness))
    pianoOutput = piano.apply_gain(20*np.log10(piano_loudness))
    
    mix = vibrOutput.overlay(harmOutput).overlay(pianoOutput)
    mix.export("TempMix.wav", format="wav")    
    
    #Create players for new mix:
    players = []
    for i in range(1, OUT_CHANNELS):
        if i < len(spk_volume):  # check if spk_volume has the correct number of elements
            player = sound.Sound("TempMix.wav")
            player.setVolume(spk_volume[i])  # set the volume for the current speaker
        players.append(player)

    # Start the server
    s.start()
    for player in players:
        player.play()
        # Wait until 10 seconds pass
        core.wait(10)
        player.stop()
    
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
        File = (participantPath + "\Multi-stream Gains.txt")
        #Open, write to file, and close.
        with open(File, 'w') as f:
            for x in gains:
                f.write("%s" % x )
            f.close()
        ctypes.windll.user32.MessageBoxW(0, "Your settings have been saved.", "Success!")        
        break

# Stop the server
s.stop()


##########################################################################################################################################
#PART 3 - SINGLE-STREAM GAINS

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
vibraphone = AudioSegment.from_wav(vibrPiece)
harmonica = AudioSegment.from_wav(harmPiece)
piano = AudioSegment.from_wav(keybPiece)

vibraphone.pan(vibrPan)
harmonica.pan(harmPan)
piano.pan(keybPan)


# Create a GUI to get the instrument selection from the user
dlg = gui.Dlg(title="Single Instrument Calibration")
dlg.addText("You will now need to adjust the instruments whilst they play one-at-a-time. You can listen to each instrument as many times as you want.")
dlg.show()
if dlg.OK:
    selected_instrument = "Vibraphone"
else:
    core.quit()

while True:
    # Create a GUI to get loudness values from the user
    dlg = gui.Dlg(title="Loudness Adjustment")
    dlg.addText("Now, please adjust the settings so that you can follow it comfortably and easily.")
    dlg.addText("The current instrumnt is the " + selected_instrument.lower() + ".")
    dlg.addField("Current instrument loudness:", initial=vibraphone_loudness if selected_instrument == "Vibraphone" else (harmonica_loudness if selected_instrument == "Harmonica" else piano_loudness))
    dlg.addField("Play next:", choices=["Vibraphone", "Harmonica", "Piano"])
    dlg.addField("Do you want to continue adjusting the instruments?", choices=["Yes", "No"]) #Yes by default- acquiescence control.
    dlg.show()
    if dlg.OK:
        loudness = dlg.data[0]
        #Update the one they were just listening to:
        if selected_instrument == "Vibraphone":
            vibraphone_loudness = loudness
        
        elif selected_instrument == "Harmonica":
            harmonica_loudness = loudness
        
        elif selected_instrument == "Piano":
            piano_loudness = loudness
        
        selected_instrument = dlg.data[1]
        continue_adjusting = (dlg.data[2] == "Yes")
    else:
        core.quit()
        break
    
    if continue_adjusting == 0: #Best to have this before playing stimuli         
        #Save the results:        
        gains = ["Vibraphone: ", vibraphone_loudness, " Harmonica: ", harmonica_loudness,
                 " Piano: ", piano_loudness]        
        #Create a new file in the appropriate location. If there's already a file there of the same name, it's wiped:
        File = (participantPath + "\Single-stream Gains.txt")
        #Open, write to file, and close.
        with open(File, 'w') as f:
            for x in gains:
                f.write("%s" % x )
            f.close
        break
    
    #Update output:
    if selected_instrument == "Vibraphone":
        output = vibraphone.apply_gain(20*np.log10(vibraphone_loudness)) #Apply gain- CONVERT TO DB!
    
    elif selected_instrument == "Harmonica":
        output = harmonica.apply_gain(20*np.log10(harmonica_loudness))
    
    else:
        output = piano.apply_gain(20*np.log10(piano_loudness))
    
    output.export("Temp.wav", format="wav")    
    
    #Create players for new mix:
    players = []
    for i in range(1, OUT_CHANNELS):
        if i < len(spk_volume):  # check if spk_volume has the correct number of elements
            player = sound.Sound("Temp.wav")
            player.setVolume(spk_volume[i])  # set the volume for the current speaker
        players.append(player)

    # Start the server
    s.start()
    for player in players:
        player.play()
        # Wait until 10 seconds pass
        core.wait(10)
        player.stop()
        
    #Stop the server
    s.stop()
        
s.stop()
s.shutdown()

os.remove("TempMix.wav")

if "Temp.wav" in dataPath:
    os.remove("Temp.wav") #Not strictly needed, keeps things terse.

ctypes.windll.user32.MessageBoxW(0, "Your settings have been saved.", "Success!")

##########################################################################################################################################
exec(open('personalisedStimuliMixer.py').read()) #Create stimuli with gains applied: both single-stream, and
#mixes of the oddball stimuli.

#Additional note: trigger files have already been created. By the nature of gainApplier and randomOddballCreator,
#all pieces have the exact same lengths enforced, so can just use one start/end trigger pair for the Set1-Harm files
#(i.e not different versions of the triggers for different participants), etc.

#Also note that for the trigger files: for oddball tests the start trigger is at the v start of the audio file.

exec(open('listMaker.py').read()) #Create lists of the stimuli and the trigger files that can be used in the scripts
#with minimal extra work.