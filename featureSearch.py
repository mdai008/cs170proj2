import random
from classifier import *

# def evalFunc(data,currFeatures,featureToBeAdded):
#     score = random.randint(0, 100)
    
#     return score

def defaultScore(data):
    # defaultScore = majority / total
    # https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.mode.html
    # https://pandas.pydata.org/docs/reference/api/pandas.Series.value_counts.html
    total = data.shape[0]
    labels = data.iloc[:,0]
    labelCounts = labels.value_counts() #pandas series
    labelCounts = labelCounts.tolist() #convert to list
    # print(total)
    # print(type(labelCounts))
    # print(labelCounts)
    labelCounts = labelCounts[0]
    # print(labelCounts)
    
    score = labelCounts / total

    return score

def featureSearchForward(data):
    featureNumbers = data.shape[1] - 1
    featureNumbers = range(featureNumbers)
    featureNumbers = np.array(featureNumbers) + 1
    featureNumbers = list(featureNumbers)
    # print(featureNumbers)
    # features = data[1:]
    featuresLen = len(featureNumbers)
    # print(featuresLen)
    usedFeatures = []
    bestFeatures = []
    bestScore = defaultScore(data)
    # print(bestScore)

    for i in range(featuresLen):
        print("Level " + str(i + 1) + " of the search tree.")
        featureToBeAdded = -1
        bestSoFar = 0 
        # currBestSoFar = 0
        # isBestSoFarFound = False
        for j in range(featuresLen):
            if featureNumbers[j] not in usedFeatures:
                # print(usedFeatures + featureNumbers[j])
                # print(type(usedFeatures))
                # print(type(featureNumbers[j]))
                # print(usedFeatures)
                # print(featureNumbers[j])
                
                # https://stackoverflow.com/questions/9452775/converting-numpy-dtypes-to-native-python-types
                # dummy = featureNumbers[j]
                # dummy = dummy.item()
                # print(type(dummy))
                
                dummyList = []
                dummyList.append(featureNumbers[j])
                # print(dummyList)
                
                accuracy = leaveOneOutCrossValidation(data,usedFeatures,dummyList)
                # accuracy = 1
                print("--Considering adding feature " + str(featureNumbers[j]) + ". Accuracy = " + str(accuracy))
                if accuracy > bestSoFar:
                    bestSoFar = accuracy
                    # print(featureNumbers[j])
                    featureToBeAdded = featureNumbers[j]
                    # print(featureToBeAdded)
        if featureToBeAdded == -1:
            print("Index error")
        else:
            usedFeatures.append(featureToBeAdded)
        # print(usedFeatures)
        print("Level " + str(i + 1) + ": added feature " + str(featureToBeAdded))
        if bestSoFar > bestScore:
            bestScore = bestSoFar
            bestFeatures = []
            for i in range(featuresLen):
                if featureNumbers[i] in usedFeatures:
                    bestFeatures.append(featureNumbers[i])
    return [bestFeatures,bestScore]

def featureSearchBackward(data):
    featureNumbers = data.shape[1] - 1
    featureNumbers = range(featureNumbers)
    featureNumbers = np.array(featureNumbers) + 1
    featureNumbers = list(featureNumbers)
    featuresLen = len(featureNumbers)
    
    removedFeatureIndex = []
    bestFeatures = []
    bestScore = defaultScore(data)

    for i in range(featuresLen):
        print("Level " + str(i + 1) + " of the search tree.")
        featureToBeRemoved = -1
        bestSoFar = 0 
        
        for j in range(featuresLen):
            if featureNumbers[j] not in removedFeatureIndex:
                dummyList = []
                dummyList.append(featureNumbers[j])
                accuracy = leaveOneOutCrossValidation(data,removedFeatureIndex,dummyList)
                print("--Considering removing feature " + str(featureNumbers[j]) + ". Accuracy = " + str(accuracy))
                if accuracy > bestSoFar:
                    bestSoFar = accuracy
                    featureToBeRemoved = featureNumbers[j]
        
        if featureToBeRemoved == -1:
            print("Index error")
        else:            
            removedFeatureIndex.append(featureToBeRemoved)
        
        print("Level " + str(i + 1) + ": removed feature " + str(featureToBeRemoved))
        if bestSoFar > bestScore:
            bestScore = bestSoFar
            bestFeatures = []
            for i in range(featuresLen):
                # if featureNumbers[i] not in removedFeatureIndex:
                if featureNumbers[i] in removedFeatureIndex:
                    bestFeatures.append(featureNumbers[i])
    
    
    
    return [bestFeatures,bestScore]






