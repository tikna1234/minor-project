import os
import numpy
import pandas as pd

def find_file_path(file_name):
    for root, dirs, files in os.walk(os.path.abspath(os.sep)):
        if file_name in files:
            return os.path.join(root, file_name)

    return f"File '{file_name}' not found in the current directory "

file_path = find_file_path('student_marksheet_final1.xlsx')
print(file_path)

career = pd.read_excel(find_file_path('student_marksheet_final1.xlsx'))

print(career)

'''import matplotlib.pyplot as plt
from sklearn.datasets import make_classification
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier

# Generating a sample dataset
X, y = make_classification(n_samples=1000, n_features=10, n_classes=2, random_state=42)

# Splitting the data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Lists to store accuracy values for different k values
k_values = list(range(1, 21))  # Change this range as needed
accuracy_values = []

# Training the KNN model for different values of k
for k in k_values:
    knn = KNeighborsClassifier(n_neighbors=k)
    knn.fit(X_train, y_train)
    accuracy = knn.score(X_test, y_test)
    accuracy_values.append(accuracy)

# Plotting the accuracy vs. k graph
plt.figure(figsize=(8, 6))
plt.plot(k_values, accuracy_values, marker='o', linestyle='-')
plt.title('Accuracy vs. Number of Neighbors (K)')
plt.xlabel('Number of Neighbors (K)')
plt.ylabel('Accuracy')
plt.xticks(k_values)
plt.grid(True)
plt.show()
