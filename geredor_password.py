
import random

print('Welcome To You password Generator')

chars = 'abcdefghijklmnopqrstuvwyzABCDEFGHIJKLMNOPQRSTUVWXYZ!@$%^&*().,?0123456789'

number = input('Amount of passwords to generate:')
number = int(number)

length = input('Input your password length: ')
length = int(length)

print('\nhere are your password:')

for pwd in range(number):
    passwords = ''
    for c in range(length):
        passwords += random.choice(chars)

    print(passwords)
    