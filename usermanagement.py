import numpy as np
import bcrypt


def manage_user(logged_user):
    import os
    os.system('cls')
    # title of the program
    print("\t***** Your Profile *****")
    print(10 * "*", "", 10 * "*")
    print("WELCOME %s" % logged_user)
    print("[1] Change User Details")
    print("[2] Delete User")
    print("[3] Print all users")
    print("[4] Quit")

    while True:
        choice = int(input("Enter Choice: "))
        os.system('cls')
        if choice == 1:
            change_user(logged_user)
            break
        elif choice == 2:
            delete_user(logged_user)
            break
        elif choice == 3:
            all_users()
            break
        elif choice == 4:
            print("Have a Nice Day!")
            break
        else:
            print("You did not choose the right option. Enter options between 1-3")


def change_user(logged_user):
    name=input("Enter new name:  ")
    pwd=input("Enter new pwd:  ")
    re_pwd = input("Retype Password")
    users = np.load('users.npy', allow_pickle=True)
    usernames, passwords = zip(*users)
    usernames = list(usernames)
    passwords = list(passwords)
    if pwd == re_pwd:
        for i in range(1,len(usernames)):
            if usernames[i] == logged_user:
                usernames[i] = name
                salt = bcrypt.gensalt()
                hashed_pw = bcrypt.hashpw(pwd.encode('utf-8'), salt)
                passwords[i] = hashed_pw
        users = list(zip(usernames, passwords))
        np.save('users.npy', users)
        print("Details Successfully Changed.\n")
    else:
        print("Password and retyped password do not match.\n")


def delete_user(logged_user):
    key = input("Are you sure you really want to delete your account?\nType y or Y for confirmation\n")
    if key.lower() != 'y':
        return
    users = np.load('users.npy', allow_pickle=True)
    usernames, passwords = zip(*users)
    usernames = list(usernames)
    passwords = list(passwords)
    for i in range(1, len(usernames)):
        if usernames[i] == logged_user:
            del usernames[i]
            del passwords[i]
            break
    print("User Deleted.\n")


def all_users():
    users = np.load('users.npy', allow_pickle=True)
    usernames, passwords = zip(*users)
    print(usernames)
