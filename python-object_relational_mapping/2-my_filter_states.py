#!/usr/bin/python3

import MySQLdb
import sys

if __name__ == "__main__":
    if len(sys.argv) != 5:
        print(f"Usage: {sys.argv[0]} <username> <password> <database_name>")
        sys.exit(1)

    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]
    ns = sys.argv[4]

    try:
        db = MySQLdb.connect(
                user=username,
                port=3306,
                host="localhost",
                passwd=password,
                db=database
                )
        cursor = db.cursor()
    except MySQLdb.Error as e:
        print("Error connecting to the database:", e)
        sys.exit(1)

    query = "SELECT * FROM states WHERE name = '{}' ORDER BY id ASC".format(ns)

    try:
        cursor.execute(query)
        states = cursor.fetchall()
    except MySQLdb.Error as e:
        print("Error executing query", e)
        db.close()
        sys.exit(1)

    for state in states:
        print(state)

    db.close()
