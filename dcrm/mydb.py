 #This python file is what I used to connect mysql to my project
import mysql.connector

dataBase = mysql.connector.connect(
    host = 'localhost',
    user = 'root',
    password = 'Emma_1234',
    
)

#prepare a cursor
cursorObject = dataBase.cursor()

#create database
cursorObject.execute("CREATE DATABASE firadb")

print('All Done!!')