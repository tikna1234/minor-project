import pandas as pd
import numpy as np
import pickle
def Printpred(eng, math, sci, sst, logical, cmp, branch):
    career = pd.read_excel(r"G:\reps\minor-project\Datasets\student_marksheet_final1.xlsx")
    from sklearn.preprocessing import LabelEncoder
    label_encoder = LabelEncoder()
    career['Courses'] = label_encoder.fit_transform(career['Courses'])
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

