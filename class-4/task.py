'''
    Plotting a graph using test data on variable test percentage
'''
from matplotlib import pyplot as plot
from sklearn.datasets import load_iris
from sklearn import tree
from sklearn.metrics import accuracy_score
from sklearn.model_selection import train_test_split
iris = load_iris()
algo = tree.DecisionTreeClassifier()
y_axis_data,x_axis_data = list(),list()
for i in xrange(1,10):
    train,test,train_target,test_target = train_test_split(iris.data,iris.target,test_size = 1/float(10))
    trained_algo = algo.fit(train,train_target)
    predicted_data = trained_algo.predict(test)
    x_axis_data.append(i*10)
    y_axis_data.append(accuracy_score(test_target,predicted_data)*100)
plot.plot(x_axis_data,y_axis_data,'')
plot.title("Test data variation")
plot.xlabel("Percentage of test Data")
plot.ylabel("Accuracy")
plot.show()
    
