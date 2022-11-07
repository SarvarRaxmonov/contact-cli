import sqlite3

conn = sqlite3.connect("contact.db")
c = conn.cursor()
conn.row_factory = sqlite3.Row



class Server:

    """ __ Bu server __
    malumotlar qushish va ular ni uchirish , o'zgartirish uchun

    """

    def new_user_create(user_name):

        assert type(user_name) is str and len(user_name) > 0, "System error"
        c.execute("INSERT INTO Users VALUES(?)", (user_name,))
        c.execute(
            f"CREATE TABLE '{user_name}'(id integer PRIMARY KEY,name text,phone_number integer)"
        )
        conn.commit()

        return print(f"{user_name} user created")

    def add_contacts_to_user_profile(user, name="Nomalum", phone_number=0):

        assert (
            len(name) > 0 and type(phone_number) == int
        ), "New contact adding system error"
        c.execute(
            f"INSERT INTO '{user}' (name, phone_number) VALUES(?,?)",
            (name, phone_number),
        )
        conn.commit()
        return print(f"{name} contact created")
    
    def updating_contacts_to_user_profile(
        user,
        contact_id: int,
        new_name: str = "Nomalum",
        new_phone_number: int = "Nomalum",
    ):

        assert user is not None and contact_id != None, "Updating contact system error"
        if new_name != "Nomalum":
            c.execute(
                f"""UPDATE '{user}' SET name = ? WHERE id = ?""", (new_name, contact_id)
            )
        if new_phone_number != "Nomalum":
            c.execute(
                f"""UPDATE '{user}' SET phone_number = ? WHERE id = ?""",
                (new_phone_number, contact_id),
            )
        conn.commit()
        return print(f"{contact_id} user data credentials updated ")  
    
    def deleting_contacts_of_user(user, contact_id: int):

        c.execute(f"""DELETE from '{user}' WHERE id LIKE {contact_id}""")
        conn.commit()
        return print(f"{contact_id} user all data deleted * * * ")

if __name__ == "__main__":
    print(Server.__doc__)


