#!/usr/bin/env python
# -*- coding: utf-8 -*-

from psychopy import locale_setup
from psychopy import prefs
from psychopy import sound, gui, visual, core, data, event, logging, clock, colors, layout
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
import json


sys.path.append('.')
from constants import *

SOUNDCARD_DEVICE_NAME = 'DAC8PRO'
volume_level = 0.009
volume_ratio = [1, 1, 27.5]
spk_volume = [x * volume_level for x in volume_ratio]
PART_2_OUT_CHANNELS = 3
TRIGGER_CHN = 2
print(f'PART_2_OUT_CHANNELS: {PART_2_OUT_CHANNELS}')

s = Server(nchnls=PART_2_OUT_CHANNELS, duplex=0)
devices = pa_get_output_devices()
for name in devices[0]:
    if SOUNDCARD_DEVICE_NAME in name:
        soundcard_idx = devices[1][devices[0].index(name)]
   #     print('sound card: ', name)
        s.setOutputDevice(soundcard_idx)
        break

s = s.boot()
s.start()

chns = [None]*(PART_2_OUT_CHANNELS-1)
mm = Mixer(outs=PART_2_OUT_CHANNELS)

# Ensure that relative paths start from the same directory as this script
_thisDir = os.path.dirname(os.path.abspath(__file__))
os.chdir(_thisDir)
# Store info about the experiment session
psychopyVersion = '2022.1.3'
expName = 'Part 2'  # from the Builder filename that created this script
expInfo = {'participant': ''}
dlg = gui.DlgFromDict(dictionary=expInfo, sortKeys=False, title=expName)
if dlg.OK == False:
    core.quit()  # user pressed cancel
expInfo['date'] = data.getDateStr()  # add a simple timestamp
expInfo['expName'] = expName

# Data file name stem = absolute path + name; later add .psyexp, .csv, .log, etc
participantPath = _thisDir + '/Data/' + expInfo['participant'] #participantPath also used for locating stimuli lists for this particular participant.
filename = participantPath + '/Part 2 Data'
jsonfilename = filename + '_oddballStimuli.json'
jsondata = {}
jsondata['trials'] = []

