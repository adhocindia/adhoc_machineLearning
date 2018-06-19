'''
    scraping data using sklearn
'''
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn import tree
# load iris data set
iris = load_iris()

# function to scrape data
'''
    three parameters
        - iris_data
        - iris_target
        - test_size = 0.1 (0.1 - > 10 %)
    four outputs
        - train_iris
        - test_iris
        - train_iris_target
        - test_iris_target
'''
train_iris,test_iris,train_iris_target,test_iris_target = train_test_split(iris.data,iris.target,test_size = 0.1)
print train_iris
print train_iris_target

# decision tree classifier
algo = tree.DecisionTreeClassifier()

# Training the dataset - > f(x)
trained_algo = algo.fit(train_iris,train_iris_target)

#Test the data set -> g(x)
output = trained_algo.predict(test_iris)

print output
print test_iris_target

#Comparing Accuracy
from sklearn.metrics import accuracy_score
print accuracy_score(output,test_iris_target)
