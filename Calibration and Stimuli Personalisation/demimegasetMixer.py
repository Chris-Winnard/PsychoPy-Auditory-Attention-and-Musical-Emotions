# -*- coding: utf-8 -*-
"""
Created on Wed Mar 29 14:36:42 2023

@author: cjwin
"""

import numpy as np
import pathlib
from numpy.random import default_rng
rng = default_rng() 
import os


#EXCLUDING NEUTRAL ONES:
positiveValenceSets = np.array(["01-Harm", "01-Keyb", "01-Vibr", "03-Harm","03-Keyb","03-Vibr", "05-Harm","05-Keyb","05-Vibr","09-Harm","09-Keyb","09-Vibr","10-Harm", "10-Vibr", "10-Keyb"]) 
negativeValenceSets = np.array(["02-Harm", "02-Keyb", "02-Vibr", "04-Harm", "04-Keyb", "04-Vibr", "06-Harm", "06-Keyb", "06-Vibr", "07-Harm", "07-Keyb", "07-Vibr", "08-Harm", "08-Keyb", "08-Vibr","11-Harm", "11-Keyb", "11-Vibr"])

activeArousalSets = np.array(["01-Harm", "01-Keyb", "01-Vibr", "02-Harm", "02-Keyb", "02-Vibr", "06-Harm", "06-Keyb", "06-Vibr", "08-Harm","08-Keyb","08-Vibr", "10-Harm","10-Keyb","10-Vibr", "11-Harm","11-Keyb","11-Vibr"])
passiveArousalSets = np.array(["03-Harm","03-Keyb","03-Vibr", "04-Harm", "04-Keyb", "04-Vibr", "05-Harm","05-Keyb","05-Vibr", "07-Harm", "07-Keyb", "07-Vibr", 9, "12-Harm","12-Keyb","12-Vibr"])

dominantDominanceSets = np.array(["02-Harm", "02-Keyb", "02-Vibr", "04-Harm", "04-Keyb", "04-Vibr", "06-Harm", "06-Keyb", "06-Vibr", "08-Harm","08-Keyb","08-Vibr", "10-Harm","10-Keyb","10-Vibr", "11-Harm","11-Keyb","11-Vibr"])
submissiveDominanceSets = np.array(["03-Harm","03-Keyb","03-Vibr", "05-Harm","05-Keyb","05-Vibr", "07-Harm", "07-Keyb", "07-Vibr", "09-Harm","09-Keyb","09-Vibr"])

sameEmotionCombos1 = np.array(["03-Harm","03-Keyb","03-Vibr", "05-Harm","05-Keyb","05-Vibr", "09-Harm","09-Keyb","09-Vibr"]) #+ve val, high, dom
sameEmotionCombos2 = np.array(["02-Harm", "02-Keyb", "02-Vibr", "06-Harm", "06-Keyb", "06-Vibr", "08-Harm","08-Keyb","08-Vibr", "11-Harm","11-Keyb","11-Vibr"]) #-ve val, low, sub

sameArtists1 = np.array(["08-Harm","08-Keyb","08-Vibr", "09-Harm","09-Keyb","09-Vibr"]) #Kyle and Sebastian
sameArtists2 = np.array(["01-Harm", "02-Harm", "03-Harm","04-Harm"]) # George
sameArtists3 = np.array(["05-Harm","05-Keyb","05-Vibr", "06-Harm", "06-Keyb", "06-Vibr", "07-Harm", "07-Keyb", "07-Vibr", "10-Harm","10-Keyb","10-Vibr", "11-Harm","11-Keyb","11-Vibr", "12-Harm","12-Keyb","12-Vibr"]) #Daksh
sameArtists4 = np.array(["01-Keyb", "01-Vibr", "02-Keyb", "02-Vibr", "03-Keyb","03-Vibr", "04-Keyb", "04-Vibr"]) #Sebastian

