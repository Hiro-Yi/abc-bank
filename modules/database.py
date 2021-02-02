import mysql.connector
import modules.util as util
from getpass import getpass

print("===================================================")
db_user = input(" Enter your Mysql username: ")
print("===================================================")

db_password = getpass("Enter your Mysql password: ")
print("===================================================")
input("\nPress Any Key to Continue ...")
print("===================================================")

try:
    util.clear()
    connection = mysql.connector.connect(host='127.0.0.1', user=db_user, password=db_password, database="abc_bank", auth_plugin="mysql_native_password")
    db = connection.cursor()

except:
    print("===================================================")
    print(" Invalid Mysql username and password !!")
    print("===================================================")
