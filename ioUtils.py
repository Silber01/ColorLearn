import os
import json


def getinitLearned():
    initLearnLoc = "initFiles/initLearned.json"
    with open(initLearnLoc, "r") as read_file:
        return json.load(read_file)

def getLearned():
    with open("learned.json", "r") as read_file:
        return json.load(read_file)

def setLearned(learnData):
    with open("learned.json", "w") as write_file:
        json.dump(learnData, write_file)

def decTTLs():
    newLearned = {}
    learned = getLearned()
    for colorType in learned:
        newColorType = []
        for c in learned[colorType]:
            if c[1] != -1:  #-1 signals permanent data
                c[1] -= 1
            if c[1] != 0:
                newColorType.append(c)
        newLearned[colorType] = newColorType
    setLearned(newLearned)
