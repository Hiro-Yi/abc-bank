from getpass import getpass
import modules.util as util
from modules.database import db, connection
import modules.dashboard as dashboard


def displayMenu():
    while True:
        util.clear()
        print("\u001b[33;1m+----------------------------------------------------+")
        print("|\u001b[34;1m                🇼‌🇪‌🇱‌🇨‌🇴‌🇲‌🇪‌ 🇹‌🇴‌ 🇦‌🇧‌🇨‌ 🇧‌🇦‌🇳‌🇰‌ \u001b[33;1m|")
        print("+----------------------------------------------------+")
        print("|\u001b[32m 1.Login                                            \u001b[33;1m|")
        print("+----------------------------------------------------+")
        print("|\u001b[32m 2.Create Account                                   \u001b[33;1m|")
        print("+----------------------------------------------------+")
        print("|\u001b[32m 3.Exit                                             \u001b[33;1m|")
        print("+----------------------------------------------------+")
        print("\u001b[31;1m\nEnter your choice: ")

        try:
            choice = int(input("\u001b[34;1m> "))

            if choice == 1:
                login()

            elif choice == 2:
                register()

            elif choice == 3:
                util.clear()
                exit()

            else:
                print("Invalid choice selected !!")
                input("\nPress Any Key to Continue ...")

        except ValueError:
            print("Invalid choice selected !!")
            input("\nPress Any Key to Continue ...")


def login():
    util.clear()
    print("+----------------------------------------------------+")
    print("|                   Login Account                    |")
    print("+----------------------------------------------------+")

    print("Enter your username:")
    username = input("> ")

    print("Enter Your Password:")
    password = input("> ")

    db.execute(
        "select * from users where username = %s and password = SHA1(%s)", (username, password))
    result = db.fetchone()

    if result != None:
        dashboard.displayMenu(result[0])

    else:
        print("Incorrect Username/Password !!")
        input("\nPress Any Key to Continue ...")


def register():
    util.clear()

    print("+----------------------------------------------------+")
    print("|                   Create Account                   |")
    print("+----------------------------------------------------+")

    print("\nEnter your first name:")
    firstName = input("> ")

    print("\nEnter your last name:")
    lastName = input("> ")

    while True:
        print("\nEnter your Username:")
        username = input("> ")

        db.execute("SELECT * FROM users WHERE username = %s", (username,))
        result = db.fetchone()

        if result != None:
            print("Username is already registered !!")

        else:
            break

    while True:
        print("\nEnter your gender(M/F):")
        gender = input("> ")

        gender = gender.upper()
        if gender == "M" or gender == "F":
            break

        else:
            print("Gender can be either M or F !!")

    while True:
        print("\nEnter your age:")
        age = input("> ")

        try:
            age = int(age)

            if age < 13:
                print("Age should be atleast 13 Years !!")

            elif age > 139:
                print("Age must be less then 140 Years !!")

            else:
                break

        except:
            print("Age must be number !!")

    while True:
        print("\nEnter Phone number:")
        phone = input("> ")

        try:
            if len(phone) == 10:
                db.execute(
                    "SELECT * FROM users WHERE phone = %s", (phone,))
                result = db.fetchone()

                if result != None:
                    print("Phone number is already registered !!")

                else:
                    break

            else:
                print("Please enter a valid phone number !!")

        except:
            print("Please enter a valid phone number !!")

    print("\nEnter Your city:")
    city = input("> ")

    while True:
        print("\nEnter your password:")
        password = input("> ")
        
        if len(password) < 8 or len(password) > 13:
            print(
                "Password must be greater than 8 characters and smaller than 13 characters !!")

        else:

            break
    values = (username, firstName, lastName, gender, age, phone, city, password)

    db.execute("INSERT INTO abc_bank.users( username, first_name, last_name, gender, age, phone, city, password ) VALUES ( %s, %s, %s, %s, %s, %s, %s, SHA1(%s) )", values)
    connection.commit()
    
    input("\nPress Any Key to Continue ...")