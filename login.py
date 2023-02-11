from user import *
import getpass

def  start_menu():
    print("Welcome in Home Budget Tracker!\nLogin Menu!\nLog In press L\nfor Sing Up press S")
start_menu()
action = input("Log In /Sing Up : ").upper()
if action == "L":
    username = input("Username: ")
    password = input("Password: ")
    if User.check_login(username, password):
        print("""Checking credentials")
...
Login successful.""")
    else:
        print("Login failed. Try again.")
if action == "S":
    print("CREATING NEW USER :")
    username = input("Input Username: ")
    print("password should contain at least 8 characters, contain at least one uppercase letter and one digit")
    password = getpass.getpass("Input Password: ")
    print("Adding Your credentials to database\nAccount created\nHave a nice day!")
    User.create_user(username,password)