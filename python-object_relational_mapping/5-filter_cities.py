#!/usr/bin/python3

"""
All cities by state
"""
import MySQLdb
import sys

if __name__ == "__main":
    if len(sys.argv) != 5:
        print("Usage: {} username password database state_name".format(sys.argv[0]))
        sys.exit(1)

    username, password, database, state_name = sys.argv[1], sys.argv[2], sys.argv[3], sys.argv[4]

    try:
        conn = MySQLdb.connect(
            host="localhost",
            port=3306,
            user=username,
            passwd=password,
            db=database
        )

        cursor = conn.cursor()

        query = """
        SELECT GROUP_CONCAT(cities.name ORDER BY cities.id ASC SEPARATOR ', ')
        FROM cities
        JOIN states ON cities.state_id = states.id
        WHERE states.name = %s;
        """

        cursor.execute(query, (state_name,))

        result = cursor.fetchone()[0]

        if result:
            print(result)
        else:
            print("State not found or has no cities.")

        cursor.close()
        conn.close()

    except MySQLdb.Error as e:
        print("MySQL Error: {}".format(e))
        sys.exit(1)

