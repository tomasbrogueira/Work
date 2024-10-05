# Load libraries
import pandas as pd
from sklearn.tree import DecisionTreeClassifier, plot_tree # Import Decision Tree Classifier
from sklearn.model_selection import train_test_split # Import train_test_split function
from sklearn import metrics #Import scikit-learn metrics module for accuracy calculation
import matplotlib.pyplot as plt

col_names = ['y1', 'y2', 'y3', 'y4']
# load dataset
mydataset = pd.read_csv("C:/Users/Tomas/OneDrive/work/IST/Aprendizagem/hw1.csv")  # Use the absolute path to the file

X = mydataset.values[:,2:5] # let's assume that the first 10 columns are the features/variables
Y = mydataset.values[:,5] # let's assume that the 11th column has the target values/classes
print(X)
print(Y)
# Create Decision Tree classifer object
clf = DecisionTreeClassifier(criterion="entropy", max_depth=3)

# Train Decision Tree Classifer
clf = clf.fit(X,Y)

# Plot the decision tree
plt.figure(figsize=(20,10))  # Optional: set the size of the plot
plot_tree(clf, filled=True, feature_names=col_names[1:4], class_names=['A', 'B', 'C'])  # Optional: set the feature names and class names
plt.show()