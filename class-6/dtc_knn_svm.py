import numpy as np 
from matplotlib import pyplot as plt 
from sklearn.metrics import accuracy_score
from sklearn.model_selection import train_test_split
from sklearn import tree
from sklearn.neighbors import KNeighborsClassifier
from sklearn.svm import SVC
from sklearn.datasets import load_iris,load_digits,load_wine,load_diabetes,load_breast_cancer

# loading data
iris = load_iris()
wine = load_wine()
digits = load_digits()
diabetes = load_diabetes()
b_cancer = load_breast_cancer()

# loading algos
algo_dtc = tree.DecisionTreeClassifier()
algo_knn = KNeighborsClassifier(n_neighbors=5)
algo_svm = SVC()

x_axis,y_axis_dtc,y_axis_knn,y_axis_svm = ['iris','wine','digits','diabetes','b_cancer'],list(),list(),list()

for data_type in x_axis:
    data_type = eval(data_type)
    #splitig train and test data
    train_data,test_data,train_target,test_target = train_test_split(data_type.data,data_type.target,test_size = .3)
    
    # training algo 
    trained_knn = algo_knn.fit(train_data,train_target)
    trained_dtc = algo_dtc.fit(train_data,train_target)
    trained_svm = algo_svm.fit(train_data,train_target)

    # predict data
    predicted_dtc = trained_dtc.predict(test_data)
    predicted_knn = trained_knn.predict(test_data)
    predicted_svm = trained_svm.predict(test_data)

    # percentage accuracy
    y_axis_dtc.append(accuracy_score(predicted_dtc,test_target)*100)
    y_axis_knn.append(accuracy_score(predicted_knn,test_target)*100)
    y_axis_svm.append(accuracy_score(predicted_svm,test_target)*100)

# Plotting graph
plt.title("DTC vs KNN vs SVM")
plt.xlabel("Datasets")
plt.ylabel("Accuracy Score")

index = np.arange(len(x_axis))
bar_width = 0.25

plt.bar(index,y_axis_dtc,bar_width,color = 'b')
plt.xticks(index,x_axis)

plt.bar(index + bar_width,y_axis_knn,bar_width,color = 'g')
plt.xticks(index,x_axis)

plt.bar(index + (bar_width*2),y_axis_svm,bar_width,color = 'r')
plt.xticks(index,x_axis)

plt.legend(["DTC","KNN","SVM"])
plt.show()

