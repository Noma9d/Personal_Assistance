
from project_willy.menu.main_menu import MainMenu
from project_willy.text_fields.general_text import GeneralText


# ----------ENTER TO MAIN MENU----------
def main() -> None:
    print(GeneralText.start_message)
    input(GeneralText.continue_input_message)
    MainMenu()


# ----------ENTRY POINT----------
if __name__ == '__main__':
    main()
