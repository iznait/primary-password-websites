import pwinput
from pyperclip import copy
from hashlib import md5

pwd = pwinput.pwinput("Enter primary password + website + username + year: \n")

h = md5(pwd.encode()).hexdigest()
h = h[:4] + h[4:16].upper()
symbols = {1: "!", 2: "@", 3: "#", 4: "$", 5: "%", 6: "^", 7: "&", 8: "*", 9: "(", 0: ")"}

for key, value in symbols.items():
    h = h[:6] + h[6:16].replace(str(key), value)
copy(h)
print('Password copied.')
