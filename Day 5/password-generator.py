import random

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

nr_letters = 0
nr_numbers = 0
nr_symbols = 0


print("Welcome to the PyPassword Generator!")

try:
    nr_letters = int(input("How many letters would you like in your password?\n"))
    nr_symbols = int(input(f"How many symbols would you like?\n"))
    nr_numbers = int(input(f"How many numbers would you like?\n"))
except ValueError:
    print("ERROR INVALID INPUT: \nPlease enter numbers only.")

if nr_letters == 0 and nr_numbers == 0 and nr_symbols == 0:
    print("You must select at least one character to generate a password.")

elif nr_letters < 0 or nr_numbers < 0 or nr_symbols < 0:
    print("ERROR INVALID INPUT: \nPlease enter positive numbers only.")

else:
    password_list = []

    for char in range(0, nr_letters):
        password_list.append(random.choice(letters))
    for char in range(0, nr_numbers):
        password_list.append(random.choice(numbers))
    for char in range(0, nr_symbols):
        password_list.append(random.choice(symbols))

    print(password_list)
    random.shuffle(password_list)
    print(password_list)

    password = ""
    for char in password_list:
        password += char

    print(f"Your password is: {password}")
