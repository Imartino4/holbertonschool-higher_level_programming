#!/usr/bin/python3
"""
Script to list elements from a database
"""
import MySQLdb

""" Connect to server"""
db = MySQLdb.connect(host='localhost', user='root', passwd='root', db='hbtn_0e_0_usa')

def list_states():
    db.cursor().execute('SELECT * FROM states ORDER by states.id ASC')
print(db)