distance = float(input("Enter distance in km: "))
mileage = float(input("Enter mileage: "))
fuel_price = float(input("Enter fuel price: "))

if distance > 0 and mileage > 0 and fuel_price > 0:
    fuel = distance / mileage
    cost = fuel * fuel_price

    print("Fuel Required:", fuel, "litres")
    print("Total Fuel Cost: Rs.", cost)
else:
    print("Invalid Input")