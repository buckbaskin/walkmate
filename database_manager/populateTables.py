import pyscopg2
import populateDestinations
def populateAll(cur):
	populateDestinations.populateDestinations(cur)