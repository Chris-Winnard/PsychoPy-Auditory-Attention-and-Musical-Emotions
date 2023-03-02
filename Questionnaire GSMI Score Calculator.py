import pathlib
import glob
import os
import pandas as pd
import numpy as np

#Find the stimuli/demo stimuli paths:
thisFilePath = pathlib.Path(__file__).parent.resolve() #Where this file is located

#Find correct path for the gain files, and for outputs:
dataPath = str(thisFilePath) + "/Data"
participantPath = max(glob.glob(os.path.join(dataPath, '*/')), key=os.path.getmtime) #Last updated subfolder in Data folder.
#Because we run this at the end of the Questionnaire script, this will be the relevant one for the current participant.

#Change to the participant path, to access questionnaire response files and add the scores to these:
os.chdir(participantPath)

#Latest csv file created:
file_type = r'\*.csv'
files = glob.glob(participantPath + file_type)
questionnaireFile = max(files, key = os.path.getctime) #Latest file created, which will be the appt Excel file.
print(questionnaireFile)
df = pd.read_csv(questionnaireFile)

def negativeValue(response): #When the answer is a negative. E.g, a rating of 7 for "I find music unemotional" would be converted to 1 for emotion score
    return 8 - response

#######################################################################################################################################################
#Calculate perception score:
perceptionResponses = np.zeros(9)
for x in range(10, 19):        
    perceptionResponses[x-10] = df.iloc[0, x]
    
#Account for negative values:
perceptionResponses[2] = negativeValue(perceptionResponses[2])
perceptionResponses[4] = negativeValue(perceptionResponses[4])
perceptionResponses[7] = negativeValue(perceptionResponses[7])

perceptionScore = sum(perceptionResponses)


###########################################################################################################################################################
#Calculate emotion score:
emotionResponses = np.zeros(6)
for x in range(19, 25):        
    emotionResponses[x-19] = df.iloc[0, x]
    
#Account for negative values:
emotionResponses[1] = negativeValue(emotionResponses[1])

emotionScore = sum(emotionResponses)

df.insert(25, "Perception score", perceptionScore)
df.insert(26, "Emotion score", emotionScore)
df.to_csv(questionnaireFile)