validHemiMegasets_A = False
validHemiMegasets_B = False
megasetA = np.array(["02-Harm", "02-Keyb", "02-Vibr", "04-Harm", "04-Keyb", "04-Vibr", "07-Harm", "07-Keyb", "07-Vibr", "09-Harm","09-Keyb","09-Vibr", "10-Harm","10-Keyb","10-Vibr", "11-Harm","11-Keyb","11-Vibr"])
megasetB = np.array(["01-Harm", "01-Keyb", "01-Vibr", "03-Harm","03-Keyb","03-Vibr", "05-Harm","05-Keyb","05-Vibr", "06-Harm", "06-Keyb", "06-Vibr", 8, "12-Harm","12-Keyb","12-Vibr"])

def intersectionCounter(arr1, arr2):
    intersections = np.intersect1d(arr1, arr2)
    return len(intersections)

while validHemiMegasets_A == False:
    hemiMegasets_A = rng.choice(megasetA, size=18, replace=False)
    hemiMegaset_A1 = hemiMegasets_A[0:9]
    hemiMegaset_A2 = hemiMegasets_A[9:18]
    
    #Enough +ve/-ve pieces for each (Change to account for neutral ones?):
    if 10 >= intersectionCounter(positiveValenceSets, hemiMegaset_A1) >= 8 and 10 >= intersectionCounter(negativeValenceSets, hemiMegaset_A1) >= 8:
    
        if 10 >= intersectionCounter(positiveValenceSets, hemiMegaset_A2) >= 8 and 10 >= intersectionCounter(negativeValenceSets, hemiMegaset_A2) >= 8:
    
    #Enough active/passive pieces for each:
            if (10 >= intersectionCounter(activeArousalSets, hemiMegaset_A1) >= 8) and (10 >= intersectionCounter(passiveArousalSets, hemiMegaset_A1) >= 8):
            
                if 10 >= intersectionCounter(activeArousalSets, hemiMegaset_A2) >= 8 and 10 >= intersectionCounter(passiveArousalSets, hemiMegaset_A2) >= 8:
        
    #Enough dom/sub pieces for each (Change to account for neutral ones?):
                    if (10 >= intersectionCounter(dominantDominanceSets, hemiMegaset_A1) >= 8) and (10 >= intersectionCounter(submissiveDominanceSets, hemiMegaset_A1) >= 8):
                    
                        if 10 >= intersectionCounter(dominantDominanceSets, hemiMegaset_A2) >= 8 and 10 >= intersectionCounter(submissiveDominanceSets, hemiMegaset_A2) >= 8:                    
                       
    #To ensure as much "spread" as possible/reduce conflating emotions, try to forbid identical combinations:       
    #DOESN'T APPEAR TO BE POSSIBLE (OR AT LEAST, V HARD TO FIND ALLOWED COMBINATIONS)                          
                #            if intersectionCounter(sameEmotionCombos1, megasetA) <= 1 and intersectionCounter(sameEmotionCombos2, megasetA) <= 1:
                                
                 #               if intersectionCounter(sameEmotionCombos1, megasetB) <= 1 and intersectionCounter(sameEmotionCombos2, megasetB) <= 1:
                  #                  print(megasetA)
                   #                 print(megasetB)
                   #                 validMegasets = True
                    #            else:
                     #               print(intersectionCounter(sameEmotionCombos1, megasetA))
                      #              print(intersectionCounter(sameEmotionCombos1, megasetB))
                      
                      #It does not appear possible to have maximum "spread" in the artists as well
                       #   if intersectionCounter(sameArtists1, hemiMegaset_A1) == 1 and intersectionCounter(sameArtists2, hemiMegaset_A1) >= 1 and intersectionCounter(sameArtists3, hemiMegaset_A1) >= 1:
                      #        if intersectionCounter(sameArtists1, hemiMegaset_A2) == 1 and intersectionCounter(sameArtists2, hemiMegaset_A2) >= 1 and intersectionCounter(sameArtists3, hemiMegaset_A1) >= 1:
                                    print(hemiMegaset_A1)
                                    print(hemiMegaset_A2)
                                    validHemiMegasets_A = True

