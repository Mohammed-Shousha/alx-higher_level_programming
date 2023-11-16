#!/usr/bin/python3
"""
Lists all states with a name starting with N
"""

from sys import argv
import MySQLdb

if __name__ == '__main__':
    db = MySQLdb.connect(host="localhost", port=3306,
                         user=argv[1], passwd=argv[2], db=argv[3])

    cur = db.cursor()
    cur.execute("SELECT * FROM states WHERE name LIKE 'N%';")
    states = cur.fetchall()

    for state in states:
        print(state)
