from featureSearch import *

data = [0,1,2,3,4]


print("--Testing forward selection--")
bestFeatures = featureSearchForward(data)
print("--Forward selection results--")
print("Best features: ")
print(bestFeatures[0])
print("Best score: ")
print(bestFeatures[1])

print("--Testing backward elimination--")
bestFeatures = featureSearchBackward(data)
print("--Backward elimination results--")
print("Best features: ")
print(bestFeatures[0])
print("Best score: ")
print(bestFeatures[1])

