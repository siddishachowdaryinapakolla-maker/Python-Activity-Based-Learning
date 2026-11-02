material = float(input("Enter material cost: "))
labour = float(input("Enter labour cost: "))
machine = float(input("Enter machine cost: "))
selling_price = float(input("Enter selling price: "))

total_cost = material + labour + machine
profit = selling_price - total_cost

print("Total Production Cost:", total_cost)
print("Profit:", profit)

if profit > 0:
    print("Result: Profit")
elif profit == 0:
    print("Result: No Profit No Loss")
else:
    print("Result: Loss")