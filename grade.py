subjects = ["English", "Maths", "Science", "Social Science", "Computer"]
total = 0
for subject in subjects:
    while True:
        try:
            marks = float(input("Enter marks for " + subject + " (0-100): "))
            if marks < 0 or marks > 100:
                print("Invalid marks! Enter a value between 0 and 100.")
                continue
            break
        except ValueError:
            print("Input failure! Please enter numbers only.")
    total += marks
percentage = total / len(subjects)
# Grade boundaries
if percentage >= 90:
    grade = "A+"
elif percentage >= 80:
    grade = "A"
elif percentage >= 70:
    grade = "B"
elif percentage >= 60:
    grade = "C"
elif percentage >= 50:
    grade = "D"
else:
    grade = "F"
print("\n--- RESULT ---")
print("Total Marks:", total, "/", len(subjects) * 100)
print("Percentage:", percentage, "%")
print("Grade:", grade)








