#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
This experiment was created using PsychoPy3 Experiment Builder (v2022.1.3),
    on June 07, 2022, at 17:27
If you publish work using this script the most relevant publication is:

    Peirce J, Gray JR, Simpson S, MacAskill M, Höchenberger R, Sogo H, Kastman E, Lindeløv JK. (2019) 
        PsychoPy2: Experiments in behavior made easy Behav Res 51: 195. 
        https://doi.org/10.3758/s13428-018-01193-y

"""

from psychopy import locale_setup
from psychopy import prefs
from psychopy import sound, gui, visual, core, data, event, logging, clock, colors, layout
from psychopy.constants import (NOT_STARTED, STARTED, PLAYING, PAUSED,
                                STOPPED, FINISHED, PRESSED, RELEASED, FOREVER)

import numpy as np  # whole numpy lib is available, prepend 'np.'
from numpy import (sin, cos, tan, log, log10, pi, average,
                   sqrt, std, deg2rad, rad2deg, linspace, asarray)
from numpy.random import random, randint, normal, shuffle, choice as randchoice
import os  # handy system and path functions
import sys  # to get file system encoding

import psychopy.iohub as io
from psychopy.hardware import keyboard



# Ensure that relative paths start from the same directory as this script
_thisDir = os.path.dirname(os.path.abspath(__file__))
os.chdir(_thisDir)
# Store info about the experiment session
psychopyVersion = '2022.1.3'
expName = 'First Attempt at Part 2 Expt Script'  # from the Builder filename that created this script
expInfo = {'participant': ''}
dlg = gui.DlgFromDict(dictionary=expInfo, sortKeys=False, title=expName)
if dlg.OK == False:
    core.quit()  # user pressed cancel
expInfo['date'] = data.getDateStr()  # add a simple timestamp
expInfo['expName'] = expName
expInfo['psychopyVersion'] = psychopyVersion

# Data file name stem = absolute path + name; later add .psyexp, .csv, .log, etc
filename = _thisDir + os.sep + u'data/%s_%s_%s' % (expInfo['participant'], expName, expInfo['date'])

# An ExperimentHandler isn't essential but helps with data saving
thisExp = data.ExperimentHandler(name=expName, version='',
    extraInfo=expInfo, runtimeInfo=None,
    originPath='C:\\Users\\Chris\\Documents\\Music Interestingness in the Brain\\PsychoPy Paradigm\\First Attempt at Part 2 Expt Script_lastrun.py',
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
    size=[1536, 864], fullscr=True, screen=0, 
    winType='pyglet', allowGUI=False, allowStencil=False,
    monitor='testMonitor', color=[0,0,0], colorSpace='rgb',
    blendMode='avg', useFBO=True, 
    units='height')
# store frame rate of monitor if we can measure it
expInfo['frameRate'] = win.getActualFrameRate()
if expInfo['frameRate'] != None:
    frameDur = 1.0 / round(expInfo['frameRate'])
else:
    frameDur = 1.0 / 60.0  # could not measure, so guess
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
    text='Welcome to Part 2 of the experiment. The instructions are as follows:\n\nThree of the music pieces you heard earlier will play at the same time: one vibraphone piece, one keyboard piece, and one harmonica piece. These will play from the left, centre, and right respectively.\n\nFirst, you will be told to pay attention to one of these pieces in particular. E.g, if you see an "^" arrow, then you should pay attention to the keyboard piece, coming from the centre.\n\nThen, the pieces will play twice in a row. The first time will just be to remind you of the pieces. During the second time, there will be some "oddballs" where the pitch is shifted for two seconds. Try to count these. Please try not to blink or move during the minute whilst the music plays.\n\nAfter the end of the second piece, you will need to type in how many oddballs you heard. You will receive feedback.\n\nImmediately after, the next trial will start. The pieces played may be the same as previously or different ones.\n\nThere will be a total of 15 trials, with three breaks between them. These are 90s long, but if you feel like your attention is slipping feel free to take longer.\n\nIf you have any questions at all please ask the experimenters.',
    font='Open Sans',
    pos=(0, 0.15), height=0.04, wrapWidth=1.8, ori=0.0, 
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

# Initialize components for Routine "Ready1stBlock"
Ready1stBlockClock = core.Clock()
top_instr_txt_3 = visual.TextStim(win=win, name='top_instr_txt_3',
    text='Are you ready for the first block of trials?',
    font='Open Sans',
    pos=(0, 0.15), height=0.04, wrapWidth=None, ori=0.0, 
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
stimuli3streams = sound.Sound(stimuli, secs=-1, stereo=True, hamming=True,
    name='stimuli3streams')
stimuli3streams.setVolume(1.0)
stimuli3streamsoddballs = sound.Sound(stimuli, secs=-1, stereo=True, hamming=True,
    name='stimuli3streamsoddballs')
stimuli3streamsoddballs.setVolume(1.0)
text = visual.TextStim(win=win, name='text',
    text='How many oddballs did you hear?',
    font='Open Sans',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-2.0);
textbox = visual.TextBox2(
     win, text=None, font='Open Sans',
     pos=(0, 0),     letterHeight=0.05,
     size=(None, None), borderWidth=2.0,
     color='white', colorSpace='rgb',
     opacity=None,
     bold=False, italic=False,
     lineSpacing=1.0,
     padding=0.0, alignment='center',
     anchor='center',
     fillColor=None, borderColor=None,
     flipHoriz=False, flipVert=False, languageStyle='LTR',
     editable=True,
     name='textbox',
     autoLog=True,
)
arrow = visual.ImageStim(
    win=win,
    name='arrow', 
    image=None, mask=None, anchor='center',
    ori=0.0, pos=(0, 0), size=(0.5, 0.5),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-4.0)
feedback = visual.ImageStim(
    win=win,
    name='feedback', 
    image=None, mask=None, anchor='center',
    ori=0.0, pos=(0, 0), size=(0.5, 0.5),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-5.0)

# Initialize components for Routine "break_2"
break_2Clock = core.Clock()
text_2 = visual.TextStim(win=win, name='text_2',
    text="Well done, it's time for a 90 second break.",
    font='Open Sans',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);

# Initialize components for Routine "Ready"
ReadyClock = core.Clock()
top_instr_txt_2 = visual.TextStim(win=win, name='top_instr_txt_2',
    text='Are you ready for the next block of trials?',
    font='Open Sans',
    pos=(0, 0.15), height=0.1, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);
mouse_3 = event.Mouse(win=win)
x, y = [None, None]
mouse_3.mouseClock = core.Clock()
nextButton_R = visual.ImageStim(
    win=win,
    name='nextButton_R', 
    image='next.png', mask=None, anchor='center',
    ori=0.0, pos=(0, -0.4), size=(0.15, 0.075),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-2.0)

# Initialize components for Routine "trial"
trialClock = core.Clock()
stimuli3streams = sound.Sound(stimuli, secs=-1, stereo=True, hamming=True,
    name='stimuli3streams')
stimuli3streams.setVolume(1.0)
stimuli3streamsoddballs = sound.Sound(stimuli, secs=-1, stereo=True, hamming=True,
    name='stimuli3streamsoddballs')
stimuli3streamsoddballs.setVolume(1.0)
text = visual.TextStim(win=win, name='text',
    text='How many oddballs did you hear?',
    font='Open Sans',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-2.0);
textbox = visual.TextBox2(
     win, text=None, font='Open Sans',
     pos=(0, 0),     letterHeight=0.05,
     size=(None, None), borderWidth=2.0,
     color='white', colorSpace='rgb',
     opacity=None,
     bold=False, italic=False,
     lineSpacing=1.0,
     padding=0.0, alignment='center',
     anchor='center',
     fillColor=None, borderColor=None,
     flipHoriz=False, flipVert=False, languageStyle='LTR',
     editable=True,
     name='textbox',
     autoLog=True,
)
arrow = visual.ImageStim(
    win=win,
    name='arrow', 
    image=None, mask=None, anchor='center',
    ori=0.0, pos=(0, 0), size=(0.5, 0.5),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-4.0)
feedback = visual.ImageStim(
    win=win,
    name='feedback', 
    image=None, mask=None, anchor='center',
    ori=0.0, pos=(0, 0), size=(0.5, 0.5),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-5.0)

# Initialize components for Routine "break_2"
break_2Clock = core.Clock()
text_2 = visual.TextStim(win=win, name='text_2',
    text="Well done, it's time for a 90 second break.",
    font='Open Sans',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);

# Initialize components for Routine "Ready"
ReadyClock = core.Clock()
top_instr_txt_2 = visual.TextStim(win=win, name='top_instr_txt_2',
    text='Are you ready for the next block of trials?',
    font='Open Sans',
    pos=(0, 0.15), height=0.1, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);
mouse_3 = event.Mouse(win=win)
x, y = [None, None]
mouse_3.mouseClock = core.Clock()
nextButton_R = visual.ImageStim(
    win=win,
    name='nextButton_R', 
    image='next.png', mask=None, anchor='center',
    ori=0.0, pos=(0, -0.4), size=(0.15, 0.075),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-2.0)

# Initialize components for Routine "trial"
trialClock = core.Clock()
stimuli3streams = sound.Sound(stimuli, secs=-1, stereo=True, hamming=True,
    name='stimuli3streams')
stimuli3streams.setVolume(1.0)
stimuli3streamsoddballs = sound.Sound(stimuli, secs=-1, stereo=True, hamming=True,
    name='stimuli3streamsoddballs')
stimuli3streamsoddballs.setVolume(1.0)
text = visual.TextStim(win=win, name='text',
    text='How many oddballs did you hear?',
    font='Open Sans',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-2.0);
textbox = visual.TextBox2(
     win, text=None, font='Open Sans',
     pos=(0, 0),     letterHeight=0.05,
     size=(None, None), borderWidth=2.0,
     color='white', colorSpace='rgb',
     opacity=None,
     bold=False, italic=False,
     lineSpacing=1.0,
     padding=0.0, alignment='center',
     anchor='center',
     fillColor=None, borderColor=None,
     flipHoriz=False, flipVert=False, languageStyle='LTR',
     editable=True,
     name='textbox',
     autoLog=True,
)
arrow = visual.ImageStim(
    win=win,
    name='arrow', 
    image=None, mask=None, anchor='center',
    ori=0.0, pos=(0, 0), size=(0.5, 0.5),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-4.0)
feedback = visual.ImageStim(
    win=win,
    name='feedback', 
    image=None, mask=None, anchor='center',
    ori=0.0, pos=(0, 0), size=(0.5, 0.5),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-5.0)

# Initialize components for Routine "break_2"
break_2Clock = core.Clock()
text_2 = visual.TextStim(win=win, name='text_2',
    text="Well done, it's time for a 90 second break.",
    font='Open Sans',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);

# Initialize components for Routine "Ready"
ReadyClock = core.Clock()
top_instr_txt_2 = visual.TextStim(win=win, name='top_instr_txt_2',
    text='Are you ready for the next block of trials?',
    font='Open Sans',
    pos=(0, 0.15), height=0.1, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);
mouse_3 = event.Mouse(win=win)
x, y = [None, None]
mouse_3.mouseClock = core.Clock()
nextButton_R = visual.ImageStim(
    win=win,
    name='nextButton_R', 
    image='next.png', mask=None, anchor='center',
    ori=0.0, pos=(0, -0.4), size=(0.15, 0.075),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-2.0)

# Initialize components for Routine "trial"
trialClock = core.Clock()
stimuli3streams = sound.Sound(stimuli, secs=-1, stereo=True, hamming=True,
    name='stimuli3streams')
stimuli3streams.setVolume(1.0)
stimuli3streamsoddballs = sound.Sound(stimuli, secs=-1, stereo=True, hamming=True,
    name='stimuli3streamsoddballs')
stimuli3streamsoddballs.setVolume(1.0)
text = visual.TextStim(win=win, name='text',
    text='How many oddballs did you hear?',
    font='Open Sans',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-2.0);
textbox = visual.TextBox2(
     win, text=None, font='Open Sans',
     pos=(0, 0),     letterHeight=0.05,
     size=(None, None), borderWidth=2.0,
     color='white', colorSpace='rgb',
     opacity=None,
     bold=False, italic=False,
     lineSpacing=1.0,
     padding=0.0, alignment='center',
     anchor='center',
     fillColor=None, borderColor=None,
     flipHoriz=False, flipVert=False, languageStyle='LTR',
     editable=True,
     name='textbox',
     autoLog=True,
)
arrow = visual.ImageStim(
    win=win,
    name='arrow', 
    image=None, mask=None, anchor='center',
    ori=0.0, pos=(0, 0), size=(0.5, 0.5),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-4.0)
feedback = visual.ImageStim(
    win=win,
    name='feedback', 
    image=None, mask=None, anchor='center',
    ori=0.0, pos=(0, 0), size=(0.5, 0.5),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-5.0)

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
thisExp.addData('top_instr_txt.started', top_instr_txt.tStartRefresh)
thisExp.addData('top_instr_txt.stopped', top_instr_txt.tStopRefresh)
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
thisExp.addData('mouse_2.x', x)
thisExp.addData('mouse_2.y', y)
thisExp.addData('mouse_2.leftButton', buttons[0])
thisExp.addData('mouse_2.midButton', buttons[1])
thisExp.addData('mouse_2.rightButton', buttons[2])
if len(mouse_2.clicked_name):
    thisExp.addData('mouse_2.clicked_name', mouse_2.clicked_name[0])
thisExp.addData('mouse_2.started', mouse_2.tStart)
thisExp.addData('mouse_2.stopped', mouse_2.tStop)
thisExp.nextEntry()
thisExp.addData('nextButton_instruct.started', nextButton_instruct.tStartRefresh)
thisExp.addData('nextButton_instruct.stopped', nextButton_instruct.tStopRefresh)
# the Routine "instructions" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# ------Prepare to start Routine "Ready1stBlock"-------
continueRoutine = True
# update component parameters for each repeat
# setup some python lists for storing info about the mouse_4
mouse_4.clicked_name = []
gotValidClick = False  # until a click is received
# keep track of which components have finished
Ready1stBlockComponents = [top_instr_txt_3, mouse_4, nextButton_R1B]
for thisComponent in Ready1stBlockComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
Ready1stBlockClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "Ready1stBlock"-------
while continueRoutine:
    # get current time
    t = Ready1stBlockClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=Ready1stBlockClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *top_instr_txt_3* updates
    if top_instr_txt_3.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        top_instr_txt_3.frameNStart = frameN  # exact frame index
        top_instr_txt_3.tStart = t  # local t and not account for scr refresh
        top_instr_txt_3.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(top_instr_txt_3, 'tStartRefresh')  # time at next scr refresh
        top_instr_txt_3.setAutoDraw(True)
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
    for thisComponent in Ready1stBlockComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "Ready1stBlock"-------
for thisComponent in Ready1stBlockComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('top_instr_txt_3.started', top_instr_txt_3.tStartRefresh)
thisExp.addData('top_instr_txt_3.stopped', top_instr_txt_3.tStopRefresh)
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
thisExp.addData('mouse_4.x', x)
thisExp.addData('mouse_4.y', y)
thisExp.addData('mouse_4.leftButton', buttons[0])
thisExp.addData('mouse_4.midButton', buttons[1])
thisExp.addData('mouse_4.rightButton', buttons[2])
if len(mouse_4.clicked_name):
    thisExp.addData('mouse_4.clicked_name', mouse_4.clicked_name[0])
thisExp.addData('mouse_4.started', mouse_4.tStart)
thisExp.addData('mouse_4.stopped', mouse_4.tStop)
thisExp.nextEntry()
thisExp.addData('nextButton_R1B.started', nextButton_R1B.tStartRefresh)
thisExp.addData('nextButton_R1B.stopped', nextButton_R1B.tStopRefresh)
# the Routine "Ready1stBlock" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# set up handler to look after randomisation of conditions etc
trials = data.TrialHandler(nReps=1.0, method='random', 
    extraInfo=expInfo, originPath=-1,
    trialList=data.importConditions('stimuliOddballsList.xlsx', selection='1:4'),
    seed=None, name='trials')
thisExp.addLoop(trials)  # add the loop to the experiment
thisTrial = trials.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisTrial.rgb)
if thisTrial != None:
    for paramName in thisTrial:
        exec('{} = thisTrial[paramName]'.format(paramName))

for thisTrial in trials:
    currentLoop = trials
    # abbreviate parameter names if possible (e.g. rgb = thisTrial.rgb)
    if thisTrial != None:
        for paramName in thisTrial:
            exec('{} = thisTrial[paramName]'.format(paramName))
    
    # ------Prepare to start Routine "trial"-------
    continueRoutine = True
    routineTimer.add(71.000000)
    # update component parameters for each repeat
    stimuli3streams.setSound(stimuli, secs=30.0, hamming=True)
    stimuli3streams.setVolume(1.0, log=False)
    stimuli3streamsoddballs.setSound(stimuli, secs=30.0, hamming=True)
    stimuli3streamsoddballs.setVolume(1.0, log=False)
    textbox.reset()
    # keep track of which components have finished
    trialComponents = [stimuli3streams, stimuli3streamsoddballs, text, textbox, arrow, feedback]
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
    while continueRoutine and routineTimer.getTime() > 0:
        # get current time
        t = trialClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=trialClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        # start/stop stimuli3streams
        if stimuli3streams.status == NOT_STARTED and tThisFlip >= 2.0-frameTolerance:
            # keep track of start time/frame for later
            stimuli3streams.frameNStart = frameN  # exact frame index
            stimuli3streams.tStart = t  # local t and not account for scr refresh
            stimuli3streams.tStartRefresh = tThisFlipGlobal  # on global time
            stimuli3streams.play(when=win)  # sync with win flip
        if stimuli3streams.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > stimuli3streams.tStartRefresh + 30.0-frameTolerance:
                # keep track of stop time/frame for later
                stimuli3streams.tStop = t  # not accounting for scr refresh
                stimuli3streams.frameNStop = frameN  # exact frame index
                win.timeOnFlip(stimuli3streams, 'tStopRefresh')  # time at next scr refresh
                stimuli3streams.stop()
        # start/stop stimuli3streamsoddballs
        if stimuli3streamsoddballs.status == NOT_STARTED and tThisFlip >= 34.0-frameTolerance:
            # keep track of start time/frame for later
            stimuli3streamsoddballs.frameNStart = frameN  # exact frame index
            stimuli3streamsoddballs.tStart = t  # local t and not account for scr refresh
            stimuli3streamsoddballs.tStartRefresh = tThisFlipGlobal  # on global time
            stimuli3streamsoddballs.play(when=win)  # sync with win flip
        if stimuli3streamsoddballs.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > stimuli3streamsoddballs.tStartRefresh + 30.0-frameTolerance:
                # keep track of stop time/frame for later
                stimuli3streamsoddballs.tStop = t  # not accounting for scr refresh
                stimuli3streamsoddballs.frameNStop = frameN  # exact frame index
                win.timeOnFlip(stimuli3streamsoddballs, 'tStopRefresh')  # time at next scr refresh
                stimuli3streamsoddballs.stop()
        
        # *text* updates
        if text.status == NOT_STARTED and tThisFlip >= 64.0-frameTolerance:
            # keep track of start time/frame for later
            text.frameNStart = frameN  # exact frame index
            text.tStart = t  # local t and not account for scr refresh
            text.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(text, 'tStartRefresh')  # time at next scr refresh
            text.setAutoDraw(True)
        if text.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > text.tStartRefresh + 5.0-frameTolerance:
                # keep track of stop time/frame for later
                text.tStop = t  # not accounting for scr refresh
                text.frameNStop = frameN  # exact frame index
                win.timeOnFlip(text, 'tStopRefresh')  # time at next scr refresh
                text.setAutoDraw(False)
        
        # *textbox* updates
        if textbox.status == NOT_STARTED and tThisFlip >= 64.0-frameTolerance:
            # keep track of start time/frame for later
            textbox.frameNStart = frameN  # exact frame index
            textbox.tStart = t  # local t and not account for scr refresh
            textbox.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(textbox, 'tStartRefresh')  # time at next scr refresh
            textbox.setAutoDraw(True)
        if textbox.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > textbox.tStartRefresh + 5.0-frameTolerance:
                # keep track of stop time/frame for later
                textbox.tStop = t  # not accounting for scr refresh
                textbox.frameNStop = frameN  # exact frame index
                win.timeOnFlip(textbox, 'tStopRefresh')  # time at next scr refresh
                textbox.setAutoDraw(False)
        
        # *arrow* updates
        if arrow.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            arrow.frameNStart = frameN  # exact frame index
            arrow.tStart = t  # local t and not account for scr refresh
            arrow.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(arrow, 'tStartRefresh')  # time at next scr refresh
            arrow.setAutoDraw(True)
        if arrow.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > arrow.tStartRefresh + 2.0-frameTolerance:
                # keep track of stop time/frame for later
                arrow.tStop = t  # not accounting for scr refresh
                arrow.frameNStop = frameN  # exact frame index
                win.timeOnFlip(arrow, 'tStopRefresh')  # time at next scr refresh
                arrow.setAutoDraw(False)
        
        # *feedback* updates
        if feedback.status == NOT_STARTED and tThisFlip >= 69.0-frameTolerance:
            # keep track of start time/frame for later
            feedback.frameNStart = frameN  # exact frame index
            feedback.tStart = t  # local t and not account for scr refresh
            feedback.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(feedback, 'tStartRefresh')  # time at next scr refresh
            feedback.setAutoDraw(True)
        if feedback.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > feedback.tStartRefresh + 2.0-frameTolerance:
                # keep track of stop time/frame for later
                feedback.tStop = t  # not accounting for scr refresh
                feedback.frameNStop = frameN  # exact frame index
                win.timeOnFlip(feedback, 'tStopRefresh')  # time at next scr refresh
                feedback.setAutoDraw(False)
        
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
    
    # -------Ending Routine "trial"-------
    for thisComponent in trialComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    stimuli3streams.stop()  # ensure sound has stopped at end of routine
    trials.addData('stimuli3streams.started', stimuli3streams.tStartRefresh)
    trials.addData('stimuli3streams.stopped', stimuli3streams.tStopRefresh)
    stimuli3streamsoddballs.stop()  # ensure sound has stopped at end of routine
    trials.addData('stimuli3streamsoddballs.started', stimuli3streamsoddballs.tStartRefresh)
    trials.addData('stimuli3streamsoddballs.stopped', stimuli3streamsoddballs.tStopRefresh)
    trials.addData('text.started', text.tStartRefresh)
    trials.addData('text.stopped', text.tStopRefresh)
    trials.addData('textbox.text',textbox.text)
    trials.addData('textbox.started', textbox.tStartRefresh)
    trials.addData('textbox.stopped', textbox.tStopRefresh)
    trials.addData('arrow.started', arrow.tStartRefresh)
    trials.addData('arrow.stopped', arrow.tStopRefresh)
    trials.addData('feedback.started', feedback.tStartRefresh)
    trials.addData('feedback.stopped', feedback.tStopRefresh)
    thisExp.nextEntry()
    
# completed 1.0 repeats of 'trials'


# ------Prepare to start Routine "break_2"-------
continueRoutine = True
routineTimer.add(90.000000)
# update component parameters for each repeat
# keep track of which components have finished
break_2Components = [text_2]
for thisComponent in break_2Components:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
break_2Clock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "break_2"-------
while continueRoutine and routineTimer.getTime() > 0:
    # get current time
    t = break_2Clock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=break_2Clock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *text_2* updates
    if text_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        text_2.frameNStart = frameN  # exact frame index
        text_2.tStart = t  # local t and not account for scr refresh
        text_2.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(text_2, 'tStartRefresh')  # time at next scr refresh
        text_2.setAutoDraw(True)
    if text_2.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > text_2.tStartRefresh + 90.0-frameTolerance:
            # keep track of stop time/frame for later
            text_2.tStop = t  # not accounting for scr refresh
            text_2.frameNStop = frameN  # exact frame index
            win.timeOnFlip(text_2, 'tStopRefresh')  # time at next scr refresh
            text_2.setAutoDraw(False)
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in break_2Components:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "break_2"-------
for thisComponent in break_2Components:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('text_2.started', text_2.tStartRefresh)
thisExp.addData('text_2.stopped', text_2.tStopRefresh)

# ------Prepare to start Routine "Ready"-------
continueRoutine = True
# update component parameters for each repeat
# setup some python lists for storing info about the mouse_3
mouse_3.clicked_name = []
gotValidClick = False  # until a click is received
# keep track of which components have finished
ReadyComponents = [top_instr_txt_2, mouse_3, nextButton_R]
for thisComponent in ReadyComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
ReadyClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "Ready"-------
while continueRoutine:
    # get current time
    t = ReadyClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=ReadyClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *top_instr_txt_2* updates
    if top_instr_txt_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        top_instr_txt_2.frameNStart = frameN  # exact frame index
        top_instr_txt_2.tStart = t  # local t and not account for scr refresh
        top_instr_txt_2.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(top_instr_txt_2, 'tStartRefresh')  # time at next scr refresh
        top_instr_txt_2.setAutoDraw(True)
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
                    iter(nextButton_R)
                    clickableList = nextButton_R
                except:
                    clickableList = [nextButton_R]
                for obj in clickableList:
                    if obj.contains(mouse_3):
                        gotValidClick = True
                        mouse_3.clicked_name.append(obj.name)
                if gotValidClick:  
                    continueRoutine = False  # abort routine on response
    
    # *nextButton_R* updates
    if nextButton_R.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        nextButton_R.frameNStart = frameN  # exact frame index
        nextButton_R.tStart = t  # local t and not account for scr refresh
        nextButton_R.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(nextButton_R, 'tStartRefresh')  # time at next scr refresh
        nextButton_R.setAutoDraw(True)
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in ReadyComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "Ready"-------
for thisComponent in ReadyComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('top_instr_txt_2.started', top_instr_txt_2.tStartRefresh)
thisExp.addData('top_instr_txt_2.stopped', top_instr_txt_2.tStopRefresh)
# store data for thisExp (ExperimentHandler)
x, y = mouse_3.getPos()
buttons = mouse_3.getPressed()
if sum(buttons):
    # check if the mouse was inside our 'clickable' objects
    gotValidClick = False
    try:
        iter(nextButton_R)
        clickableList = nextButton_R
    except:
        clickableList = [nextButton_R]
    for obj in clickableList:
        if obj.contains(mouse_3):
            gotValidClick = True
            mouse_3.clicked_name.append(obj.name)
thisExp.addData('mouse_3.x', x)
thisExp.addData('mouse_3.y', y)
thisExp.addData('mouse_3.leftButton', buttons[0])
thisExp.addData('mouse_3.midButton', buttons[1])
thisExp.addData('mouse_3.rightButton', buttons[2])
if len(mouse_3.clicked_name):
    thisExp.addData('mouse_3.clicked_name', mouse_3.clicked_name[0])
thisExp.addData('mouse_3.started', mouse_3.tStart)
thisExp.addData('mouse_3.stopped', mouse_3.tStop)
thisExp.nextEntry()
thisExp.addData('nextButton_R.started', nextButton_R.tStartRefresh)
thisExp.addData('nextButton_R.stopped', nextButton_R.tStopRefresh)
# the Routine "Ready" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# set up handler to look after randomisation of conditions etc
trials_2 = data.TrialHandler(nReps=1.0, method='random', 
    extraInfo=expInfo, originPath=-1,
    trialList=data.importConditions('stimuliOddballsList.xlsx', selection='5:8'),
    seed=None, name='trials_2')
thisExp.addLoop(trials_2)  # add the loop to the experiment
thisTrial_2 = trials_2.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisTrial_2.rgb)
if thisTrial_2 != None:
    for paramName in thisTrial_2:
        exec('{} = thisTrial_2[paramName]'.format(paramName))

for thisTrial_2 in trials_2:
    currentLoop = trials_2
    # abbreviate parameter names if possible (e.g. rgb = thisTrial_2.rgb)
    if thisTrial_2 != None:
        for paramName in thisTrial_2:
            exec('{} = thisTrial_2[paramName]'.format(paramName))
    
    # ------Prepare to start Routine "trial"-------
    continueRoutine = True
    routineTimer.add(71.000000)
    # update component parameters for each repeat
    stimuli3streams.setSound(stimuli, secs=30.0, hamming=True)
    stimuli3streams.setVolume(1.0, log=False)
    stimuli3streamsoddballs.setSound(stimuli, secs=30.0, hamming=True)
    stimuli3streamsoddballs.setVolume(1.0, log=False)
    textbox.reset()
    # keep track of which components have finished
    trialComponents = [stimuli3streams, stimuli3streamsoddballs, text, textbox, arrow, feedback]
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
    while continueRoutine and routineTimer.getTime() > 0:
        # get current time
        t = trialClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=trialClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        # start/stop stimuli3streams
        if stimuli3streams.status == NOT_STARTED and tThisFlip >= 2.0-frameTolerance:
            # keep track of start time/frame for later
            stimuli3streams.frameNStart = frameN  # exact frame index
            stimuli3streams.tStart = t  # local t and not account for scr refresh
            stimuli3streams.tStartRefresh = tThisFlipGlobal  # on global time
            stimuli3streams.play(when=win)  # sync with win flip
        if stimuli3streams.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > stimuli3streams.tStartRefresh + 30.0-frameTolerance:
                # keep track of stop time/frame for later
                stimuli3streams.tStop = t  # not accounting for scr refresh
                stimuli3streams.frameNStop = frameN  # exact frame index
                win.timeOnFlip(stimuli3streams, 'tStopRefresh')  # time at next scr refresh
                stimuli3streams.stop()
        # start/stop stimuli3streamsoddballs
        if stimuli3streamsoddballs.status == NOT_STARTED and tThisFlip >= 34.0-frameTolerance:
            # keep track of start time/frame for later
            stimuli3streamsoddballs.frameNStart = frameN  # exact frame index
            stimuli3streamsoddballs.tStart = t  # local t and not account for scr refresh
            stimuli3streamsoddballs.tStartRefresh = tThisFlipGlobal  # on global time
            stimuli3streamsoddballs.play(when=win)  # sync with win flip
        if stimuli3streamsoddballs.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > stimuli3streamsoddballs.tStartRefresh + 30.0-frameTolerance:
                # keep track of stop time/frame for later
                stimuli3streamsoddballs.tStop = t  # not accounting for scr refresh
                stimuli3streamsoddballs.frameNStop = frameN  # exact frame index
                win.timeOnFlip(stimuli3streamsoddballs, 'tStopRefresh')  # time at next scr refresh
                stimuli3streamsoddballs.stop()
        
        # *text* updates
        if text.status == NOT_STARTED and tThisFlip >= 64.0-frameTolerance:
            # keep track of start time/frame for later
            text.frameNStart = frameN  # exact frame index
            text.tStart = t  # local t and not account for scr refresh
            text.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(text, 'tStartRefresh')  # time at next scr refresh
            text.setAutoDraw(True)
        if text.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > text.tStartRefresh + 5.0-frameTolerance:
                # keep track of stop time/frame for later
                text.tStop = t  # not accounting for scr refresh
                text.frameNStop = frameN  # exact frame index
                win.timeOnFlip(text, 'tStopRefresh')  # time at next scr refresh
                text.setAutoDraw(False)
        
        # *textbox* updates
        if textbox.status == NOT_STARTED and tThisFlip >= 64.0-frameTolerance:
            # keep track of start time/frame for later
            textbox.frameNStart = frameN  # exact frame index
            textbox.tStart = t  # local t and not account for scr refresh
            textbox.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(textbox, 'tStartRefresh')  # time at next scr refresh
            textbox.setAutoDraw(True)
        if textbox.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > textbox.tStartRefresh + 5.0-frameTolerance:
                # keep track of stop time/frame for later
                textbox.tStop = t  # not accounting for scr refresh
                textbox.frameNStop = frameN  # exact frame index
                win.timeOnFlip(textbox, 'tStopRefresh')  # time at next scr refresh
                textbox.setAutoDraw(False)
        
        # *arrow* updates
        if arrow.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            arrow.frameNStart = frameN  # exact frame index
            arrow.tStart = t  # local t and not account for scr refresh
            arrow.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(arrow, 'tStartRefresh')  # time at next scr refresh
            arrow.setAutoDraw(True)
        if arrow.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > arrow.tStartRefresh + 2.0-frameTolerance:
                # keep track of stop time/frame for later
                arrow.tStop = t  # not accounting for scr refresh
                arrow.frameNStop = frameN  # exact frame index
                win.timeOnFlip(arrow, 'tStopRefresh')  # time at next scr refresh
                arrow.setAutoDraw(False)
        
        # *feedback* updates
        if feedback.status == NOT_STARTED and tThisFlip >= 69.0-frameTolerance:
            # keep track of start time/frame for later
            feedback.frameNStart = frameN  # exact frame index
            feedback.tStart = t  # local t and not account for scr refresh
            feedback.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(feedback, 'tStartRefresh')  # time at next scr refresh
            feedback.setAutoDraw(True)
        if feedback.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > feedback.tStartRefresh + 2.0-frameTolerance:
                # keep track of stop time/frame for later
                feedback.tStop = t  # not accounting for scr refresh
                feedback.frameNStop = frameN  # exact frame index
                win.timeOnFlip(feedback, 'tStopRefresh')  # time at next scr refresh
                feedback.setAutoDraw(False)
        
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
    
    # -------Ending Routine "trial"-------
    for thisComponent in trialComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    stimuli3streams.stop()  # ensure sound has stopped at end of routine
    trials_2.addData('stimuli3streams.started', stimuli3streams.tStartRefresh)
    trials_2.addData('stimuli3streams.stopped', stimuli3streams.tStopRefresh)
    stimuli3streamsoddballs.stop()  # ensure sound has stopped at end of routine
    trials_2.addData('stimuli3streamsoddballs.started', stimuli3streamsoddballs.tStartRefresh)
    trials_2.addData('stimuli3streamsoddballs.stopped', stimuli3streamsoddballs.tStopRefresh)
    trials_2.addData('text.started', text.tStartRefresh)
    trials_2.addData('text.stopped', text.tStopRefresh)
    trials_2.addData('textbox.text',textbox.text)
    trials_2.addData('textbox.started', textbox.tStartRefresh)
    trials_2.addData('textbox.stopped', textbox.tStopRefresh)
    trials_2.addData('arrow.started', arrow.tStartRefresh)
    trials_2.addData('arrow.stopped', arrow.tStopRefresh)
    trials_2.addData('feedback.started', feedback.tStartRefresh)
    trials_2.addData('feedback.stopped', feedback.tStopRefresh)
    thisExp.nextEntry()
    
# completed 1.0 repeats of 'trials_2'


# ------Prepare to start Routine "break_2"-------
continueRoutine = True
routineTimer.add(90.000000)
# update component parameters for each repeat
# keep track of which components have finished
break_2Components = [text_2]
for thisComponent in break_2Components:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
break_2Clock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "break_2"-------
while continueRoutine and routineTimer.getTime() > 0:
    # get current time
    t = break_2Clock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=break_2Clock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *text_2* updates
    if text_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        text_2.frameNStart = frameN  # exact frame index
        text_2.tStart = t  # local t and not account for scr refresh
        text_2.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(text_2, 'tStartRefresh')  # time at next scr refresh
        text_2.setAutoDraw(True)
    if text_2.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > text_2.tStartRefresh + 90.0-frameTolerance:
            # keep track of stop time/frame for later
            text_2.tStop = t  # not accounting for scr refresh
            text_2.frameNStop = frameN  # exact frame index
            win.timeOnFlip(text_2, 'tStopRefresh')  # time at next scr refresh
            text_2.setAutoDraw(False)
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in break_2Components:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "break_2"-------
for thisComponent in break_2Components:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('text_2.started', text_2.tStartRefresh)
thisExp.addData('text_2.stopped', text_2.tStopRefresh)

# ------Prepare to start Routine "Ready"-------
continueRoutine = True
# update component parameters for each repeat
# setup some python lists for storing info about the mouse_3
mouse_3.clicked_name = []
gotValidClick = False  # until a click is received
# keep track of which components have finished
ReadyComponents = [top_instr_txt_2, mouse_3, nextButton_R]
for thisComponent in ReadyComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
ReadyClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "Ready"-------
while continueRoutine:
    # get current time
    t = ReadyClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=ReadyClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *top_instr_txt_2* updates
    if top_instr_txt_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        top_instr_txt_2.frameNStart = frameN  # exact frame index
        top_instr_txt_2.tStart = t  # local t and not account for scr refresh
        top_instr_txt_2.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(top_instr_txt_2, 'tStartRefresh')  # time at next scr refresh
        top_instr_txt_2.setAutoDraw(True)
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
                    iter(nextButton_R)
                    clickableList = nextButton_R
                except:
                    clickableList = [nextButton_R]
                for obj in clickableList:
                    if obj.contains(mouse_3):
                        gotValidClick = True
                        mouse_3.clicked_name.append(obj.name)
                if gotValidClick:  
                    continueRoutine = False  # abort routine on response
    
    # *nextButton_R* updates
    if nextButton_R.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        nextButton_R.frameNStart = frameN  # exact frame index
        nextButton_R.tStart = t  # local t and not account for scr refresh
        nextButton_R.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(nextButton_R, 'tStartRefresh')  # time at next scr refresh
        nextButton_R.setAutoDraw(True)
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in ReadyComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "Ready"-------
for thisComponent in ReadyComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('top_instr_txt_2.started', top_instr_txt_2.tStartRefresh)
thisExp.addData('top_instr_txt_2.stopped', top_instr_txt_2.tStopRefresh)
# store data for thisExp (ExperimentHandler)
x, y = mouse_3.getPos()
buttons = mouse_3.getPressed()
if sum(buttons):
    # check if the mouse was inside our 'clickable' objects
    gotValidClick = False
    try:
        iter(nextButton_R)
        clickableList = nextButton_R
    except:
        clickableList = [nextButton_R]
    for obj in clickableList:
        if obj.contains(mouse_3):
            gotValidClick = True
            mouse_3.clicked_name.append(obj.name)
thisExp.addData('mouse_3.x', x)
thisExp.addData('mouse_3.y', y)
thisExp.addData('mouse_3.leftButton', buttons[0])
thisExp.addData('mouse_3.midButton', buttons[1])
thisExp.addData('mouse_3.rightButton', buttons[2])
if len(mouse_3.clicked_name):
    thisExp.addData('mouse_3.clicked_name', mouse_3.clicked_name[0])
thisExp.addData('mouse_3.started', mouse_3.tStart)
thisExp.addData('mouse_3.stopped', mouse_3.tStop)
thisExp.nextEntry()
thisExp.addData('nextButton_R.started', nextButton_R.tStartRefresh)
thisExp.addData('nextButton_R.stopped', nextButton_R.tStopRefresh)
# the Routine "Ready" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# set up handler to look after randomisation of conditions etc
trials_3 = data.TrialHandler(nReps=1.0, method='random', 
    extraInfo=expInfo, originPath=-1,
    trialList=data.importConditions('stimuliOddballsList.xlsx', selection='9:12'),
    seed=None, name='trials_3')
thisExp.addLoop(trials_3)  # add the loop to the experiment
thisTrial_3 = trials_3.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisTrial_3.rgb)
if thisTrial_3 != None:
    for paramName in thisTrial_3:
        exec('{} = thisTrial_3[paramName]'.format(paramName))

for thisTrial_3 in trials_3:
    currentLoop = trials_3
    # abbreviate parameter names if possible (e.g. rgb = thisTrial_3.rgb)
    if thisTrial_3 != None:
        for paramName in thisTrial_3:
            exec('{} = thisTrial_3[paramName]'.format(paramName))
    
    # ------Prepare to start Routine "trial"-------
    continueRoutine = True
    routineTimer.add(71.000000)
    # update component parameters for each repeat
    stimuli3streams.setSound(stimuli, secs=30.0, hamming=True)
    stimuli3streams.setVolume(1.0, log=False)
    stimuli3streamsoddballs.setSound(stimuli, secs=30.0, hamming=True)
    stimuli3streamsoddballs.setVolume(1.0, log=False)
    textbox.reset()
    # keep track of which components have finished
    trialComponents = [stimuli3streams, stimuli3streamsoddballs, text, textbox, arrow, feedback]
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
    while continueRoutine and routineTimer.getTime() > 0:
        # get current time
        t = trialClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=trialClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        # start/stop stimuli3streams
        if stimuli3streams.status == NOT_STARTED and tThisFlip >= 2.0-frameTolerance:
            # keep track of start time/frame for later
            stimuli3streams.frameNStart = frameN  # exact frame index
            stimuli3streams.tStart = t  # local t and not account for scr refresh
            stimuli3streams.tStartRefresh = tThisFlipGlobal  # on global time
            stimuli3streams.play(when=win)  # sync with win flip
        if stimuli3streams.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > stimuli3streams.tStartRefresh + 30.0-frameTolerance:
                # keep track of stop time/frame for later
                stimuli3streams.tStop = t  # not accounting for scr refresh
                stimuli3streams.frameNStop = frameN  # exact frame index
                win.timeOnFlip(stimuli3streams, 'tStopRefresh')  # time at next scr refresh
                stimuli3streams.stop()
        # start/stop stimuli3streamsoddballs
        if stimuli3streamsoddballs.status == NOT_STARTED and tThisFlip >= 34.0-frameTolerance:
            # keep track of start time/frame for later
            stimuli3streamsoddballs.frameNStart = frameN  # exact frame index
            stimuli3streamsoddballs.tStart = t  # local t and not account for scr refresh
            stimuli3streamsoddballs.tStartRefresh = tThisFlipGlobal  # on global time
            stimuli3streamsoddballs.play(when=win)  # sync with win flip
        if stimuli3streamsoddballs.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > stimuli3streamsoddballs.tStartRefresh + 30.0-frameTolerance:
                # keep track of stop time/frame for later
                stimuli3streamsoddballs.tStop = t  # not accounting for scr refresh
                stimuli3streamsoddballs.frameNStop = frameN  # exact frame index
                win.timeOnFlip(stimuli3streamsoddballs, 'tStopRefresh')  # time at next scr refresh
                stimuli3streamsoddballs.stop()
        
        # *text* updates
        if text.status == NOT_STARTED and tThisFlip >= 64.0-frameTolerance:
            # keep track of start time/frame for later
            text.frameNStart = frameN  # exact frame index
            text.tStart = t  # local t and not account for scr refresh
            text.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(text, 'tStartRefresh')  # time at next scr refresh
            text.setAutoDraw(True)
        if text.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > text.tStartRefresh + 5.0-frameTolerance:
                # keep track of stop time/frame for later
                text.tStop = t  # not accounting for scr refresh
                text.frameNStop = frameN  # exact frame index
                win.timeOnFlip(text, 'tStopRefresh')  # time at next scr refresh
                text.setAutoDraw(False)
        
        # *textbox* updates
        if textbox.status == NOT_STARTED and tThisFlip >= 64.0-frameTolerance:
            # keep track of start time/frame for later
            textbox.frameNStart = frameN  # exact frame index
            textbox.tStart = t  # local t and not account for scr refresh
            textbox.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(textbox, 'tStartRefresh')  # time at next scr refresh
            textbox.setAutoDraw(True)
        if textbox.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > textbox.tStartRefresh + 5.0-frameTolerance:
                # keep track of stop time/frame for later
                textbox.tStop = t  # not accounting for scr refresh
                textbox.frameNStop = frameN  # exact frame index
                win.timeOnFlip(textbox, 'tStopRefresh')  # time at next scr refresh
                textbox.setAutoDraw(False)
        
        # *arrow* updates
        if arrow.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            arrow.frameNStart = frameN  # exact frame index
            arrow.tStart = t  # local t and not account for scr refresh
            arrow.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(arrow, 'tStartRefresh')  # time at next scr refresh
            arrow.setAutoDraw(True)
        if arrow.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > arrow.tStartRefresh + 2.0-frameTolerance:
                # keep track of stop time/frame for later
                arrow.tStop = t  # not accounting for scr refresh
                arrow.frameNStop = frameN  # exact frame index
                win.timeOnFlip(arrow, 'tStopRefresh')  # time at next scr refresh
                arrow.setAutoDraw(False)
        
        # *feedback* updates
        if feedback.status == NOT_STARTED and tThisFlip >= 69.0-frameTolerance:
            # keep track of start time/frame for later
            feedback.frameNStart = frameN  # exact frame index
            feedback.tStart = t  # local t and not account for scr refresh
            feedback.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(feedback, 'tStartRefresh')  # time at next scr refresh
            feedback.setAutoDraw(True)
        if feedback.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > feedback.tStartRefresh + 2.0-frameTolerance:
                # keep track of stop time/frame for later
                feedback.tStop = t  # not accounting for scr refresh
                feedback.frameNStop = frameN  # exact frame index
                win.timeOnFlip(feedback, 'tStopRefresh')  # time at next scr refresh
                feedback.setAutoDraw(False)
        
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
    
    # -------Ending Routine "trial"-------
    for thisComponent in trialComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    stimuli3streams.stop()  # ensure sound has stopped at end of routine
    trials_3.addData('stimuli3streams.started', stimuli3streams.tStartRefresh)
    trials_3.addData('stimuli3streams.stopped', stimuli3streams.tStopRefresh)
    stimuli3streamsoddballs.stop()  # ensure sound has stopped at end of routine
    trials_3.addData('stimuli3streamsoddballs.started', stimuli3streamsoddballs.tStartRefresh)
    trials_3.addData('stimuli3streamsoddballs.stopped', stimuli3streamsoddballs.tStopRefresh)
    trials_3.addData('text.started', text.tStartRefresh)
    trials_3.addData('text.stopped', text.tStopRefresh)
    trials_3.addData('textbox.text',textbox.text)
    trials_3.addData('textbox.started', textbox.tStartRefresh)
    trials_3.addData('textbox.stopped', textbox.tStopRefresh)
    trials_3.addData('arrow.started', arrow.tStartRefresh)
    trials_3.addData('arrow.stopped', arrow.tStopRefresh)
    trials_3.addData('feedback.started', feedback.tStartRefresh)
    trials_3.addData('feedback.stopped', feedback.tStopRefresh)
    thisExp.nextEntry()
    
# completed 1.0 repeats of 'trials_3'


# ------Prepare to start Routine "break_2"-------
continueRoutine = True
routineTimer.add(90.000000)
# update component parameters for each repeat
# keep track of which components have finished
break_2Components = [text_2]
for thisComponent in break_2Components:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
break_2Clock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "break_2"-------
while continueRoutine and routineTimer.getTime() > 0:
    # get current time
    t = break_2Clock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=break_2Clock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *text_2* updates
    if text_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        text_2.frameNStart = frameN  # exact frame index
        text_2.tStart = t  # local t and not account for scr refresh
        text_2.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(text_2, 'tStartRefresh')  # time at next scr refresh
        text_2.setAutoDraw(True)
    if text_2.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > text_2.tStartRefresh + 90.0-frameTolerance:
            # keep track of stop time/frame for later
            text_2.tStop = t  # not accounting for scr refresh
            text_2.frameNStop = frameN  # exact frame index
            win.timeOnFlip(text_2, 'tStopRefresh')  # time at next scr refresh
            text_2.setAutoDraw(False)
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in break_2Components:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "break_2"-------
for thisComponent in break_2Components:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('text_2.started', text_2.tStartRefresh)
thisExp.addData('text_2.stopped', text_2.tStopRefresh)

# ------Prepare to start Routine "Ready"-------
continueRoutine = True
# update component parameters for each repeat
# setup some python lists for storing info about the mouse_3
mouse_3.clicked_name = []
gotValidClick = False  # until a click is received
# keep track of which components have finished
ReadyComponents = [top_instr_txt_2, mouse_3, nextButton_R]
for thisComponent in ReadyComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
ReadyClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "Ready"-------
while continueRoutine:
    # get current time
    t = ReadyClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=ReadyClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *top_instr_txt_2* updates
    if top_instr_txt_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        top_instr_txt_2.frameNStart = frameN  # exact frame index
        top_instr_txt_2.tStart = t  # local t and not account for scr refresh
        top_instr_txt_2.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(top_instr_txt_2, 'tStartRefresh')  # time at next scr refresh
        top_instr_txt_2.setAutoDraw(True)
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
                    iter(nextButton_R)
                    clickableList = nextButton_R
                except:
                    clickableList = [nextButton_R]
                for obj in clickableList:
                    if obj.contains(mouse_3):
                        gotValidClick = True
                        mouse_3.clicked_name.append(obj.name)
                if gotValidClick:  
                    continueRoutine = False  # abort routine on response
    
    # *nextButton_R* updates
    if nextButton_R.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        nextButton_R.frameNStart = frameN  # exact frame index
        nextButton_R.tStart = t  # local t and not account for scr refresh
        nextButton_R.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(nextButton_R, 'tStartRefresh')  # time at next scr refresh
        nextButton_R.setAutoDraw(True)
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in ReadyComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "Ready"-------
for thisComponent in ReadyComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('top_instr_txt_2.started', top_instr_txt_2.tStartRefresh)
thisExp.addData('top_instr_txt_2.stopped', top_instr_txt_2.tStopRefresh)
# store data for thisExp (ExperimentHandler)
x, y = mouse_3.getPos()
buttons = mouse_3.getPressed()
if sum(buttons):
    # check if the mouse was inside our 'clickable' objects
    gotValidClick = False
    try:
        iter(nextButton_R)
        clickableList = nextButton_R
    except:
        clickableList = [nextButton_R]
    for obj in clickableList:
        if obj.contains(mouse_3):
            gotValidClick = True
            mouse_3.clicked_name.append(obj.name)
thisExp.addData('mouse_3.x', x)
thisExp.addData('mouse_3.y', y)
thisExp.addData('mouse_3.leftButton', buttons[0])
thisExp.addData('mouse_3.midButton', buttons[1])
thisExp.addData('mouse_3.rightButton', buttons[2])
if len(mouse_3.clicked_name):
    thisExp.addData('mouse_3.clicked_name', mouse_3.clicked_name[0])
thisExp.addData('mouse_3.started', mouse_3.tStart)
thisExp.addData('mouse_3.stopped', mouse_3.tStop)
thisExp.nextEntry()
thisExp.addData('nextButton_R.started', nextButton_R.tStartRefresh)
thisExp.addData('nextButton_R.stopped', nextButton_R.tStopRefresh)
# the Routine "Ready" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# set up handler to look after randomisation of conditions etc
trials_4 = data.TrialHandler(nReps=1.0, method='random', 
    extraInfo=expInfo, originPath=-1,
    trialList=data.importConditions('stimuliOddballsList.xlsx', selection='13:15'),
    seed=None, name='trials_4')
thisExp.addLoop(trials_4)  # add the loop to the experiment
thisTrial_4 = trials_4.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisTrial_4.rgb)
if thisTrial_4 != None:
    for paramName in thisTrial_4:
        exec('{} = thisTrial_4[paramName]'.format(paramName))

for thisTrial_4 in trials_4:
    currentLoop = trials_4
    # abbreviate parameter names if possible (e.g. rgb = thisTrial_4.rgb)
    if thisTrial_4 != None:
        for paramName in thisTrial_4:
            exec('{} = thisTrial_4[paramName]'.format(paramName))
    
    # ------Prepare to start Routine "trial"-------
    continueRoutine = True
    routineTimer.add(71.000000)
    # update component parameters for each repeat
    stimuli3streams.setSound(stimuli, secs=30.0, hamming=True)
    stimuli3streams.setVolume(1.0, log=False)
    stimuli3streamsoddballs.setSound(stimuli, secs=30.0, hamming=True)
    stimuli3streamsoddballs.setVolume(1.0, log=False)
    textbox.reset()
    # keep track of which components have finished
    trialComponents = [stimuli3streams, stimuli3streamsoddballs, text, textbox, arrow, feedback]
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
    while continueRoutine and routineTimer.getTime() > 0:
        # get current time
        t = trialClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=trialClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        # start/stop stimuli3streams
        if stimuli3streams.status == NOT_STARTED and tThisFlip >= 2.0-frameTolerance:
            # keep track of start time/frame for later
            stimuli3streams.frameNStart = frameN  # exact frame index
            stimuli3streams.tStart = t  # local t and not account for scr refresh
            stimuli3streams.tStartRefresh = tThisFlipGlobal  # on global time
            stimuli3streams.play(when=win)  # sync with win flip
        if stimuli3streams.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > stimuli3streams.tStartRefresh + 30.0-frameTolerance:
                # keep track of stop time/frame for later
                stimuli3streams.tStop = t  # not accounting for scr refresh
                stimuli3streams.frameNStop = frameN  # exact frame index
                win.timeOnFlip(stimuli3streams, 'tStopRefresh')  # time at next scr refresh
                stimuli3streams.stop()
        # start/stop stimuli3streamsoddballs
        if stimuli3streamsoddballs.status == NOT_STARTED and tThisFlip >= 34.0-frameTolerance:
            # keep track of start time/frame for later
            stimuli3streamsoddballs.frameNStart = frameN  # exact frame index
            stimuli3streamsoddballs.tStart = t  # local t and not account for scr refresh
            stimuli3streamsoddballs.tStartRefresh = tThisFlipGlobal  # on global time
            stimuli3streamsoddballs.play(when=win)  # sync with win flip
        if stimuli3streamsoddballs.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > stimuli3streamsoddballs.tStartRefresh + 30.0-frameTolerance:
                # keep track of stop time/frame for later
                stimuli3streamsoddballs.tStop = t  # not accounting for scr refresh
                stimuli3streamsoddballs.frameNStop = frameN  # exact frame index
                win.timeOnFlip(stimuli3streamsoddballs, 'tStopRefresh')  # time at next scr refresh
                stimuli3streamsoddballs.stop()
        
        # *text* updates
        if text.status == NOT_STARTED and tThisFlip >= 64.0-frameTolerance:
            # keep track of start time/frame for later
            text.frameNStart = frameN  # exact frame index
            text.tStart = t  # local t and not account for scr refresh
            text.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(text, 'tStartRefresh')  # time at next scr refresh
            text.setAutoDraw(True)
        if text.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > text.tStartRefresh + 5.0-frameTolerance:
                # keep track of stop time/frame for later
                text.tStop = t  # not accounting for scr refresh
                text.frameNStop = frameN  # exact frame index
                win.timeOnFlip(text, 'tStopRefresh')  # time at next scr refresh
                text.setAutoDraw(False)
        
        # *textbox* updates
        if textbox.status == NOT_STARTED and tThisFlip >= 64.0-frameTolerance:
            # keep track of start time/frame for later
            textbox.frameNStart = frameN  # exact frame index
            textbox.tStart = t  # local t and not account for scr refresh
            textbox.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(textbox, 'tStartRefresh')  # time at next scr refresh
            textbox.setAutoDraw(True)
        if textbox.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > textbox.tStartRefresh + 5.0-frameTolerance:
                # keep track of stop time/frame for later
                textbox.tStop = t  # not accounting for scr refresh
                textbox.frameNStop = frameN  # exact frame index
                win.timeOnFlip(textbox, 'tStopRefresh')  # time at next scr refresh
                textbox.setAutoDraw(False)
        
        # *arrow* updates
        if arrow.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            arrow.frameNStart = frameN  # exact frame index
            arrow.tStart = t  # local t and not account for scr refresh
            arrow.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(arrow, 'tStartRefresh')  # time at next scr refresh
            arrow.setAutoDraw(True)
        if arrow.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > arrow.tStartRefresh + 2.0-frameTolerance:
                # keep track of stop time/frame for later
                arrow.tStop = t  # not accounting for scr refresh
                arrow.frameNStop = frameN  # exact frame index
                win.timeOnFlip(arrow, 'tStopRefresh')  # time at next scr refresh
                arrow.setAutoDraw(False)
        
        # *feedback* updates
        if feedback.status == NOT_STARTED and tThisFlip >= 69.0-frameTolerance:
            # keep track of start time/frame for later
            feedback.frameNStart = frameN  # exact frame index
            feedback.tStart = t  # local t and not account for scr refresh
            feedback.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(feedback, 'tStartRefresh')  # time at next scr refresh
            feedback.setAutoDraw(True)
        if feedback.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > feedback.tStartRefresh + 2.0-frameTolerance:
                # keep track of stop time/frame for later
                feedback.tStop = t  # not accounting for scr refresh
                feedback.frameNStop = frameN  # exact frame index
                win.timeOnFlip(feedback, 'tStopRefresh')  # time at next scr refresh
                feedback.setAutoDraw(False)
        
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
    
    # -------Ending Routine "trial"-------
    for thisComponent in trialComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    stimuli3streams.stop()  # ensure sound has stopped at end of routine
    trials_4.addData('stimuli3streams.started', stimuli3streams.tStartRefresh)
    trials_4.addData('stimuli3streams.stopped', stimuli3streams.tStopRefresh)
    stimuli3streamsoddballs.stop()  # ensure sound has stopped at end of routine
    trials_4.addData('stimuli3streamsoddballs.started', stimuli3streamsoddballs.tStartRefresh)
    trials_4.addData('stimuli3streamsoddballs.stopped', stimuli3streamsoddballs.tStopRefresh)
    trials_4.addData('text.started', text.tStartRefresh)
    trials_4.addData('text.stopped', text.tStopRefresh)
    trials_4.addData('textbox.text',textbox.text)
    trials_4.addData('textbox.started', textbox.tStartRefresh)
    trials_4.addData('textbox.stopped', textbox.tStopRefresh)
    trials_4.addData('arrow.started', arrow.tStartRefresh)
    trials_4.addData('arrow.stopped', arrow.tStopRefresh)
    trials_4.addData('feedback.started', feedback.tStartRefresh)
    trials_4.addData('feedback.stopped', feedback.tStopRefresh)
    thisExp.nextEntry()
    
# completed 1.0 repeats of 'trials_4'


# Flip one final time so any remaining win.callOnFlip() 
# and win.timeOnFlip() tasks get executed before quitting
win.flip()

# these shouldn't be strictly necessary (should auto-save)
thisExp.saveAsWideText(filename+'.csv', delim='auto')
thisExp.saveAsPickle(filename)
logging.flush()
# make sure everything is closed down
if eyetracker:
    eyetracker.setConnectionState(False)
thisExp.abort()  # or data files will save again on exit
win.close()
core.quit()
