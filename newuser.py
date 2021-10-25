
def new_user():
    import numpy as np
    import bcrypt
    users = np.load('users.npy', allow_pickle=True)
    usernames, passwords = zip(*users)
    usernames = list(usernames)
    passwords = list(passwords)
    print("New Account Creation Wizard")
    newusername = input("Enter Username:\t")
    password = input("Enter Password:\t")
    re_pass = input("Retype Password:\t")
    if password == re_pass:
        if newusername.lower() in usernames:
            print("Sorry. Someone with this username already exists.\nPlease Choose a new one")
            new_user()
        else:
            usernames.append(newusername)
            salt = bcrypt.gensalt()
            hashed_pw = bcrypt.hashpw(password.encode('utf-8'), salt)
            passwords.append(hashed_pw)
            users = list(zip(usernames, passwords))
            np.save('users.npy', users)
            print("Account Successfully Created.\nPlease Login to continue")
