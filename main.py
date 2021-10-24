import os
import newuser
import login
import weathersearch

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
    print("[3] User Management")
    print("[4] Quit")

    while True:
        choice = int(input("Enter Choice: "))
        import os
        os.system('cls')
        if choice == 1:
            new_user()
            break
        elif choice == 2:
            login.login()
            import os
            os.system('cls')
            print("Logged in....")
            choice = input("Press x to search weather of your location.\nPress l to logout.\n")
            if choice == 'l':
                main_menu()
            if choice == 'x':
                weathersearch.weather_search()
            break
        elif choice == 4:
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
main_menu()

