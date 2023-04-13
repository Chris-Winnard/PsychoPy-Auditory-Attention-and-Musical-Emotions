#!/usr/bin/env python
# -*- coding: utf-8 -*-

from psychopy import locale_setup
from psychopy import prefs
#prefs.hardware['audioLib'] = ['PTB'] -  causes sound.Sound to crash
from psychopy import sound, gui, visual, core, data, event, logging, clock, colors
from psychopy.constants import (NOT_STARTED, STARTED, PLAYING, PAUSED,
                                STOPPED, FINISHED, PRESSED, RELEASED, FOREVER)

import numpy as np
from numpy import (sin, cos, tan, log, log10, pi, average,
                   sqrt, std, deg2rad, rad2deg, linspace, asarray)
from numpy.random import random, randint, normal, shuffle, choice as randchoice
import os  # handy system and path functions
import sys  # to get file system encoding

import psychopy.iohub as io
from psychopy.hardware import keyboard
from pyo import *
import random
import json

sys.path.append('.')
from constants import *

SOUNDCARD_DEVICE_NAME = 'DAC8PRO'

volume_level = 0.05
volume_ratio = [1, 1]
spk_volume = [x * volume_level for x in volume_ratio]
pa_list_devices()
pa_list_devices()
s = Server(nchnls=PART_1_OUT_CHANNELS, duplex=0)
devices = pa_get_output_devices()
#print(devices[0])
#print(devices[1])
indx = []
#for name in devices[0]:
for i in range(len(devices[0])):
    name = devices[0][i]
    if SOUNDCARD_DEVICE_NAME in name:
    #    print(name)
        soundcard_idx = devices[1][devices[0].index(name)]
        s.setOutputDevice(soundcard_idx)
        indx.append(devices[1][i])
        break
#print(indx)
s = s.boot()
s.start()

chns = [None]*(PART_1_OUT_CHANNELS-1)
mm = Mixer(outs=PART_1_OUT_CHANNELS)

# Ensure that relative paths start from the same directory as this script
_thisDir = os.path.dirname(os.path.abspath(__file__))
os.chdir(_thisDir)
# Store info about the experiment session
psychopyVersion = '2022.1.3'
expName = 'Part1'  # from the Builder filename that created this script
expInfo = {'participant': ''}
dlg = gui.DlgFromDict(dictionary=expInfo, sortKeys=False, title=expName)
if dlg.OK == False:
    core.quit()  # user pressed cancel
expInfo['date'] = data.getDateStr()  # add a simple timestamp
expInfo['expName'] = expName

# Data file name stem = absolute path + name; later add .psyexp, .csv, .log, etc
participantPath = _thisDir + '/Data/' + expInfo['participant'] #participantPath also used for locating stimuli lists for this particular participant.
filename = participantPath + '/Part 1 Data'
jsonfilename = filename + '_stimuli.json'
jsondata = {}
jsondata['trials'] = []

# An ExperimentHandler isn't essential but helps with data saving
thisExp = data.ExperimentHandler(name=expName,
    extraInfo=expInfo, runtimeInfo=None,
    originPath= _thisDir + '/Part 1 Script.py',
    savePickle=True, saveWideText=True,
    dataFileName=filename)
# save a log file for detail verbose info
logFile = logging.LogFile(filename+'.log', level=logging.EXP)
logging.console.setLevel(logging.WARNING)  # this outputs to the screen, not a file

endExpNow = False  # flag for 'escape' or other condition => quit the exp
frameTolerance = 0.001  # how close to onset before 'same' frame

# Start Code - component code to be run after the window creation

# Setup the Window
win = visual.Window(
    size=[1920, 1080], fullscr=False, screen=0, 
    winType='pyglet', allowGUI=False, allowStencil=False,
    monitor='AIM Laptop', color=[-0.4510, 0.0196, 0.4118], colorSpace='rgb',
    blendMode='avg', useFBO=True, 
    units='height')
# Setup ioHub
ioConfig = {}

# Setup iohub keyboard
ioConfig['Keyboard'] = dict(use_keymap='psychopy')

ioSession = '1'
if 'session' in expInfo:
    ioSession = str(expInfo['session'])
ioServer = io.launchHubServer(window=win, **ioConfig)
eyetracker = None

# create a default keyboard (e.g. to check for escape)
defaultKeyboard = keyboard.Keyboard(backend='iohub')

# Initialize components for Routine "instructions"
instructionsClock = core.Clock()
instr_txt = visual.TextStim(win=win, name='instr_txt',
    text='Some music will play. Please close your eyes, and try not to move during this period. \n\nYou will then be asked to rate your emotions. You can then take a break.\n\nIf you have any questions at all please ask the experimenters.',
    font='Open Sans',
    pos=(0, 0.15), height=0.05, wrapWidth=1.8, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);
mouse_2 = event.Mouse(win=win)
x, y = [None, None]
mouse_2.mouseClock = core.Clock()
nextButton_instruct = visual.ImageStim(
    win=win,
    name='nextButton_instruct', 
    image='next.png', mask=None, anchor='center',
    ori=0.0, pos=(0, -0.4), size=(0.15, 0.075),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-2.0)

# Initialize components for Routine "practiceReady"
practiceReadyClock = core.Clock()
practiceReadyTxt = visual.TextStim(win=win, name='practiceReadyTxt',
    text='We are now going to run a practice trial.\n\nWhen you are ready, click "NEXT".',
    font='Open Sans',
    pos=(0, 0.15), height=0.05, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);
mouse_4 = event.Mouse(win=win)
x, y = [None, None]
mouse_4.mouseClock = core.Clock()
nextButton_R1B = visual.ImageStim(
    win=win,
    name='nextButton_R1B', 
    image='next.png', mask=None, anchor='center',
    ori=0.0, pos=(0, -0.4), size=(0.15, 0.075),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-2.0)

# Initialize components for Routine "trial"
#These will also be used for practiceTrial
trialClock = core.Clock()
clickForEmotionInfo = visual.TextBox2(
     win, text='Click here for information on how the scales relate to particular emotions.', font='Open Sans',
     pos=(0, 0.4),     letterHeight=0.04,
     size=(1.7, 0.04625), borderWidth=2.0,
     color=[0.5961, -0.7333, -0.7333], colorSpace='rgb',
     opacity=None,
     bold=True, italic=False,
     lineSpacing=1.0,
     padding=0.0, alignment='center',
     anchor='center',
     fillColor=None, borderColor=None,
     flipHoriz=False, flipVert=False, languageStyle='LTR',
     editable=False,
     name='clickForEmotionInfo',
     autoLog=True,
)

valence = visual.TextStim(win=win, name='valence',
    text='How positive/negative is your current emotion?',
    font='Open Sans',
    pos=(0, 0.28), height=0.04, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-1.0);
