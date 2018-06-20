from sklearn.datasets import load_digits
from sklearn.svm import SVC
import numpy as np
from matplotlib import pyplot as plt
# loading digit images
digit = load_digits()

# only feature data
training_data = digit.data
#only target data
training_target = digit.target

# training data extract from original data
td_original = np.delete(training_data,-1,axis = 0)
# training target extract from original data
tt_original = np.delete(training_target,-1,axis = 0)

# calling support vector classifier
clf = SVC()
# training algo
trained = clf.fit(td_original,tt_original)
# now time for predection
output = trained.predict([digit.data[-2]])
print output
print digit.target[-2]
plt.imshow(digit.images[-2])
plt.show()
