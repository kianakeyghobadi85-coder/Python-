import random
import string

length = int(input("Enter password length: "))

characters = string.ascii_letters + string.digits + string.punctuation

password = ""

for i in range(length):
    password += random.choice(characters)

print(f"Your password is: {password}")

import random

number = random.randint(1, 100)

for i in range(7):

    guess = int(input("Guess the number: "))

    if guess > number:
        print("Bigger!")

    elif guess < number:
        print("Smaller!")

    else:
        print("You Win!")
        break

else:
    print(f"You Lost! The number was {number}")