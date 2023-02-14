import sqlite3
from server import Server


conn = sqlite3.connect('test.db')
cursor = conn.cursor()
table_query = """CREATE TABLE IF NOT EXISTS servers(
                server_name text,
                ip text,
                user text,
                password text
                )"""
cursor.execute(table_query)
conn.commit()

def get_server_names_from_database():
    server_names_query = conn.execute("SELECT server_name FROM servers")
    server_names = []
    for record in server_names_query:
        server_names.append(record[0])
    return server_names

def add_server_to_database(server:Server):
    server_name = server.get_server_name()
    ip = server.get_server_ip()
    user = server.get_server_user()
    password = server.get_user_password()
    server_names = get_server_names_from_database()
    if server_name in server_names:
        print("Server Already Exists in Database")
        return 0

    cursor.execute("INSERT INTO servers(server_name,ip,user,password) VALUES(:server_name,:ip,:user,:password)",
                   {'server_name':server_name, 'ip':ip, 'user':user, 'password':password})
    conn.commit()

def delete_server_from_database(server:Server):
    server_name = server.get_server_name()
    ip = server.get_server_ip()
    user = server.get_server_user()
    password = server.get_user_password()
    server_names = get_server_names_from_database()
    if server_name not in server_names:
        print("Server Doesn't Exists in Database")
        return 0

    cursor.execute("DELETE FROM servers WHERE server_name=:server_name ",{'server_name':server_name})

def edit_server_in_database(server:Server):







    conn.commit()




