from getpass import getpass
from modules.home import home
from modules.database import db, connection


def profile():
    print("1. Change your {username}")
    print("2. Change your {age}")
    print("3. Change your {gender}")
    print("4. Change your {city}")
    print("5. Change your Password !!")
    print("6. Exit")
    answer = input("> ")
    if answer == 1 :
        print("Enter your username")
        usernameNew = input("> ")
        db.execute("UPDATE users SET username = %s where username = %s ",(usernameNew,username))
    elif answer == 5 :
        username = "qw"
        print("Enter Your Password: ")
        password = getpass("> ")

        db.execute(
            "select * from users where username = %s and password = SHA1(%s)", (username, password))
        result = db.fetchone()

        if result != None:
            while True:
                print("Enter Your Password: ")
                passwordOne = getpass("> ")
                print("Enter Retype Your Password: ")
                passwordSec = getpass("> ")
                if passwordOne == passwordSec :
                    print("Password changed !!")
                    pass
                else:
                    print("Password dosen`t match !!")
                    print("Try again !!")

