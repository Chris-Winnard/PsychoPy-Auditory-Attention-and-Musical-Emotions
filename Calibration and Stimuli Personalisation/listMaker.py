import pathlib
import os
import glob
import xlsxwriter
import re
import numpy as np
from numpy.random import default_rng

##############################################################################################################
##############################################################################################################
#Navigating the files, and also specifying which set is the practice set.
    
#Find the personalised stimuli path:
calibrationStimPrepPath = pathlib.Path(__file__).parent.resolve() #Where this file is located = pathlib.Path(__file__).parent.resolve() #Current folder path
upperFolderPath = calibrationStimPrepPath.parent.resolve() #Where this file is located.parent.resolve() #Path for next level up.
dataPath = str(upperFolderPath) + "/Data"

sub_paths = list() # Collect all files in sub directories
for root, dirs, files in os.walk(dataPath):
    sub_paths += [os.path.join(root,i) for i in files]

participantLastStimFile = max(sub_paths,key=os.path.getmtime) #Participant stimuli file that was just created- the most recently updated file
#in "Data" folder
participantPath = pathlib.Path(participantLastStimFile).parent.resolve() #Subfolder where that file is located, i.e participant's folder
participantPath = str(participantPath)

semimegasetFile = str(upperFolderPath) + "/Data/Semimegasets.txt"

#Also, change to the participant path so that this .xlsx list is saved there:
os.chdir(participantPath)

#When we write the stimuli filenames, we will also need to include the location relative to the PsychoPy
#paradigm scripts. This does NOT apply for trigger files, which are in a single general folder.
participantName = os.path.split(os.getcwd())[1]

if "Group A1" in participantPath:
    group = "Group A1"
    semimegaset = "Semimegaset A1"
    practiceSetPrimary = "Set04"
    practiceSetSecondary = "Set01"
elif "Group A2" in participantPath:
    group = "Group A2"
    semimegaset = "Semimegaset A2"
    practiceSetPrimary = "Set04"
    practiceSetSecondary = "Set01"
elif "Group B1" in participantPath:
    group = "Group B1"
    semimegaset = "Semimegaset B1"
    practiceSetPrimary = "Set01"
    practiceSetSecondary = "Set04"
elif "Group B2" in participantPath:
    group = "Group B2"
    semimegaset = "Semimegaset B2"
    practiceSetPrimary = "Set01"
    practiceSetSecondary = "Set04"

stimLoc = 'Data/' + group + '/' + participantName + '/'    
##############################################################################################################
##############################################################################################################
#PART 1: CREATING LIST OF STIMULI AND TRIGGER FILES. EXCLUDE PRACTICE TRIAL MATERIALS AND ODDBALL TEST
#MATERIALS

workbook = xlsxwriter.Workbook('stimuliList.xlsx')
worksheet = workbook.add_worksheet()

#First column- names of stimuli files, and second column- names of trigger files:
 
worksheet.write('A1', 'stimuli_0')
worksheet.write('B1', 'trigger')
worksheet.write('C1', 'music_attended')

#Need to get attendance data for part 3:
with open(semimegasetFile, 'r') as f:
    lines = f.readlines()
    i=-1
    for line in lines:
        i+=1
        if semimegaset in line:
            attendedFiles = line + lines[i+1] #It will span two lines.
    f.close
    
i = 2 #Index for row in sheet. 
for file in os.scandir(participantPath):
    stimCell = "A" + str(i)
    trigCell = "B" + str(i)
    attdCell = "C" + str(i)
    if practiceSetPrimary not in file.name and practiceSetSecondary not in file.name:
        if ".wav" in file.name and "Oddball" not in file.name: #Only audio, and no oddball files. 
            stimPath = stimLoc + str(file.name)
            worksheet.write(stimCell, stimPath)
            
            trigFilename = "trigger_" + str(file.name)
            trigFolderPlusFilename = "Trigger Files/" + trigFilename #Here we need to specify the folder
#from main folder where the scripts are)   
            worksheet.write(trigCell, trigFolderPlusFilename)
            
            if file.name[3:10] in attendedFiles:
                musicAttended = "Yes"
            else:
                musicAttended = "No"
            
            worksheet.write(attdCell, musicAttended)
            i+=1

# Close the xlsx file
workbook.close()



##############################################################################################################
##############################################################################################################
#PART 2: CREATING LIST OF STIMULI AND TRIGGER FILES FOR PRACTICE TRIALS. EXCLUDE MATERIALS FOR MAIN TRIALS AND
#ODDBALL TEST MATERIALS. This is EXACTLY the same as above, just the list has a different name, and we ONLY
#input practiceSet data to the lists. Since we're done with the above, here we can reuse i, j variables.

workbook = xlsxwriter.Workbook('practiceStimuliList.xlsx')
worksheet = workbook.add_worksheet()

#First column- names of stimuli files, and second column- names of trigger files:
 
worksheet.write('A1', 'stimuli_0')
worksheet.write('B1', 'trigger')
worksheet.write('C1', 'music_attended')
i = 2 #Index for row in sheet.

