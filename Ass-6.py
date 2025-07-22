# Create a student report card program. Use variables for student name, three subject marks, calculate total and average, then display a formatted report using f-strings.

Math = 85
Science = 90
English = 78
Total_marks = Math+Science+English
Average = Total_marks/3
Average = round(Average,2)

print("=== STUDENT REPORT CARD ===")

print(f"Student: John Doe")
print(f"Math: 85, Science: 90, English: 78")
print(f"Total Marks: {Total_marks}")
print(f"Average: {Average}")

#Python Note
# Use round(average, 2) to round the average to 2 decimal places!, for eg: Average = Total_marks/3
# Average = round(Average,2)

# Expected Output (example)
# === STUDENT REPORT CARD ===
# Student Name: John Doe
# Math: 85, Science: 90, English: 78
# Total Marks: 253
# Average: 84.33