import random
class User:
    def __init__(self, username, password):
        self.username = username
        self.password = password
        self.list_users = []
        
    def check_password(self, entered_password):
        return entered_password == self.password
    
    def create_user(username, password):
        new_user = User(username, password)
        print("Yourd username is : ",username,"and password is :",password)
        print("Creating new user ...")
        return new_user
    
    def passwordGenerator():
        inits = range(32, 127)

        password = ''
        for i in range(15):
            password += chr(random.choice(inits))   
        print(password)
        return password
        

    
    def create_new_user():
        username = input("Enter a username: ")
        choice = input("Would You like do generate random password?(Y/N) ")
        password = ''
        if choice == "y":
            User.passwordGenerator() 
            User.create_user(username, password)
        elif choice =="n":
            password = input("Enter a password: ")
            User.create_user(username, password)
      