valenceResp = visual.Slider(win=win, name='valenceResp',
    startValue=None, size=(1.0, 0.04), pos=(0, 0.18), units=None,
    labels=("Very negative","Neutral","Very positive"), ticks=(0,1,2,3,4,5,6,7,8,9,10), granularity=0.0,
    style='rating', styleTweaks=(), opacity=None,
    labelColor='LightGray', markerColor='Red', lineColor='White', colorSpace='rgb',
    font='Open Sans', labelHeight=0.025,
    flip=False, ori=0.0, depth=-2, readOnly=False)
arousal = visual.TextStim(win=win, name='arousal',
    text='How active/passive is your current emotion?',
    font='Open Sans',
    pos=(0, 0.06), height=0.04, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-3.0);
arousalResp = visual.Slider(win=win, name='arousalResp',
    startValue=None, size=(1.0, 0.04), pos=(0, -0.04), units=None,
    labels=("Very passive","Neutral","Very active"), ticks=(0,1,2,3,4,5,6,7,8,9,10), granularity=0.0,
    style='rating', styleTweaks=(), opacity=None,
    labelColor='LightGray', markerColor='Red', lineColor='White', colorSpace='rgb',
    font='Open Sans', labelHeight=0.025,
    flip=False, ori=0.0, depth=-4, readOnly=False)
dominance = visual.TextStim(win=win, name='dominance',
    text='How dominant/submissive is your current emotion?',
    font='Open Sans',
    pos=(0, -0.16), height=0.04, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-5.0);
dominanceResp = visual.Slider(win=win, name='dominanceResp',
    startValue=None, size=(1.0, 0.04), pos=(0, -0.26), units=None,
    labels=("Very submissive","Neutral","Very dominant"), ticks=(0,1,2,3,4,5,6,7,8,9,10), granularity=0.0,
    style='rating', styleTweaks=(), opacity=None,
    labelColor='LightGray', markerColor='Red', lineColor='White', colorSpace='rgb',
    font='Open Sans', labelHeight=0.025,
    flip=False, ori=0.0, depth=-6, readOnly=False)
mouse = event.Mouse(win=win)
x, y = [None, None]
mouse.mouseClock = core.Clock()
nextButton = visual.ImageStim(
    win=win,
    name='nextButton', 
    image='next.png', mask=None, anchor='center',
    ori=0.0, pos=(0, -0.4), size=(0.15, 0.075),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-8.0)

# Initialize components for Routine "Categorical_Emotions_to_VAD_Mapping"
Categorical_Emotions_to_VAD_MappingClock = core.Clock()
Emotions_Mapping_Figure = visual.ImageStim(
    win=win,
    name='Emotions_Mapping_Figure', 
    image='V-A-D to Ekman model mapping.png', mask=None, anchor='center',
    ori=0.0, pos=(0.43, 0.05), size=(0.81944505, 0.612),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=0.0)
nextButton_3 = visual.ImageStim(
    win=win,
    name='nextButton_3', 
    image='next.png', mask=None, anchor='center',
    ori=0.0, pos=(0, -0.4), size=(0.15, 0.075),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-10.0)
mouse_3 = event.Mouse(win=win)
x, y = [None, None]
mouse_3.mouseClock = core.Clock()
text_4 = visual.TextStim(win=win, name='text_4',
    text='Arousal examples: a sleepy person feels passive, whereas an excited person feels active.\n\nDominance examples: fear is negative/active/submissive, but anger is negative/active/dominant.\n\n Positive emotions are not always dominant. For example, when a person fulfils an assignment for a boss, they may feel positive/active/submissive.',
    font='Open Sans',
    pos=(-0.43, 0.05), height=0.04, wrapWidth=0.8, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-3.0);
text_3 = visual.TextStim(win=win, name='text_3',
    text='Image adapted from Buechel and Hahn, 2016. Used under the terms of the Creative Commons Attribution Non-Commercial License 4.0.\n',
    font='Open Sans',
    pos=(0, -0.47), height=0.02, wrapWidth=1.7, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-3.0);

# Initialize components for Routine "interTrialPause"
interTrialPauseClock = core.Clock()
interTrialPauseText = visual.TextStim(win=win, name='interTrialPauseText',
    text='When you are ready for the next trial, click "NEXT".',
    font='Open Sans',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);
mouse_4 = event.Mouse(win=win)
x, y = [None, None]
mouse_4.mouseClock = core.Clock()
nextButton_R1B = visual.ImageStim(
    win=win,
    name='nextButton_R1B', 
    image='next.png', mask=None, anchor='center',
    ori=0.0, pos=(0, -0.4), size=(0.15, 0.075),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-2.0)
    
# Create some handy timers
globalClock = core.Clock()  # to track the time since experiment started
routineTimer = core.CountdownTimer()  # to track time remaining of each (non-slip) routine 

# ------Prepare to start Routine "instructions"-------
continueRoutine = True
# update component parameters for each repeat
# setup some python lists for storing info about the mouse_2
mouse_2.clicked_name = []
gotValidClick = False  # until a click is received
# keep track of which components have finished
instructionsComponents = [instr_txt, mouse_2, nextButton_instruct]
for thisComponent in instructionsComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
instructionsClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "instructions"-------
while continueRoutine:
    # get current time
    t = instructionsClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=instructionsClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *instr_txt* updates
    if instr_txt.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        instr_txt.frameNStart = frameN  # exact frame index
        instr_txt.tStart = t  # local t and not account for scr refresh
        instr_txt.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(instr_txt, 'tStartRefresh')  # time at next scr refresh
        instr_txt.setAutoDraw(True)
    # *mouse_2* updates
    if mouse_2.status == NOT_STARTED and t >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        mouse_2.frameNStart = frameN  # exact frame index
        mouse_2.tStart = t  # local t and not account for scr refresh
        mouse_2.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(mouse_2, 'tStartRefresh')  # time at next scr refresh
        mouse_2.status = STARTED
        mouse_2.mouseClock.reset()
        prevButtonState = mouse_2.getPressed()  # if button is down already this ISN'T a new click
    if mouse_2.status == STARTED:  # only update if started and not finished!
        buttons = mouse_2.getPressed()
        if buttons != prevButtonState:  # button state changed?
            prevButtonState = buttons
            if sum(buttons) > 0:  # state changed to a new click
                # check if the mouse was inside our 'clickable' objects
                gotValidClick = False
                try:
                    iter(nextButton_instruct)
                    clickableList = nextButton_instruct
                except:
                    clickableList = [nextButton_instruct]
                for obj in clickableList:
                    if obj.contains(mouse_2):
                        gotValidClick = True
                        mouse_2.clicked_name.append(obj.name)
                if gotValidClick:  
                    continueRoutine = False  # abort routine on response
    
    # *nextButton_instruct* updates
    if nextButton_instruct.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        nextButton_instruct.frameNStart = frameN  # exact frame index
        nextButton_instruct.tStart = t  # local t and not account for scr refresh
        nextButton_instruct.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(nextButton_instruct, 'tStartRefresh')  # time at next scr refresh
        nextButton_instruct.setAutoDraw(True)
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in instructionsComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "instructions"-------
for thisComponent in instructionsComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# store data for thisExp (ExperimentHandler)
x, y = mouse_2.getPos()
buttons = mouse_2.getPressed()
if sum(buttons):
    # check if the mouse was inside our 'clickable' objects
    gotValidClick = False
    try:
        iter(nextButton_instruct)
        clickableList = nextButton_instruct
    except:
        clickableList = [nextButton_instruct]
    for obj in clickableList:
        if obj.contains(mouse_2):
            gotValidClick = True
            mouse_2.clicked_name.append(obj.name)
