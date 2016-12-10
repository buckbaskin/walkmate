import pyscopg2
import populateDestinations
import populateUsers
def populateAll(cur):
	populateDestinations.populateDestinations(cur)
	populateUsers.populateUsers(cur)
	cur.commit()