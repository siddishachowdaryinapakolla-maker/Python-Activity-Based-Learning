consultation = float(input("Enter consultation fee: "))
diagnostic = float(input("Enter diagnostic fee: "))
treatment = float(input("Enter treatment fee: "))

total = consultation + diagnostic + treatment

if total >= 3000:
    discount = total * 0.10
else:
    discount = 0

final_bill = total - discount

print("Total Bill:", total)
print("Discount:", discount)
print("Final Bill:", final_bill)