balance = 35000000

while True:

    print("\n ATM MENU ")
    print("1. Check Balance")
    print("2. Withdraw")
    print("3. Deposit")
    print("4. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        print(f"Your balance is: {balance} Toman")

    elif choice == "2":
        amount = int(input("Enter withdrawal amount: "))

        if amount <= 0:
            print("Invalid amount")

        elif amount > balance:
            print("Insufficient balance")

        else:
            balance -= amount
            print("Withdrawal successful")
            print(f"New balance: {balance}")

    elif choice == "3":
        amount = int(input("Enter deposit amount: "))

        if amount <= 0:
            print("Invalid amount")

        else:
            balance += amount
            print("Deposit successful")
            print(f"New balance: {balance}")

    elif choice == "4":
        print("Thank you for using ATM")
        break

    else:
        print("Invalid choice")