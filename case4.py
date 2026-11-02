attendance = float(input("Enter attendance percentage: "))
lab = int(input("Lab completed? (1 for Yes, 0 for No): "))
internal = int(input("Enter internal marks: "))
fee = int(input("Fee paid? (1 for Yes, 0 for No): "))

if attendance >= 75 and lab == 1 and internal >= 25 and fee == 1:
    print("Eligible for Examination")
else:
    print("Not Eligible for Examination")

    if attendance < 75:
        print("Attendance is insufficient")
    if lab == 0:
        print("Lab work is incomplete")
    if internal < 25:
        print("Internal marks are insufficient")
    if fee == 0:
        print("Fees are not paid")