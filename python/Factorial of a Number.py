num = input("Enter a non-negative integer: ")

if not num.isdigit():
    print("Invalid input! Enter a non-negative integer.")
else:
    n = int(num)
    factorial = 1
    for i in range(1, n + 1):
        factorial *= i
    print(f"Factorial of {n} is {factorial}")
