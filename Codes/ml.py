# Importing necessary libraries
from sklearn import datasets
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier

# Loading the iris dataset
iris = datasets.load_iris()
X = iris.data
y = iris.target

# Splitting the data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=1)

# Initializing the k-nearest neighbors classifier
knn = KNeighborsClassifier(n_neighbors=3)

# Fitting the classifier to the training data
knn.fit(X_train, y_train)

# Predicting the classes of the testing data
y_pred = knn.predict(X_test)

# Evaluating the performance of the classifier
print("Accuracy:", knn.score(X_test, y_test))
