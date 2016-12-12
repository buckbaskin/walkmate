import psycopg2
import populateDestinations
import populateUsers
import populateTrips
def populateAll(conn, cur):
    populateDestinations.populateDestinations(conn, cur)
    populateUsers.populateUsers(conn, cur)
    populateTrips.populateTrips(conn, cur)
    conn.commit()