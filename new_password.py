from hashlib import md5
from pyperclip import copy
from getpass import getpass
from termcolor import colored

def replace(input_str):
    symbols = {1: "!", 2: "@", 3: "#", 4: "$", 5: "%", 6: "^", 7: "&", 8: "*", 9: "(", 0: ")"}

    digits = [(index, char) for index, char in enumerate(input_str) if char.isdigit()]
    letters = [(index, char) for index, char in enumerate(input_str) if char.isalpha()]

    num_digits = len(digits)
    num_letters = len(letters)

    # Calculate the number of digits and letters to replace
    half_digits_count = num_digits // 2
    half_letters_count = num_letters // 2

    # Replace half of the digits to special symbols
    for i in range(half_digits_count):
        index, digit = digits[i]
        input_str = input_str[:index] + symbols[int(digit)] + input_str[index + 1:]

    # Replace half of the lower letters to uppercase letters
    for i in range(half_letters_count):
        index, letter = letters[i]
        input_str = input_str[:index] + letter.upper() + input_str[index + 1:]

    return input_str

try:
    pwd = getpass('Primary password: ')
    web = input('Website: ')
    usr = input('Username: ')
    opt = input('Optional text: ')

    h = md5((pwd + web + usr + opt).encode()).hexdigest()
    p = replace(h[:16])

    copy(p)
    print(colored('Password copied.', 'green'))

except KeyboardInterrupt:
    print(colored("\nKeyboard interrupted", 'red'))
