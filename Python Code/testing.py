'''import os
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

print(career)'''

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
plt.show()'''


## Tips for weak subjects

import pandas as pd
tips = pd.read_excel(r"G:\reps\minor-project\Datasets\Tips_all_subjects.xlsx")
tips.set_index('subject',inplace = True)
#weak = ['Mathematics','Computer']
#for i in weak:
#    for j in tips.loc[i].values:
#        print(j)



## websites

sites={"English":["British Council: Offers online courses, study materials, and resources to improve English skills.","Grammarly: Provides grammar tips, exercises, and writing enhancement tools.","BBC Learning English: Offers resources for improving English language skills."],
               "Mathematics":["NCERT Official Website: Provides textbooks and resources aligned with the curriculum.","Khan Academy: Offers video tutorials and practice exercises covering various math topics.","Cuemath: Provides math resources and practice material for students."],
               "Science":["National Science Digital Library (NSDL): Offers a wide range of educational resources related to science.","TopperLearning: Provides study materials, video lessons, and practice tests for science subjects.","Embibe: Offers study materials, practice questions, and tests for science subjects."],
               "Social_Studies":["NCERT Official Website: Provides textbooks and resources for social studies subjects.","BYJU'S: Offers study materials, videos, and interactive content for social studies.","Meritnation: Provides study materials and resources for social studies subjects"],
               "Logical_Reasoning":["TCY Online: Offers practice tests and study material for logical reasoning.","Indiabix: Provides logical reasoning questions and solutions for practice.","Gradeup: Offers practice questions and quizzes for logical reasoning."],
               "Computer":["Codecademy: Offers coding tutorials and exercises for beginners.","Udemy: Provides various computer-related courses at different levels.","GeeksforGeeks: Offers coding challenges, articles, and tutorials related to computer science."]}

weaksubs = ['Mathematics','Computer']

def GenTips_websites(sites, weaksubs):
    for i in weaksubs:
        print("Tips for ",i)
        for j in tips.loc[i].values:
            print(j)
        print("Websites that will be helpful in your studies")
        for j in sites[i]:
            print(j)
        print("")

GenTips_websites(sites, weaksubs)
