from server_functions import *
from auth import *
from front_menu import *
from user import User
from server import Server

def main():
    # TODO
    # 1) interactive menu
    # 2) User Authentication -- Database
    # 3) Special Authenthiaction for password change
    # 4) Add Connect Feature that allows users to connect to specific server

    server1 = Server(f"gni-training-01","10.1.1.118","sadmin","softel13")
    #show_server_info(server1,validate_sever(server1))
    # add_server_to_database(server1)
    # delete_server_from_database(server1)
    # edit_server_in_database(server1,"Changed_training-04_1","10.1.1.90909","changed","pass")

    user1 = User("marcin","Pass","Simple user")
    #valid_user(user1)
    #add_user_to_database(user1)
    #delete_user_from_database(user1)
    #print(get_all_users_logins_from_database())

main()