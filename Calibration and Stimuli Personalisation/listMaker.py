import pathlib
import os
import glob
import xlsxwriter
import re

##############################################################################################################
##############################################################################################################
#PART 1: CREATING LIST OF STIMULI AND TRIGGER FILES. EXCLUDE PRACTICE TRIAL MATERIALS AND ODDBALL TEST
#MATERIALS

workbook = xlsxwriter.Workbook('stimuliList.xlsx')
worksheet = workbook.add_worksheet()

#First column- names of stimuli files:
    
#Find the personalised stimuli path:
currentFolderPath = pathlib.Path(__file__).parent.resolve() #Current folder path
upperFolderPath = currentFolderPath.parent.resolve() #Path for next level up.
dataPath = str(upperFolderPath) + "/Data" 
participantPath = max(glob.glob(os.path.join(dataPath, '*/')), key=os.path.getmtime) #Last updated
#subfolder in Data folder.

#Also, change to the participant path so that this .xlsx list is saved there:
os.chdir(participantPath)

#When we write the stimuli filenames, we will also need to include the location relative to the PsychoPy
#paradigm scripts. This does NOT apply for trigger files, which are in a single general folder.
participantName = os.path.split(os.getcwd())[1]
stimLoc = 'Data/' + participantName + '/'
 
worksheet.write('A1', 'stimuli_0')
i = 2 #Index for row in sheet.

for file in os.scandir(participantPath):
    stimCell = "A" + str(i)
    if "Set2" not in file.name: #Set 2 ones are used for practice, so these are excluded.
        if ".wav" in file.name and "oddball" not in file.name: #Only audio, and no oddball files. 
            stimPath = stimLoc + str(file.name)
            worksheet.write(stimCell, stimPath)
            i+=1

#Second column- names of trigger files:
    
#Find the trigger file path:
currentFolderPath = pathlib.Path(__file__).parent.resolve() #Current folder path
upperFolderPath = currentFolderPath.parent.resolve() #Path for next level up.
triggerPath = str(upperFolderPath) + "/Trigger Files" 

#Change to the participant path, to find all the personalised stimuli:
worksheet.write('B1', 'trigger')
j = 2
for file in os.scandir(triggerPath):
    trigCell = "B" + str(j)
    if "Set2" not in file.name: #Set 2 ones are used for practice, so these are excluded.
        if ".wav" in file.name and "oddball" not in file.name:
            folderPlusFileName = "Trigger Files/" + str(file.name) #Here we need to specify the folder
#from main folder where the scripts are)               
            worksheet.write(trigCell, folderPlusFileName)
            j+=1

# Close the xlsx file
workbook.close()



##############################################################################################################
##############################################################################################################
#PART 2: CREATING LIST OF STIMULI AND TRIGGER FILES FOR PRACTICE TRIALS. EXCLUDE MATERIALS FOR MAIN TRIALS AND
#ODDBALL TEST MATERIALS. This is EXACTLY the same as above, just the list has a different name, and we ONLY
#input Set2 data to the lists. Since we're done with the above, here we can reuse i, j variables.

workbook = xlsxwriter.Workbook('practiceStimuliList.xlsx')
worksheet = workbook.add_worksheet()

#First column- names of stimuli files:
 
worksheet.write('A1', 'stimuli_0')
i = 2 #Index for row in sheet.

for file in os.scandir(participantPath):
    stimCell = "A" + str(i)
    if "Set2" in file.name: #Set 2 ones are used for practice, so excluded. #Set 2 ones ONLY
        if ".wav" in file.name and "oddball" not in file.name: #Only audio, and no oddball files. 
            stimPath = stimLoc + str(file.name)
            worksheet.write(stimCell, stimPath)
            i+=1

#Second column- names of trigger files:

worksheet.write('B1', 'trigger')
j = 2
for file in os.scandir(triggerPath):
    trigCell = "B" + str(j)
    if "Set2"  in file.name: #Set 2 ones ONLY
        if ".wav" in file.name and "oddball" not in file.name:
            folderPlusFileName = "Trigger Files/" + str(file.name)
            worksheet.write(trigCell, folderPlusFileName)
            j+=1

# Close the xlsx file
workbook.close()



