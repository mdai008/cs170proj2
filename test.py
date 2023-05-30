from featureSearch import *

# # --- PART 1 ---
# data = [0,1,2,3,4]


# print("--Testing forward selection--")
# bestFeatures = featureSearchForward(data)
# print("--Forward selection results--")
# print("Best features: ")
# print(bestFeatures[0])
# print("Best score: ")
# print(bestFeatures[1])

# print("--Testing backward elimination--")
# bestFeatures = featureSearchBackward(data)
# print("--Backward elimination results--")
# print("Best features: ")
# print(bestFeatures[0])
# print("Best score: ")
# print(bestFeatures[1])


# # --- PART 2 ---
# # columnNames = ["label","f1","f2","f3","f4","f5","f6","f7","f8","f9","f10"]
# # -- observation --
# # the original dataset has inconsistent delimiters, uses "  " and " -"
# # cleaned dataset uses only "  " delimiters
# # -- fix?, not yet --
# # using " " as delimiter works, since the extra space in front is ignored
# # -- fixed --
# # use skipinitialspace = True, which skips spaces after delimiter
# data = pd.read_csv('small-test-dataset.txt', sep=' ', header = None, engine = 'python', skipinitialspace = True)
# # print(data.head())
# # print(data.shape)

# currFeatures = [1,2,3,4,5,6,7,8,9]
# featureToBeAdded = [10]
# accuracy = leaveOneOutCrossValidation(data,currFeatures,featureToBeAdded)
# print(accuracy) #0.68


# data = pd.read_csv('small-test-dataset.txt', sep=' ', header = None, engine = 'python', skipinitialspace = True)
# currFeatures = [3,5]
# featureToBeAdded = [7]
# startTime = time.time()
# accuracy = leaveOneOutCrossValidation(data,currFeatures,featureToBeAdded)
# endTime = time.time()
# totalTime = (endTime - startTime) * 10**3
# print("Accuracy: " + str(accuracy)) #0.89
# print("Total time: " + str(totalTime) + " ms") #149 ms

# data = pd.read_csv('large-test-dataset-1.txt', sep=' ', header = None, engine = 'python', skipinitialspace = True)
# currFeatures = [1,15]
# featureToBeAdded = [27]
# startTime = time.time()
# accuracy = leaveOneOutCrossValidation(data,currFeatures,featureToBeAdded)
# endTime = time.time()
# totalTime = (endTime - startTime) * 10**3
# print("Accuracy: " + str(accuracy)) #0.949
# print("Total time: " + str(totalTime) + " ms") #4667 ms

