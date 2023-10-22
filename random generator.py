import csv
import random

# Define the subjects
subjects = ["English", "Mathematics", "Science", "Social Studies", "Logical Reasoning", "Computer Awareness"]

# Create a CSV file and write the header
with open("Vocational_marks.csv", mode='w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(["Student ID",] + subjects)

    # Generate random data for 150 students
    for student_id in range(6501, 10001):
        marks = [random.randint(40, 54) for _ in subjects]
        """num = random.randint(1,10)
        if(num <= 2):
            marks = [random.randint(80, 95) for _ in subjects]
        elif(num > 2 and num < 7):
            marks = [random.randint(65, 85) for _ in subjects]
        else:
            marks = [random.randint(40, 65) for _ in subjects]"""
        
        writer.writerow([student_id] + marks)

print("CSV dataset generated successfully.")
