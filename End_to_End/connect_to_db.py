import mysql.connector
import base64
import sqlite3
import pandas as pd


def getConfig():
    with open(r"C:\Tamil\temp_data\db_chatbot\connect_to_db\db_creds.txt") as f:
        connectionString = f.read()
    base64_message = connectionString
    base64_bytes = base64_message.encode('ascii')
    message_bytes = base64.b64decode(base64_bytes)
    connectionString = message_bytes.decode('ascii')
    userid = connectionString.split('username = ')[1].split("\npassword")[0]
    password = connectionString.split('password = ')[1].split(" hide\nhost")[0]
    server = connectionString.split('hide\nhost = ')[1].split("\nport = ")[0]
    port = connectionString.split('\nport = ')[1].split("\ndatabase = ")[0]
    database = connectionString.split('\ndatabase = ')[1].split("\nsslmode")[0]
    ssl_ca = connectionString.split('\nssl_ca = ')[1]
    return {
        "server": server,
        "user": userid,
        "password": password,
        "database": database,
        "port": port,
        "ssl_ca": ssl_ca
    }


def connectToDigitalOcean():
    connectionDict = getConfig()
    mydb = mysql.connector.connect(
        host=connectionDict['server'],
        user=connectionDict['user'],
        password=connectionDict['password'],
        port=connectionDict['port'],
        database=connectionDict['database'],
        ssl_ca=connectionDict['ssl_ca']
    )

    return mydb


def connectToSqliteDB():
    return sqlite3.connect(r"C:\Tamil\temp\db_chatbot\django_connecter\pythonsqlite.db")


# dataFrame = pd.read_sql("SELECT Time_Stamp FROM  polls_events", con=connectToSqliteDB())