while validHemiMegasets_B == False:
    hemiMegasets_B = rng.choice(megasetB, size=18, replace=False)
    hemiMegaset_B1 = hemiMegasets_B[0:9]
    hemiMegaset_B2 = hemiMegasets_B[9:18]
    
    #Enough +ve/-ve pieces for each (Change to account for neutral ones?):
    if 2 >= intersectionCounter(positiveValenceSets, hemiMegaset_B1) >= 1 and 2 >= intersectionCounter(negativeValenceSets, hemiMegaset_B1) >= 1:
    
        if 2 >= intersectionCounter(positiveValenceSets, hemiMegaset_B2) >= 1 and 2 >= intersectionCounter(negativeValenceSets, hemiMegaset_B2) >= 1:
    
    #Enough active/passive pieces for each:
            if (2 >= intersectionCounter(activeArousalSets, hemiMegaset_B1) >= 1) and (2 >= intersectionCounter(passiveArousalSets, hemiMegaset_B1) >= 1):
            
                if 2 >= intersectionCounter(activeArousalSets, hemiMegaset_B2) >= 1 and 2 >= intersectionCounter(passiveArousalSets, hemiMegaset_B2) >= 1:
        
    #Enough dom/sub pieces for each (Change to account for neutral ones?):
                    if (2 >= intersectionCounter(dominantDominanceSets, hemiMegaset_B1) >= 1) and (2 >= intersectionCounter(submissiveDominanceSets, hemiMegaset_B1) >= 1):
                    
                        if 2 >= intersectionCounter(dominantDominanceSets, hemiMegaset_B2) >= 1 and 2 >= intersectionCounter(submissiveDominanceSets, hemiMegaset_B2) >= 1:                    
                       
    #To ensure as much "spread" as possible/reduce conflating emotions, try to forbid identical combinations:       
    #DOESN'T APPEAR TO BE POSSIBLE (OR AT LEAST, V HARD TO FIND ALLOWED COMBINATIONS)                          
                #            if intersectionCounter(sameEmotionCombos1, megasetA) <= 1 and intersectionCounter(sameEmotionCombos2, megasetA) <= 1:
                                
                 #               if intersectionCounter(sameEmotionCombos1, megasetB) <= 1 and intersectionCounter(sameEmotionCombos2, megasetB) <= 1:
                  #                  print(megasetA)
                   #                 print(megasetB)
                   #                 validMegasets = True
                    #            else:
                     #               print(intersectionCounter(sameEmotionCombos1, megasetA))
                      #              print(intersectionCounter(sameEmotionCombos1, megasetB))
                      
                      #It does not appear possible to have maximum "spread" in the artists as well
                       #   if intersectionCounter(sameArtists1, hemiMegaset_A1) == 1 and intersectionCounter(sameArtists2, hemiMegaset_A1) >= 1 and intersectionCounter(sameArtists3, hemiMegaset_A1) >= 1:
                      #        if intersectionCounter(sameArtists1, hemiMegaset_A2) == 1 and intersectionCounter(sameArtists2, hemiMegaset_A2) >= 1 and intersectionCounter(sameArtists3, hemiMegaset_A1) >= 1:
                                    print(hemiMegaset_B1)
                                    print(hemiMegaset_B2)
                                    validHemiMegasets_B = True

#Find the data path:
currentFolderPath = pathlib.Path(__file__).parent.resolve()
upperFolderPath = currentFolderPath.parent.resolve()
dataPath = str(upperFolderPath) + "/Data/"
hemiMegasetFile = (dataPath + "\Demimegasets.txt")
with open(hemiMegasetFile, 'w') as f:
    f.write("Demimegaset A1 - the sets to be attended to in part 3 by group A1: ")
    f.write(str(hemiMegaset_A1))
    f.write("\n")
    f.write("Demimegaset A2 - the sets to be attended to in part 3 by group A2: ")
    f.write(str(hemiMegaset_A2))
    f.write("\n")
    f.write("Demimegaset B1 - the sets to be attended to in part 3 by group B1: ")
    f.write(str(hemiMegaset_B1))
    f.write("\n")
    f.write("Demimegaset B2 - the sets to be attended to in part 3 by group B2: ")    
    f.write(str(hemiMegaset_B2))
    f.write("\n")
    f.write("Remember to add in leading zeros for single-digit numbers.")
    f.close
        
    print("Remember to add in leading zeros for single-digit numbers.")