# the Routine "instructions" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# ------Prepare to start Routine "practiceReady"-------
continueRoutine = True
# update component parameters for each repeat
# setup some python lists for storing info about the mouse_4
mouse_4.clicked_name = []
gotValidClick = False  # until a click is received
# keep track of which components have finished
practiceReadyComponents = [practiceReadyTxt, mouse_4, nextButton_R1B]
for thisComponent in practiceReadyComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
practiceReadyClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "practiceReady"-------
while continueRoutine:
    # get current time
    t = practiceReadyClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=practiceReadyClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *practiceReadyTxt* updates
    if practiceReadyTxt.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        practiceReadyTxt.frameNStart = frameN  # exact frame index
        practiceReadyTxt.tStart = t  # local t and not account for scr refresh
        practiceReadyTxt.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(practiceReadyTxt, 'tStartRefresh')  # time at next scr refresh
        practiceReadyTxt.setAutoDraw(True)
    # *mouse_4* updates
    if mouse_4.status == NOT_STARTED and t >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        mouse_4.frameNStart = frameN  # exact frame index
        mouse_4.tStart = t  # local t and not account for scr refresh
        mouse_4.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(mouse_4, 'tStartRefresh')  # time at next scr refresh
        mouse_4.status = STARTED
        mouse_4.mouseClock.reset()
        prevButtonState = mouse_4.getPressed()  # if button is down already this ISN'T a new click
    if mouse_4.status == STARTED:  # only update if started and not finished!
        buttons = mouse_4.getPressed()
        if buttons != prevButtonState:  # button state changed?
            prevButtonState = buttons
            if sum(buttons) > 0:  # state changed to a new click
                # check if the mouse was inside our 'clickable' objects
                gotValidClick = False
                try:
                    iter(nextButton_R1B)
                    clickableList = nextButton_R1B
                except:
                    clickableList = [nextButton_R1B]
                for obj in clickableList:
                    if obj.contains(mouse_4):
                        gotValidClick = True
                        mouse_4.clicked_name.append(obj.name)
                if gotValidClick:  
                    continueRoutine = False  # abort routine on response
    
    # *nextButton_R1B* updates
    if nextButton_R1B.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        nextButton_R1B.frameNStart = frameN  # exact frame index
        nextButton_R1B.tStart = t  # local t and not account for scr refresh
        nextButton_R1B.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(nextButton_R1B, 'tStartRefresh')  # time at next scr refresh
        nextButton_R1B.setAutoDraw(True)
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in practiceReadyComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "practiceReady"-------
for thisComponent in practiceReadyComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# store data for thisExp (ExperimentHandler)
x, y = mouse_4.getPos()
buttons = mouse_4.getPressed()
if sum(buttons):
    # check if the mouse was inside our 'clickable' objects
    gotValidClick = False
    try:
        iter(nextButton_R1B)
        clickableList = nextButton_R1B
    except:
        clickableList = [nextButton_R1B]
    for obj in clickableList:
        if obj.contains(mouse_4):
            gotValidClick = True
            mouse_4.clicked_name.append(obj.name)
# the Routine "practiceReady" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

#block0 contains the practice trial. Additional practice trials can be added in.
# set up handler to look after randomisation of conditions etc
randomNum = np.random.randint(1, 3) #Only want ONE piece to be picked for practice trial. Using TrialHandler randomisation would mean all 3 picked.
block0 = data.TrialHandler(nReps=1.0, method='sequential', 
    extraInfo=expInfo, originPath=-1,
    trialList=data.importConditions(participantPath + '\practiceStimuliList.xlsx', selection=str(randomNum)),
    seed=None, name='block0')
thisBlock0 = block0.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisBlock1.rgb)
if thisBlock0 != None:
    for paramName in thisBlock0:
        exec('{} = thisBlock0[paramName]'.format(paramName))

