#!/usr/bin/python3
"""
Script to list all cities from a database
username, password, and database must
be given as argv argument in that order
Display id city state
only one execute()
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
    cursor.execute('SELECY c.id,c.name,s.name FROM states s INNER JOIN cities c ON s.id = c.state_id ORDER by s.id ASC')
    datos = cursor.fetchall()
    for d in datos:
        print(d)
