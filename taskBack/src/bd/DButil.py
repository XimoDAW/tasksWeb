import pymysql

def connect (host1, user1, passwd1, db1):
    return pymysql.connect(host=host1, user=user1, passwd=passwd1, db=db1)

def open (connection):
    return connection.cursor()

def close (connection):
    connection.cursor()
