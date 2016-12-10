import psycopg2
import datetime
import uuid
def populateTrips(cur):
	query = 'INSERT INTO TRIPS(tripid,start_destination,end_destination,start_time,number_participants) VALUES (%s,%s,%s,%s,%s)'
	tripid = uuid.uuid.uuid4()
	start_time = datetime.datetime.utcnow()
	data = (tripid,start_destination,end_destination,start_time,number_participants)
	try:
		cur.execute(query,data)
	except psycopg2.Error as e:
		if e.pgcode = '23505':
			tripid = uuid.uuid.uuid4()
			data = (tripid,start_destination,end_destination,start_time,number_participants)
			try:
				cur.execute(query,data)
			except psycopg2.Error as e:
				raise e
		else:
			raise e