import os
import sqlite3
from pathlib import Path
from sqlite3 import Error


def create_connection():
    #root = os.path.dirname(os.path.realpath(__file__))
    root = os.getcwd()
    database = os.path.join(root, 'base', 'base.db')
    mydb = Path(root + '/base.db')
    dbconn = None
    try:
        dbconn = sqlite3.connect(database)
    except Error as e:
        print(e)
    if mydb.exists():
        return dbconn
    else:
        return dbconn 

def create_connection2():
    #root = os.path.dirname(os.path.realpath(__file__))
    root = os.getcwd()
    database = os.path.join(root, 'base', 'base_compare.db')
    mydb = Path(root + '/base_compare.db')
    dbconn = None
    try:
        dbconn = sqlite3.connect(database)
    except Error as e:
        print(e)
    if mydb.exists():
        return dbconn
    else:
        return dbconn 


def create_table(create_connection, command):
    connection = create_connection()
    try:
        conn = connection.cursor()
        conn.execute(command)
    except Error as e:
        print(e)

def read_sql():
    root = os.path.dirname(os.path.realpath(__file__))
    path_sql = os.path.join(root, 'tables_create.sql')
    fd = open(path_sql,'r')
    sqlFile = fd.read()
    fd.close()
    sqlcommands = sqlFile.split(';')
    for command in sqlcommands:
        create_table(create_connection,command)

def start():
    read_sql()