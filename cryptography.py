"""
cryptography.py
Author: Nick Lee
Credit: none yet

Assignment: Cryptography

Write and submit a program that encrypts and decrypts user data.

See the detailed requirements at https://github.com/HHS-IntroProgramming/Cryptography/blob/master/README.md
"""
chars = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789 .,:;'\"/\\<>(){}[]-=_+?!☃"
message = 'hello world'
key = 'hi'
output = ''
keyp = 0
messagep = -1
letter = 0
def encrypt(m,k):
    global chars, keyp, messagep, letter
    for i in range(len(m)):
        messagep = 0
        keyp = 0
        if letter >= len(k):
            letter = 0
        else: 
            letter += 1
        while m[i] != chars[messagep] or i == len(m):
            messagep += 1
        print(messagep)
        for j in range(len(chars)):
            if k[letter] == chars[j]:
                break
            keyp += 1
        print(keyp,'q')
        
encrypt('aabbajsba;jbfasdfa', 'hello worldz')




"""

def enter():
    global message, key
    start = input('Enter e to encrypt, d to decrypt, or q to quit:') 
    if start == 'e' or 'd' or 'q':
        if start == 'e':
            message = input("Message: ")
            key = input("Key: ")
        elif start == 'd':
            message = input("Message: ")
            key = input("Key: ")
        elif start == 'q':
            print('Goodbye!')
            #break
            
        else:
            print("Did not understand command, try again.")
            enter()

enter()
"""



print("Hello, world.")