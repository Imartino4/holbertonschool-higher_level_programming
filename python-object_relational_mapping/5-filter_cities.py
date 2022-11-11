#!/usr/bin/python3
"""
Script to list all cities from a state from a database
username, password database adn the state must
be given as argv argument in that order
order ascending by cities.id
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
    cursor.execute('SELECT c.name FROM cities c\
                    JOIN states ON c.states_id=states.id\
                    WHERE states.name=%s\
                    ORDER by s.id ASC', [argv[4]])
    datos = cursor.fetchall()
    for d in datos:
        print(d)
