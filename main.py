from featureSearch import *

data = pd.read_csv('CS170_Spring_2023_Small_data__35.txt', sep=' ', header = None, engine = 'python', skipinitialspace = True)

bestFeatures = featureSearchForward(data)
print(bestFeatures) #[ [3,5,9,10] , 0.99 ], keep these features to get 99% accuracy

bestFeatures = featureSearchBackward(data)
print(bestFeatures) #[ [1,2,4,6,7,8] , 0.99 ], remove these features to get 99% accuracy



