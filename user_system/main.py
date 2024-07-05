import time
import os

users = ['admin']
passwords = ['admin']
isAdmin = [True]

current_user = ''

def registration(pswrd, user_name):
    users.append(user_name)
    passwords.append(pswrd)
    isAdmin.append(False)
    return user_name

while True:
    os.system('clear')
    command = input('1)Registraion\n2)Login\n3)Account\n4)Admin panel\n5)Exit\n\ncommand: ')
    if command == '1':
        reg_loop = True
        while reg_loop:
            os.system('clear')
            if current_user != '':
                print('You are already logged in to your account\nPlease log out of your account to register a new account.')
                time.sleep(2)
                reg_loop = False
            else:
                reg_username = input('Enter your new username: ')
                reg_password = input('Enter your new password: ')
                if reg_username in users:
                    print('This username is already taken\nPlease enter another username')
                    time.sleep(2)
                elif reg_username == '' or reg_password == '':
                    print('You cannot register account with empty password or username')
                    time.sleep(2)
                else:
                    current_user = registration(reg_password, reg_username)
                    print('Registration was successful')
                    time.sleep(2)
                    os.system('clear')
                    reg_loop = False
    elif command == '2':
        login_loop = True
        while login_loop:
            os.system('clear')
            login_username = input('Enter your username: ')
            login_password = input('Enter your password: ')
            if current_user != '':
                print('You are already logged in to your account\nPlease log out of your account to login to another.')
                time.sleep(2)
                os.system('clear')
                login_loop = False
            elif login_username not in users:
                print('Username or password was incorrect')
                time.sleep(2)
                login_loop = False
            else:
                login_username_index = users.index(login_username)
                password_for_login_username = passwords[login_username_index]
                if login_username in users and login_password in passwords and password_for_login_username == login_password:
                    current_user = login_username
                    print('Login was successful')
                    time.sleep(2)
                    os.system('clear')
                    login_loop = False
                else:
                    print('Username or password was incorrect')
                    time.sleep(2)
                    os.system('clear')
    elif command == '3':
        if current_user == '':
            print('You are not logged in to your account')
            time.sleep(2)
            os.system('clear')
        else:
            account_loop = True
            while account_loop:
                os.system('clear')
                print(f'Username: {current_user}\nPassword: {passwords[users.index(current_user)]}\n\n')
                account_command = input('1)Logout\n2)Delete account\n3)Change username\n4)Change password\n5)Exit\n\ncommand: ')
                if account_command == '1':
                    current_user = ''
                    print('Logout was successful')
                    time.sleep(2)
                    os.system('clear')
                    account_loop = False
                elif account_command == '2':
                    account_del_loop = True
                    while account_del_loop:
                        if isAdmin[users.index(current_user)]:
                            print('You last admin\nPlease, grant another user with admin rights to delete this account')
                            time.sleep(2)
                            account_del_loop = False
                        else:
                            if input('Are you sure?\nY/N: ') == 'Y' or 'y':
                                del passwords[users.index(current_user)]
                                del users[users.index(current_user)]
                                current_user = ''
                                print('Your account deleted successful')
                                time.sleep(2)
                                os.system('clear')
                                account_del_loop = False
                                account_loop = False
                            elif input('Are you sure?\nY/N: ') == 'N' or 'n':
                                time.sleep(1)
                                os.system('clear')
                                account_del_loop = False
                                account_loop = False
                            else:
                                print('Enter Y or N')
                                time.sleep(2)
                                os.system('clear')
                elif account_command == '3':
                    change_username = input('Enter new username: ')
                    users[users.index(current_user)] = change_username
                    current_user = change_username
                    print('Username was chaged successul')
                    time.sleep(2)
                    os.system('clear')
                    account_loop = False
                elif account_command == '4':
                    change_password = input('Enter new password: ')
                    passwords[users.index(current_user)] = change_password
                    print('Password was chaged successul')
                    time.sleep(2)
                    os.system('clear')
                    account_loop = False
                elif account_command == '5':
                    time.sleep(1)
                    os.system('clear')
                    account_loop = False
                else:
                    print('Please, enter number of operation')
                    time.sleep(2)
                    os.system('clear')
    elif command == '4':
        os.system('clear')
        if current_user == '':
            print('You are not logged in')
            time.sleep(2)
            os.system('clear')
        elif isAdmin[users.index(current_user)] == False:
            print('Not enough permissions to start admin panel')
            time.sleep(2)
            os.system('clear')
        else:
            admin_panel_loop = True
            while admin_panel_loop:
                print('index    user__name    password    isAdmin')
                for i in range(len(users)):
                    print(f'{i}    {users[i]}    {passwords[i]}    {isAdmin[i]}')
                admin_panel_command = input('\n1)Grant administrator rights\n2)Take back the administrator\'s rights\n3)Delete user\n4)Exit\n\ncommand: ')
                if admin_panel_command == '1':
                    admin_grant_admin_command = input('Enter index: ')
                    isAdmin[int(admin_grant_admin_command)] = True
                    print('Administrator rights granted successful')
                    time.sleep(2)
                    os.system('clear')
                elif admin_panel_command == '2':
                    admin_takeback_admin_command = input('Enter index: ')
                    if isAdmin.count(True) == 1:
                        print('This is last admin\nYou cannot take back admin rights or delete this account until there is a new admin on the system')
                        time.sleep(2)
                        os.system('clear')
                    else:
                        isAdmin[int(admin_takeback_admin_command)] = False
                        print('Administrator rights taked back successful')
                        time.sleep(2)
                        os.system('clear')                                       
                elif admin_panel_command == '3':
                    admin_delete_account = input('Enter index: ')
                    if isAdmin[int(admin_delete_account)] == True and isAdmin.count(True) == 1:
                        print('This is last admin\nYou cannot take back admin rights or delete this account until there is a new admin on the system')
                        time.sleep(2)
                        os.system('clear')
                    else:                
                        del users[int(admin_delete_account)]
                        del passwords[int(admin_delete_account)]
                        del isAdmin[int(admin_delete_account)]
                        print('Account deleted successful')
                        time.sleep(2)
                        os.system('clear')
                        admin_panel_loop = False
                elif admin_panel_command == '4':
                    time.sleep(1)
                    os.system('clear')
                    admin_panel_loop = False
                else:
                    print('Please, enter number of operation')
                    time.sleep(2)
                    os.system('clear')
    elif command == '5':
        exit()
    else:
        print('Pleace, enter number of operation')
        time.sleep(2)
        os.system('clear')
