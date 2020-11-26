import mysql.connector
import modules.util as util
from getpass import getpass


try:
    util.clear()
    print("===================================================")
    db_user = input(" Enter your Mysql username: ")
    print("===================================================")
    db_password = getpass(" Enter your Mysql password: ")
    print("===================================================")
    input("\nPress Any Key to Continue ...")
    print("===================================================")

    connection = mysql.connector.connect(
        host='127.0.0.1', user=db_user, password=db_password, database="abc_bank")
    db = connection.cursor()

except:
    print(" Invalid Mysql username and password !!")
    print("===================================================")
