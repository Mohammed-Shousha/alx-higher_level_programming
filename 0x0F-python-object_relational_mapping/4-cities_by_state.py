#!/usr/bin/python3
"""
Lists all cities
"""

from sys import argv
import MySQLdb

if __name__ == '__main__':
    db = MySQLdb.connect(host="localhost", port=3306,
                         user=argv[1], passwd=argv[2], db=argv[3])

    cur = db.cursor()
    cur.execute(f"SELECT cities.id, cities.name, states.name FROM cities JOIN states ON cities.state_id = states.id;")
    cities = cur.fetchall()

    for city in cities:
        print(city)
