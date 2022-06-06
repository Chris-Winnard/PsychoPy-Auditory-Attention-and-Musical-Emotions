#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
This experiment was created using PsychoPy3 Experiment Builder (v2022.1.3),
    on June 01, 2022, at 14:26
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
expName = 'First Attempt at Part 3 Expt Script'  # from the Builder filename that created this script
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
    originPath='C:\\Users\\Chris\\Documents\\Music Interestingness in the Brain\\PsychoPy Paradigm\\First Attempt at Part 3 Expt Script_lastrun.py',
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

# Initialize components for Routine "trial"
trialClock = core.Clock()
silentFilm = visual.MovieStim3(
    win=win, name='silentFilm', units='',
    noAudio = False,
    filename=None,
    ori=0.0, pos=(0, 0), opacity=None,
    loop=False, anchor='center',
    depth=0.0,
    )
attendNote = visual.TextStim(win=win, name='attendNote',
    text='Attend to the music\n',
    font='Open Sans',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-1.0);
dontAttendNote = visual.TextStim(win=win, name='dontAttendNote',
    text='Do not attend to the music\n',
    font='Open Sans',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-2.0);

# Create some handy timers
globalClock = core.Clock()  # to track the time since experiment started
routineTimer = core.CountdownTimer()  # to track time remaining of each (non-slip) routine 

# ------Prepare to start Routine "trial"-------
continueRoutine = True
routineTimer.add(5.000000)
# update component parameters for each repeat
# keep track of which components have finished
trialComponents = [silentFilm, attendNote, dontAttendNote]
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
    
    # *silentFilm* updates
    if silentFilm.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        silentFilm.frameNStart = frameN  # exact frame index
        silentFilm.tStart = t  # local t and not account for scr refresh
        silentFilm.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(silentFilm, 'tStartRefresh')  # time at next scr refresh
        silentFilm.setAutoDraw(True)
    if silentFilm.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > silentFilm.tStartRefresh + 1.0-frameTolerance:
            # keep track of stop time/frame for later
            silentFilm.tStop = t  # not accounting for scr refresh
            silentFilm.frameNStop = frameN  # exact frame index
            win.timeOnFlip(silentFilm, 'tStopRefresh')  # time at next scr refresh
            silentFilm.setAutoDraw(False)
    
    # *attendNote* updates
    if attendNote.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
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
    if dontAttendNote.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
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
silentFilm.stop()
thisExp.addData('attendNote.started', attendNote.tStartRefresh)
thisExp.addData('attendNote.stopped', attendNote.tStopRefresh)
thisExp.addData('dontAttendNote.started', dontAttendNote.tStartRefresh)
thisExp.addData('dontAttendNote.stopped', dontAttendNote.tStopRefresh)

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
