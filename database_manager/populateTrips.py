import psycopg2
import datetime
import uuid
def populateTrips(conn, cur):
	query = 'INSERT INTO TRIPS(tripid,start_destination,end_destination,start_time,number_participants) VALUES (%s,%s,%s,%s,%s)'
	tripid = uuid.uuid4().hex
	start_time = datetime.datetime.utcnow()
	start_destination_name = ('Fribley',)
	end_destination_name = ('Nord',)
	number_participants = 3
	start_destination_query = '''SELECT d.did
	FROM DESTINATIONS AS d
	WHERE d.dname = %s''' 
	end_destination_query = '''SELECT d.did
	FROM DESTINATIONS AS d
	WHERE d.dname = %s'''
	cur.execute(start_destination_query,start_destination_name)
	start_destination = cur.fetchone()
	cur.execute(end_destination_query,end_destination_name)
	end_destination = cur.fetchone()
	data = (tripid,start_destination,end_destination,start_time,number_participants)
	try:
		cur.execute(query,data)
		conn.commit()
	except psycopg2.Error as e:
		if e.pgcode == '23505':
			tripid = uuid.uuid4().hex
			data = (tripid,start_destination,end_destination,start_time,number_participants)
			try:
				cur.execute(query,data)
				conn.commit()
			except psycopg2.Error as e:
				raise e
		else:
			raise e
	member_query = 'INSERT INTO MEMBERS(tripid,caseid) VALUES (%s, %s)'
	try:
		member_data = (tripid,'wcb38')
		cur.execute(member_query,member_data)
		conn.commit()
		member_data = (tripid,'pjt37')
		cur.execute(member_query,member_data)
		conn.commit()
		member_data = (tripid,'raw141')
		cur.execute(member_query,member_data)
		conn.commit()
	except Exception as e:
		raise e
	query = 'INSERT INTO TRIPS(tripid,start_destination,end_destination,start_time,number_participants) VALUES (%s,%s,%s,%s,%s)'
	tripid = uuid.uuid4().hex
	start_time = datetime.datetime.utcnow()+ datetime.timedelta(hours = 10)
	start_destination_name = ('Ugly Statue',)
	end_destination_name = ('Glasier',)
	number_participants = 2
	start_destination_query = '''SELECT d.did
	FROM DESTINATIONS AS d
	WHERE d.dname = %s'''
	end_destination_query = '''SELECT d.did
	FROM DESTINATIONS AS d
	WHERE d.dname = %s'''
	cur.execute(start_destination_query,start_destination_name)
	start_destination = cur.fetchone()
	cur.execute(end_destination_query,end_destination_name)
	end_destination = cur.fetchone()
	data = (tripid,start_destination,end_destination,start_time,number_participants)
	try:
		cur.execute(query,data)
		conn.commit()
	except psycopg2.Error as e:
		if e.pgcode == '23505':
			tripid = uuid.uuid4().hex
			data = (tripid,start_destination,end_destination,start_time,number_participants)
			try:
				cur.execute(query,data)
				conn.commit()
			except psycopg2.Error as e:
				raise e
		else:
			raise e
	member_query = 'INSERT INTO MEMBERS(tripid,caseid) VALUES (%s, %s)'
	try:
		member_data = (tripid,'peb30')
		cur.execute(member_query,member_data)
		conn.commit()
		member_data = (tripid,'prn15')
		cur.execute(member_query,member_data)
		conn.commit()
	except Exception as e:
		raise e
	query = 'INSERT INTO TRIPS(tripid,start_destination,end_destination,start_time,number_participants) VALUES (%s,%s,%s,%s,%s)'
	tripid = uuid.uuid4().hex
	start_time = datetime.datetime.utcnow()- datetime.timedelta(hours = 10)
	start_destination_name = ('Veale',)
	end_destination_name = ('Village Starbucks',)
	number_participants = 1
	start_destination_query = '''SELECT d.did
	FROM DESTINATIONS AS d
	WHERE d.dname = %s'''
	end_destination_query = '''SELECT d.did
	FROM DESTINATIONS AS d
	WHERE d.dname = %s'''
	cur.execute(start_destination_query,start_destination_name)
	start_destination = cur.fetchone()
	cur.execute(end_destination_query,end_destination_name)
	end_destination = cur.fetchone()
	data = (tripid,start_destination,end_destination,start_time,number_participants)
	try:
		cur.execute(query,data)
		conn.commit()
	except psycopg2.Error as e:
		if e.pgcode == '23505':
			tripid = uuid.uuid4().hex
			data = (tripid,start_destination,end_destination,start_time,number_participants)
			try:
				cur.execute(query,data)
				conn.commit()
			except psycopg2.Error as e:
				raise e
		else:
			raise e
	member_query = 'INSERT INTO MEMBERS(tripid,caseid) VALUES (%s, %s)'
	try:
		member_data = (tripid,'raw141')
		cur.execute(member_query,member_data)
		conn.commit()
		member_data = (tripid,'jns83')
		cur.execute(member_query,member_data)
		conn.commit()
	except Exception as e:
		raise e