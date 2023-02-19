
class User:
    def __init__(self,user_login,user_password,user_role):
        self.user_login = user_login
        self.user_password = user_password
        self.user_role = user_role

    #Setters
    def set_user_login(self,new_login):
        self.user_login = new_login
    def set_user_password(self,new_password):
        self.user_password = new_password
    def set_user_role(self,new_role):
        self.user_role = new_role

    #getters
    def get_user_login(self):
        return self.user_login
    def get_user_password(self):
        return self.user_password
    def get_user_role(self):
        return self.user_role