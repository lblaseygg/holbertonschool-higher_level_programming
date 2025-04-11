#!/usr/bin/python3
"""
This script lists all cities of a given state from the database hbtn_0e_4_usa.
It takes 4 arguments: mysql username, mysql password, database name and state name.
"""

import MySQLdb
import sys

if __name__ == "__main__":
    # Get command line arguments
    username = sys.argv[1]
    password = sys.argv[2]
    db_name = sys.argv[3]
    state_name = sys.argv[4]

    # Connect to MySQL server
    db = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=username,
        passwd=password,
        db=db_name
    )

    # Create cursor
    cursor = db.cursor()

    # Execute query with parameterized query to prevent SQL injection
    cursor.execute("""
        SELECT cities.name
        FROM cities
        JOIN states ON cities.state_id = states.id
        WHERE states.name = %s
        ORDER BY cities.id ASC
    """, (state_name,))

    # Fetch all results
    results = cursor.fetchall()

    # Print results as comma-separated list
    cities = [row[0] for row in results]
    print(", ".join(cities))

    # Close cursor and database connection
    cursor.close()
    db.close() 