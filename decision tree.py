from sklearn.datasets import load_iris
from sklearn.tree import DecisionTreeClassifier, export_text

# Load dataset
iris = load_iris()
X, y = iris.data, iris.target

# Create Decision Tree
clf = DecisionTreeClassifier()
clf = clf.fit(X, y)

# Print the tree
tree_rules = export_text(clf, feature_names=iris.feature_names)
print(tree_rules)
