import sqlite3
import colorama
from dataclasses import dataclass, field
from colorama import Fore, Style, Back

colorama.init()

conn = sqlite3.connect("contact.db")
c = conn.cursor()
conn.row_factory = sqlite3.Row


@dataclass(init=True)
class Server:

    """__ Bu server __
    malumotlar qushish va ular ni uchirish , o'zgartirish uchun

    """

    _user: str
    _dicts: dict

    # USER CHECKING SECURITY ////////////////////////////////////////////////////////////////

    def is_user_exists(self):
        is_user_exists = self._dicts.get("is_user_exists")

        if is_user_exists == True:
            assert (
                type(self._user) is str and len(self._user) > 0 and self._user != None
            ), "System error"
            c.execute(
                f"SELECT EXISTS(SELECT name FROM Users WHERE name='{self._user}' LIMIT 1)"
            )

            if c.fetchone()[0] == 1:
                return True
            return False

    def is_user_contact_id_exists(self):
        contact_id = self._dicts.get("contact_id")
        if contact_id != None:
            assert (
                len(self._user)
                and len(str(contact_id)) > 0
                and isinstance(contact_id, int)
            ), "IS USER CONTACT ID EXISTS | SYSTEM ERROR"
            c.execute(
                f"SELECT EXISTS(SELECT id FROM {self._user} WHERE id='{contact_id}' LIMIT 1)"
            )
            if c.fetchone()[0] == 1:
                return True
            return False

    # END OF USER CHECKING SECURITY ////////////////////////////////////////////////////////////////

    # START OF THE USER ACTIONS    \\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\

    def user_all_contacts(self):
        user_all_contact = self._dicts.get("user_all_contact")
        if user_all_contact == True:
            c.execute(f"SELECT id, name, phone_number FROM {self._user}")
            record = c.fetchall()
            return record

    def new_user_create(self):
        new_username = self._dicts.get("new_username")
        if new_username != None:
            assert type(new_username) is str and len(new_username) > 0, "System error"
            c.execute("INSERT INTO Users VALUES(?)", (new_username,))
            c.execute(
                f"CREATE TABLE '{new_username}'(id integer PRIMARY KEY,name text,phone_number integer)"
            )
            conn.commit()

            return print(Fore.GREEN + f"\n {new_username} user created ***")

    def add_contacts_to_user_profile(self):
        add_contact_name = self._dicts.get("add_contact_name")
        add_contact_number = self._dicts.get("add_contact_number", 0)
        if add_contact_name != None:
            assert (
                len(add_contact_name) > 0 and type(add_contact_number) == int
            ), "New contact adding system error"
            c.execute(
                f"INSERT INTO '{self._user}' (name, phone_number) VALUES(?,?)",
                (add_contact_name, add_contact_number),
            )
            conn.commit()
            return print(Fore.GREEN + f" \n {add_contact_name} contact created ***")

    def updating_contacts_to_user_profile(self):
        user_upd_contact_id = self._dicts.get("user_upd_contact_id")
        user_upd_new_name = self._dicts.get("user_upd_new_name", None)
        user_upd_new_phone_number = self._dicts.get("user_upd_new_phone_number", 0)
        if user_upd_contact_id != None:
            assert (
                self._user is not None and user_upd_contact_id != None
            ), "Updating contact system error"
            if user_upd_new_name != None or user_upd_new_name != "":
                c.execute(
                    f"""UPDATE '{self._user}' SET name = ? WHERE id = ?""",
                    (user_upd_new_name, user_upd_contact_id),
                )
            elif user_upd_new_phone_number != 0:
                c.execute(
                    f"""UPDATE '{self._user}' SET phone_number = ? WHERE id = ?""",
                    (user_upd_new_phone_number, user_upd_contact_id),
                )
            else:
                print(Fore.RED + "   Siz hech qaysi malumotni o'zgartirmadingiz !!!")
            conn.commit()
            print(f"   {user_upd_contact_id} user data credentials updated ")

    def deleting_contacts_of_user(self):
        delet_contact_id = self._dicts.get("delet_contact_id")
        if delet_contact_id != None:
            c.execute(
                f"""DELETE FROM '{self._user}' WHERE id LIKE {delet_contact_id}"""
            )
            conn.commit()
            return print(
                Fore.CYAN + f"  [ID : {delet_contact_id}] user all data deleted * * * "
            )

    def searching_name_in_user_contacts(self):
        search_contact_name = self._dicts.get("search_contact_name")
        if search_contact_name != None:
            c.execute(
                f"SELECT * FROM {self._user} WHERE name LIKE '{str(search_contact_name)}%'"
            )
            result = c.fetchall()

            return result


class Server_transaction:
    def meet_requiremnts(self, user=None, data=None):
        cv = Server(user, data)
        requirment_meet = None
        for dir_names in dir(cv):
            if not dir_names.startswith("_"):
                if getattr(cv, dir_names)() != None:
                    requirment_meet = getattr(cv, dir_names)()

        return requirment_meet


if __name__ == "__main__":
    print(Server.__doc__)
