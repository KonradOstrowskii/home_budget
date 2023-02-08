import sqlite3
from hashlib import sha256


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
    @staticmethod
    def hash_password(password):
        return sha256(password.encode()).hexdigest()
    
    def check_login(username, password):
        hashed_password = User.hash_password(password)
        cursor.execute("""
        SELECT * FROM User
        WHERE username=? AND password=?
        """, (username, hashed_password))
        return cursor.fetchone() is not None
def add_user(username, password):
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

def check_login(username, password):
    hashed_password = User.hash_password(password)
    cursor.execute("""
    SELECT * FROM User
    WHERE username=? AND password=?
    """, (username, hashed_password))
    return cursor.fetchone() is not None
x = input("Add Username : ")
y = input("Add password : ")
add_user(x,y)
while True:
    username = input("Username: ")
    password = input("Password: ")
    if check_login(username, password):
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
