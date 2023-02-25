import sqlite3
from user import User


conn = sqlite3.connect("servers_database.db")
cursor = conn.cursor()
table_query = """CREATE TABLE IF NOT EXISTS users(
                user_login text,
                user_password text,
                user_role text      
                )"""
cursor.execute(table_query)
conn.commit()


def get_all_users_logins_from_database():
    all_user_logins_query = conn.execute("SELECT user_login FROM users")
    all_users = []
    for record in all_user_logins_query:
        all_users.append(record[0])
    return all_users

def add_user_to_database(user:User) -> bool:
    user_login = user.get_user_login()
    user_password = user.get_user_password()
    user_role = user.get_user_role()
    users = get_all_users_logins_from_database()
    if user_login in users:
        print(f"User Already in Database FAILED")
        return False

    conn.execute("INSERT INTO users(user_login,user_password,user_role) VALUES(:user_login,:user_password,:user_role)",
                 {'user_login':user_login,'user_password':user_password,'user_role':user_role})
    conn.commit()
    return True


def delete_user_from_database(user:User) -> bool:
    user_login = user.get_user_login()
    user_password = user.get_user_password()
    user_role = user.get_user_role()
    users = get_all_users_logins_from_database()
    if not user_login in users:
        print(f"Cannot delete user, Not in Database FAILED")
        return False

    cursor.execute("DELETE FROM users WHERE user_login=:user_login ", {'user_login': user_login})
    conn.commit()

def valid_user(user:User) -> bool:
    user_login = user.get_user_login()
    user_password = user.get_user_password()
    user_role = user.get_user_role()
    users = get_all_users_logins_from_database()
    if not user_login in users:
        print(f"login Failed user {user_login} not in database")
        return False

    passw = cursor.execute("SELECT user_password FROM users WHERE user_login=:user_login",{'user_login':user_login}).fetchone()
    role = cursor.execute("SELECT user_role FROM users WHERE user_login=:user_login",{'user_login':user_login}).fetchone()
    if passw[0] == user_password:
        print(f"User '{user_login}' logged SUCCESFULLY")
        #Checking User Role
        print(role[0])
        if role[0] == user_role:
            return True
        else:
            print(f"Wrong user Role Selected FAILED")
            return False
    else:
        print(f"Wrong password for user {user_login}")
        return False

def check_admin(user:User) -> bool:
    user_role = user.get_user_role()
    if user_role == "Administrator":
        return True
    else:
        return False











