import psycopg2

# make a connection
try:
    conn = psycopg2.connect(database='postgres', user='postgres', password='economicalchinchillacorndog', host='localhost')
    cur = conn.cursor()
except:
    print('Database Connection Failed')
    raise
try:
    cur.execute('''
CREATE TABLE FRIENDSHIPS
(userid1 uuid NOT NULL,
userid2 uuid NOT NULL,
PRIMARY KEY(userid1, userid2),
FORIEGN KEY(userid1) REFERENCES USERS(uuuid),
FORIEGN KEY(userid1) REFERENCES USERS(uuuid));''')
except:
    pass
try:
    cur.execute('''
CREATE TABLE BLOCKS
(userid1 uuid NOT NULL,
userid2 uuid NOT NULL,
PRIMARY KEY(userid1, userid2),
FORIEGN KEY(userid1) REFERENCES USERS(uuuid),
FORIEGN KEY(userid1) REFERENCES USERS(uuuid));''')
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
    try:
    cur.execute('''
CREATE TABLE MEMBERS
(tripid uuid NOT NULL,
uuuid uuid NOT NULL,
PRIMARY KEY(tripid, uuuid),
FORIEGN KEY(tripid) REFERENCES TRIPS(tripid),
FORIEGN KEY(uuuid) REFERENCES USERS(uuuid));''')
except:
    pass
