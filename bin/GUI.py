import tkinter
import tkinter.messagebox
import customtkinter as ctk
from auth import add_user_to_database,delete_user_from_database,valid_user
from user import User
import tkinter.messagebox as tkmb

ctk.set_appearance_mode("dark")  # Modes: "System" (standard), "Dark", "Light"
ctk.set_default_color_theme("dark-blue")  # Themes: "blue" (standard), "green", "dark-blue"

app = ctk.CTk()
app.geometry("400x400")
app.title("Login")

login_label = tkinter.StringVar()


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
        new_window.geometry("500x150")
        ctk.CTkLabel(new_window,text=f"Welcome to service {user_form_login}! ").pack()

        label.configure(text="Login Successfull",text_color="green",font=("Sans Serif",17,"bold"))
    else:
        label.configure(text="Wrong Password or Username",text_color="red",font=("Sans Serif",17,"bold"))
        #tkmb.showinfo(title="Wrong Passowrd or Username",message="Check Username or Password")

   
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

combobox_var = ctk.StringVar(value="Simple User")
combobox = ctk.CTkComboBox(master=frame,values=["Simple user","Technical User","Administrator"],command=combobox_callback
                           ,variable=combobox_var)
combobox.pack(padx=20,pady=20)

button = ctk.CTkButton(master=frame,text="Login",command=login_user)
button.pack(padx=15,pady=30)



if __name__ == "__main__":
    app.mainloop()