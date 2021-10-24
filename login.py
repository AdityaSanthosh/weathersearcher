def login():
    import numpy as np
    import bcrypt
    users = np.load('users.npy', allow_pickle=True)
    usernames, passwords = zip(*users)
    print("Login...")
    username = input("Username:")
    password = input("Password:").encode('utf-8')

    if username not in usernames:
        print("User not found. Create Account or Check the formatting")
        login()
    else:
        salt = bcrypt.gensalt()
        hashed = bcrypt.hashpw(password, salt)
        if bcrypt.checkpw(password, hashed):
            print("Logged in.../")

        else:
            print("Wrong Password")