for thisBlock0 in block0:
    trial = {}
    
    currentLoop = block0
    # abbreviate parameter names if possible (e.g. rgb = thisBlock0.rgb)
    if thisBlock0 != None:
        for paramName in thisBlock0:
            exec('{} = thisBlock0[paramName]'.format(paramName))

    # ------Prepare to start Routine "practiceTrial"-------
    continueRoutine = True

    # stimuli channels
    trial['stimuli'] = []
    # create an empty list to store the players
    players = []
    
    # create the first player for stimuli_0
    spk_name = "stimuli_0"
    trial['stimuli'].append(os.path.abspath(globals()[spk_name]))
    player = sound.Sound(globals()[spk_name])
    player.setVolume(1)  # set the volume to 1
    players.append(player)
    
    # create the rest of the players for stimuli_0
    for i in range(1, PART_2_OUT_CHANNELS):
        spk_name = f"stimuli_0"
        trial['stimuli'].append(os.path.abspath(globals()[spk_name]))
        if i < len(spk_volume):  # check if spk_volume has the correct number of elements
            player = sound.Sound(globals()[spk_name])
            player.setVolume(spk_volume[i])  # set the volume for the current speaker
        else:
            player = sound.Sound(globals()[spk_name])
            print(f"Warning: no volume specified for speaker {i}")
        players.append(player)
    
    # play the sounds and wait for them to finish
    for player in players:
        player.play()
 #   while any([player.status == PLAYING for player in players]):
  #      continue
    clickForEmotionInfo.reset()    
    valenceResp.reset()
    arousalResp.reset()
    dominanceResp.reset()
    # setup some python lists for storing info about the mouse
    mouse.clicked_name = []
    gotValidClick = False  # until a click is received
    # keep track of which components have finished
    trialComponents = [valence, valenceResp, arousal, arousalResp, dominance, dominanceResp, mouse, nextButton, clickForEmotionInfo]
    for thisComponent in trialComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    trialClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1    
    moveToPause = False #Needed so we can open an information page without skipping ahead to the next section of questions.
    goToQuestions = False
    
    # -------Run Routine "practiceTrial"-------
    while moveToPause == False:
        while continueRoutine:
            # get current time
            t = trialClock.getTime()
            tThisFlip = win.getFutureFlipTime(clock=trialClock)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            mm.out()
            
                    
            # *clickForEmotionInfo* updates
            if (clickForEmotionInfo.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance) or goToQuestions == True:
                # keep track of start time/frame for later
                clickForEmotionInfo.frameNStart = frameN  # exact frame index
                clickForEmotionInfo.tStart = t  # local t and not account for scr refresh
                clickForEmotionInfo.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(clickForEmotionInfo, 'tStartRefresh')  # time at next scr refresh
                clickForEmotionInfo.setAutoDraw(True)
            
            # *valence* updates
            if (valence.status == NOT_STARTED and tThisFlip >= PART_1_STIMULI_LEN-frameTolerance) or goToQuestions == True:
                # keep track of start time/frame for later
                valence.frameNStart = frameN  # exact frame index
                valence.tStart = t  # local t and not account for scr refresh
                valence.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(valence, 'tStartRefresh')  # time at next scr refresh
                valence.setAutoDraw(True)
            
            # *valenceResp* updates
            if (valenceResp.status == NOT_STARTED and tThisFlip >= PART_1_STIMULI_LEN-frameTolerance) or goToQuestions == True:
                # keep track of start time/frame for later
                valenceResp.frameNStart = frameN  # exact frame index
                valenceResp.tStart = t  # local t and not account for scr refresh
                valenceResp.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(valenceResp, 'tStartRefresh')  # time at next scr refresh
                valenceResp.setAutoDraw(True)
            
            # *arousal* updates
            if (arousal.status == NOT_STARTED and tThisFlip >= PART_1_STIMULI_LEN-frameTolerance) or goToQuestions == True:
                # keep track of start time/frame for later
                arousal.frameNStart = frameN  # exact frame index
                arousal.tStart = t  # local t and not account for scr refresh
                arousal.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(arousal, 'tStartRefresh')  # time at next scr refresh
                arousal.setAutoDraw(True)
            
            # *arousalResp* updates
            if (arousalResp.status == NOT_STARTED and tThisFlip >= PART_1_STIMULI_LEN-frameTolerance) or goToQuestions == True:
                # keep track of start time/frame for later
                arousalResp.frameNStart = frameN  # exact frame index
                arousalResp.tStart = t  # local t and not account for scr refresh
                arousalResp.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(arousalResp, 'tStartRefresh')  # time at next scr refresh
                arousalResp.setAutoDraw(True)
            
            # *dominance* updates
            if (dominance.status == NOT_STARTED and tThisFlip >= PART_1_STIMULI_LEN-frameTolerance) or goToQuestions == True:
                # keep track of start time/frame for later
                dominance.frameNStart = frameN  # exact frame index
                dominance.tStart = t  # local t and not account for scr refresh
                dominance.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(dominance, 'tStartRefresh')  # time at next scr refresh
                dominance.setAutoDraw(True)
            
            # *dominanceResp* updates
            if (dominanceResp.status == NOT_STARTED and tThisFlip >= PART_1_STIMULI_LEN-frameTolerance) or goToQuestions == True:
                # keep track of start time/frame for later
                dominanceResp.frameNStart = frameN  # exact frame index
                dominanceResp.tStart = t  # local t and not account for scr refresh
                dominanceResp.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(dominanceResp, 'tStartRefresh')  # time at next scr refresh
                dominanceResp.setAutoDraw(True)
            # *mouse* updates
            if mouse.status == NOT_STARTED and t >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                mouse.frameNStart = frameN  # exact frame index
                mouse.tStart = t  # local t and not account for scr refresh
                mouse.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(mouse, 'tStartRefresh')  # time at next scr refresh
                mouse.status = STARTED
                mouse.mouseClock.reset()
                prevButtonState = mouse.getPressed()  # if button is down already this ISN'T a new click
            if mouse.status == STARTED:  # only update if started and not finished!
                buttons = mouse.getPressed()
                if buttons != prevButtonState:  # button state changed?
                    prevButtonState = buttons
                    if sum(buttons) > 0:  # state changed to a new click
                        # check if the mouse was inside our 'clickable' objects
                        gotValidClick = False
                        if (nextButton.status == STARTED and valenceResp.rating and arousalResp.rating and dominanceResp.rating): #Only want the next button to be clickable if it's actually been activated!
                            try:
                                iter([nextButton, clickForEmotionInfo])
                                clickableList = [nextButton, clickForEmotionInfo]
                            except:
                                clickableList = [[nextButton, clickForEmotionInfo]]
                            for obj in clickableList:
                                if obj.contains(mouse):
                                    gotValidClick = True
                                    mouse.clicked_name.append(obj.name)
                                    if obj.name == 'nextButton':
                                        moveToPause = True
                        else:
                            try:
                                iter([clickForEmotionInfo])
                                clickableList = [clickForEmotionInfo]
                            except:
                                clickableList = [[clickForEmotionInfo]]
                            for obj in clickableList:
                                if obj.contains(mouse):
                                    gotValidClick = True
                                    mouse.clicked_name.append(obj.name)
                        if gotValidClick:  
                            continueRoutine = False  # abort routine on response
            
            # *nextButton* updates
            if (nextButton.status == NOT_STARTED and valenceResp.rating and arousalResp.rating and dominanceResp.rating) or (goToQuestions == True and valenceResp.rating and arousalResp.rating and dominanceResp.rating):
                # keep track of start time/frame for later
                nextButton.frameNStart = frameN  # exact frame index
                nextButton.tStart = t  # local t and not account for scr refresh
                nextButton.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(nextButton, 'tStartRefresh')  # time at next scr refresh
                nextButton.setAutoDraw(True)
            
            # check for quit (typically the Esc key)
            if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
                core.quit()
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in trialComponents:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        mm.stop()
        # -------Ending Routine "practiceTrial"-------
        for thisComponent in trialComponents:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
                

        # the Routine "practiceTrial" was not non-slip safe, so reset the non-slip timer
        routineTimer.reset()
        
        if moveToPause == False: #Due to a bug, this needs to be here as well.
            # ------Prepare to start Routine "Categorical_Emotions_to_VAD_Mapping"-------
            continueRoutine = True
            # update component parameters for each repeat
            # setup some python lists for storing info about the mouse_3
            mouse_3.clicked_name = []
            gotValidClick = False  # until a click is received
            # keep track of which components have finished
            Categorical_Emotions_to_VAD_MappingComponents = [Emotions_Mapping_Figure, nextButton_3, mouse_3, text_4, text_3]
            for thisComponent in Categorical_Emotions_to_VAD_MappingComponents:
                thisComponent.tStart = None
                thisComponent.tStop = None
                thisComponent.tStartRefresh = None
                thisComponent.tStopRefresh = None
                if hasattr(thisComponent, 'status'):
                    thisComponent.status = NOT_STARTED
            # reset timers
            t = 0
            _timeToFirstFrame = win.getFutureFlipTime(clock="now")
            Categorical_Emotions_to_VAD_MappingClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
            frameN = -1
            
            # -------Run Routine "Categorical_Emotions_to_VAD_Mapping"-------
            while continueRoutine:
                # get current time
                t = Categorical_Emotions_to_VAD_MappingClock.getTime()
                tThisFlip = win.getFutureFlipTime(clock=Categorical_Emotions_to_VAD_MappingClock)
                tThisFlipGlobal = win.getFutureFlipTime(clock=None)
                frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
                # update/draw components on each frame
                
                # *Emotions_Mapping_Figure* updates
                if Emotions_Mapping_Figure.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                    # keep track of start time/frame for later
                    Emotions_Mapping_Figure.frameNStart = frameN  # exact frame index
                    Emotions_Mapping_Figure.tStart = t  # local t and not account for scr refresh
                    Emotions_Mapping_Figure.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(Emotions_Mapping_Figure, 'tStartRefresh')  # time at next scr refresh
                    Emotions_Mapping_Figure.setAutoDraw(True)
                
                # *nextButton_3* updates
                if nextButton_3.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                    # keep track of start time/frame for later
                    nextButton_3.frameNStart = frameN  # exact frame index
                    nextButton_3.tStart = t  # local t and not account for scr refresh
                    nextButton_3.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(nextButton_3, 'tStartRefresh')  # time at next scr refresh
                    nextButton_3.setAutoDraw(True)
                # *mouse_3* updates
                if mouse_3.status == NOT_STARTED and t >= 0.0-frameTolerance:
                    # keep track of start time/frame for later
                    mouse_3.frameNStart = frameN  # exact frame index
                    mouse_3.tStart = t  # local t and not account for scr refresh
                    mouse_3.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(mouse_3, 'tStartRefresh')  # time at next scr refresh
                    mouse_3.status = STARTED
                    mouse_3.mouseClock.reset()
                    prevButtonState = mouse_3.getPressed()  # if button is down already this ISN'T a new click
                if mouse_3.status == STARTED:  # only update if started and not finished!
                    buttons = mouse_3.getPressed()
                    if buttons != prevButtonState:  # button state changed?
                        prevButtonState = buttons
                        if sum(buttons) > 0:  # state changed to a new click
                            # check if the mouse was inside our 'clickable' objects
                            gotValidClick = False
                            try:
                                iter([nextButton])
                                clickableList = [nextButton]
                            except:
                                clickableList = [[nextButton]]
                            for obj in clickableList:
                                if obj.contains(mouse_3):
                                    gotValidClick = True
                                    mouse_3.clicked_name.append(obj.name)
                                    goToQuestions = True
                            if gotValidClick:  
                                continueRoutine = False  # abort routine on response
                                
                # *text_3* updates
                if text_3.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                    # keep track of start time/frame for later
                    text_3.frameNStart = frameN  # exact frame index
                    text_3.tStart = t  # local t and not account for scr refresh
                    text_3.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(text_3, 'tStartRefresh')  # time at next scr refresh
                    text_3.setAutoDraw(True)
                
                # *text_4* updates
                if text_4.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                    # keep track of start time/frame for later
                    text_4.frameNStart = frameN  # exact frame index
                    text_4.tStart = t  # local t and not account for scr refresh
                    text_4.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(text_4, 'tStartRefresh')  # time at next scr refresh
                    text_4.setAutoDraw(True)
                
                # check for quit (typically the Esc key)
                if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
                    core.quit()
                
                # check if all components have finished
                if not continueRoutine:  # a component has requested a forced-end of Routine
                    break
                continueRoutine = False  # will revert to True if at least one component still running
                for thisComponent in Categorical_Emotions_to_VAD_MappingComponents:
                    if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                        continueRoutine = True
                        break  # at least one component has not yet finished
                
                # refresh the screen
                if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                    win.flip()
            
            # -------Ending Routine "Categorical_Emotions_to_VAD_Mapping"-------
            for thisComponent in Categorical_Emotions_to_VAD_MappingComponents:
                if hasattr(thisComponent, "setAutoDraw"):
                    thisComponent.setAutoDraw(False)
            # store data for thisExp (ExperimentHandler)
            x, y = mouse_3.getPos()
            buttons = mouse_3.getPressed()
            if sum(buttons):
                # check if the mouse was inside our 'clickable' objects
                gotValidClick = False
                try:
                    iter(nextButton)
                    clickableList = nextButton
                except:
                    clickableList = [nextButton]
                for obj in clickableList:
                    if obj.contains(mouse_3):
                        gotValidClick = True
                        mouse_3.clicked_name.append(obj.name)
            # the Routine "Categorical_Emotions_to_VAD_Mapping" was not non-slip safe, so reset the non-slip timer
            routineTimer.reset()
            continueRoutine = True
    
    
    # ------Prepare to start Routine "interTrialPause"-------
    continueRoutine = True
    # update component parameters for each repeat
    # keep track of which components have finished
    interTrialPauseComponents = [interTrialPauseText, mouse_4, nextButton_R1B]
    for thisComponent in interTrialPauseComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    interTrialPauseClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
