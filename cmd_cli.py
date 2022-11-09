from sqlite_saver import Server
import colorama
import getpass
import os
from colorama import Fore, Style, Back
from cli_print import (
    print_all_contact,
    logo,
    entering_menu,
    menu,
    entering_menu,
    print_searched_contacts,
)

os.system("cls")
colorama.init()
db = Server()

USER = ""

#


class cmd_contact_book:
    """\n \n __ Contact buyicha hamma actionlar __
    * Yangi username
    * Contact filter
    * All contacts
    * Add, update, delete kabi actionlar junata olish serverga
    * exit (Yani offline datasini parchalab o'zi chiqib ketadi)
    """

    def __init__(self):
        self.USER = USER

    def enter(self):

        click = input(entering_menu + "\n Login yoki new user ? : ")
        if click == "login":
            user = getpass.getpass("  Your username : ")
            checker = db.is_user_exists(username=user)
            if checker is True:
                self.USER = user
                return self.all_actions_menu()
            print(Fore.RED + "  Siz new user create qilmagansiz  ")
            return self.enter()

        if click == "new user":
            yangi_user = input("\n Iltimos name yozing :  ")
            return self.new_user(click=yangi_user)

    def new_user(self, click):
        if isinstance(click, str) and len(click) > 0:
            Server.new_user_create(user_name=click)
            self.USER = click
            return self.all_actions_menu()

        else:
            click = input(
                Fore.RED + "\n Iltimos to'g'ri kiriting name ni | orqaga : < | "
            )
            if click == "<":
                self.enter()
            return self.new_user(click=click)

    def all_actions_menu(self):
        click = input(menu + Fore.LIGHTCYAN_EX + "\n  Qaysi actioni tanlaysiz : ")
        if len(click) > 0 and isinstance(click, str):
            if click == "add contact":
                return self.add_contact()
            if click == "update contact":
                return self.update_contact()
            if click == "delete contact":
                return self.delete_contact()
            if click == "search contact":
                cd = print_all_contact(user=self.USER)
                return self.search_contact()

    def add_contact(self):
        click_name = input(Fore.LIGHTWHITE_EX + "\n Name : ")
        click_phone = input(Fore.LIGHTWHITE_EX + "\n Phone number : ")
        if len(click_name) > 0 and len(click_phone) > 0:
            user = self.USER
            cv = db.add_contacts_to_user_profile(
                user=user, name=click_name, phone_number=int(click_phone)
            )
            return self.all_actions_menu()

    def update_contact(self):
        cn = print_all_contact(user=self.USER)
        click_id = int(input(Fore.LIGHTGREEN_EX + "\n  ID : ") or 0)
        click_new_name = input("\n  Yangi Nom : ")
        click_new_phone = int(input("\n  Yangi Phone number : \n") or 0)

        if click_id != 0:
            check = db.is_user_contact_id_exists(user=self.USER, contc_id=click_id)
            if check == True:
                db.updating_contacts_to_user_profile(
                    self.USER,
                    contact_id=click_id,
                    new_name=click_new_name,
                    new_phone_number=click_new_phone,
                )

                return self.all_actions_menu()
            else:
                print(Fore.RED + "\n  Iltimos ID ni to'gri kiriting \n", Fore.RESET)
                return self.update_contact()
        elif click_id == 0:
            print(Fore.RED + "   Siz hech qaysi malumotni o'zgartirmadingiz !!!")
            return self.all_actions_menu()

    def delete_contact(self):
        cn = print_all_contact(user=self.USER)
        click_id = int(
            input(Fore.LIGHTRED_EX + "\n  Delete qilmoqchi bulgan contact ID yozing : ")
            or 0
        )
        if click_id != 0:
            check = db.is_user_contact_id_exists(user=self.USER, contc_id=click_id)
            if check == True:
                db.deleting_contacts_of_user(user=self.USER, contact_id=click_id)
                return self.all_actions_menu()
            return self.all_actions_menu()

    def search_contact(self):

        click_searching_name = input(Fore.BLUE + "\n  Contact name ? : " or " ")
        print_searched_contacts(user=self.USER, name=click_searching_name)
        if click_searching_name == "<":
            return self.all_actions_menu()
        self.search_contact()


if __name__ == "__main__":

    print(Fore.LIGHTGREEN_EX + cmd_contact_book.__doc__, Fore.CYAN + logo)
    contact = cmd_contact_book()
    contact.enter()
