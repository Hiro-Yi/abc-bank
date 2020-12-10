import mysql.connector
import modules.util as util
from getpass import getpass


try:
    util.clear()
    connection = mysql.connector.connect(host='127.0.0.1', user="root", password="root", database="abc_bank", auth_plugin="mysql_native_password")
    db = connection.cursor()

except:
    print("===================================================")
    print(" Invalid Mysql username and password !!")
    print("===================================================")
