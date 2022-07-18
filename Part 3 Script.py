#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
This experiment was created using PsychoPy3 Experiment Builder (v2022.1.3),
    on June 15, 2022, at 13:15
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
from pyo import *
import random
import json

sys.path.append('.')
from constants import *

SOUNDCARD_DEVICE_NAME = 'DAC8PRO'
volume_level = 0.05
volume_ratio = [1, 1]
spk_volume = [x * volume_level for x in volume_ratio]

s = Server(nchnls=PART_1_OUT_CHANNELS, duplex=0)
devices = pa_get_output_devices()
for name in devices[0]:
    if SOUNDCARD_DEVICE_NAME in name:
        soundcard_idx = devices[1][devices[0].index(name)]
   #     print('sound card: ', name)
        s.setOutputDevice(soundcard_idx)
        break

s = s.boot()
s.start()

chns = [None]*(PART_1_OUT_CHANNELS-1)
mm = Mixer(outs=PART_1_OUT_CHANNELS)

# Ensure that relative paths start from the same directory as this script
_thisDir = os.path.dirname(os.path.abspath(__file__))
os.chdir(_thisDir)
# Store info about the experiment session
psychopyVersion = '2022.1.3'
expName = 'Part 3 Script'  # from the Builder filename that created this script
expInfo = {'participant': ''}
dlg = gui.DlgFromDict(dictionary=expInfo, sortKeys=False, title=expName)
if dlg.OK == False:
    core.quit()  # user pressed cancel
expInfo['date'] = data.getDateStr()  # add a simple timestamp
expInfo['expName'] = expName
expInfo['psychopyVersion'] = psychopyVersion

# Data file name stem = absolute path + name; later add .psyexp, .csv, .log, etc
filename = _thisDir + os.sep + u'data/%s/%s/experiment' % (expInfo['participant'], expName)
jsonfilename = filename + '_stimuli.json'
jsondata = {}
jsondata['trials'] = []

