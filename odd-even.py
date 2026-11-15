number = int(input("enter your number:"))

if number % 2 == 0:
    if number > 0:
        print(f"{number} is even and positive.")
    elif number < 0:
        print(f"{number} is even and negative.")
    else:
        print("number is 0")

elif number % 2 != 0:
    if number > 0:
        print(f"{number} is odd and positive.")
    elif number < 0:
        print(f"{number} is odd and negative.")
    else:
        print("number is 0")
    
