import bcrypt
import os
import sys
import urllib3
import json
from dotenv import load_dotenv
import pickle
import time

""" Helper Functions """


def clear_console():
    os.system('cls')


def title_bar():
    clear_console()
    # title of the program
    print("\t**********************************************")
    print("\t***** Weather Information System *****")
    print("\t**********************************************")


def hash_password(password):
    salt = bcrypt.gensalt()
    hashed_pw = bcrypt.hashpw(password.encode('utf-8'), salt)
    return hashed_pw


def save_obj(obj, filename='db.pkl'):
    with open(filename, 'wb') as outp:  # Overwrites any existing file.
        pickle.dump(obj, outp, pickle.HIGHEST_PROTOCOL)
    print("Saved!")
    outp.close()
    return True


def load_db():
    open_file = open('db.pkl', "rb")
    loaded_list = pickle.load(open_file)
    return loaded_list


class User:
    def __init__(self, username, password):
        self.username = username
        self.password = hash_password(password).decode('utf-8')

    def delete_user(self):
        key = input("Are you sure you really want to delete your account?\nType y or Y for confirmation\n")
        if key.lower() != 'y':
            return False
        obj_list = load_db()
        for obj in obj_list:
            if obj.username == self.username:
                obj_list.remove(obj)
                print("User deleted!")
                break
        save_obj(obj_list)
        return True

    def update_user(self):
        name = input("Enter new name:  ")
        pwd = input("Enter new Password:    ")
        password = hash_password(pwd)
        obj_list = load_db()
        for obj in obj_list:
            if obj.username == self.username:
                obj.username = name
                obj.password = password
                break
        save_obj(obj_list)
        print("User successfully updated")


def all_users():
    i = 1
    users_list = load_db()
    print("Users registered:\n")
    for user in users_list:
        print(i, getattr(user, "username"), sep='\t')
        i += 1


def new_user():
    username = input("Enter Username:    ")
    pwd = input("Enter pwd:    ")
    newuser = User(username, pwd)
    users_list = load_db()
    users_list.append(newuser)
    save_obj(users_list)
    return True


class App:
    def login(self):
        clear_console()
        users_list = load_db()
        usernames = [getattr(user, "username") for user in users_list]
        print("Login...")
        username = input("Username:\t")
        password = input("Password:\t").encode('utf-8')
        if username not in usernames:
            print("User not found. Create Account or Check the formatting, Try Again!!\n")
            time.sleep(2)
            self.login()
        else:
            for user in users_list:
                if bcrypt.checkpw(password, user.password.encode('utf-8')):
                    print("Logged in\n")
                    self.weather_search(user)
                    return
                else:
                    print("Wrong Password. Try again\n")
                    time.sleep(2)
                    self.login()

    def weather_search(self, user):
        title_bar()
        choice = input("Press x to search weather of your location.\nPress l to logout.\nPress c to change User "
                       "Details.\nPress d to delete user")
        if choice == 'l':
            app()
        if choice == 'd':
            user.delete_user()
        if choice == 'c':
            user.update_user()
        if choice == 'x':
            load_dotenv()
            API_KEY = os.getenv('API_KEY')
            clear_console()
            cityinput = input("Enter City Location to get weather data\n")
            print("Please Wait. This may take some time")
            link = 'api.openweathermap.org/data/2.5/weather?q={}&appid={}'.format(cityinput, API_KEY)
            http = urllib3.PoolManager()
            r = http.request('GET', link)
            clear_console()
            print("Here is the data....")
            raw_data = r.data.decode('utf-8')
            data = json.loads(raw_data)
            try:
                if data['cod']:
                    print(data["message"], end='\n')
                    key = input("Press Enter to search again.\nPress q to quit")
                    if key == '':
                        self.weather_search()
                    return
            except:
                print("city:", data['name'])
                print("humidity:", data['main']['humidity'])
                print("pressure:", data['main']['pressure'])
                print("temperature:", data['main']['temp'])
                print("wind speed:", data['wind']['speed'])
                print("city:", data['wind']['deg'])
                print("\n")
                choice = input("Press x to search new city or any other key to quit")
                if choice == 'x':
                    self.weather_search()


def app():
    title_bar()
    print(10 * "*", "WELCOME MENU", 10 * "*")
    print("[1] New User")
    print("[2] Login")
    print("[3] All Users")
    print("[4] Quit")

    while True:
        choice = int(input("Enter Choice: "))
        clear_console()
        if choice == 1:
            new_user()
            break
        elif choice == 2:
            app_instance = App()
            app_instance.login()
            break
        elif choice == 3:
            all_users()
            break
        elif choice == 4:
            print("Have a Nice Day!")
            break
        else:
            print("You did not choose the right option. Enter options between 1-3\nRetry")
            app()


def run():
    try:
        if sys.argv[1] == "--help":
            print("How it Works\nThe Weather Data is fetched from OpenWeatherMap API \
        You need an Account and API key for that\n\
        The data is fetched using urllib3 library\n\
        The returned data is parsed and displayed on the Console.\n\
        The login System is implemented using bcrypt library.\n")
    except:
        app()


# main driver
run()
