print("1. No Helmet")
print("2. Signal Jump")
print("3. Over Speeding")

choice = int(input("Enter your choice: "))

if choice == 1:
    print("Violation: No Helmet")
    print("Fine Amount: Rs.500")
elif choice == 2:
    print("Violation: Signal Jump")
    print("Fine Amount: Rs.1000")
elif choice == 3:
    print("Violation: Over Speeding")
    print("Fine Amount: Rs.2000")
else:
    print("Invalid Choice")