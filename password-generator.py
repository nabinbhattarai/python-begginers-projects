import random

print("Welcome to the password generator")
character = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890!@#$%^&*()?"

number = int(input("How many password you want to generate? "))
length = int(input("Character length of password: "))

for num in range(number):
    password = " "
    for pwd in range(length):
        password += random.choice(character)

    print(password)

