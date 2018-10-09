"""
cryptography.py
Author: Nick Lee
Credit: overflow for one or two syntax corrections

Assignment: Cryptography

Write and submit a program that encrypts and decrypts user data.

See the detailed requirements at https://github.com/HHS-IntroProgramming/Cryptography/blob/master/README.md
Two plus two = Five
Lorem ipsum
"""
import string
chars = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789 .,:;'\"/\\<>(){}[]-=_+?!"
message = ''
key = ''
start = ''
output = list()
keyp = 0
messagep = -1
letter = 0
new = 0
def encrypt(m,k):
    global chars, keyp, messagep, letter, output, new
    output = list()
    for i in range(len(m)):
        messagep = 0
        keyp = 0
        new = 0
        while m[i] != chars[messagep]:
            if messagep == 84:
                break
            messagep += 1
        while k[letter] != chars[keyp]:
            if keyp == len(chars):
                break
            keyp += 1
        if letter == (len(k)-1):
            letter = 0
        else: 
            letter += 1
        new = (keyp+messagep)
        if new >= 85:
            new = new - 85
        output.append(chars[new])
    output = ''.join(output)
    print(output)
def decrypt(m,k):
    global chars, keyp, messagep, letter, output, new
    output = list()
    for i in range(len(m)):
        messagep = 0
        keyp = 0
        new = 0
        while m[i] != chars[messagep]:
            if messagep == len(chars):
                break
            messagep += 1
        while k[letter] != chars[keyp]:
            if keyp == len(chars):
                break
            keyp += 1
        if letter == (len(k)-1):
            letter = 0 
        else:
            letter += 1
        new = (messagep-keyp)
        output.append(chars[new])
    output = ''.join(output)
    print(output)
    
while start != 'q':
    start = input('Enter e to encrypt, d to decrypt, or q to quit: ')
    if start == 'e':    
        message = input("Message: ")
        key = input("Key: ")
        encrypt(message, key)
    elif start == 'd':
        message = input("Message: ")
        key = input("Key: ")
        decrypt(message, key)
    elif start == 'q':
        print('Goodbye!')
    else:
        print("Did not understand command, try again.")