# -------Run Routine "interTrialPause"-------
    while continueRoutine:
        # get current time
        t = interTrialPauseClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=interTrialPauseClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        if interTrialPauseText.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            interTrialPauseText.frameNStart = frameN  # exact frame index
            interTrialPauseText.tStart = t  # local t and not account for scr refresh
            interTrialPauseText.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(interTrialPauseText, 'tStartRefresh')  # time at next scr refresh
            interTrialPauseText.setAutoDraw(True)        
        # *mouse_4* updates
        if mouse_4.status == NOT_STARTED and t >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            mouse_4.frameNStart = frameN  # exact frame index
            mouse_4.tStart = t  # local t and not account for scr refresh
            mouse_4.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(mouse_4, 'tStartRefresh')  # time at next scr refresh
            mouse_4.status = STARTED
            mouse_4.mouseClock.reset()
            prevButtonState = mouse_4.getPressed()  # if button is down already this ISN'T a new click
        if mouse_4.status == STARTED:  # only update if started and not finished!
            buttons = mouse_4.getPressed()
            if buttons != prevButtonState:  # button state changed?
                prevButtonState = buttons
                if sum(buttons) > 0:  # state changed to a new click
                    # check if the mouse was inside our 'clickable' objects
                    gotValidClick = False
                    try:
                        iter(nextButton_R1B)
                        clickableList = nextButton_R1B
                    except:
                        clickableList = [nextButton_R1B]
                    for obj in clickableList:
                        if obj.contains(mouse_4):
                            gotValidClick = True
                            mouse_4.clicked_name.append(obj.name)
                    if gotValidClick:  
                        continueRoutine = False  # abort routine on response
        
        # *nextButton_R1B* updates
        if nextButton_R1B.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            nextButton_R1B.frameNStart = frameN  # exact frame index
            nextButton_R1B.tStart = t  # local t and not account for scr refresh
            nextButton_R1B.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(nextButton_R1B, 'tStartRefresh')  # time at next scr refresh
            nextButton_R1B.setAutoDraw(True)
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in interTrialPauseComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
        
    # -------Ending Routine "interTrialPause"-------
    for thisComponent in interTrialPauseComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # store data for thisExp (ExperimentHandler)
    x, y = mouse_4.getPos()
    buttons = mouse_4.getPressed()
    if sum(buttons):
        # check if the mouse was inside our 'clickable' objects
        gotValidClick = False
        try:
            iter(nextButton_R1B)
            clickableList = nextButton_R1B
        except:
            clickableList = [nextButton_R1B]
        for obj in clickableList:
            if obj.contains(mouse_4):
                gotValidClick = True
                mouse_4.clicked_name.append(obj.name)
    # the Routine "interTrialPause" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
        
