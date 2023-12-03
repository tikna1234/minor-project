'''import csv
import random

# Define the subjects
subjects = ["English", "Mathematics", "Science", "Social Studies", "Logical Reasoning", "Computer Awareness"]

# Create a CSV file and write the header
with open("Vocational_marks.csv", mode='w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(["Student ID",] + subjects)

    # Generate random data for 150 students
    for student_id in range(1, 667):
        for a in subject:
            if (a == 'English')
            
        marks = [random.randint(40, 54) for _ in subjects]
        """num = random.randint(1,10)
        if(num <= 2):
            marks = [random.randint(80, 95) for _ in subjects]
        elif(num > 2 and num < 7):
            marks = [random.randint(65, 85) for _ in subjects]
        else:
            marks = [random.randint(40, 65) for _ in subjects]
            marks = [random.randint(40, 54) for _ in subjects]"""
        
        writer.writerow([student_id] + marks)

print("CSV dataset generated successfully.")'''

import csv
import random

# Define the subjects and their corresponding criteria
subjects = ["English", "Mathematics", "Science","Logical Reasoning", "Computer Awareness"]

# Criteria for each set of marks
criteria = [
    {"English": (56, 74), "Mathematics": (70, 74), "Science": (60, 74), "Social Studies":(40, 74), "Logical Reasoning": (65, 74), "Computer Awareness": (70, 74)},
    {"English": (56, 74), "Mathematics": (70, 74), "Science": (70, 74), "Social Studies":(40, 74), "Logical Reasoning": (60, 74), "Computer Awareness": (65, 74)},
    {"English": (60, 74), "Mathematics": (70, 74), "Science": (70, 74), "Social Studies":(40, 74), "Logical Reasoning": (56, 74), "Computer Awareness": (65, 74)},
    {"English": (60, 74), "Mathematics": (70, 74), "Science": (70, 74), "Social Studies":(40, 74), "Logical Reasoning": (65, 74), "Computer Awareness": (56, 74)},
    {"English": (70, 74), "Mathematics": (60, 74), "Science": (70, 74), "Social Studies":(40, 74), "Logical Reasoning": (65, 74), "Computer Awareness": (56, 74)}
]

# Create and write data to the CSV file
with open("iti_marks1.csv", "w", newline="") as csvfile:
    writer = csv.writer(csvfile)
    
    # Write the header row with subject names
    writer.writerow(["Student ID"] + subjects)

    # Generate 20 random records for each criteria
    for i in range(3501):
        for criterion in criteria:
            student_id = f"Student_{i+1}_{criteria.index(criterion) + 1}"
            marks = {subject: random.randint(criterion[subject][0], criterion[subject][1]) for subject in subjects}
            writer.writerow([student_id] + list(marks.values()))

print("CSV dataset generated successfully.")
