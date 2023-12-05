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
subjects = ["English", "Mathematics", "Science","Social Studies","Logical Reasoning", "Computer Awareness"]

# Criteria for each set of marks
criteria = [
    {"English": (40, 55), "Mathematics": (45, 55), "Science": (40, 55), "Social Studies":(35, 45), "Logical Reasoning": (41, 50), "Computer Awareness": (45, 55),"Course":"Vocational in Computer Science and Information Technology"},
    {"English": (40, 55), "Mathematics": (45, 55), "Science": (45, 55), "Social Studies":(35, 45), "Logical Reasoning": (41, 50), "Computer Awareness": (41, 50),"Course":"Vocational in Mechanical and Electrical"},
    {"English": (40, 55), "Mathematics": (41, 50), "Science": (35, 45), "Social Studies":(45, 55), "Logical Reasoning": (45, 55), "Computer Awareness": (41, 50),"Course":"Vocational in Construction and Design"},
    {"English": (40, 55), "Mathematics": (41, 50), "Science": (35, 45), "Social Studies":(45, 55), "Logical Reasoning": (41, 50), "Computer Awareness": (41, 50),"Course":"Vocational in Hospitality and Event Management"},
    {"English": (40, 55), "Mathematics": (45, 55), "Science": (35, 45), "Social Studies":(35, 45), "Logical Reasoning": (45, 55), "Computer Awareness": (41, 50),"Course":"Vocational in Finance, Business and Marketing"},
    {"English": (40, 55), "Mathematics": (35, 45), "Science": (35, 45), "Social Studies":(45, 55), "Logical Reasoning": (41, 50), "Computer Awareness": (41, 50),"Course":"Vocational in Arts and Media"},
    {"English": (40, 55), "Mathematics": (35, 45), "Science": (45, 55), "Social Studies":(35, 45), "Logical Reasoning": (41, 50), "Computer Awareness": (41, 50),"Course":"Vocational in Physical Education and Wellness"},
    {"English": (35, 40), "Mathematics": (35, 40), "Science": (35, 40), "Social Studies":(35, 40), "Logical Reasoning": (35, 40), "Computer Awareness": (35, 40),"Course":"Vocational in Culinary Studies and Cooking"}
]

# Create and write data to the CSV file
with open("Vocational_marks2.csv", "w", newline="") as csvfile:
    writer = csv.writer(csvfile)
    
    # Write the header row with subject names
    writer.writerow(["Student ID"] + subjects+["Branch"]+["Course"])

    # Generate 20 random records for each criteria
    for i in range(3000):
        for criterion in criteria:
            student_id = f"Student_{i+1}_{criteria.index(criterion) + 1}"
            marks = {subject: random.randint(criterion[subject][0], criterion[subject][1]) for subject in subjects}
            writer.writerow([student_id] + list(marks.values())+ ["Vocational"] + [criterion['Course']])

print("CSV dataset generated successfully.")