# An ExperimentHandler isn't essential but helps with data saving
thisExp = data.ExperimentHandler(name=expName,
    extraInfo=expInfo, runtimeInfo=None,
    originPath= _thisDir + '/Part 2 Script.py',
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
    winType='pyglet', allowGUI=True, allowStencil=False,
    monitor='otherExternalMonitor', color=[-0.4510, 0.0196, 0.4118], colorSpace='rgb',
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
top_instr_txt = visual.TextStim(win=win, name='top_instr_txt',
    text='You will hear three instruments playing together, from different directions. You will be asked to focus on one.\n\nThey will play to remind you what they sound like. After a pause they will repeat, this time with 1-3 oddballs per instrument - close your eyes and try not to move during this. Count the attended instrument\'s oddballs. You will be asked how many you heard, before a break.\n\nIf you have any questions at all please ask the experimenters.',
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
trialClock = core.Clock()
attendVibraphoneNote = visual.TextStim(win=win, name='attendVibraphoneNote',
    text='Attend to the vibraphone (left)\n',
    font='Open Sans',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);
attendHarmonicaNote = visual.TextStim(win=win, name='attendHarmonicaNote',
    text='Attend to the harmonica (centre)\n',
    font='Open Sans',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-1.0);
attendKeyboardNote = visual.TextStim(win=win, name='attendKeyboardNote',
    text='Attend to the keyboard (right)\n',
    font='Open Sans',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-1.0);

# Initialize components for Routine "QuestionBreakPause"
QuestionBreakPauseClock = core.Clock()
oddballsQuestion = visual.TextStim(win=win, name='oddballsQuestion',
    text='How many oddballs did you hear?',
    font='Open Sans',
    pos=(0, 0.15), height=0.05, wrapWidth=1.8, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0); 
oddballsResp = visual.TextBox2(
     win, text=None, font='Open Sans',
     pos=(0.0, 0.01),     letterHeight=0.025,
     size=(0.3, 0.04), borderWidth=2.0,
     color='Black', colorSpace='rgb',
     opacity=None,
     bold=False, italic=False,
     lineSpacing=1.0,
     padding=0.0, alignment='center',
     anchor='center',
     fillColor='White', borderColor='Black',
     flipHoriz=False, flipVert=False, languageStyle='LTR',
     editable=True,
     name='oddballsResp',
     autoLog=True,
)
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

# Initialize components for Routine "CorrectAnswerFeedback"
CorrectAnswerFeedbackClock = core.Clock()
CorrectAnswerFeedbackTxt = visual.TextStim(win=win, name='readyTxt',
    text='Correct!\n\nWhen you are ready for the next trial, click "NEXT".',
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

# Initialize components for Routine "IncorrectAnswerFeedback"
IncorrectAnswerFeedbackClock = core.Clock()
IncorrectAnswerFeedbackTxt = visual.TextStim(win=win, name='readyTxt',
    text='Incorrect- better luck next time.\n\nWhen you are ready for the next trial, click "NEXT".',
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

# Initialize components for Routine "thisPartComplete"
thisPartCompleteClock = core.Clock()
thisPartCompleteText = visual.TextStim(win=win, name='thisPartCompleteText',
    text='Part 2 completed.',
    font='Open Sans',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);
    
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
instructionsComponents = [top_instr_txt, mouse_2, nextButton_instruct]
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
    
    # *top_instr_txt* updates
    if top_instr_txt.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        top_instr_txt.frameNStart = frameN  # exact frame index
        top_instr_txt.tStart = t  # local t and not account for scr refresh
        top_instr_txt.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(top_instr_txt, 'tStartRefresh')  # time at next scr refresh
        top_instr_txt.setAutoDraw(True)
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
        if attendVibraphoneNote != FINISHED and attendHarmonicaNote != FINISHED and attendKeyboardNote:
            continueRoutine = True
            break  # if none have finished
    
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

#Practice trial:
# set up handler to look after randomisation of conditions etc
randomNum = np.random.randint(1, 3) #Only want ONE piece to be picked for practice trial. Using TrialHandler randomisation would mean all 3 picked.
block0 = data.TrialHandler(nReps=1.0, method='sequential', 
    extraInfo=expInfo, originPath=-1,
    trialList=data.importConditions(participantPath + '\practiceOddballStimuliList.xlsx', selection=str(randomNum)),
    seed=None, name='block0')
thisBlock0 = block0.trialList[0]  # so we can initialise stimuli with some values

# abbreviate parameter names if possible (e.g. rgb = thisBlock0.rgb)
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
    
    # update stimuliStarted parameter for each repeat
    stimuliStarted = False
    
    # keep track of which components have finished
    trialComponents = [attendVibraphoneNote, attendHarmonicaNote, attendKeyboardNote]
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
    
    # -------Run Routine "practiceTrial"-------
    while continueRoutine:
        # get current time
        t = trialClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=trialClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        attendedInst = f'{attendedInst}' #Setting the attended instrument, from the column in oddballStimuliList.xlsx
        
        # *attendVibraphoneNote* updates
        if attendedInst == 'Vibr' and attendVibraphoneNote.status == NOT_STARTED:
            # keep track of start time/frame for later
            attendVibraphoneNote.frameNStart = frameN  # exact frame index
            attendVibraphoneNote.tStart = t  # local t and not account for scr refresh
            attendVibraphoneNote.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(attendVibraphoneNote, 'tStartRefresh')  # time at next scr refresh
            attendVibraphoneNote.setAutoDraw(True)
        if attendVibraphoneNote.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > attendVibraphoneNote.tStartRefresh + 5.0-frameTolerance:
                # keep track of stop time/frame for later
                attendVibraphoneNote.tStop = t  # not accounting for scr refresh
                attendVibraphoneNote.frameNStop = frameN  # exact frame index
                win.timeOnFlip(attendVibraphoneNote, 'tStopRefresh')  # time at next scr refresh
                attendVibraphoneNote.setAutoDraw(False)
        
        # *attendHarmonicaNote* updates
        if attendedInst == 'Harm' and attendHarmonicaNote.status == NOT_STARTED:
            # keep track of start time/frame for later
            attendHarmonicaNote.frameNStart = frameN  # exact frame index
            attendHarmonicaNote.tStart = t  # local t and not account for scr refresh
            attendHarmonicaNote.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(attendHarmonicaNote, 'tStartRefresh')  # time at next scr refresh
            attendHarmonicaNote.setAutoDraw(True)
        if attendHarmonicaNote.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > attendHarmonicaNote.tStartRefresh + 5.0-frameTolerance:
                # keep track of stop time/frame for later
                attendHarmonicaNote.tStop = t  # not accounting for scr refresh
                attendHarmonicaNote.frameNStop = frameN  # exact frame index
                win.timeOnFlip(attendHarmonicaNote, 'tStopRefresh')  # time at next scr refresh
                attendHarmonicaNote.setAutoDraw(False)
        
                # *attendKeyboardNote* updates
        if attendedInst == 'Keyb' and attendKeyboardNote.status == NOT_STARTED:
            # keep track of start time/frame for later
            attendKeyboardNote.frameNStart = frameN  # exact frame index
            attendKeyboardNote.tStart = t  # local t and not account for scr refresh
            attendKeyboardNote.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(attendKeyboardNote, 'tStartRefresh')  # time at next scr refresh
            attendKeyboardNote.setAutoDraw(True)
        if attendKeyboardNote.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > attendKeyboardNote.tStartRefresh + 5.0-frameTolerance:
                # keep track of stop time/frame for later
                attendKeyboardNote.tStop = t  # not accounting for scr refresh
                attendKeyboardNote.frameNStop = frameN  # exact frame index
                win.timeOnFlip(attendKeyboardNote, 'tStopRefresh')  # time at next scr refresh
                attendKeyboardNote.setAutoDraw(False)
        
        if stimuliStarted == False and (attendVibraphoneNote.status == FINISHED or attendHarmonicaNote.status == FINISHED or attendKeyboardNote.status == FINISHED):
            
            trial['stimuli'] = []
            # create an empty list to store the players
            players = []
            
            # create the first player for stimuli_0
        #        spk_name = "stimuli_0"
        #    trial['stimuli'].append(os.path.abspath(globals()[spk_name]))
         #   player = sound.Sound(globals()[spk_name])
          #  player.setVolume(0.05)  # set the volume to 1
           # players.append(player)
            
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
        
            stimuliStarted = True
            
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
        
        if tThisFlip >= PART_2_STIMULI_LEN+5.0-frameTolerance:
            continueRoutine = False
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()            
    mm.stop()

    # -------Ending Routine "practiceTrial"-------
    for thisComponent in trialComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    
    if attendedInst == 'Vibr':
        block0.addData('attendedInst', 'Vibr')
        print("Vibraphone was attended.")
    elif attendedInst == 'Harm':
        block0.addData('attendedInst', 'Harm')
        print("Harmonica was attended.")
    elif attendedInst == 'Keyb':
        block0.addData('attendedInst', 'Keyb')
        print("Keyboard was attended.")
    # the Routine "trial" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # ------Prepare to start Routine "QuestionBreakPause"-------
    continueRoutine = True
    # update component parameters for each repeat
    # setup some python lists for storing info about the mouse_4
    mouse_4.clicked_name = []
    gotValidClick = False  # until a click is received
    # keep track of which components have finished
    QuestionBreakPauseComponents = [oddballsQuestion, oddballsResp, mouse_4, nextButton_R1B]
    for thisComponent in QuestionBreakPauseComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    QuestionBreakPauseClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1

    # -------Run Routine "QuestionBreakPause"-------
    while continueRoutine:
        # get current time
        t = QuestionBreakPauseClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=QuestionBreakPauseClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *oddballsQuestion* updates
        if oddballsQuestion.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            oddballsQuestion.frameNStart = frameN  # exact frame index
            oddballsQuestion.tStart = t  # local t and not account for scr refresh
            oddballsQuestion.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(oddballsQuestion, 'tStartRefresh')  # time at next scr refresh
            oddballsQuestion.setAutoDraw(True)        
        # *oddballsResp* updates
        if oddballsResp.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            oddballsResp.frameNStart = frameN  # exact frame index
            oddballsResp.tStart = t  # local t and not account for scr refresh
            oddballsResp.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(oddballsResp, 'tStartRefresh')  # time at next scr refresh
            oddballsResp.setAutoDraw(True)
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
        for thisComponent in QuestionBreakPauseComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "QuestionBreakPause"-------
    for thisComponent in QuestionBreakPauseComponents:
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
                
    oddballsMinusResp = float(f'{attendedOddballs}') - float(oddballsResp.text)
    oddballsResp.reset()
    # the Routine "QuestionBreakPause" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()

    ##FEEDBACK:
    if oddballsMinusResp == 0:
    
        # ------Prepare to start Routine "CorrectAnswerFeedback"-------
        continueRoutine = True
        # update component parameters for each repeat
        # setup some python lists for storing info about the mouse_4
        mouse_4.clicked_name = []
        gotValidClick = False  # until a click is received
        # keep track of which components have finished
        CorrectAnswerFeedbackComponents = [CorrectAnswerFeedbackTxt, mouse_4, nextButton_R1B]
        for thisComponent in CorrectAnswerFeedbackComponents:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        # reset timers
        t = 0
        _timeToFirstFrame = win.getFutureFlipTime(clock="now")
        CorrectAnswerFeedbackClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
        frameN = -1

    # -------Run Routine "CorrectAnswerFeedback"-------
        while continueRoutine:
            # get current time
            t = CorrectAnswerFeedbackClock.getTime()
            tThisFlip = win.getFutureFlipTime(clock=CorrectAnswerFeedbackClock)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *oddballsQuestion* updates
            if CorrectAnswerFeedbackTxt.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                CorrectAnswerFeedbackTxt.frameNStart = frameN  # exact frame index
                CorrectAnswerFeedbackTxt.tStart = t  # local t and not account for scr refresh
                CorrectAnswerFeedbackTxt.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(CorrectAnswerFeedbackTxt, 'tStartRefresh')  # time at next scr refresh
                CorrectAnswerFeedbackTxt.setAutoDraw(True)        
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
            for thisComponent in CorrectAnswerFeedbackComponents:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # -------Ending Routine "CorrectAnswerFeedback"-------
        for thisComponent in CorrectAnswerFeedbackComponents:
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
        # the Routine "CorrectAnswerFeedback" was not non-slip safe, so reset the non-slip timer
        routineTimer.reset()
    
    else:
            # ------Prepare to start Routine "IncorrectAnswerFeedback"-------
        continueRoutine = True
        # update component parameters for each repeat
        # setup some python lists for storing info about the mouse_4
        mouse_4.clicked_name = []
        gotValidClick = False  # until a click is received
        # keep track of which components have finished
        IncorrectAnswerFeedbackComponents = [IncorrectAnswerFeedbackTxt, mouse_4, nextButton_R1B]
        for thisComponent in IncorrectAnswerFeedbackComponents:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        # reset timers
        t = 0
        _timeToFirstFrame = win.getFutureFlipTime(clock="now")
        IncorrectAnswerFeedbackClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
        frameN = -1

    # -------Run Routine "IncorrectAnswerFeedback"-------
        while continueRoutine:
            # get current time
            t = IncorrectAnswerFeedbackClock.getTime()
            tThisFlip = win.getFutureFlipTime(clock=IncorrectAnswerFeedbackClock)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *oddballsQuestion* updates
            if IncorrectAnswerFeedbackTxt.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                IncorrectAnswerFeedbackTxt.frameNStart = frameN  # exact frame index
                IncorrectAnswerFeedbackTxt.tStart = t  # local t and not account for scr refresh
                IncorrectAnswerFeedbackTxt.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(IncorrectAnswerFeedbackTxt, 'tStartRefresh')  # time at next scr refresh
                IncorrectAnswerFeedbackTxt.setAutoDraw(True)        
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
            for thisComponent in IncorrectAnswerFeedbackComponents:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # -------Ending Routine "IncorrectAnswerFeedback"-------
        for thisComponent in IncorrectAnswerFeedbackComponents:
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
        # the Routine "IncorrectAnswerFeedback" was not non-slip safe, so reset the non-slip timer
        routineTimer.reset()
        
# completed 1.0 repeats of 'block0'

# playing part starting trig
print(f'Playing start trigger')
continueRoutine = True
routineTimer.add(1)
startExpTrigger = SfPlayer('start_trigger.wav')
for i in range(PART_2_OUT_CHANNELS):
    mm.delInput(i)
mm.addInput(0, startExpTrigger)
#mm.setAmp(0,i,0)
#for i in range(PART_2_OUT_CHANNELS):
#    mm.setAmp(0,i,0)
mm.setAmp(0,TRIGGER_CHN,spk_volume[TRIGGER_CHN])
while continueRoutine and routineTimer.getTime() > 0:
    mm.out()
mm.stop()
routineTimer.reset()
# end of playing part starting trig


# set up handler to look after randomisation of conditions etc
block1 = data.TrialHandler(nReps=1.0, method='random', 
    extraInfo=expInfo, originPath=-1,
    trialList=data.importConditions(participantPath + '\oddballStimuliList.xlsx', selection='0:15'),
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
    # update stimuliStarted parameter for each repeat
    stimuliStarted = False
    
    # keep track of which components have finished
    trialComponents = [attendVibraphoneNote, attendHarmonicaNote, attendKeyboardNote]
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
    
    # -------Run Routine "trial"-------
    while continueRoutine:
        # get current time
        t = trialClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=trialClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        attendedInst = f'{attendedInst}' #Setting the attended instrument, from the column in oddballStimuliList.xlsx
        
        # *attendVibraphoneNote* updates
        if attendedInst == 'Vibr' and attendVibraphoneNote.status == NOT_STARTED:
            # keep track of start time/frame for later
            attendVibraphoneNote.frameNStart = frameN  # exact frame index
            attendVibraphoneNote.tStart = t  # local t and not account for scr refresh
            attendVibraphoneNote.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(attendVibraphoneNote, 'tStartRefresh')  # time at next scr refresh
            attendVibraphoneNote.setAutoDraw(True)
        if attendVibraphoneNote.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > attendVibraphoneNote.tStartRefresh + 5.0-frameTolerance:
                # keep track of stop time/frame for later
                attendVibraphoneNote.tStop = t  # not accounting for scr refresh
                attendVibraphoneNote.frameNStop = frameN  # exact frame index
                win.timeOnFlip(attendVibraphoneNote, 'tStopRefresh')  # time at next scr refresh
                attendVibraphoneNote.setAutoDraw(False)
        
        # *attendHarmonicaNote* updates
        if attendedInst == 'Harm' and attendHarmonicaNote.status == NOT_STARTED:
            # keep track of start time/frame for later
            attendHarmonicaNote.frameNStart = frameN  # exact frame index
            attendHarmonicaNote.tStart = t  # local t and not account for scr refresh
            attendHarmonicaNote.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(attendHarmonicaNote, 'tStartRefresh')  # time at next scr refresh
            attendHarmonicaNote.setAutoDraw(True)
        if attendHarmonicaNote.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > attendHarmonicaNote.tStartRefresh + 5.0-frameTolerance:
                # keep track of stop time/frame for later
                attendHarmonicaNote.tStop = t  # not accounting for scr refresh
                attendHarmonicaNote.frameNStop = frameN  # exact frame index
                win.timeOnFlip(attendHarmonicaNote, 'tStopRefresh')  # time at next scr refresh
                attendHarmonicaNote.setAutoDraw(False)
        
                # *attendKeyboardNote* updates
        if attendedInst == 'Keyb' and attendKeyboardNote.status == NOT_STARTED:
            # keep track of start time/frame for later
            attendKeyboardNote.frameNStart = frameN  # exact frame index
            attendKeyboardNote.tStart = t  # local t and not account for scr refresh
            attendKeyboardNote.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(attendKeyboardNote, 'tStartRefresh')  # time at next scr refresh
            attendKeyboardNote.setAutoDraw(True)
        if attendKeyboardNote.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > attendKeyboardNote.tStartRefresh + 5.0-frameTolerance:
                # keep track of stop time/frame for later
                attendKeyboardNote.tStop = t  # not accounting for scr refresh
                attendKeyboardNote.frameNStop = frameN  # exact frame index
                win.timeOnFlip(attendKeyboardNote, 'tStopRefresh')  # time at next scr refresh
                attendKeyboardNote.setAutoDraw(False)
        
        if stimuliStarted == False and (attendVibraphoneNote.status == FINISHED or attendHarmonicaNote.status == FINISHED or attendKeyboardNote.status == FINISHED):
            print(f'trigger: {trigger}')
            trigger_filename, trigger_ext = os.path.splitext(trigger)
            trigger_logfile = os.path.abspath(trigger_filename + '.txt')
            trial['trigger'] = os.path.abspath(trigger)
            trial['trigger_log'] = os.path.abspath(trigger_logfile)
        
            # trigger channel
            trigger_chn = SfPlayer(trigger)
            mm.delInput(0)
            mm.addInput(0, trigger_chn)
            mm.setAmp(0,TRIGGER_CHN,spk_volume[TRIGGER_CHN])
            
            # stimuli channels
            trial['stimuli'] = []
            # create an empty list to store the players
            players = []
            
            # create the first player for stimuli_0
         #   spk_name = "stimuli_0"
          #  trial['stimuli'].append(os.path.abspath(globals()[spk_name]))
           # player = sound.Sound(globals()[spk_name])
            #player.setVolume(0.05)  # set the volume to 1
            #players.append(player)
            
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
            while any([player.status == PLAYING for player in players]):
                continue
                
            stimuliStarted = True
     
        mm.out()
        
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
        
        if tThisFlip >= PART_2_STIMULI_LEN+5.0-frameTolerance:
            continueRoutine = False
        
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

    # the Routine "trial" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # ------Prepare to start Routine "QuestionBreakPause"-------
    continueRoutine = True
    # update component parameters for each repeat
    # setup some python lists for storing info about the mouse_4
    mouse_4.clicked_name = []
    gotValidClick = False  # until a click is received
    # keep track of which components have finished
    QuestionBreakPauseComponents = [oddballsQuestion, oddballsResp, mouse_4, nextButton_R1B]
    for thisComponent in QuestionBreakPauseComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    QuestionBreakPauseClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "QuestionBreakPause"-------
    while continueRoutine:
        # get current time
        t = QuestionBreakPauseClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=QuestionBreakPauseClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *oddballsQuestion* updates
        if oddballsQuestion.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            oddballsQuestion.frameNStart = frameN  # exact frame index
            oddballsQuestion.tStart = t  # local t and not account for scr refresh
            oddballsQuestion.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(oddballsQuestion, 'tStartRefresh')  # time at next scr refresh
            oddballsQuestion.setAutoDraw(True) 
        # *oddballsResp* updates
        if oddballsResp.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            oddballsResp.frameNStart = frameN  # exact frame index
            oddballsResp.tStart = t  # local t and not account for scr refresh
            oddballsResp.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(oddballsResp, 'tStartRefresh')  # time at next scr refresh
            oddballsResp.setAutoDraw(True)
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
        for thisComponent in QuestionBreakPauseComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "QuestionBreakPause"-------
    for thisComponent in QuestionBreakPauseComponents:
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
    
    oddballsMinusResp = float(f'{attendedOddballs}') - float(oddballsResp.text) #Ignores things like spaces after the number, or new lines after it.           
    oddballsResp.reset()
    block1.addData('oddballsMinusResp', oddballsMinusResp)
    thisExp.nextEntry() #Next row on the record.
    # the Routine "QuestionBreakPause" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    ##FEEDBACK:
    if oddballsMinusResp == 0:
    
        # ------Prepare to start Routine "CorrectAnswerFeedback"-------
        continueRoutine = True
        # update component parameters for each repeat
        # setup some python lists for storing info about the mouse_4
        mouse_4.clicked_name = []
        gotValidClick = False  # until a click is received
        # keep track of which components have finished
        CorrectAnswerFeedbackComponents = [CorrectAnswerFeedbackTxt, mouse_4, nextButton_R1B]
        for thisComponent in CorrectAnswerFeedbackComponents:
            thisComponent.tStart = None
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        # reset timers
        t = 0
        _timeToFirstFrame = win.getFutureFlipTime(clock="now")
        CorrectAnswerFeedbackClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
        frameN = -1

    # -------Run Routine "CorrectAnswerFeedback"-------
        while continueRoutine:
            # get current time
            t = CorrectAnswerFeedbackClock.getTime()
            tThisFlip = win.getFutureFlipTime(clock=CorrectAnswerFeedbackClock)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *oddballsQuestion* updates
            if CorrectAnswerFeedbackTxt.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                CorrectAnswerFeedbackTxt.frameNStart = frameN  # exact frame index
                CorrectAnswerFeedbackTxt.tStart = t  # local t and not account for scr refresh
                CorrectAnswerFeedbackTxt.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(CorrectAnswerFeedbackTxt, 'tStartRefresh')  # time at next scr refresh
                CorrectAnswerFeedbackTxt.setAutoDraw(True)        
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
            for thisComponent in CorrectAnswerFeedbackComponents:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # -------Ending Routine "CorrectAnswerFeedback"-------
        for thisComponent in CorrectAnswerFeedbackComponents:
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
        # the Routine "CorrectAnswerFeedback" was not non-slip safe, so reset the non-slip timer
        routineTimer.reset()
    
    else:
            # ------Prepare to start Routine "IncorrectAnswerFeedback"-------
        continueRoutine = True
        # update component parameters for each repeat
        # setup some python lists for storing info about the mouse_4
        mouse_4.clicked_name = []
        gotValidClick = False  # until a click is received
        # keep track of which components have finished
        IncorrectAnswerFeedbackComponents = [IncorrectAnswerFeedbackTxt, mouse_4, nextButton_R1B]
        for thisComponent in IncorrectAnswerFeedbackComponents:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        # reset timers
        t = 0
        _timeToFirstFrame = win.getFutureFlipTime(clock="now")
        IncorrectAnswerFeedbackClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
        frameN = -1

    # -------Run Routine "IncorrectAnswerFeedback"-------
        while continueRoutine:
            # get current time
            t = IncorrectAnswerFeedbackClock.getTime()
            tThisFlip = win.getFutureFlipTime(clock=IncorrectAnswerFeedbackClock)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *oddballsQuestion* updates
            if IncorrectAnswerFeedbackTxt.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                IncorrectAnswerFeedbackTxt.frameNStart = frameN  # exact frame index
                IncorrectAnswerFeedbackTxt.tStart = t  # local t and not account for scr refresh
                IncorrectAnswerFeedbackTxt.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(IncorrectAnswerFeedbackTxt, 'tStartRefresh')  # time at next scr refresh
                IncorrectAnswerFeedbackTxt.setAutoDraw(True)        
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
            for thisComponent in IncorrectAnswerFeedbackComponents:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # -------Ending Routine "IncorrectAnswerFeedback"-------
        for thisComponent in IncorrectAnswerFeedbackComponents:
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
        # the Routine "IncorrectAnswerFeedback" was not non-slip safe, so reset the non-slip timer
        routineTimer.reset()
        
# completed 1.0 repeats of 'block1'

# playing part stop trig
continueRoutine = True
routineTimer.add(1)
stopExpTrigger = SfPlayer('stop_trigger.wav')
mm.delInput(0)
mm.addInput(0, stopExpTrigger)

#for i in range(PART_2_OUT_CHANNELS):
#    mm.setAmp(0,i,0)
#mm.setAmp(0,0,spk_volume[0])
mm.setAmp(0,TRIGGER_CHN,spk_volume[TRIGGER_CHN])
while continueRoutine and routineTimer.getTime() > 0:
    mm.out()
mm.stop()
routineTimer.reset()
thisExp.nextEntry()
# End of playing part stop trig

# ------Prepare to start Routine "thisPartComplete"-------
# update component parameters for each repeat
# keep track of which components have finished
continueRoutine = True

thisPartCompleteComponents = [thisPartCompleteText]
for thisComponent in thisPartCompleteComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
thisPartCompleteClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1
    
# -------Run Routine "thisPartComplete"-------
while continueRoutine:
    # get current time
    t = thisPartCompleteClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=thisPartCompleteClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    if thisPartCompleteText.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        thisPartCompleteText.frameNStart = frameN  # exact frame index
        thisPartCompleteText.tStart = t  # local t and not account for scr refresh
        thisPartCompleteText.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(thisPartCompleteText, 'tStartRefresh')  # time at next scr refresh
        thisPartCompleteText.setAutoDraw(True) 
        
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    if thisPartCompleteClock.getTime() > 6:
        thisPartCompleteText.status = FINISHED
        
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in thisPartCompleteComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()
    
# -------Ending Routine "thisPartComplete"-------
for thisComponent in thisPartCompleteComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)

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