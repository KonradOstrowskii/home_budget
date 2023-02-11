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
    def check_username_exist(username: str)->bool:
        """
        Static method to check if username already exist in DB 

        Args:
            username (str): Checking if username exists in `DB`

        Returns:
            bool: Return True if exists and False if doesn't
        """
        cursor.execute("SELECT * FROM User WHERE username=?", (username,))
        if cursor.fetchone():
            return True
        return False
    
    @staticmethod
    def check_valid_password(password: str) -> bool:
        """
        Static method to check if password got at least 8 chars, at least one upper char and at least one digit

        Args:
            password (str): Checking password from User

        Returns:
            bool: Return True if password is correct and False if is incorrect
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
    def hash_password(password:str)->str:
        """
        Static method that hash password using hashlib 
        """
        return sha256(password.encode()).hexdigest()
    
    def check_login(username: str, password: str)-> any:
        """
        Function to check if username exist in `DB`
        """
        hashed_password = User.hash_password(password)
        cursor.execute("""
        SELECT * FROM User
        WHERE username=? AND password=?
        """, (username, hashed_password))
        return cursor.fetchone() is not None

    def create_user(username: str, password: str)->any:
        """
        Creating new user, checking if user already exists and verify if password complies with requirements,
        at least 8 character, one uppercase letter and one digit
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
    
    def checking_users_in_db():
        conn = sqlite3.connect("users.db")

        # Create a cursor
        c = conn.cursor()

        # Execute a SELECT statement
        c.execute("SELECT * FROM User")

        # Retrieve the results
        result = c.fetchall()

        # Print the results
        print(result)

# x = input("Add Username : ")
# y = input("Add password : ")
# create_user(x,y)
# while True:
#     username = input("Username: ")
#     password = input("Password: ")
#     if User.check_login(username, password):
#         print("Login successful.")
#         break
#     else:
#         print("Login failed. Try again.")

# db.close()

# Connect to the database
# conn = sqlite3.connect("users.db")

# # Create a cursor
# c = conn.cursor()

# # Execute a SELECT statement
# c.execute("SELECT * FROM User")

# # Retrieve the results
# result = c.fetchall()

# # Print the results
# print(result)
