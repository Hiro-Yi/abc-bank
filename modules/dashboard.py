from os import name
from modules.profile import profile
import modules.util as util
from modules.database import db, connection


def displayMenu(userId):
    while True:
        util.clear()
        db.execute(
                "select * from users where id = %s ", (userId,))
        user = db.fetchone()
        print(
            "\u001b[33;1m+----------------------------------------------------+")
        print(
            f"\u001b[34;1m                 Welcome { user[1] }               \u001b[33;1m ")
        print("+----------------------------------------------------+")
        print(
            "|\u001b[32m 1.Check Balance                                   \u001b[33;1m |")
        print("+----------------------------------------------------+")
        print(
            "|\u001b[32m 2.Deposit                                          \u001b[33;1m|")
        print("+----------------------------------------------------+")
        print(
            "|\u001b[32m 3.Withdraw                                         \u001b[33;1m|")
        print("+----------------------------------------------------+")
        print(
            "|\u001b[32m 4.Logout                                           \u001b[33;1m|")
        print("+----------------------------------------------------+")
        print(
            "|\u001b[32m 5.Profile                                         \u001b[33;1m |")
        print("+----------------------------------------------------+")
        print(
            "|\u001b[32m 6.Exit                                             \u001b[33;1m|")
        print("+----------------------------------------------------+")
        print("\u001b[31;1m\nEnter your choice: \u001b[36m")

        try:
            choice = int(input("> "))
            
            if choice == 1:
                checkBalance(user[0])

            elif choice == 2:
                deposit(user[0])

            elif choice == 3:
                withdraw(user[0])

            elif choice == 4:
                break
            
            elif choice == 5:
                profile(user)

            elif choice == 6:
                util.clear()
                exit()

            else:
                print("Invalid choice selected !!")
                input("\nPress Any Key to Continue ...")

        except ValueError:
            print("Invalid choice selected !!")
            input("\nPress Any Key to Continue ...")


def getBalance(uid):
    db.execute("SELECT * FROM transactions WHERE user_id = %s", (uid,))
    result = db.fetchall()

    balance = 0
    for i in result:
        if i[2] == "DEPOSIT":
            balance += i[3]

        else:
            balance -= i[3]

    return balance


def deposit(uid):
    try:
        print("\nEnter Amount for Deposit:")
        amount = float(input("> "))

        db.execute("INSERT INTO transactions (user_id, type, amount) VALUES (%s, %s, %s)",
                   (uid, "DEPOSIT", amount))
        connection.commit()
        checkBalance(uid)

    except:
        print("Enter amount only !!")
        input("\nPress Any Key to Continue ...")


def withdraw(uid):
    try:
        print("\nEnter Amount for Withdraw:")
        amount = float(input("> "))
        
        if amount > getBalance(uid):
            print("Insufficiant balance !!")
            

    except:
        print("Enter amount only !!")
        input("\nPress Any Key to Continue ...")

    else:
        db.execute("INSERT INTO transactions (user_id, type, amount) VALUES (%s, %s, %s)",
                   (uid, "WITHDRAW", amount))
        connection.commit()
    checkBalance(uid)


def checkBalance(uid):
    print("Balance: ", getBalance(uid))
    input("\nPress Any Key to Continue ...")
