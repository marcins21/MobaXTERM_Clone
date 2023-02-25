import tkinter
import tkinter.messagebox
import customtkinter as ctk

from user import User
from auth import add_user_to_database,delete_user_from_database,valid_user,get_all_users_logins_from_database,check_admin
import tkinter.messagebox as tkmb

ctk.set_appearance_mode("dark")  # Modes: "System" (standard), "Dark", "Light"
ctk.set_default_color_theme("dark-blue")  # Themes: "blue" (standard), "green", "dark-blue"

app = ctk.CTk()
app.geometry("400x400")
app.title("Login")

login_label = tkinter.StringVar()

def print_users_in_database(new_window,button):
    # Printing all usernames
    T = tkinter.Text(new_window, height=10, width=50)
    T.pack()
    text = "\nUsers In Database\n\n"
    __users_name_from_database = get_all_users_logins_from_database()
    for name in __users_name_from_database:
        text += f"name: {name} \n"
    T.insert(tkinter.END, text)
    button.configure(state="disabled",fg_color="grey")

def register_form_user():
    def register_user():
        register_login_form = register_login.get()
        register_password_form = register_password.get()
        register_combobox_form = register_combobox.get()

        registartion_user = User(register_login_form,register_password_form,register_combobox_form)
        regsistration_valid = add_user_to_database(registartion_user)

        if regsistration_valid:
            print("Registartion Completed FAILED")
        else:
            print("Something went wrong FAILED")

    register_window = ctk.CTkToplevel(app)
    register_window.title("Register user")
    register_window.geometry("500x250")
    ctk.CTkLabel(register_window,text="Register User").pack()

    register_frame = ctk.CTkFrame(master=register_window)
    register_frame.pack(padx=20,pady=10,fill="both",expand=True)

    register_login = ctk.CTkEntry(master=register_frame,placeholder_text="Username")
    register_login.pack(padx=20,pady=10)

    register_password = ctk.CTkEntry(master=register_frame,placeholder_text="Password",show="*")
    register_password.pack(padx=20,pady=1)

    register_combobox_var = ctk.StringVar(value="Simple User")
    register_combobox = ctk.CTkComboBox(master=register_frame, values=["Simple user", "Technical user", "Administrator"],
                               command=combobox_callback)
    register_combobox.pack(padx=10,pady=10)

    register_button_form = ctk.CTkButton(master=register_frame,text="Sumbit",command=register_user)
    register_button_form.pack(padx=10,pady=10)

def login_user():
    #Information Given by user
    user_form_login=user_login.get()
    user_form_password =user_password.get()
    user_form_role = combobox_var.get()
    user = User(user_form_login,user_form_password,user_form_role)
    user_valid = valid_user(user)

    if user_valid:
        #TODO
        #1) Redirect to -->Main Aplliaction after loggin user
        new_window = ctk.CTkToplevel(app)
        new_window.title("Login Info")
        new_window.geometry("500x250")
        ctk.CTkLabel(new_window, text=f"Welcome to service {user_form_login}! ").pack()
        is_user_admin = check_admin(user)
        if is_user_admin:
            show_user_names_Button = ctk.CTkButton(master=new_window,text="Show users",
                                                   command=lambda : print_users_in_database(new_window,show_user_names_Button))
            show_user_names_Button.pack()
        label.configure(text="Login Successfull",text_color="green",font=("Sans Serif",17,"bold"))
    else:
        label.configure(text="Wrong Password or Username",text_color="red",font=("Sans Serif",17,"bold"))


    #Debug info---
    print(f"login '{user_form_login}' :: password '{user_form_password}' :: role '{user_form_role}'")
   
def combobox_callback(choice):
    user_combobox_choice = choice
    return user_combobox_choice

label = ctk.CTkLabel(app,text="Login Form")
label.pack(padx=20,pady=20)

frame = ctk.CTkFrame(master=app)
frame.pack(padx=20,pady=10,fill="both",expand=True)

user_login = ctk.CTkEntry(master=frame,placeholder_text="Username")
user_login.pack(padx=20,pady=20)

user_password = ctk.CTkEntry(master=frame,placeholder_text="Password",show="*")
user_password.pack(padx=20,pady=1)

combobox_var = ctk.StringVar(value="Simple user")
combobox = ctk.CTkComboBox(master=frame,values=["Simple user","Technical user","Administrator"],command=combobox_callback
                           ,variable=combobox_var)
combobox.pack(padx=20,pady=20)

button = ctk.CTkButton(master=frame,text="Login",command=login_user)
button.pack(padx=15,pady=30)

register_button = ctk.CTkButton(master=app, text="Register", command=register_form_user)
register_button.pack()

if __name__ == "__main__":
    app.mainloop()