# ATM Simulation
correct_pin = "1234"
balance = 10000

pin = input("Enter your 4-digit PIN: ")

if pin == correct_pin:
    print("PIN verified. You can proceed.")
    amount = int(input("Enter withdrawal amount (multiples of Rs100): "))

    if amount % 100 != 0:
        print("Amount must be in multiples of Rs100.")
    elif amount > balance:
        print("Insufficient balance!")
    else:
        balance -= amount
        print(f"Withdrawal successful. Remaining balance: Rs{balance}")
else:
    print("Incorrect PIN. Access denied.")
1223