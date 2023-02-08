import sqlite3
from hashlib import sha256

# Creating users.db containing username and password 
with sqlite3.connect("users.db") as db:
    cursor = db.cursor()
cursor.execute("""
CREATE TABLE IF NOT EXISTS User(
id INTEGER PRIMARY KEY,
username TEXT NOT NULL,
password TEXT NOT NULL);
""")
db.commit()
class User:
    def __init__(self, username: any, password: any)-> object:
        self.username = username 
        self.password = password
          
    @staticmethod
    def check_username_exist(username: any)->bool:
        """
        Static method that checking if username already exist in DB 

        Args:
            username (any): Checking username in `DB`

        Returns:
            any: Return True/False depends if user exist or not
        """
        cursor.execute("SELECT * FROM User WHERE username=?", (username,))
        if cursor.fetchone():
            return True
        return False
    
    @staticmethod
    def check_valid_password(password: any) -> bool:
        """
        Static method that checking if password got at least 8 char,at least one upper char and at least one digit

        Args:
            password (any): Checking  if password from User compiles with requirements

        Returns:
            bool: Return True/False
        """
        
        if len(password) < 8:
            return False
        elif not any(c.isupper() for c in password):
            return False
        elif not any(c.isdigit() for c in password):
            return False
        return True
    
    # Static method that hash password using hashlib 
    @staticmethod
    def hash_password(password:any)->any:
        """
        Static method that hash password using hashlib 
        """
        return sha256(password.encode()).hexdigest()
    
    def check_login(username: any, password: any)-> any:
        """
        Function that checking if username exist in `DB`
        """
        hashed_password = User.hash_password(password)
        cursor.execute("""
        SELECT * FROM User
        WHERE username=? AND password=?
        """, (username, hashed_password))
        return cursor.fetchone() is not None

def create_user(username: any, password: any)->any:
    """
    Creating new user , checking if user already exist and verify if password compiles with requirements,
    at least 8 character once uppercase letter and one digit
    """
    if User.check_username_exist(username):
            print("username already exist")
            return
    if not User.check_valid_password(password):
        print("Invalid password, it should be at least 8 characters, contain at least one uppercase letter and one digit")
        return
    hashed_password = User.hash_password(password)
    cursor.execute("""
    INSERT INTO User (username, password)
    VALUES (?, ?)
    """, (username, hashed_password))
    db.commit()

x = input("Add Username : ")
y = input("Add password : ")
create_user(x,y)
while True:
    username = input("Username: ")
    password = input("Password: ")
    if User.check_login(username, password):
        print("Login successful.")
        break
    else:
        print("Login failed. Try again.")

db.close()

# Connect to the database
conn = sqlite3.connect("users.db")

# Create a cursor
c = conn.cursor()

# Execute a SELECT statement
c.execute("SELECT * FROM User")

# Retrieve the results
result = c.fetchall()

# Print the results
print(result)
