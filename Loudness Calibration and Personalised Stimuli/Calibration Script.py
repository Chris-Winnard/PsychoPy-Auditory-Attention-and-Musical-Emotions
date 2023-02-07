#Created with help from ChatGPT (a lot of the code written by it, then edited)

#PART 1: MULTI-STREAM GAINS:

from psychopy import core, gui
from pyo import Server, SfPlayer, Pan
import time
import ctypes  #For dialogue boxes without option to cancel.

expName = 'Loudness Calibration'  # from the Builder filename that created this script
expInfo = {'Participant': ''}
print(str(expInfo['Participant']))
dlg = gui.DlgFromDict(dictionary=expInfo, sortKeys=False, title=expName)
if dlg.OK == False:
    core.quit()  # user pressed cancel

# Create a server and start it
s = Server().boot()

# Load the audio files
vibraphone = SfPlayer("Set1-Vibr.wav", loop=True, mul=0.5)
piano = SfPlayer("Set1-Keyb.wav", loop=True, mul=0.5)

# Create panner for each sound
vibraphone_pan = Pan(vibraphone, outs=2, pan=-1)
piano_pan = Pan(piano, outs=2, pan=1)

start_time = time.time()

while True:
    # Create a GUI to get loudness values from the user for each audio stream
    dlg = gui.Dlg(title="Loudness Adjustment")
    dlg.addText("Please adjust the loudness of the instruments, so that you can hear them and pay "
                 + "attention to them both comfortably. The gains do not need to add up to 1.")
    dlg.addField("Vibraphone Loudness:", initial=vibraphone.mul)
    dlg.addField("Piano Loudness:", initial=piano.mul)
    dlg.show()
    if dlg.OK:
        vibraphone_loudness = dlg.data[0]
        piano_loudness = dlg.data[1]
    else:
        core.quit()

    # Update the loudness of each audio stream
    vibraphone.mul = vibraphone_loudness
    piano.mul = piano_loudness

    # Connect the panners to the server
    vibraphone_pan.out()
    piano_pan.out()

    # Start the server
    s.start()

    # Wait until 10 seconds pass
    core.wait(10)
    
    # Stop the server
    s.stop()

    # Ask user if they are happy with the loudness gains:
    dlg = gui.Dlg(title="Loudness Adjustment")
    dlg.addField("Are you happy with the gains?", choices=["Yes", "No"])
    dlg.show()
    
    if dlg.OK and dlg.data[0] == "Yes":
       
        #Save the results:        
        gains = ["Vibraphone: ", vibraphone_loudness, "\nPiano: ", piano_loudness]        
        #Create a new file in the appropriate location. If there's already a file there of the same name, it's wiped:
        File = ("Multi-stream gains for " + str(expInfo['Participant']) + ".txt")
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

# Create a server and start it
s = Server().boot()

#Set default gains. To avoid confusion, these are not necessarily the same as the .mul
#values which are actually used to control loudness. E.g, piano_loudness might be 1, but the
#piano output will be 0 whilst the vibraphone plays.
vibraphone_loudness = 0.5
piano_loudness = 0.5

# Reload the audio files, this time without panning
vibraphone = SfPlayer("Set1-Vibr.wav", loop=True, mul=vibraphone_loudness)
piano = SfPlayer("Set1-Keyb.wav", loop=True, mul=piano_loudness)

while continue_adjusting:
    # Create a GUI to get the instrument selection from the user
    dlg = gui.Dlg(title="Single Instrument Calibration")
    dlg.addField("You will now need to adjust the instruments whilst they play one-at-a-time. "
                 + "Which instrument would you like to listen to first?", choices=["Vibraphone", "Piano"])
    dlg.show()
    if dlg.OK:
        selected_instrument = dlg.data[0]
    else:
        core.quit()

    # Mute the unselected instrument
    if selected_instrument == "Vibraphone":
        vibraphone.out()
        piano.mul= 0
    else:
        piano.out()
        vibraphone.mul = 0

    s.start()
    start_time = time.time()

    while True:
        # Create a GUI to get loudness values from the user
        dlg = gui.Dlg(title="Loudness Adjustment")
        dlg.addText("Now, please adjust the settings so that you can follow it comfortably and easily.")
        dlg.addField("Loudness:", initial=vibraphone_loudness if selected_instrument == "Vibraphone" else piano_loudness)
        dlg.addField("Play next:", choices=["Vibraphone", "Piano"])
        dlg.addField("Do you want to continue adjusting?", choices=["Yes", "No"])
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
            print("Vibraphone loudness has been updated to " + str(vibraphone_loudness))
        else:
            piano_loudness = loudness
            print("Piano loudness has been updated to " + str(piano_loudness))
       
        # Check what instrument the user has selected now. Make sure that it is not muted, and the other one is
        if new_selected_instrument == "Vibraphone":
            vibraphone.mul = vibraphone_loudness
            vibraphone.out()
            piano.mul = 0
        else:
            piano.mul = piano_loudness
            piano.out()
            vibraphone.mul = 0
        selected_instrument = new_selected_instrument
        
        if continue_adjusting == 0:           
            #Save the results:        
            gains = ["Vibraphone: ", vibraphone_loudness, "\nPiano: ", piano_loudness]        
            #Create a new file in the appropriate location. If there's already a file there of the same name, it's wiped:
            File = ("Single-stream Gains for " + str(expInfo['Participant']) + ".txt")
            #Open, write to file, and close.
            with open(File, 'w') as f:
                for x in gains:
                    f.write("%s" % x )
                f.close
            break
        
s.stop()
s.shutdown()

ctypes.windll.user32.MessageBoxW(0, "Your settings have been saved.", "Success!")