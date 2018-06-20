from sklearn.datasets import load_boston,load_iris
from sklearn import tree
from sklearn.neighbors import KNeighborsClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
from matplotlib import pyplot as plt
import numpy as np

iris = load_iris()

algo_dtc = tree.DecisionTreeClassifier()
algo_knn = KNeighborsClassifier(n_neighbors=5)

x_axis,y_axis_knn,y_axis_dtc = list(),list(),list()
for i in xrange(1,10):
    x_axis.append(i*10)

    train_data,test_data,train_target,test_target = train_test_split(iris.data,iris.target,test_size = i/float(10))
    # Training both algorithm
    trained_dtc = algo_dtc.fit(train_data,train_target)
    trained_knn = algo_knn.fit(train_data,train_target)

    #Predicting output from trained algorithm

    predict_dtc = trained_dtc.predict(test_data)
    predict_knn = trained_knn.predict(test_data)

    #Finding accuracy score for target_data
    y_axis_knn.append(accuracy_score(test_target,predict_knn)*100)
    y_axis_dtc.append(accuracy_score(test_target,predict_dtc)*100)
plt.title("KNN VS DTC")
#plt.plot(x_axis,y_axis_dtc)
#plt.plot(x_axis,y_axis_knn)
''' for bar graph plotting -- start'''
index = np.arange(len(x_axis))
bar_width = 0.33
plt.bar(index,y_axis_dtc,bar_width,color = 'b')
plt.xticks(index,x_axis)

plt.bar(index+bar_width,y_axis_knn,bar_width,color = 'g')
plt.xticks(index,x_axis)
''' for bar graph plotting -- end'''

plt.xlabel("Percentage of Test data")
plt.ylabel("Accuracy Score")
plt.legend(["DTC","KNN"])
plt.show()


