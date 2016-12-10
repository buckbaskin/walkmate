import psycopg2
def createAll(cur):
	try:
    	cur.execute('''
CREATE TABLE FRIENDSHIPS
(userid1 uuid NOT NULL,
userid2 uuid NOT NULL,
PRIMARY KEY(userid1, userid2),
FORIEGN KEY(userid1) REFERENCES USERS(caseid),
FORIEGN KEY(userid1) REFERENCES USERS(caseid));''')
	except:
    	pass
	try:
    	cur.execute('''
CREATE TABLE BLOCKS
(userid1 uuid NOT NULL,
userid2 uuid NOT NULL,
PRIMARY KEY(userid1, userid2),
FORIEGN KEY(userid1) REFERENCES USERS(caseid),
FORIEGN KEY(userid1) REFERENCES USERS(caseid));''')
	except:
    	pass
	try:
    	cur.execute('''
CREATE TABLE TRIPS
(tripid uuid NOT NULL PRIMARY KEY,
start_destination varchar NOT NULL,
end_destination varchar NOT NULL,
start_time timestamp NOT NULL,
number_participants integer NOT NULL,
FORIEGN KEY(start_destination) REFERENCES DESTINATIONS(did),
FORIEGN KEY(end_destination) REFERENCES DESTINATIONS(did));''')
	except:
    	pass
	try:
    	cur.execute('''
CREATE TABLE MEMBERS
(tripid uuid NOT NULL,
uuuid uuid NOT NULL,
PRIMARY KEY(tripid, uuuid),
FORIEGN KEY(tripid) REFERENCES TRIPS(tripid),
FORIEGN KEY(uuuid) REFERENCES USERS(caseid));''')
	except:
    	pass
	try:
    	cur.execute('''
CREATE TABLE DESTINATIONS
(did uuid NOT NULL PRIMARY KEY,
dname varchar NOT NULL,
area_of_campus varchar);''')
	except:
    	pass
	try:
    	cur.execute('''
CREATE TABLE RATINGS
(raterid uuid NOT NULL,
rateeid uuid NOT NULL,
rating integer NOT NULL
PRIMARY KEY(raterid, rateeid),
FORIEGN KEY(raterid) REFERENCES USERS(caseid),
FORIEGN KEY(rateeid) REFERENCES USERS(caseid));''')
	except:
    	pass
    cur.commit()