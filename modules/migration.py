import mysql.connector
from bullet import Password


print("===================================================")
db_user = input(" Enter your Mysql username: ")
print("===================================================")

db_password = Password(prompt="Enter your Mysql password: ", hidden="*")
db_password = db_password.launch()

print("===================================================")
input("\nPress Any Key to Continue ...")
print("===================================================")


try:
    conn = mysql.connector.connect(
        host='127.0.0.1', user=db_user, password=db_password)
    myCursor = conn.cursor()
    myCursor.execute("drop database if exists abc_bank")
    myCursor.execute("create database abc_bank")
    myCursor.execute("use abc_bank")
    myCursor.execute("create table users(id int(11) NOT NULL Primary Key auto_increment, username varchar(64) NOT NULL UNIQUE, first_name varchar(64) NOT NULL,last_name varchar(64) NOT NULL,gender enum('M','F') NOT NULL,age int(3) NOT NULL,phone varchar(10) NOT NULL Unique Key,city varchar(255) NOT NULL,password varchar(100) NOT NULL)")
    myCursor.execute("create table transactions(id int(11) NOT NULL Primary Key auto_increment, user_id int(11) NOT NULL, type enum('WITHDRAW','DEPOSIT') NOT NULL, amount double(16,2) NOT NULL, FOREIGN KEY (user_id) REFERENCES users(id))")

except:
    print("Invalid Mysql username/password !!")
