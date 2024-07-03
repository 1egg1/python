import time

users = []
passwords = []

current_user = ''

def registration(pswrd, user_name):
    users.append(user_name)
    passwords.append(pswrd)

while True:
    command = input('1)Registraion\n2)Login\n3)Account\n4)Exit\n\ncommand: ')
    if command == '1':
        print('test')
