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
    print("\u001b[33;1m+----------------------------------------------------+")
    print("|\u001b[32m                   Login Account                    \u001b[33;1m|")
    print("+----------------------------------------------------+")

    print("\u001b[31;1mEnter your username:")
    username = input("\u001b[34;1m> ")

    print("\u001b[31;1mEnter Your Password:")
    password = input("\u001b[34;1m> ")

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

    print("\u001b[33;1m+----------------------------------------------------+")
    print("|\u001b[32m                   Create Account                   \u001b[33;1m|")
    print("+----------------------------------------------------+")

    print("\u001b[32m\nEnter your first name:")
    firstName = input("\u001b[34;1m> ")

    print("\u001b[32m\nEnter your last name:")
    lastName = input("\u001b[34;1m> ")

    while True:
        print("\u001b[32m\nEnter your Username:")
        username = input("\u001b[34;1m> ")

        db.execute("SELECT * FROM users WHERE username = %s", (username,))
        result = db.fetchone()

        if result != None:
            print("\u001b[31;1mUsername is already registered !!")

        else:
            break

    while True:
        print("\u001b[32m\nEnter your gender(M/F):")
        gender = input("\u001b[34;1m> ")

        gender = gender.upper()
        if gender == "M" or gender == "F":
            break

        else:
            print("\u001b[31;1mGender can be either M or F !!")

    while True:
        print("\u001b[32m\nEnter your age:")
        age = input("\u001b[34;1m> ")

        try:
            age = int(age)

            if age < 13:
                print("\u001b[31;1mAge should be atleast 13 Years !!")

            elif age > 139:
                print("\u001b[31;1mAge must be less then 140 Years !!")

            else:
                break

        except:
            print("\u001b[31;1mAge must be number !!")

    while True:
        print("\u001b[32m\nEnter Phone number:")
        phone = input("\u001b[34;1m> ")

        try:
            if len(phone) == 10:
                db.execute(
                    "SELECT * FROM users WHERE phone = %s", (phone,))
                result = db.fetchone()

                if result != None:
                    print("\u001b[31;1mPhone number is already registered !!")

                else:
                    break

            else:
                print("\u001b[31;1mPlease enter a valid phone number !!")

        except:
            print("\u001b[31;1mPlease enter a valid phone number !!")

    print("\u001b[32m\nEnter Your city:")
    city = input("> ")

    while True:
        print("\u001b[32m\nEnter your password:")
        password = input("\u001b[34;1m> ")
        
        if len(password) < 5:
            print(
                "\u001b[31;1mPassword must be greater than 5 characters !!")

        else:

            break
    values = (username, firstName, lastName, gender, age, phone, city, password)

    db.execute("INSERT INTO abc_bank.users( username, first_name, last_name, gender, age, phone, city, password ) VALUES ( %s, %s, %s, %s, %s, %s, %s, SHA1(%s) )", values)
    connection.commit()
    
    input("\u001b[32m\nPress Any Key to Continue ...")