# An ExperimentHandler isn't essential but helps with data saving
thisExp = data.ExperimentHandler(name=expName, version='',
    extraInfo=expInfo, runtimeInfo=None,
    originPath='C:\\Users\\Chris\\Documents\\Music Interestingness in the Brain\\NEWEST PsychoPy-Auditory-Attention-and-Musical-Emotions-main\\PsychoPy-Auditory-Attention-and-Musical-Emotions-main\\Part 3 Script.py',
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
    text='You will be told to focus on either music or a silent film. They will then play together; please try not to blink/move during this period.\n\nNext, the experimenter will ask you about the stimulus you were told to focus on. You can take a break here before the next trial.\n\nIf you have any questions at all please ask the experimenters.',
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

# Initialize components for Routine "Ready"
ReadyClock = core.Clock()
top_instr_txt_3 = visual.TextStim(win=win, name='top_instr_txt_3',
    text='When you are ready, click "NEXT".',
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
attendNote = visual.TextStim(win=win, name='attendNote',
    text='Attend to the music\n',
    font='Open Sans',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);
dontAttendNote = visual.TextStim(win=win, name='dontAttendNote',
    text='Do NOT attend to the music\n',
    font='Open Sans',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-1.0);

# Initialize components for Routine "QuestionBreakPause"
QuestionBreakPauseClock = core.Clock()
top_instr_txt_4 = visual.TextStim(win=win, name='top_instr_txt_4',
    text='The experimenter will now ask you about the stimulus you were focusing on, and you can take a break. When you are ready for the next trial, click "NEXT".',
    font='Open Sans',
    pos=(0, 0.15), height=0.05, wrapWidth=1.8, ori=0.0, 
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
        if attendNote != FINISHED and dontAttendNote != FINISHED:
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
thisExp.nextEntry()
# end of playing part starting trig

# ------Prepare to start Routine "Ready"-------
continueRoutine = True
# update component parameters for each repeat
# setup some python lists for storing info about the mouse_4
mouse_4.clicked_name = []
gotValidClick = False  # until a click is received
# keep track of which components have finished
ReadyComponents = [top_instr_txt_3, mouse_4, nextButton_R1B]
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
# the Routine "Ready" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# set up handler to look after randomisation of conditions etc
block = data.TrialHandler(nReps=1.0, method='random', 
    extraInfo=expInfo, originPath=-1,
    trialList=data.importConditions('stimuliList.xlsx', selection='1:15'),
    seed=None, name='block')
thisExp.addLoop(block)  # add the loop to the experiment
thisBlock = block.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisBlock.rgb)
if thisBlock != None:
    for paramName in thisBlock:
        exec('{} = thisBlock[paramName]'.format(paramName))

idx = -1
for thisBlock in block:
    trial = {}
    idx += 1
    print(f'trial {idx}')
    currentLoop = block
    # abbreviate parameter names if possible (e.g. rgb = thisBlock.rgb)
    if thisBlock != None:
        for paramName in thisBlock:
            exec('{} = thisBlock[paramName]'.format(paramName))
    
    # ------Prepare to start Routine "trial"-------
    continueRoutine = True
    # update stimuliStarted parameter for each repeat
    stimuliStarted = False
    
    # keep track of which components have finished
    trialComponents = [attendNote, dontAttendNote]
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
    #Reset window minimisation parameter
    windowMinimised = False
    
    #Set random attend condition:
    attend = bool(random.getrandbits(1))
    
    # -------Run Routine "trial"-------
    while continueRoutine:
        # get current time
        t = trialClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=trialClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        #Minimise window when music starts:
        if tThisFlip >= 5 and windowMinimised == False:
            win.winHandle.minimize() # minimise the PsychoPy window
            #win.flip() # redraw the (minimised) window
            windowMinimised=True
        
        #Maximise window when music ends:
        if  tThisFlip >= PART_1_STIMULI_LEN-frameTolerance+5 and windowMinimised == True:
            win.winHandle.maximize()
            win.winHandle.activate()
            windowMinimised = False
            
        # *attendNote* updates
        if attend==True and attendNote.status == NOT_STARTED:
            # keep track of start time/frame for later
            attendNote.frameNStart = frameN  # exact frame index
            attendNote.tStart = t  # local t and not account for scr refresh
            attendNote.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(attendNote, 'tStartRefresh')  # time at next scr refresh
            attendNote.setAutoDraw(True)
        if attendNote.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > attendNote.tStartRefresh + 5.0-frameTolerance:
                # keep track of stop time/frame for later
                attendNote.tStop = t  # not accounting for scr refresh
                attendNote.frameNStop = frameN  # exact frame index
                win.timeOnFlip(attendNote, 'tStopRefresh')  # time at next scr refresh
                attendNote.setAutoDraw(False)
        
        # *dontAttendNote* updates
        if attend==False and dontAttendNote.status == NOT_STARTED:
            # keep track of start time/frame for later
            dontAttendNote.frameNStart = frameN  # exact frame index
            dontAttendNote.tStart = t  # local t and not account for scr refresh
            dontAttendNote.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(dontAttendNote, 'tStartRefresh')  # time at next scr refresh
            dontAttendNote.setAutoDraw(True)
        if dontAttendNote.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > dontAttendNote.tStartRefresh + 5.0-frameTolerance:
                # keep track of stop time/frame for later
                dontAttendNote.tStop = t  # not accounting for scr refresh
                dontAttendNote.frameNStop = frameN  # exact frame index
                win.timeOnFlip(dontAttendNote, 'tStopRefresh')  # time at next scr refresh
                dontAttendNote.setAutoDraw(False)
        
        if stimuliStarted == False and (attendNote.status == FINISHED or dontAttendNote.status == FINISHED):
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
            trial['stimulies'] = []
            for i in range(0, PART_1_OUT_CHANNELS-1):
                spk_name = "stimuli_{}".format(i)
                print(f'{spk_name}: {globals()[spk_name]}')
                trial['stimulies'].append(os.path.abspath(globals()[spk_name]))
                chns[i] = SfPlayer(globals()[spk_name])
                mm.delInput(i+1)
                mm.addInput(i+1,chns[i])
        
            jsondata['trials'].append(trial) 
            
            for i in range(PART_1_OUT_CHANNELS):
                for j in range(PART_1_OUT_CHANNELS):
                    mm.setAmp(i,j,0)
            # set volume for output
            output_idx = [0] + list(range(1,PART_1_OUT_CHANNELS))
            input_idx = [0] + list(range(1,PART_1_OUT_CHANNELS))
            for i in input_idx:
                mm.setAmp(i, output_idx[i], spk_volume[i])
            mm.out()
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
        
        if tThisFlip >= PART_3_STIMULI_LEN+5.0-frameTolerance:
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
    
    if attend == True:
        block.addData('Attended the music')
        print("attended")
    else:
        block.addData('Did not attend the music')
        print("not attended")
    # the Routine "trial" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # ------Prepare to start Routine "QuestionBreakPause"-------
    continueRoutine = True
    # update component parameters for each repeat
    # setup some python lists for storing info about the mouse_4
    mouse_4.clicked_name = []
    gotValidClick = False  # until a click is received
    # keep track of which components have finished
    QuestionBreakPauseComponents = [top_instr_txt_4, mouse_4, nextButton_R1B]
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
        
        # *top_instr_txt_4* updates
        if top_instr_txt_4.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            top_instr_txt_4.frameNStart = frameN  # exact frame index
            top_instr_txt_4.tStart = t  # local t and not account for scr refresh
            top_instr_txt_4.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(top_instr_txt_4, 'tStartRefresh')  # time at next scr refresh
            top_instr_txt_4.setAutoDraw(True)
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
    # the Routine "QuestionBreakPause" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
# completed 1.0 repeats of 'block'

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
