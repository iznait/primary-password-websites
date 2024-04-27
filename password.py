from hashlib import md5
from pyperclip import copy
from getpass import getpass
from termcolor import colored

try:
    pwd = getpass('Primary password: ')
    web = input('Website: ')
    usr = input('Username: ')
    opt = input('Optional text: ')

    h = md5((pwd + web + usr + opt).encode()).hexdigest()
    h = h[:4] + h[4:16].upper()
    symbols = {1: "!", 2: "@", 3: "#", 4: "$", 5: "%", 6: "^", 7: "&", 8: "*", 9: "(", 0: ")"}

    for key, value in symbols.items():
        h = h[:6] + h[6:16].replace(str(key), value)

    copy(h)
    print(colored('Password copied.', 'green'))

except KeyboardInterrupt:
    print(colored("\nKeyboard interrupted", 'red'))
