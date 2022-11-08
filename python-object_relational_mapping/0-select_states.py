#!/usr/bin/python3
"""
Script to list elements from a database
"""
import MySQLdb

""" Connect to server"""
db = MySQLdb.connect(host='localhost', user='root', passwd='root', db='hbtn_0e_0_usa')

print(db)