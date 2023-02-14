from functions import *
from server import Server

def main():
    server1 = Server("gni-training-322","10.1.1.118","sadmin","softel13")
    add_server_to_database(server1)
    #delete_server_from_database(server1)
main()