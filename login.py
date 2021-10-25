def login():
    import numpy as np
    import bcrypt
    users = np.load('users.npy', allow_pickle=True)
    usernames, passwords = zip(*users)
    print("Login...")
    username = input("Username:\t")
    password = input("Password:\t").encode('utf-8')
    logged_in = False
    if username not in usernames:
        print("User not found. Create Account or Check the formatting, Try Again!!\n")
        login()
    else:
        for i in range(1, len(usernames)):
            if bcrypt.checkpw(password, passwords[i].encode('utf-8')):
                logged_in = True
                LOGGED_USER = username
                return LOGGED_USER
        if not logged_in:
            print("Wrong Password\n")
            login()
