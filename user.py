import sqlite3

with sqlite3.connect('user_base.db') as db:
    cursor = db.cursor()
# Creating DB containing users with ID, username, password
cursor.execute("""
CREATE TABLE IF NOT EXISTS User(
id INTEGER PRIMARY KEY,
username TEXT NOT NULL,
password TEXT NOT NULL);
""")
# User class 
class User:
    def __init__(self, username, password):
        self.username = username 
        self.password = password
    # Staticmethod that checking if username already exist in DB   
    @staticmethod
    def check_username_exist(username):
        cursor.execute("SELECT * FROM User WHERE username=?", (username,))
        if cursor.fetchone():
            return True
        return False
    # Staticmethod that checking if password got at least 8 char,at least one upper char and at least one digit
    @staticmethod
    def check_valid_password(password):
        if len(password) < 8:
            return False
        elif not any(c.isupper() for c in password):
            return False
        elif not any(c.isdigit() for c in password):
            return False
        return True
    # Creating new user 
    def create(self):
        if User.check_username_exist(self.username):
            print("username already exist")
            return
        if not User.check_valid_password(self.password):
            print("Invalid password, it should be at least 8 characters, contain at least one uppercase letter and one digit")
            return
        cursor.execute("INSERT INTO User (username, password) VALUES (?,?)", (self.username, self.password))
        db.commit()
        print(f"user {self.username} created")
        



def create_new_user():
    while True:
        username = input("Enter a username: ")  
        password = input("Enter a password: ")
        if User.check_username_exist(username):
            print("username already exist")
            break
        if not User.check_valid_password(password):
            print("Invalid password, it should be at least 8 characters, contain at least one uppercase letter and one digit")
            break
        new_user = User(username, password)
        new_user.create()
        break


create_new_user()

# Connect to the database
conn = sqlite3.connect("user_base.db")

# Create a cursor
c = conn.cursor()

# Execute a SELECT statement
c.execute("SELECT * FROM User")

# Retrieve the results
result = c.fetchall()

# Print the results
print(result)
