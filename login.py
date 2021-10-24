def login():
    import numpy as np
    import bcrypt
    import os
    users = np.load('users.npy', allow_pickle=True)
    usernames, passwords = zip(*users)
    print(passwords[1])
    print("Login...")
    username = input("Username:\t")
    password = input("Password:\t").encode('utf-8')
    logged_in = False
    if username not in usernames:
        print("User not found. Create Account or Check the formatting")
        os.system("clear")
        login()
    else:
        for i in range(1, len(usernames)):
            if bcrypt.checkpw(password, passwords[i].encode('utf-8')):
                logged_in = True
                break
        if not logged_in:
            print("Wrong Password")
            login()
