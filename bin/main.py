from functions import *
from server import Server

def main():
    server1 = Server("gni-training-04","10.1.1.118","sadmin","softel13")
    add_server_to_database(server1)
    #delete_server_from_database(server1)
    #edit_server_in_database(server1,"Changed_training-04_1","10.1.1.90909","changed","pass")
main()