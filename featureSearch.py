import random
from classifier import *

def evalFunc(data,currFeatures,featureToBeAdded):
    score = random.randint(0, 100)
    
    return score

def defaultScore(data):
    # defaultScore = majority / total
    score = 50
    
    return score

def featureSearchForward(dataArray):
    features = dataArray[1:]
    featuresLen = len(features)
    usedFeatures = []
    bestFeatures = []
    bestScore = defaultScore(features)

    for i in range(featuresLen):
        print("Level " + str(i + 1) + " of the search tree.")
        featureToBeAdded = 0
        bestSoFar = 0 
        for j in range(featuresLen):
            if features[j] not in usedFeatures:    
                accuracy = evalFunc(features,usedFeatures,features[j])
                print("--Considering adding feature " + str(features[j]) + ". Accuracy = " + str(accuracy))
                if accuracy > bestSoFar:
                    bestSoFar = accuracy
                    featureToBeAdded = features[j]
        usedFeatures.append(featureToBeAdded)
        print("Level " + str(i + 1) + ": added feature " + str(featureToBeAdded))
        if bestSoFar > bestScore:
            bestScore = bestSoFar
            bestFeatures = []
            for i in range(featuresLen):
                if features[i] in usedFeatures:
                    bestFeatures.append(features[i])
    return [bestFeatures,bestScore]

def featureSearchBackward(dataArray):
    features = dataArray[1:]
    featuresLen = len(features)
    removedFeatureIndex = []
    bestFeatures = []
    bestScore = defaultScore(features)

    for i in range(featuresLen):
        print("Level " + str(i + 1) + " of the search tree.")
        featureToBeRemoved = 0
        bestSoFar = 0 
        for j in range(featuresLen):
            if features[j] not in removedFeatureIndex:    
                accuracy = evalFunc(features,removedFeatureIndex,features[j])
                print("--Considering removing feature " + str(features[j]) + ". Accuracy = " + str(accuracy))
                if accuracy > bestSoFar:
                    bestSoFar = accuracy
                    featureToBeRemoved = features[j]
        removedFeatureIndex.append(featureToBeRemoved)
        print("Level " + str(i + 1) + ": removed feature " + str(featureToBeRemoved))
        if bestSoFar > bestScore:
            bestScore = bestSoFar
            bestFeatures = []
            for i in range(featuresLen):
                if features[i] not in removedFeatureIndex:
                    bestFeatures.append(features[i])
    return [bestFeatures,bestScore]