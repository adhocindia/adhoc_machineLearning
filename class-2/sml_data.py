from sklearn.datasets import load_iris
from sklearn import tree
from sys import stdin,stdout

# Getting the data from the sklearn
data = load_iris()

#Printing the attributes
print data.feature_names

#algo for decision tree
algo = tree.DecisionTreeClassifier()

#Traing from data
trained_algo = algo.fit(data.data,data.target)

#Testing from the data
predict = trained_algo.predict([[5.9, 3. , 5.1, 1]])
stdout.write("%d\n"%(predict[0]))
