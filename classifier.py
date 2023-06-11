import numpy as np
import pandas as pd
import math
import time


def leaveOneOutCrossValidation(data,currFeatures,featureToBeAdded):
    # accuracy = correct classifications / total data points
    # index data using a tree 
    correctClassifications = 0
    numRows = len(data) #100
    labels = data.iloc[:,0].values #100 x 1 numpy array
    features = data.iloc[:,currFeatures+featureToBeAdded].values #100 x 10
    # for i in range(numRows):
    #     features[i] = list(map(float, features[i]))
    

    for i in range(numRows):
        objToClassify = features[i]
        objToClassifyLabel = labels[i]
        nearestNeighborDist = math.inf
        nearestNeighborIndex = 111
        nearestNeighborLabel = 111
        # print("Object " + str(i+1) + " is of class " + str(int(objToClassifyLabel)))
        # https://www.geeksforgeeks.org/how-to-check-the-execution-time-of-python-script/
        startTime = time.time()
        for j in range(numRows):
            if i != j:
                distance = math.sqrt(sum(pow((objToClassify - features[j]),2)))
                if distance < nearestNeighborDist:
                    nearestNeighborDist = distance
                    nearestNeighborIndex = j
                    nearestNeighborLabel = labels[j]
        endTime = time.time()
        totalTime = (endTime - startTime) * 10**3
        # print("Its nearest neighbor is Object " + str(nearestNeighborIndex+1) + " of class " + str(int(nearestNeighborLabel)))
        # print("Time taken: " + str(totalTime) + " ms")
        if objToClassifyLabel == nearestNeighborLabel:
            correctClassifications = correctClassifications + 1


    accuracy = correctClassifications / numRows
    return accuracy










