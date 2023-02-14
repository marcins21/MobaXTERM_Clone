
class Server:
    def __init__(self,server_name,ip_address,server_user,user_password):
        self.name = server_name
        self.ip = ip_address
        self.user = server_user
        self.__password = user_password

    #Setters
    def set_server_name(self,server_name):
        self.name = server_name
    def set_server_ip_address(self,server_ip):
        self.ip = server_ip
    def set_server_user(self,server_user):
        self.user = server_user
    def set_user_password(self,user_password):
        # Auth ... !! Password !!
        self.__password = user_password

    #Getters
    def get_server_name(self):
        return self.name
    def get_server_ip(self):
        return self.ip
    def get_server_user(self):
        return self.user
    def get_user_password(self):
        # Auth... !! Password !!
        return self.__password

