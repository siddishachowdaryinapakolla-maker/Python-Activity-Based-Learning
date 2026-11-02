python_marks = int(input("Enter Python marks: "))
maths_marks = int(input("Enter Maths marks: "))
english_marks = int(input("Enter English marks: "))

total = python_marks + maths_marks + english_marks
percentage = total / 3

print("Total Marks:", total)
print("Percentage:", percentage)

if python_marks >= 35 and maths_marks >= 35 and english_marks >= 35:
    print("Result: PASS")
else:
    print("Result: FAIL")