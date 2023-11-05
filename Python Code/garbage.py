'''import csv
import random

subjects = ["English", "Mathematics", "Science", "Social Studies", "Logical Reasoning", "Computer Awareness"]

with open("garbage.csv", mode='w', newline='') as file:
    writer = csv.writer(file)
    row_count = 0  # Initialize a counter for the rows

    for student_id in range(1, 4001):  # Adjust the range to iterate 4000 times
        for a in range(6):
            num = random.randint(1, 3)
            if num == 3:
                marks = [random.randint(100, 150) for _ in subjects]
            else:
                marks = [random.randint(0, 40) for _ in subjects]
            print(marks)

            writer.writerow([student_id] + marks)
            row_count += 1  # Increment the counter

            if row_count >= 4000:  # Check if the row count has reached 4000
                break

        if row_count >= 4000:  # Check if the row count has reached 4000
            break

print("CSV dataset created successfully")'''

'''import csv
import random

subjects = ["English", "Mathematics", "Science", "Social Studies", "Logical Reasoning", "Computer Awareness"]

with open("garbage.csv", mode='w', newline='') as file:
    writer = csv.writer(file)
    row_count = 0  # Initialize a counter for the rows

    for student_id in range(1, 4001):  # Adjust the range to iterate 4000 times
        for a in range(6):
            marks = [random.randint(0, 39) for _ in subjects]
            # Choose one subject randomly and set its value between 50 and 80
            random_subject_index = random.randint(0, len(subjects) - 1)
            marks[random_subject_index] = random.randint(50, 80)

            writer.writerow([student_id] + marks)
            row_count += 1  # Increment the counter

            if row_count >= 4000:  # Check if the row count has reached 4000
                break

        if row_count >= 4000:  # Check if the row count has reached 4000
            break

print("CSV dataset created successfully")'''

import csv
import random

courses = ["DIPLOMA", "ITI", "VOCATIONAL"]
interests = [
    "Computer Science and Information Technology",
    "Mechanical and Electrical",
    "Electronics and Communication",
    "Construction and Design",
    "Hospitality and Event Management",
    "Life Sciences and Environment",
    "Arts and Media",
    "Physical Education and Wellness",
    "Finance, Business, and Marketing",
    "Culinary studies and cooking"
]

with open("courses_interests.csv", mode='w', newline='') as file:
    writer = csv.writer(file)

    for _ in range(4000):  # Adjust the number of rows as needed
        course = random.choice(courses)
        interest = random.choice(interests)
        writer.writerow([course, interest])

print("CSV file created successfully")


