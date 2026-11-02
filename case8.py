units = int(input("Enter water consumption units: "))

if units <= 50:
    bill = units * 3
elif units <= 100:
    bill = 50 * 3 + (units - 50) * 5
else:
    bill = 50 * 3 + 50 * 5 + (units - 100) * 8

print("Water Consumption:", units)
print("Total Water Bill: Rs.", bill)