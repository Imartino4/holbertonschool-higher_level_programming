#!/usr/bin/python3
"""
Script to list elements from a database
"""
import MySQLdb
from sys import argv

if __name__ == "__main__":
    """ Connect to server"""
    db = MySQLdb.connect(
        host = 'localhost',
        user = argv[1],
        passwd = argv[2],
        db = argv[3])

    cursor = db.cursor()
    cursor.execute('SELECT * FROM states ORDER by states.id ASC')
    datos = cursor.fetchall()
    for d in datos:
        print(d)
