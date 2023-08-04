import getpass
import sys

from project_willy.methods.registration import Registration
from project_willy.methods.authorization import Authorization
# from project_willy.menu.main_menu import MainMenu
from project_willy.menu.main_menu import MainMenu
from project_willy.text_fields.general_text import GeneralText


# ----------ENTER TO MAIN MENU----------
def main() -> None:
    print("Welcome to Project Willy")
    print("1. Registration")
    print("2. Authorization")
    print("0. EXIT")
    choice = input("Enter your choice (1 or 2 or EXIT): ")

    if choice == "0" or choice.upper() == "EXIT":
        print(f'Goodbye {getpass.getuser()}')
        sys.exit()
    elif choice == "1":
        registration = Registration()
        registration.registration_user()
        main()
    elif choice == "2":
        # Открытие файла users.json и загрузка данных пользователей
        
        authorization = Authorization()
        authorization.load_users()
        authorization.login()

        if authorization.key:
            print("Authorization successful.")
            print("-------")
            print(GeneralText.start_message)
            input(GeneralText.continue_input_message)
            MainMenu()
        else:
            print("Try again")
            print(" ")
            main()

    else:
        print("Invalid choice")
        print('Try again')
        print(" ")
        main()


# ----------ENTRY POINT----------
if __name__ == '__main__':
    main()
    