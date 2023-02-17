import sqlite3
from server import Server

conn = sqlite3.connect('servers_database.db')
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

def add_server_to_database(server:Server) -> bool:
    server_name = server.get_server_name()
    ip = server.get_server_ip()
    user = server.get_server_user()
    password = server.get_user_password()
    server_names = get_server_names_from_database()
    if server_name in server_names:
        print("Server Already Exists in Database FAILED")
        return False

    cursor.execute("INSERT INTO servers(server_name,ip,user,password) VALUES(:server_name,:ip,:user,:password)",
                   {'server_name':server_name, 'ip':ip, 'user':user, 'password':password})
    conn.commit()
    print(f"Server {server.get_server_name()} added Successfully to Database")
    return True

def delete_server_from_database(server:Server) -> bool:
    server_name = server.get_server_name()
    ip = server.get_server_ip()
    user = server.get_server_user()
    password = server.get_user_password()
    server_names = get_server_names_from_database()
    if server_name not in server_names:
        print("Server Doesn't Exists in Database FAILED")
        return False

    cursor.execute("DELETE FROM servers WHERE server_name=:server_name ",{'server_name':server_name})
    conn.commit()
    print(f"Server {server.get_server_name()} Deleted Successfully from Database")
    return True


def edit_server_in_database(server:Server,new_server_name="",new_ip="",new_user="",new_password="") -> bool:
    server_name = server.get_server_name()
    server_name_before_change = server.get_server_name()
    ip = server.get_server_ip()
    user = server.get_server_user()
    password = server.get_user_password()
    server_names = get_server_names_from_database()

    if server_name in server_names:
        #if user doesnt give all informations
        if (new_server_name == "") or (new_ip == "") or (new_user == "") or (new_password == ""):
            if new_server_name == "":
                new_server_name = server_name
            if new_ip == "":
                new_ip  = ip
            if new_user == "":
                new_user = user
            if new_password == "":
                new_password = password

        server_name = new_server_name
        ip = new_ip
        user = new_user
        password = new_password

        cursor.execute("UPDATE servers SET server_name=:new_server_name,ip=:new_ip,user=:new_user,password=:new_password WHERE server_name=:server_name"
                       ,{'new_server_name':server_name,'new_ip':ip,'new_user':user,'new_password':password,'server_name':server_name_before_change})
        conn.commit()
        return True

    else:
        print(f"Server {server.get_server_name()} is not in Database FAILED")
        return False





