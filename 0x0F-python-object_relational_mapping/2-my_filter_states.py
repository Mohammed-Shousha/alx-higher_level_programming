#!/usr/bin/python3
"""
Lists all states where name matches the argument
"""

from sys import argv
import MySQLdb

if __name__ == '__main__':
    db = MySQLdb.connect(host="localhost", port=3306,
                         user=argv[1], passwd=argv[2], db=argv[3])

    cur = db.cursor()
    cur.execute(f"SELECT * FROM states WHERE name LIKE '{argv[4]}';")
    states = cur.fetchall()

    for state in states:
        print(state)
