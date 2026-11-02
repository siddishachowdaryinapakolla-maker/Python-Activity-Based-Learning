basic_salary = float(input("Enter basic salary: "))
allowance = float(input("Enter allowance: "))
deduction = float(input("Enter deduction: "))

gross_salary = basic_salary + allowance
net_salary = gross_salary - deduction

print("Gross Salary:", gross_salary)
print("Net Salary:", net_salary)

if net_salary >= 20000:
    print("Salary Category: High")
else:
    print("Salary Category: Normal")