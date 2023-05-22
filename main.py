from featureSearch import *

data = [0,1,2,3,4]


print("--Testing forward selection--")
bestFeatures = featureSearchForward(data)

print("--Testing backward elimination--")
bestFeatures = featureSearchBackward(data)

