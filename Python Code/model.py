import pandas as pd
import numpy as np
import pickle
import os

def find_file_path(file_name):
    for root, dirs, files in os.walk(os.path.abspath(os.sep)):
        if file_name in files:
            return os.path.join(root, file_name)

    return f"File '{file_name}' not found"

def Printpred(eng, math, sci, sst, logical, cmp, branch):
    career = pd.read_excel(find_file_path('student_marksheet_final3.xlsx'))
    from sklearn.preprocessing import LabelEncoder
    label_encoder = LabelEncoder()
    career['Branch'] = label_encoder.fit_transform(career['Branch'])
    x = np.array(career.iloc[:, 1:8])
    y = np.array(career.iloc[:, 8])
    from sklearn.model_selection import train_test_split 
    x_train, x_test, y_train, y_test = train_test_split(x, y,test_size = 0.3, random_state = 1)
    from sklearn.neighbors import KNeighborsClassifier
    from sklearn import metrics
    scores = {}
    knn = KNeighborsClassifier(n_neighbors=9)
    knn.fit(x_train, y_train)
    y_pred = knn.predict([[eng, math, sci, sst, logical, cmp, branch]])
    return y_pred

def PrintBranch(eng, math, sci, sst, logical, cmp):
    career = pd.read_excel(find_file_path('student_marksheet_final3.xlsx'))
    from sklearn.preprocessing import LabelEncoder
    label_encoder = LabelEncoder()
    career['Branch'] = label_encoder.fit_transform(career['Branch'])
    x = np.array(career.iloc[:, 1:7])
    y = np.array(career.iloc[:, 7])
    from sklearn.model_selection import train_test_split 
    x_train, x_test, y_train, y_test = train_test_split(x, y,test_size = 0.3, random_state = 1)
    from sklearn.neighbors import KNeighborsClassifier
    from sklearn import metrics
    scores = {}
    knn = KNeighborsClassifier(n_neighbors=9)
    knn.fit(x_train, y_train)
    y_pred = knn.predict([[eng, math, sci, sst, logical, cmp]])
    return y_pred.item()
