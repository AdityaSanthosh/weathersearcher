
def new_user():
    import numpy as np
    users = np.load('users.npy', allow_pickle=True)
    usernames, passwords = zip(*users)
    usernames = list(usernames)
    passwords = list(passwords)
    type(usernames)
    print("New Account Creation Wizard")
    newusername = input("Enter Username")
    password = input("Enter Password")
    re_pass = input("Retype Password")
    if password == re_pass:
        if newusername.lower() in usernames:
            print("Sorry. Someone with this username already exists.\n.Please Choose a new one")
            new_user()
        else:
            usernames.append(newusername)
            passwords.append(password)
            users = list(zip(usernames, passwords))
            np.save('users.npy', users)
            print("Account Successfully Created.\nPlease Login to continue")
