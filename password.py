import argparse
from hashlib import md5
from pyperclip import copy
from getpass import getpass
from termcolor import colored

def replace(input_str):
    symbols = {1: "!", 2: "@", 3: "#", 4: "$", 5: "%", 6: "^", 7: "&", 8: "*", 9: "(", 0: ")"}

    # Get lists of digit and letter indices
    digits = [(i, char) for i, char in enumerate(input_str) if char.isdigit()]
    letters = [(i, char) for i, char in enumerate(input_str) if char.isalpha()]

    # Replace half of the digits with symbols
    for i, (index, digit) in enumerate(digits[:len(digits) // 2]):
        input_str = input_str[:index] + symbols[int(digit)] + input_str[index + 1:]

    # Replace half of the letters with uppercase
    for i, (index, letter) in enumerate(letters[:len(letters) // 2]):
        input_str = input_str[:index] + letter.upper() + input_str[index + 1:]

    return input_str

try:
    parser = argparse.ArgumentParser()
    parser.add_argument('--file', '-f', type=str)
    args = parser.parse_args()

    if args.file:
        pwd = open(args.file, 'r').read().rstrip('\n')
    else:
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