##############################################################################################################
##############################################################################################################
#PART 3: CREATING LIST OF STIMULI AND TRIGGER FILES FOR ODDBALL TRIALS. EXCLUDE MATERIALS FOR PRACTICE TRIALS
#AND SINGLE-STREAM WORK. Since we're done with the above, here we can reuse i, j variables.

#First, let's read and convert the start time data. This will also be useful for part 4.
startTimesFile = participantPath + "Oddball Start Times.txt"
startTimesData = open(startTimesFile, 'r')
lines = startTimesData.readlines()
startTimesData.close()

workbook = xlsxwriter.Workbook('oddballStimuliList.xlsx')
worksheet = workbook.add_worksheet()

#First two columns: names of stimuli files and attended instruments. Also add 4th- attended oddballs:
 
worksheet.write('A1', 'stimuli_0')
worksheet.write('B1', 'attendedInst')
worksheet.write('D1', 'attendedOddballs')
i = 2 #Index for row in sheet.

for file in os.scandir(participantPath):
    stimCell = "A" + str(i)
    attCell = "B" + str(i)
    oddCell = "D" + str(i)
    if "Set2" not in file.name: #Set 2 ones are used for practice, so excluded.
        if ".wav" in file.name and "oddball test mix" in file.name: #Only audio, only oddball files.
            if "Keyb attended" in file.name:
                attendedInst = "Keyb"
            elif "Vibr attended" in file.name:
                attendedInst = "Vibr"
            else:
                attendedInst = "Harm"
            stimPath = stimLoc + str(file.name)
            worksheet.write(stimCell, stimPath)
            worksheet.write(attCell, str(attendedInst))
            for line in lines:
                if file.name[:3] in line and line.count(attendedInst) ==2: #E.g "Set3 Vibr stream for Vibr attended"...
                    oddballStartTimes = re.findall("\d+\.\d+", line) 
                    numOddballs = len(oddballStartTimes)
                    worksheet.write(oddCell, str(numOddballs))
            i+=1

#3rd column- triggers:
worksheet.write('C1', 'trigger')
j = 2
for file in os.scandir(triggerPath):
    trigCell = "C" + str(j)
    if "Set2" not in file.name: #Set 2 ones are used for practice, so excluded.
        if ".wav" in file.name and "oddball test mix" in file.name:
            folderPlusFileName = "Trigger Files/" + str(file.name)
            worksheet.write(trigCell, folderPlusFileName)
            j+=1

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
worksheet.write('D1', 'attendedOddballs')
i = 2 #Index for row in sheet.


for file in os.scandir(participantPath):
    stimCell = "A" + str(i)
    attCell = "B" + str(i)
    oddCell = "D" + str(i)
    if "Set2" in file.name:  #Set 2 ones ONLY
        if ".wav" in file.name and "oddball test mix" in file.name: #Only audio, only oddball files.
            if "Keyb attended" in file.name:
                attendedInst = "Keyb"
            elif "Vibr attended" in file.name:
                attendedInst = "Vibr"
            else:
                attendedInst = "Harm"
            stimPath = stimLoc + str(file.name)
            worksheet.write(stimCell, stimPath)
            worksheet.write(attCell, str(attendedInst))
            for line in lines:
                if "Set2" in line and line.count(attendedInst) ==2: #E.g "Set2 Vibr stream for Vibr attended"...
                    oddballStartTimes = re.findall("\d+\.\d+", line)
                    numOddballs = len(oddballStartTimes)
                    worksheet.write(oddCell, str(numOddballs))
            i+=1

#3rd column- triggers:
worksheet.write('C1', 'trigger')
j = 2
for file in os.scandir(triggerPath):
    trigCell = "C" + str(j)
    if "Set2" in file.name: #Set 2 ones ONLY
        if ".wav" in file.name and "oddball test mix" in file.name:
            folderPlusFileName = "Trigger Files/" + str(file.name)
            worksheet.write(trigCell, folderPlusFileName)
            j+=1

workbook.close()

#For parts 3 and 4 need to keep eye on how trigger filenames dealt with... not an issue if we
#run generate_trig.py before doing ANY of this, for some generic versions of the files/mixes.