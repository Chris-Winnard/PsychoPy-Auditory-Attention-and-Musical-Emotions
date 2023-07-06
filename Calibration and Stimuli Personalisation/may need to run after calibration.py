exec(open('personalisedStimuliMixer.py').read()) #Create stimuli with gains applied: both single-stream, and
#mixes of the oddball stimuli.

#Additional note: trigger files have already been created. By the nature of gainApplier and randomOddballCreator,
#all pieces have the exact same lengths enforced, so can just use one start/end trigger pair for the Set1-Harm files
#(i.e not different versions of the triggers for different participants), etc.

#Also note that for the trigger files: for oddball tests the start trigger is at the v start of the audio file.

exec(open('listMaker.py').read()) #Create lists of the stimuli and the trigger files that can be used in the scripts
#with minimal extra work.

exec(open('generate_trig_P2.py').read())