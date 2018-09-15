import random

length = int(input("Please enter a length for your password: ")) # Takes user input to create the length in characters for the password
amount = int(input("How many passwords would you like to choose from? ")) # This input will create more than one password at a time to choose from
characters = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890?.!@#$&*%$-'
password = ''

for passphrase in range(amount):
    password = ''
    for character in range(length):
        password += random.choice(characters)
    print(password)
