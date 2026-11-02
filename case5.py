dollars = float(input("Enter amount in USD: "))
rate = float(input("Enter exchange rate: "))
budget = float(input("Enter travel budget in INR: "))

amount = dollars * rate

print("Amount in INR:", amount)

if amount <= budget:
    print("Status: Within Budget")
else:
    print("Status: Exceeded Budget")
    print("Extra Amount:", amount - budget)