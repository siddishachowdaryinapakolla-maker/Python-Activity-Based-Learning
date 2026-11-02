attended = int(input("Enter attended classes: "))
total = int(input("Enter total classes: "))

if total > 0 and attended >= 0 and attended <= total:
    percentage = (attended / total) * 100

    print("Attendance Percentage:", percentage)

    if percentage >= 75:
        print("Eligible")
    else:
        print("Not Eligible")

        required = (75 * total - 100 * attended) / 25
        print("Minimum Additional Classes Required:", int(required) + 1)
else:
    print("Invalid Attendance Details")