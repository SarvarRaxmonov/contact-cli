from sqlite_saver import Server
import colorama
import os
from colorama import Fore, Style, Back
from cmd_cli import print_searched_contacts 
os.system("cls")
colorama.init()
db = Server()

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

logo = """                     
      
                                                             
            ====  +++   = =  ====   /  ^  \    ==== ====       ////////////
            ||   || || || ||  ||   / /   \ \   ||    ||       ||         || 
            ||   || || || ||  ||  / /= = =\ \  ||    ||       || contact ||
            ====  +++  || ||  || / /       \ \ ====  ||       ||_________||                                                           
                                                              
        =======================================================  ++++++++++
        =======================================================  ++++++++++
            """


def print_all_contact(user):
    cv = db.user_all_contacts(user=user)
    print("\n   ","ID".ljust(12)+"NAME".ljust(17)+"PHONE NUMBER \n")
    print("  ___________________________________________ \n")
    for i in cv:
        print("   |", str(i[0]).ljust(4),"  |  " , str(i[1]).ljust(10),"  |  ",i[2])

def print_searched_contacts(user,name):
    cv = db.searching_name_in_user_contacts(user=user,name=name)
    print("\n   ","ID".ljust(12)+"NAME".ljust(17)+"PHONE NUMBER \n")
    print("  ___________________________________________ \n")
    for i in cv:
        print("   |", str(i[0]).ljust(4),"  |  " , str(i[1]).ljust(10),"  |  ",i[2])    
   
    return print_searched_contacts()  