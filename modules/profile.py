from modules.util import clear
from getpass import getpass
from modules.database import db, connection


def profile(userId):
    while True:
        clear()
        db.execute(
                "select * from users where id = %s ", (userId,))
        user = db.fetchone()
        print("\u001b[33;1m+----------------------------------------------------+")
        print(f"|\u001b[32m  1. Change your Username | { user[1] } ")
        print("\u001b[33;1m+--------------------------+--------------------------+")
        print(f"|\u001b[32m  2. Change your Gender   | { user[4] } ")
        print("\u001b[33;1m+--------------------------+--------------------------+")
        print(f"|\u001b[32m  3. Change your Age      | { user[5] } ")
        print("\u001b[33;1m+--------------------------+--------------------------+")
        print(f"|\u001b[32m  4. Change your City     | { user[7] } ")
        print("\u001b[33;1m+--------------------------+--------------------------+")
        print(f"|\u001b[32m  5. Change Your Phone No | { user[6] } ")
        print("\u001b[33;1m+----------------------------------------------------+")
        print(f"|\u001b[32m  6. Change your Password <0>")
        print("\u001b[33;1m+----------------------------------------------------+")
        print(f"|\u001b[32m  7. Back")
        print("\u001b[33;1m+----------------------------------------------------+")
        print("\u001b[31;1mEnter your choice: ")
        answer = int(input("\u001b[34;1m> "))
        try:
            if answer == 1 :
                print("Enter your username")
                input_user = input("> ")
                db.execute("SELECT * FROM users WHERE username = %s", (input_user,))
                result = db.fetchone()

                if result != None:
                    print("\u001b[31;1mUsername is already registered !!")
                    input("\nPress Any Key to Continue ...\u001b[34;1m")

                else:
                    db.execute("UPDATE users SET username = %s where username = %s ",(input_user,f"{user[1]}"))

            elif answer == 2 :
                print("Enter your Gender (M/F)")
                input_user = input("> ")
                input_user = input_user.upper()
                if input_user == "M" or "F" :
                    db.execute("UPDATE users SET gender = %s where username = %s ",(input_user,f"{user[1]}"))
                    connection.commit()
                
                else:
                    print("\u001b[31;1mPlease enter a valid Gender !!")
                    input("\nPress Any Key to Continue ...\u001b[34;1m")
                    
            elif answer == 3 :
                print("Enter your Age ")
                input_user = int(input("> "))
                if input_user < 13:
                    print("\u001b[31;1mAge should be atleast 13 Years !!")
                    input("\nPress Any Key to Continue ...\u001b[34;1m")

                elif input_user > 139:
                    print("\u001b[31;1mAge must be less then 140 Years !!")
                    input("\nPress Any Key to Continue ...\u001b[34;1m")

                else:
                    db.execute("UPDATE users SET age = %s where username = %s ",(input_user,f"{user[1]}"))
                    connection.commit()
                    
            
            elif answer == 4 :
                print("Enter your City")
                input_user = input("> ")
                db.execute("UPDATE users SET city = %s where username = %s ",(input_user,f"{user[1]}"))
                connection.commit()

            elif answer == 5 :
                print("Enter your Phone No ")
                input_user = int(input("> "))
                try:
                    if len(input_user) == 10:
                        db.execute(
                            "SELECT * FROM users WHERE phone = %s", (input_user,))
                        result = db.fetchone()
                        connection.commit()

                        if result != None:
                            print("\u001b[31;1mPhone number is already registered !!")
                            input("\nPress Any Key to Continue ...\u001b[34;1m")

                        else:
                            db.execute("UPDATE users SET phone = %s where username = %s ",(input_user,f"{user[1]}"))
                            connection.commit()

                    else:
                        print("\u001b[31;1mPlease enter a valid phone number !!")
                        input("\nPress Any Key to Continue ...\u001b[34;1m")

                except:
                    print("\u001b[31;1mPlease enter a valid phone number !!")
                    input("\nPress Any Key to Continue ...\u001b[34;1m")

            elif answer == 6 :
                print("Enter Your Current Password: ")
                password = getpass("> ")

                db.execute(
                    "select * from users where username = %s and password = SHA1(%s)", ({user[1]}, password))
                result = db.fetchone()
                

                if result != None:
                    while True:
                        print("Enter Your Password: ")
                        passwordOne = getpass("> ")
                        print("Enter Retype Your Password: ")
                        passwordSec = getpass("> ")
                        if passwordOne == passwordSec and len(passwordOne) < 5 :
                            print("\u001b[32mPassword changed .\u001b[34;1m")
                            db.execute("select * from users where username = %s and password = SHA1(%s)", ({user[1]}, passwordOne))
                            connection.commit()
                
                            pass
                        else:
                            print("\u001b[31;1mPassword dosen`t match !!")
                            print("Try again !!")
                            input("\nPress Any Key to Continue ...\u001b[34;1m")
                else:
                    print("\u001b[31;1mPassword dosen`t match !!")
                    print("Try again !!")
                    input("\nPress Any Key to Continue ...\u001b[34;1m")
            
            elif answer == 7 :
                break     
            
            else:
                print("\u001b[31;1mInvalid choice selected !!")
                input("\nPress Any Key to Continue ...\u001b[34;1m")

        except:
            print("\u001b[31;1mInvalid choice selected !!")
            input("\nPress Any Key to Continue ...\u001b[34;1m")