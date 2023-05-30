from featureSearch import *

data = pd.read_csv('small-test-dataset.txt', sep=' ', header = None, engine = 'python', skipinitialspace = True)
currFeatures = [3,5]
featureToBeAdded = [7]
startTime = time.time()
accuracy = leaveOneOutCrossValidation(data,currFeatures,featureToBeAdded)
endTime = time.time()
totalTime = (endTime - startTime) * 10**3
print("Accuracy: " + str(accuracy)) #0.89
print("Total time: " + str(totalTime) + " ms") #149 ms

data = pd.read_csv('large-test-dataset-1.txt', sep=' ', header = None, engine = 'python', skipinitialspace = True)
currFeatures = [1,15]
featureToBeAdded = [27]
startTime = time.time()
accuracy = leaveOneOutCrossValidation(data,currFeatures,featureToBeAdded)
endTime = time.time()
totalTime = (endTime - startTime) * 10**3
print("Accuracy: " + str(accuracy)) #0.949
print("Total time: " + str(totalTime) + " ms") #4667 ms



