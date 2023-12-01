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

