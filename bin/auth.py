import sqlite3
from users import User


conn = sqlite3.connect("users_database.db")
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