# completed 1.0 repeats of 'block0'


# playing part starting trig
continueRoutine = True
routineTimer.add(1)
startExpTrigger = SfPlayer('start_trigger.wav')
for i in range(PART_1_OUT_CHANNELS):
    mm.delInput(i)
mm.addInput(0, startExpTrigger)
for i in range(PART_1_OUT_CHANNELS):
    mm.setAmp(0,i,0)
mm.setAmp(0,0,spk_volume[0])
while continueRoutine and routineTimer.getTime() > 0:
    mm.out()
mm.stop()
routineTimer.reset()
# end of playing part starting trig


# set up handler to look after randomisation of conditions etc
block1 = data.TrialHandler(nReps=1.0, method='random', 
    extraInfo=expInfo, originPath=-1,
    trialList=data.importConditions(participantPath + '\stimuliList.xlsx', selection='0:15'),
    seed=None, name='block1')
thisExp.addLoop(block1)  # add the loop to the experiment
thisBlock1 = block1.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisBlock1.rgb)
if thisBlock1 != None:
    for paramName in thisBlock1:
        exec('{} = thisBlock1[paramName]'.format(paramName))

idx = 0
for thisBlock1 in block1:
    trial = {}
    idx += 1
    print(f'Not counting the practice trial, this is trial {idx}')
    currentLoop = block1
    # abbreviate parameter names if possible (e.g. rgb = thisBlock1.rgb)
    if thisBlock1 != None:
        for paramName in thisBlock1:
            exec('{} = thisBlock1[paramName]'.format(paramName))

    # ------Prepare to start Routine "trial"-------
    continueRoutine = True
    # update component parameters for each repeat
    print(f'trigger: {trigger}')

    trigger_filename, trigger_ext = os.path.splitext(trigger)
    trigger_logfile = os.path.abspath(trigger_filename + '.txt')
    trial['trigger'] = os.path.abspath(trigger)
    trial['trigger_log'] = os.path.abspath(trigger_logfile)

    # trigger channel
    trigger_chn = SfPlayer(trigger)
    mm.delInput(0)
    mm.addInput(0, trigger_chn)
    # stimuli channels
    trial['stimuli'] = []
    # create an empty list to store the players
    players = []
    
    # create the first player for stimuli_0
    spk_name = "stimuli_0"
    trial['stimuli'].append(os.path.abspath(globals()[spk_name]))
    player = sound.Sound(globals()[spk_name])
    player.setVolume(1)  # set the volume to 1
    players.append(player)
    
    # create the rest of the players for stimuli_0
    for i in range(1, PART_2_OUT_CHANNELS):
        spk_name = f"stimuli_0"
        trial['stimuli'].append(os.path.abspath(globals()[spk_name]))
        if i < len(spk_volume):  # check if spk_volume has the correct number of elements
            player = sound.Sound(globals()[spk_name])
            player.setVolume(spk_volume[i])  # set the volume for the current speaker
        else:
            player = sound.Sound(globals()[spk_name])
            print(f"Warning: no volume specified for speaker {i}")
        players.append(player)
    
    # play the sounds and wait for them to finish
    for player in players:
        player.play()
 #   while any([player.status == PLAYING for player in players]):
  #      continue
        
    clickForEmotionInfo.reset()    
    valenceResp.reset()
    arousalResp.reset()
    dominanceResp.reset()
    # setup some python lists for storing info about the mouse
    mouse.clicked_name = []
    gotValidClick = False  # until a click is received
    # keep track of which components have finished
    trialComponents = [valence, valenceResp, arousal, arousalResp, dominance, dominanceResp, mouse, nextButton, clickForEmotionInfo]
    for thisComponent in trialComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    trialClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1    

    moveToPause = False #Needed so we can open an information page without skipping ahead to the next section of questions.
    goToQuestions = False
    
    # -------Run Routine "trial"-------
    while moveToPause == False:
        while continueRoutine:
            # get current time
            t = trialClock.getTime()
            tThisFlip = win.getFutureFlipTime(clock=trialClock)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            mm.out()
            
            # *clickForEmotionInfo* updates
            if (clickForEmotionInfo.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance) or goToQuestions == True:
                # keep track of start time/frame for later
                clickForEmotionInfo.frameNStart = frameN  # exact frame index
                clickForEmotionInfo.tStart = t  # local t and not account for scr refresh
                clickForEmotionInfo.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(clickForEmotionInfo, 'tStartRefresh')  # time at next scr refresh
                clickForEmotionInfo.setAutoDraw(True)
            
            # *valence* updates
            if (valence.status == NOT_STARTED and tThisFlip >= PART_1_STIMULI_LEN-frameTolerance) or goToQuestions == True:
                # keep track of start time/frame for later
                valence.frameNStart = frameN  # exact frame index
                valence.tStart = t  # local t and not account for scr refresh
                valence.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(valence, 'tStartRefresh')  # time at next scr refresh
                valence.setAutoDraw(True)
            
            # *valenceResp* updates
            if (valenceResp.status == NOT_STARTED and tThisFlip >= PART_1_STIMULI_LEN-frameTolerance) or goToQuestions == True:
                # keep track of start time/frame for later
                valenceResp.frameNStart = frameN  # exact frame index
                valenceResp.tStart = t  # local t and not account for scr refresh
                valenceResp.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(valenceResp, 'tStartRefresh')  # time at next scr refresh
                valenceResp.setAutoDraw(True)
            
            # *arousal* updates
            if (arousal.status == NOT_STARTED and tThisFlip >= PART_1_STIMULI_LEN-frameTolerance) or goToQuestions == True:
                # keep track of start time/frame for later
                arousal.frameNStart = frameN  # exact frame index
                arousal.tStart = t  # local t and not account for scr refresh
                arousal.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(arousal, 'tStartRefresh')  # time at next scr refresh
                arousal.setAutoDraw(True)
            
            # *arousalResp* updates
            if (arousalResp.status == NOT_STARTED and tThisFlip >= PART_1_STIMULI_LEN-frameTolerance) or goToQuestions == True:
                # keep track of start time/frame for later
                arousalResp.frameNStart = frameN  # exact frame index
                arousalResp.tStart = t  # local t and not account for scr refresh
                arousalResp.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(arousalResp, 'tStartRefresh')  # time at next scr refresh
                arousalResp.setAutoDraw(True)
            
            # *dominance* updates
            if (dominance.status == NOT_STARTED and tThisFlip >= PART_1_STIMULI_LEN-frameTolerance) or goToQuestions == True:
                # keep track of start time/frame for later
                dominance.frameNStart = frameN  # exact frame index
                dominance.tStart = t  # local t and not account for scr refresh
                dominance.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(dominance, 'tStartRefresh')  # time at next scr refresh
                dominance.setAutoDraw(True)
            
            # *dominanceResp* updates
            if (dominanceResp.status == NOT_STARTED and tThisFlip >= PART_1_STIMULI_LEN-frameTolerance) or goToQuestions == True:
                # keep track of start time/frame for later
                dominanceResp.frameNStart = frameN  # exact frame index
                dominanceResp.tStart = t  # local t and not account for scr refresh
                dominanceResp.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(dominanceResp, 'tStartRefresh')  # time at next scr refresh
                dominanceResp.setAutoDraw(True)
            # *mouse* updates
            if mouse.status == NOT_STARTED and t >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                mouse.frameNStart = frameN  # exact frame index
                mouse.tStart = t  # local t and not account for scr refresh
                mouse.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(mouse, 'tStartRefresh')  # time at next scr refresh
                mouse.status = STARTED
                mouse.mouseClock.reset()
                prevButtonState = mouse.getPressed()  # if button is down already this ISN'T a new click
            if mouse.status == STARTED:  # only update if started and not finished!
                buttons = mouse.getPressed()
                if buttons != prevButtonState:  # button state changed?
                    prevButtonState = buttons
                    if sum(buttons) > 0:  # state changed to a new click
                        # check if the mouse was inside our 'clickable' objects
                        gotValidClick = False
                        if (nextButton.status == STARTED and valenceResp.rating and arousalResp.rating and dominanceResp.rating): #Only want the next button to be clickable if it's actually been activated!
                            try:
                                iter([nextButton, clickForEmotionInfo])
                                clickableList = [nextButton, clickForEmotionInfo]
                            except:
                                clickableList = [[nextButton, clickForEmotionInfo]]
                            for obj in clickableList:
                                if obj.contains(mouse):
                                    gotValidClick = True
                                    mouse.clicked_name.append(obj.name)
                                    if obj.name == 'nextButton':
                                        moveToPause = True
                        else:
                            try:
                                iter([clickForEmotionInfo])
                                clickableList = [clickForEmotionInfo]
                            except:
                                clickableList = [[clickForEmotionInfo]]
                            for obj in clickableList:
                                if obj.contains(mouse):
                                    gotValidClick = True
                                    mouse.clicked_name.append(obj.name)
                        if gotValidClick:  
                            continueRoutine = False  # abort routine on response
            
            # *nextButton* updates
            if (nextButton.status == NOT_STARTED and valenceResp.rating and arousalResp.rating and dominanceResp.rating) or (goToQuestions == True and valenceResp.rating and arousalResp.rating and dominanceResp.rating):
                # keep track of start time/frame for later
                nextButton.frameNStart = frameN  # exact frame index
                nextButton.tStart = t  # local t and not account for scr refresh
                nextButton.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(nextButton, 'tStartRefresh')  # time at next scr refresh
                nextButton.setAutoDraw(True)
            
            # check for quit (typically the Esc key)
            if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
                core.quit()
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in trialComponents:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        mm.stop()
        jsondata['trial_number'] = len(jsondata['trials'])
        # save json file
        with open(jsonfilename, 'w') as fp:
            json.dump(jsondata, fp, separators=(',\n', ': '))
            fp.close()
        # -------Ending Routine "trial"-------
        for thisComponent in trialComponents:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        
        block1.addData('valenceResp.response', valenceResp.getRating())
        block1.addData('arousalResp.response', arousalResp.getRating())
        block1.addData('dominanceResp.response', dominanceResp.getRating())
        thisExp.nextEntry() #Next row on the record.
        # store data for block1 (TrialHandler)
        x, y = mouse.getPos()
        buttons = mouse.getPressed()
        if sum(buttons):
            # check if the mouse was inside our 'clickable' objects
            gotValidClick = False
            if (nextButton.status == STARTED and valenceResp.rating and arousalResp.rating and dominanceResp.rating): #Only want the next button to be clickable if it's actually been activated!
                try:
                    iter([nextButton, clickForEmotionInfo])
                    clickableList = [nextButton, clickForEmotionInfo]
                except:
                    clickableList = [[nextButton, clickForEmotionInfo]]
                for obj in clickableList:
                    if obj.contains(mouse):
                        gotValidClick = True
                        mouse.clicked_name.append(obj.name)
            else:
                try:
                    iter([clickForEmotionInfo])
                    clickableList = [clickForEmotionInfo]
                except:
                    clickableList = [[clickForEmotionInfo]]
                for obj in clickableList:
                    if obj.contains(mouse):
                        gotValidClick = True
                        mouse.clicked_name.append(obj.name)
        # the Routine "trial" was not non-slip safe, so reset the non-slip timer
        routineTimer.reset()
        
        if moveToPause == False: #Due to a bug, this needs to be here as well.
            # ------Prepare to start Routine "Categorical_Emotions_to_VAD_Mapping"-------
            continueRoutine = True
            # update component parameters for each repeat
            # setup some python lists for storing info about the mouse_3
            mouse_3.clicked_name = []
            gotValidClick = False  # until a click is received
            # keep track of which components have finished
            Categorical_Emotions_to_VAD_MappingComponents = [Emotions_Mapping_Figure, nextButton_3, mouse_3, text_4, text_3]
            for thisComponent in Categorical_Emotions_to_VAD_MappingComponents:
                thisComponent.tStart = None
                thisComponent.tStop = None
                thisComponent.tStartRefresh = None
                thisComponent.tStopRefresh = None
                if hasattr(thisComponent, 'status'):
                    thisComponent.status = NOT_STARTED
            # reset timers
            t = 0
            _timeToFirstFrame = win.getFutureFlipTime(clock="now")
            Categorical_Emotions_to_VAD_MappingClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
            frameN = -1
            
            # -------Run Routine "Categorical_Emotions_to_VAD_Mapping"-------
            while continueRoutine:
                # get current time
                t = Categorical_Emotions_to_VAD_MappingClock.getTime()
                tThisFlip = win.getFutureFlipTime(clock=Categorical_Emotions_to_VAD_MappingClock)
                tThisFlipGlobal = win.getFutureFlipTime(clock=None)
                frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
                # update/draw components on each frame
                
                # *Emotions_Mapping_Figure* updates
                if Emotions_Mapping_Figure.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                    # keep track of start time/frame for later
                    Emotions_Mapping_Figure.frameNStart = frameN  # exact frame index
                    Emotions_Mapping_Figure.tStart = t  # local t and not account for scr refresh
                    Emotions_Mapping_Figure.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(Emotions_Mapping_Figure, 'tStartRefresh')  # time at next scr refresh
                    Emotions_Mapping_Figure.setAutoDraw(True)
                
                # *nextButton_3* updates
                if nextButton_3.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                    # keep track of start time/frame for later
                    nextButton_3.frameNStart = frameN  # exact frame index
                    nextButton_3.tStart = t  # local t and not account for scr refresh
                    nextButton_3.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(nextButton_3, 'tStartRefresh')  # time at next scr refresh
                    nextButton_3.setAutoDraw(True)
                # *mouse_3* updates
                if mouse_3.status == NOT_STARTED and t >= 0.0-frameTolerance:
                    # keep track of start time/frame for later
                    mouse_3.frameNStart = frameN  # exact frame index
                    mouse_3.tStart = t  # local t and not account for scr refresh
                    mouse_3.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(mouse_3, 'tStartRefresh')  # time at next scr refresh
                    mouse_3.status = STARTED
                    mouse_3.mouseClock.reset()
                    prevButtonState = mouse_3.getPressed()  # if button is down already this ISN'T a new click
                if mouse_3.status == STARTED:  # only update if started and not finished!
                    buttons = mouse_3.getPressed()
                    if buttons != prevButtonState:  # button state changed?
                        prevButtonState = buttons
                        if sum(buttons) > 0:  # state changed to a new click
                            # check if the mouse was inside our 'clickable' objects
                            gotValidClick = False
                            try:
                                iter([nextButton])
                                clickableList = [nextButton]
                            except:
                                clickableList = [[nextButton]]
                            for obj in clickableList:
                                if obj.contains(mouse_3):
                                    gotValidClick = True
                                    mouse_3.clicked_name.append(obj.name)
                                    goToQuestions = True
                            if gotValidClick:  
                                continueRoutine = False  # abort routine on response
                                
                # *text_3* updates
                if text_3.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                    # keep track of start time/frame for later
                    text_3.frameNStart = frameN  # exact frame index
                    text_3.tStart = t  # local t and not account for scr refresh
                    text_3.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(text_3, 'tStartRefresh')  # time at next scr refresh
                    text_3.setAutoDraw(True)
                
                # *text_4* updates
                if text_4.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                    # keep track of start time/frame for later
                    text_4.frameNStart = frameN  # exact frame index
                    text_4.tStart = t  # local t and not account for scr refresh
                    text_4.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(text_4, 'tStartRefresh')  # time at next scr refresh
                    text_4.setAutoDraw(True)
                
                # check for quit (typically the Esc key)
                if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
                    core.quit()
                
                # check if all components have finished
                if not continueRoutine:  # a component has requested a forced-end of Routine
                    break
                continueRoutine = False  # will revert to True if at least one component still running
                for thisComponent in Categorical_Emotions_to_VAD_MappingComponents:
                    if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                        continueRoutine = True
                        break  # at least one component has not yet finished
                
                # refresh the screen
                if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                    win.flip()
            
            # -------Ending Routine "Categorical_Emotions_to_VAD_Mapping"-------
            for thisComponent in Categorical_Emotions_to_VAD_MappingComponents:
                if hasattr(thisComponent, "setAutoDraw"):
                    thisComponent.setAutoDraw(False)
            # store data for thisExp (ExperimentHandler)
            x, y = mouse_3.getPos()
            buttons = mouse_3.getPressed()
            if sum(buttons):
                # check if the mouse was inside our 'clickable' objects
                gotValidClick = False
                try:
                    iter(nextButton)
                    clickableList = nextButton
                except:
                    clickableList = [nextButton]
                for obj in clickableList:
                    if obj.contains(mouse_3):
                        gotValidClick = True
                        mouse_3.clicked_name.append(obj.name)
            # the Routine "Categorical_Emotions_to_VAD_Mapping" was not non-slip safe, so reset the non-slip timer
            routineTimer.reset()
            continueRoutine = True
            
            
    # ------Prepare to start Routine "interTrialPause"-------
    continueRoutine = True
    # update component parameters for each repeat
    # keep track of which components have finished
    interTrialPauseComponents = [interTrialPauseText, mouse_4, nextButton_R1B]
    for thisComponent in interTrialPauseComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    interTrialPauseClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
