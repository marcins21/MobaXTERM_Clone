from server_functions import *
from auth import *
from user import User
from server import Server

def main():

    server1 = Server(f"Dns-name","192.168.0.1","sadmin","pass")
    #show_server_info(server1,validate_sever(server1))
    # add_server_to_database(server1)
    # delete_server_from_database(server1)
    # edit_server_in_database(server1,"Changed_training-04_1","10.1.1.90909","changed","pass")

    user1 = User("username","Pass","Simple user")
    #valid_user(user1)
    #add_user_to_database(user1)
    #delete_user_from_database(user1)
    #print(get_all_users_logins_from_database())

main()
