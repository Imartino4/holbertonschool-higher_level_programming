#!/usr/bin/python3
"""
Script to list states elements from a database
username, password, database and state name searched must
be given as argv argument in that order
"""
import MySQLdb
from sys import argv

if __name__ == "__main__":
    """ Connect to server"""
    db = MySQLdb.connect(
        host='localhost',
        user=argv[1],
        passwd=argv[2],
        db=argv[3])

    cursor = db.cursor()
    cursor.execute("SELECT * FROM states WHERE name='{}'".format(argv[4]))
    datos = cursor.fetchall()
    for d in datos:
        if d[1] == argv[4]:
            print(d)
