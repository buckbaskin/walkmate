import pyscopg2
import populateDestinations
import populateUsers
import populateTrips
def populateAll(cur):
	populateDestinations.populateDestinations(cur)
	populateUsers.populateUsers(cur)
	populateTrips.populateTrips(cur)
	cur.commit()