# -------Run Routine "interTrialPause"-------
    while continueRoutine:
        # get current time
        t = interTrialPauseClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=interTrialPauseClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        if interTrialPauseText.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            interTrialPauseText.frameNStart = frameN  # exact frame index
            interTrialPauseText.tStart = t  # local t and not account for scr refresh
            interTrialPauseText.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(interTrialPauseText, 'tStartRefresh')  # time at next scr refresh
            interTrialPauseText.setAutoDraw(True)        
        # *mouse_4* updates
        if mouse_4.status == NOT_STARTED and t >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            mouse_4.frameNStart = frameN  # exact frame index
            mouse_4.tStart = t  # local t and not account for scr refresh
            mouse_4.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(mouse_4, 'tStartRefresh')  # time at next scr refresh
            mouse_4.status = STARTED
            mouse_4.mouseClock.reset()
            prevButtonState = mouse_4.getPressed()  # if button is down already this ISN'T a new click
        if mouse_4.status == STARTED:  # only update if started and not finished!
            buttons = mouse_4.getPressed()
            if buttons != prevButtonState:  # button state changed?
                prevButtonState = buttons
                if sum(buttons) > 0:  # state changed to a new click
                    # check if the mouse was inside our 'clickable' objects
                    gotValidClick = False
                    try:
                        iter(nextButton_R1B)
                        clickableList = nextButton_R1B
                    except:
                        clickableList = [nextButton_R1B]
                    for obj in clickableList:
                        if obj.contains(mouse_4):
                            gotValidClick = True
                            mouse_4.clicked_name.append(obj.name)
                    if gotValidClick:  
                        continueRoutine = False  # abort routine on response
        
        # *nextButton_R1B* updates
        if nextButton_R1B.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            nextButton_R1B.frameNStart = frameN  # exact frame index
            nextButton_R1B.tStart = t  # local t and not account for scr refresh
            nextButton_R1B.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(nextButton_R1B, 'tStartRefresh')  # time at next scr refresh
            nextButton_R1B.setAutoDraw(True)
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in interTrialPauseComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
        
    # -------Ending Routine "interTrialPause"-------
    for thisComponent in interTrialPauseComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # store data for thisExp (ExperimentHandler)
    x, y = mouse_4.getPos()
    buttons = mouse_4.getPressed()
    if sum(buttons):
        # check if the mouse was inside our 'clickable' objects
        gotValidClick = False
        try:
            iter(nextButton_R1B)
            clickableList = nextButton_R1B
        except:
            clickableList = [nextButton_R1B]
        for obj in clickableList:
            if obj.contains(mouse_4):
                gotValidClick = True
                mouse_4.clicked_name.append(obj.name)
    # the Routine "interTrialPause" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
        
# completed 1.0 repeats of 'block1'

# playing part stop trig
continueRoutine = True
routineTimer.add(1)
stopExpTrigger = SfPlayer('stop_trigger.wav')
mm.delInput(0)
mm.addInput(0, stopExpTrigger)
for i in range(PART_1_OUT_CHANNELS):
    mm.setAmp(0,i,0)
mm.setAmp(0,0,spk_volume[0])
while continueRoutine and routineTimer.getTime() > 0:
    mm.out()
mm.stop()
routineTimer.reset()
thisExp.nextEntry()
# End of playing part stop trig

# Flip one final time so any remaining win.callOnFlip() 
# and win.timeOnFlip() tasks get executed before quitting
win.flip()

#Save csv of data:
thisExp.saveAsWideText(filename+'.csv', delim='auto')
thisExp.saveAsPickle(filename)
logging.flush()

# make sure everything is closed down
if eyetracker:
    eyetracker.setConnectionState(False)
thisExp.abort()  # or data files will save again on exit
win.close()
core.quit()