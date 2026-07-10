correct_username = "dhanush"
correct_password = "2009"

attempt = 1
max_attempts = 3

while attempt <= max_attempts:
    username = input("Enter username: ")
    password = input("Enter password: ")

    if username == correct_username and password == correct_password:
        print("Login successful! Welcome.")
        break
    else:
        print(f"Incorrect username or password. Attempt {attempt} of {max_attempts}.")

    attempt += 1
else:
    print("All attempts exhausted. Access denied.")
