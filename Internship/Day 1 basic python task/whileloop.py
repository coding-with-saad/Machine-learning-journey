password = ""
attempts = 0

while password != "python123" and attempts < 3:

    print(f"\nAttempt {attempts + 1} of 3")

    password = input("Enter Password: ")

    if password != "python123":
        attempts += 1
        print("Incorrect Password!")

if password == "python123":
    print("\nAccess Granted")
else:
    print("\nYour account has been blocked.")