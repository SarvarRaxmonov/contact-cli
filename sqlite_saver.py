import sqlite3
import colorama
from colorama import Fore, Style, Back

colorama.init()

conn = sqlite3.connect("contact.db")
c = conn.cursor()
conn.row_factory = sqlite3.Row


class Server:

    """__ Bu server __
    malumotlar qushish va ular ni uchirish , o'zgartirish uchun

    """
  # USER CHECKING SECURITY ////////////////////////////////////////////////////////////////
  
    def is_user_exists(self, username=None):
        assert (
            type(username) is str and len(username) > 0 and username != None
        ), "System error"
        c.execute(
            f"SELECT EXISTS(SELECT name FROM Users WHERE name='{username}' LIMIT 1)"
        )
        if c.fetchone()[0] == 1:
            return True
        return False
  
    def is_user_contact_id_exists(self,user,contc_id=None):
        assert (
            len(user) and len(str(contc_id)) > 0 and isinstance(contc_id,int)
        ), "IS USER CONTACT ID EXISTS | SYSTEM ERROR"
        c.execute(
            f"SELECT EXISTS(SELECT id FROM {user} WHERE id='{contc_id}' LIMIT 1)"
        )
        if c.fetchone()[0] == 1:
            return True
        return False
  
  # END OF USER CHECKING SECURITY ////////////////////////////////////////////////////////////////
  
  # START OF THE USER ACTIONS    \\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\
           
    def user_all_contacts(self, user):
    
        c.execute(f"SELECT id, name, phone_number FROM {user}")
        record = c.fetchall()
        return record 
         
    def new_user_create(user_name):

        assert type(user_name) is str and len(user_name) > 0, "System error"
        c.execute("INSERT INTO Users VALUES(?)", (user_name,))
        c.execute(
            f"CREATE TABLE '{user_name}'(id integer PRIMARY KEY,name text,phone_number integer)"
        )
        conn.commit()

        return print(Fore.GREEN + f"\n {user_name} user created ***")

    def add_contacts_to_user_profile(self, user, name="Nomalum", phone_number=0):

        assert (
            len(name) > 0 and type(phone_number) == int
        ), "New contact adding system error"
        c.execute(
            f"INSERT INTO '{user}' (name, phone_number) VALUES(?,?)",
            (name, phone_number),
        )
        conn.commit()
        return print(Fore.GREEN + f" \n {name} contact created ***")

    def updating_contacts_to_user_profile(
        self,
        user,
        contact_id: int,
        new_name: str = "Nomalum",
        new_phone_number: int = "Nomalum",
    ):

        assert user is not None and contact_id != None, "Updating contact system error"
        if new_name != "":
            c.execute(
                f"""UPDATE '{user}' SET name = ? WHERE id = ?""", (new_name, contact_id)
            )
        if new_phone_number != 0:
            c.execute(
                f"""UPDATE '{user}' SET phone_number = ? WHERE id = ?""",
                (new_phone_number, contact_id),
            )
        else:
            print(Fore.RED+"   Siz hech qaysi malumotni o'zgartirmadingiz !!!")
        conn.commit()
        print(f"   {contact_id} user data credentials updated ")

    def deleting_contacts_of_user(self,user, contact_id: int):
        
        c.execute(f"""DELETE FROM '{user}' WHERE id LIKE {contact_id}""")
        conn.commit()
        return print(Fore.CYAN + f"  [ID : {contact_id}] user all data deleted * * * ")

    def searching_name_in_user_contacts(self,user,name):
        c.execute(f"SELECT * FROM {user} WHERE name LIKE '{str(name)}%'")
        result = c.fetchall() 
            
        return result



if __name__ == "__main__":
    cv = Server()
    cv.user_all_contacts(user="uzbek")
    print(Server.__doc__)
