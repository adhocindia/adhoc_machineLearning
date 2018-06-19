'''
    Supervised machine learning example
    To make computer differentiate between a apple and orange
'''

from sklearn import tree
from sys import stdin,stdout
# Features about apple and orange (arttribute)
## --------------------------------
type_ ={"smooth" : 0 ,"bumpy" : 1}
data = [
    [100,0],
    [130,0],
    [135,1],
    [150,1]
    ]
output = ["apple","apple","orange","orange"]
## --------------------------------

# decision tree algo call
algo = tree.DecisionTreeClassifier()

for i in range(10):
    # train from data
    trained_algo = algo.fit(data,output)

    # test form generated function
    predict = trained_algo.predict([[150,0]])
    stdout.write(predict[0]+"\n")