for file in os.scandir(participantPath):
    stimCell = "A" + str(i)
    trigCell = "B" + str(i)    
    attdCell = "C" + str(i)
    if practiceSetPrimary in file.name:
        if ".wav" in file.name and "Oddball" not in file.name: #Only audio, and no oddball files. 
            stimPath = stimLoc + str(file.name)
            worksheet.write(stimCell, stimPath)
            
            trigFilename = "trigger_" + str(file.name)
            trigFolderPlusFilename = "Trigger Files/" + trigFilename
            worksheet.write(trigCell, trigFolderPlusFilename)
            
            if file.name[3:10] in attendedFiles:
                musicAttended = "Yes"
            else:
                musicAttended = "No"

            worksheet.write(attdCell, musicAttended)
            i+=1

# Close the xlsx file
workbook.close()



##############################################################################################################
##############################################################################################################
#PART 3: CREATING LIST OF STIMULI AND TRIGGER FILES FOR ODDBALL TRIALS. EXCLUDE MATERIALS FOR PRACTICE TRIALS
#AND SINGLE-STREAM WORK. Since we're done with the above, here we can reuse i, j variables.

#First, let's read and convert the start time data. This will also be useful for part 4.
startTimesFile = participantPath + "\Oddball Start Times.txt"
startTimesData = open(startTimesFile, 'r')
lines = startTimesData.readlines()
startTimesData.close()

workbook = xlsxwriter.Workbook('oddballStimuliList.xlsx')
worksheet = workbook.add_worksheet()

 
worksheet.write('A1', 'stimuli_0')
worksheet.write('B1', 'attendedInst')
worksheet.write('C1', 'trigger')
worksheet.write('D1', 'attendedOddballs')
i = 2 #Index for row in sheet.

for file in os.scandir(participantPath):
    stimCell = "A" + str(i)
    attCell = "B" + str(i)
    trigCell = "C" + str(i)
    oddCell = "D" + str(i)
    if practiceSetPrimary not in file.name and practiceSetSecondary not in file.name:
        if ".wav" in file.name and "Oddball Test Mix" in file.name: #Only audio, only oddball files.
            if "Keyb Attended" in file.name:
                attendedInst = "Keyb"
            elif "Vibr Attended" in file.name:
                attendedInst = "Vibr"
            else:
                attendedInst = "Harm"
                
            stimPath = stimLoc + str(file.name)
            worksheet.write(stimCell, stimPath)
            worksheet.write(attCell, str(attendedInst))
            
            trigFilename = "trigger_" + str(file.name)
            trigFolderPlusFilename = stimLoc + "P2 Trigger Files/" + trigFilename
            worksheet.write(trigCell, trigFolderPlusFilename)
    
            for line in lines:
                if file.name[0:5] in line and line.count(attendedInst) ==2: #E.g "Set03 Vibr stream for Vibr Attended"...
                    oddballStartTimes = re.findall("\d+\.\d+", line) 
                    numOddballs = len(oddballStartTimes)
                    worksheet.write(oddCell, str(numOddballs))
            i+=1

workbook.close()

##############################################################################################################
##############################################################################################################
#PART 4: CREATING LIST OF STIMULI AND TRIGGER FILES FOR ODDBALL PRACTICE TRIALS. EXCLUDE MATERIALS FOR ALL OTHER
#TRIALS. Since we're done with the above, here we can reuse i/j/k variables.

workbook = xlsxwriter.Workbook('practiceOddballStimuliList.xlsx')
worksheet = workbook.add_worksheet()

#First two columns: names of stimuli files and attended instruments. Also add 4th- attended oddballs:
 
worksheet.write('A1', 'stimuli_0')
worksheet.write('B1', 'attendedInst')
worksheet.write('C1', 'trigger')
worksheet.write('D1', 'attendedOddballs')
i = 2 #Index for row in sheet.


for file in os.scandir(participantPath):
    stimCell = "A" + str(i)
    attCell = "B" + str(i)
    trigCell = "C" + str(i)
    oddCell = "D" + str(i)
    if practiceSetPrimary in file.name or practiceSetSecondary in file.name:
        if ".wav" in file.name and "Oddball Test Mix" in file.name: #Only audio, only oddball files.
            if "Keyb Attended" in file.name:
                attendedInst = "Keyb"
            elif "Vibr Attended" in file.name:
                attendedInst = "Vibr"
            else:
                attendedInst = "Harm"
                
            stimPath = stimLoc + str(file.name)
            worksheet.write(stimCell, stimPath)
            worksheet.write(attCell, str(attendedInst))
            
            trigFilename = "trigger_" + str(file.name)
            trigFolderPlusFilename = stimLoc + "P2 Trigger Files/" + trigFilename
            worksheet.write(trigCell, trigFolderPlusFilename)
            
            for line in lines:
                if file.name[0:5] in line and line.count(attendedInst) ==2:
                    oddballStartTimes = re.findall("\d+\.\d+", line)
                    numOddballs = len(oddballStartTimes)
                    worksheet.write(oddCell, str(numOddballs))
            i+=1


workbook.close()

#For parts 3 and 4 need to keep eye on how trigger filenames dealt with... not an issue if we
#run generate_trig.py before doing ANY of this, for some generic versions of the files/mixes.

os.chdir(calibrationStimPrepPath)