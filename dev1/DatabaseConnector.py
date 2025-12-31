class DatabaseConnector:
    def __init__(self,host,user,password):
        self.__host = host
        self.__user = user
        self.__password = password
    
    def connect(self):
        return f"Connected to {self.__host}"
    
    def get_host(self):
        return self.__host
    
host=input("Enter the Host name : ")
user=input("Enter the user name: ")
password =input("Enter the password: ")

d1=DatabaseConnector(host,user,password)

print('-'*20)

print(d1.connect())
print(d1.get_host()) 