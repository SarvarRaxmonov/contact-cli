import getpass
import os
from cli_print import (
    entering_menu,
    logo,
    menu,
    print_all_contact,
    print_searched_contacts,
    light_collor,
    green_collor,
    red_collor,
    blue_collor,
    cyan_collor,
    light_cyan_collor,
    light_red_collor,
    stop_color,
)
from sqlite_saver import Server_transaction

os.system("cls")
db = True

db_transaction = Server_transaction()


class Enter_the_contact:

    """\n \n __ Enter to Contact __
    * Registiration
    * Login
    * Actionlarni bajaradi
    """

    def enter(self):

        click = input(entering_menu + "\n Login yoki new user ? : ")
        if click == "login":
            user = getpass.getpass("  Your username : ")
            checker = db_transaction.meet_requiremnts(
                user, data={"is_user_exists": True}
            )
            if checker == True:
                return Contact_actions().all_actions_menu(user=user)
            print(red_collor + "  Siz new user create qilmagansiz  ")
            return self.enter()

        if click == "new user":
            yangi_user = input("\n Iltimos name yozing :  ")
            return self.new_user(click=yangi_user)

    def new_user(self, click):
        if isinstance(click, str) and len(click) > 0:
            db_transaction.meet_requiremnts(data={"new_username": click})
            return Contact_actions().all_actions_menu(user=click)

        else:
            click = input(
                red_collor + "\n Iltimos to'g'ri kiriting name ni | orqaga : < | "
            )
            if click == "<":
                self.enter()
            return self.new_user(click=click)


class Contact_actions:

    """\n \n __ Contact buyicha hamma actionlar __
    * Contact filter
    * All contacts
    * Add, update, delete kabi actionlar junata olish serverga
    * exit (Yani offline datasini parchalab o'zi chiqib ketadi)
    """

    def all_actions_menu(self, user="Nomalum"):
        click = input(menu + light_cyan_collor + "\n  Qaysi actioni tanlaysiz : ")
        CA = Contact_actions()
        if len(click) > 0 and isinstance(click, str):
            for dir_actions in dir(CA):
                if click == dir_actions.replace("_", " "):
                    cn = print_all_contact(user=user)
                    return getattr(CA, dir_actions)(user)

        return self.all_actions_menu()

    def add_contact(self, user):
        click_name = input(light_collor + "\n Name : ")
        click_phone = int(input(light_collor + "\n Phone number : "))
        if len(click_name) > 0 and click_phone > 0:
            db_transaction.meet_requiremnts(
                user=user,
                data={
                    "add_contact_name": click_name,
                    "add_contact_number": click_phone,
                },
            )
            return self.all_actions_menu(user=user)

    def update_contact(self, user):
        click_id = int(input(green_collor + "\n  ID : ") or 0)
        click_new_name = input("\n  Yangi Nom : " or None)
        click_new_phone = int(input("\n  Yangi Phone number : ") or 0)

        if click_id != 0:
            check = db_transaction.meet_requiremnts(
                user=user, data={"contact_id": click_id}
            )
            if check == True:
                db_transaction.meet_requiremnts(
                    user,
                    data={
                        "user_upd_contact_id": click_id,
                        "user_upd_new_name": click_new_name,
                        "user_upd_new_phone_number": click_new_phone,
                    },
                )

                return self.all_actions_menu(user=user)
            else:
                print(red_collor + "\n  Iltimos ID ni to'gri kiriting \n", stop_color)
                return self.update_contact(user=user)
        elif click_id == 0:
            print(red_collor + "   Siz hech qaysi malumotni o'zgartirmadingiz !!!")
            return self.all_actions_menu(user=user)

    def delete_contact(self, user):

        click_id = int(
            input(light_red_collor + "\n  Delete qilmoqchi bulgan contact ID yozing : ")
            or 0
        )
        if click_id != 0:
            check = db_transaction.meet_requiremnts(
                user=user, data={"contact_id": click_id}
            )
            if check == True:
                db_transaction.meet_requiremnts(
                    user=user, data={"delet_contact_id": click_id}
                )
                return self.all_actions_menu(user=user)
        return self.all_actions_menu(user=user)

    def search_contact(self, user):
        click_searching_name = input(blue_collor + "\n  Contact name ? : " or " ")
        print_searched_contacts(user=user, name=click_searching_name)
        if click_searching_name == "<":
            return self.all_actions_menu(user=user)
        return self.search_contact(user=user)


if __name__ == "__main__":

    print(Enter_the_contact.__doc__, cyan_collor + logo)
    contact = Enter_the_contact()
    contact.enter()
