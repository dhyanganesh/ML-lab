import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from scipy.spatial.distance import cdist

# Load Fruit dataset
fruit = pd.read_csv("fruit.csv")
fruit_X = fruit.drop("fruit_label", axis=1)
fruit_y = fruit["fruit_label"]

# Define distance metrics
def manhattan_distance(x1, x2):
    return np.sum(np.abs(x1 - x2))

# Define KNN classifier
def KNN_classifier(X_train, y_train, X_test, k, distance_metric):
    y_pred = []
    for i in range(X_test.shape[0]):
        distances = cdist(X_train, [X_test.iloc[i]], metric=distance_metric)
        nearest_indices = np.argsort(distances, axis=0)[:k].flatten()
        nearest_labels = y_train.iloc[nearest_indices]
        label_counts = np.bincount(nearest_labels)
        predicted_label = np.argmax(label_counts)
        y_pred.append(predicted_label)
    return y_pred

# Define function to split dataset into training and testing
def split_data(X, y, method):
    if method == "80-20":
        X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
    else:
        raise ValueError("Invalid split method")
    return X_train, X_test, y_train, y_test

# Run KNN classifier for Fruit dataset
for method in ["80-20"]:
    print(f"Results for Fruit dataset using {method} split and Manhattan distance:")
    X_train, X_test, y_train, y_test = split_data(fruit_X, fruit_y, method)
    for k in [5]:
        y_pred = KNN_classifier(X_train, y_train, X_test, k, manhattan_distance)
        accuracy = sum(y_pred[i] == y_test.iloc[i] for i in range(len(y_test))) / len(y_test)
        print(f"k={k}: Accuracy = {accuracy}")
    print()
