import mysql.connector
import util as util
from bullet import Password


try:
    util.clear()
    print("===================================================")
    db_user = input(" Enter your Mysql username: ")
    print("===================================================")
    db_password = Password(prompt=" Enter your Mysql password: ", hidden="*")
    db_password = db_password.launch()
    print("===================================================")
    input("\nPress Any Key to Continue ...")
    print("===================================================")

    connection = mysql.connector.connect(
        host='127.0.0.1', user=db_user, password=db_password, database="abc_bank")
    db = connection.cursor()

except:
    print(" Invalid Mysql username and password !!")
    print("===================================================")
