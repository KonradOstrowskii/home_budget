class User:
    users = []
    def __init__(self, username, password):
        self.username = username
        self.password = password
    # Function that checking if username already exist
    @classmethod
    def check_username_exist(cls, username):
        for user in cls.users:
            if user.username == username:
                return True
        return False
    # Function that checking if password contain length of at least 8 char ,is there any digit and at least one char is upper
    @classmethod
    def check_valid_password(cls, password):
        if len(password) < 8:
            return False
        if not any(c.isupper() for c in password):
            return False
        if not any(c.isdigit() for c in password):
            return False
        return True
# Creating new user   
def create_new_user():
    username = input("Enter a username: ")
    password = input("Enter a password: ")
    
    if User.check_username_exist(username):
        print("username already exist")
        return
    if not User.check_valid_password(password):
        print("Invalid password, it should be at least 8 characters, contain at least one uppercase letter and one digit")
        return
    new_user = User(username, password)
    User.users.append(new_user)
    print(f"user {username} created")
    
create_new_user()

