import os
import newuser
import login
import weathersearch
import sys
import usermanagement


def run():
    try:
        if sys.argv[1] == "--help":
            print("How it Works\nThe Weather Data is fetched from OpenWeatherMap API \
        You need an Account and API key for that\n\
        The data is fetched using urllib3 library\n\
        The returned data is parsed and displayed on the Console.\n\
        The login System is implemented using bcrypt library.\n")
    except:
        main_menu()

def title_bar():
    # os.system('clear')
    os.system('cls')
    # title of the program
    print("\t**********************************************")
    print("\t***** Weather Information System *****")
    print("\t**********************************************")


def main_menu():
    title_bar()
    print(10 * "*", "WELCOME MENU", 10 * "*")
    print("[1] New User")
    print("[2] Login")
    print("[3] Quit")

    while True:
        choice = int(input("Enter Choice: "))
        import os
        os.system('cls')
        if choice == 1:
            new_user()
            break
        elif choice == 2:
            logged_user = login.login()
            import os
            os.system('cls')
            print("Logged in....")
            choice = input("Press x to search weather of your location.\nPress l to logout.\nPress u to access User "
                           "Management.\n")
            if choice == 'l':
                main_menu()
            if choice == 'u':
                usermanagement.manage_user(logged_user)
            if choice == 'x':
                weathersearch.weather_search()
            break
        elif choice == 3:
            print("Have a Nice Day!")
            break
        else:
            print("You did not choose the right option. Enter options between 1-3")
            main_menu()


def new_user():
    newuser.new_user()
    key = input("Enter any key to return main menu")
    main_menu()



# main driver
run()

