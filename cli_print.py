from sqlite_saver import Server_transaction
import colorama
import os
from colorama import Fore, Style, Back

os.system("cls")
colorama.init()
db_transaction = Server_transaction()



menu = (
    Fore.LIGHTWHITE_EX
    + """         
 _____________________________________________________________________________
   ===========      ==============      ==============     ================ 
 | ADD CONTACT |  | UPDATE CONTACT |  | DELETE CONTACT |  | SEARCH CONTACT | 
   ===========      ==============      ==============     ================
"""
)

enter_menu = """
 _________________________
   =======     =========
 |  LOGIN  | | NEW USER  | 
   =======     =========
"""
entering_menu = Fore.BLUE + enter_menu
light_collor = Fore.LIGHTWHITE_EX
green_collor = Fore.LIGHTWHITE_EX
red_collor = Fore.RED
blue_collor = Fore.BLUE
cyan_collor = Fore.CYAN
light_cyan_collor = Fore.LIGHTCYAN_EX
light_red_collor = Fore.LIGHTRED_EX
stop_color = Fore.RESET
logo = """                     
      
                                                             
            ====  +++   = =  ====   /  ^  \    ==== ====       ////////////
            ||   || || || ||  ||   / /   \ \   ||    ||       ||         || 
            ||   || || || ||  ||  / /= = =\ \  ||    ||       || contact ||
            ====  +++  || ||  || / /       \ \ ====  ||       ||_________||                                                           
                                                              
        =======================================================  ++++++++++
        =======================================================  ++++++++++
            """


def print_all_contact(user):
    cv = db_transaction.meet_requiremnts(user=user, data={"user_all_contact": True})
    print("\n   ", "ID".ljust(12) + "NAME".ljust(17) + "PHONE NUMBER \n")
    print("  ___________________________________________ \n")
    for i in cv:
        print("   |", str(i[0]).ljust(4), "  |  ", str(i[1]).ljust(10), "  |  ", i[2])


def print_searched_contacts(user, name):
    cv = db_transaction.meet_requiremnts(user=user, data={"search_contact_name": name})
    print("\n   ", "ID".ljust(12) + "NAME".ljust(17) + "PHONE NUMBER \n")
    print("  ___________________________________________ \n")
    for i in cv:
        print("   |", str(i[0]).ljust(4), "  |  ", str(i[1]).ljust(10), "  |  ", i[2])
