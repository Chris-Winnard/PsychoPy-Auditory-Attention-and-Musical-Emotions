import pathlib
import os
import glob
import xlsxwriter

##############################################################################################################
##############################################################################################################
#PART 1: CREATING LIST OF STIMULI AND TRIGGER FILES. EXCLUDE PRACTICE TRIAL MATERIALS AND ODDBALL TEST
#MATERIALS

# Workbook() takes one, non-optional, argument
# which is the filename that we want to create.
workbook = xlsxwriter.Workbook('stimuliList.xlsx')
 
# The workbook object is then used to add new
# worksheet via the add_worksheet() method.
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
 
worksheet.write('A1', 'stimuli_0')
i = 2 #Index for row in sheet.

for file in os.scandir(participantPath):
    stimCell = "A" + str(i)
    if file.name[3] != "2": #Set 2 ones are used for practice, so these are excluded.
        if ".wav" in file.name and "oddball" not in file.name: #Only audio, and no oddball files.      
            worksheet.write(stimCell, str(file.name))
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
    if file.name[11] != "2": #Set 2 ones are used for practice, so these are excluded.
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

# Workbook() takes one, non-optional, argument
# which is the filename that we want to create.
workbook = xlsxwriter.Workbook('practiceStimuliList.xlsx')
 
# The workbook object is then used to add new
# worksheet via the add_worksheet() method.
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
 
worksheet.write('A1', 'stimuli_0')
i = 2 #Index for row in sheet.

for file in os.scandir(participantPath):
    stimCell = "A" + str(i)
    if file.name[3] == "2": #Set 2 ones ONLY
        if ".wav" in file.name and "oddball" not in file.name: #Only audio, and no oddball files.      
            worksheet.write(stimCell, str(file.name))
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
    if file.name[11] == "2": #Set 2 ones are used for practice, so these are excluded.
        if ".wav" in file.name and "oddball" not in file.name:
            folderPlusFileName = "Trigger Files/" + str(file.name) #Here we need to specify the folder
#from main folder where the scripts are)               
            worksheet.write(trigCell, folderPlusFileName)
            j+=1

# Close the xlsx file
workbook.close()



##############################################################################################################
##############################################################################################################
#PART 3: CREATING LIST OF STIMULI AND TRIGGER FILES FOR ODDBALL TRIALS. EXCLUDE MATERIALS FOR PRACTICE TRIALS
#AND SINGLE-STREAM WORK. Since we're done with the above, here we can reuse i, j variables.

