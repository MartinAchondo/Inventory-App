import os
import json
import mysql.connector

def read_sql():
    L_paths = ['tables.sql','triggers.sql']
    convert = lambda x: os.path.join(os.getcwd(),'database_mysql','sql',x)
    L_paths = map(convert,L_paths)
    for path_sql in L_paths:
        with open(path_sql,'r') as fd:
            sqlFile = fd.read()
        sqlcommands = sqlFile.split('----')
        for command in sqlcommands:
            query(command)


def query(command):
    filename = os.path.join(os.getcwd(),'database_mysql','user.json')
    with open(filename,"r") as file_json:
        data = json.load(file_json)
        key = data["connection"]
    con = mysql.connector.connect(
    host=key['host'],
    user=key['user'],
    password=key['password'],
    database=key['database']
    )
    cur = con.cursor()
    cur.execute(command)
    con.commit()
    con.close()

def create_base():
    path_sql = os.path.join(os.getcwd(),'database_mysql','sql','create_base.sql')
    with open(path_sql,'r') as fd:
        sqlFile = fd.read()
    sqlcommands = sqlFile.split(';')
    for command in sqlcommands:
        filename = os.path.join(os.getcwd(),'database_mysql','user.json')
        with open(filename,"r") as file_json:
            data = json.load(file_json)
            key = data["connection"]
        con = mysql.connector.connect(
        host=key['host'],
        user=key['user'],
        password=key['password'],
        )
        cur = con.cursor()
        cur.execute(command)
        con.commit()
        con.close()


if __name__=='__main__':
    new = True
    if new:
        create_base()
    read_sql() 