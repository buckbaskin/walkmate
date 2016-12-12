import psycopg2
def createAll(conn, cur):
    try:
        cur.execute('''
CREATE TABLE USERS
(caseid varchar NOT NULL PRIMARY KEY,
hashed_password varchar NOT NULL,
first_name varchar NOT NULL,
last_name varchar NOT NULL,
date_joined timestamp NOT NULL);''')
    except:
        raise
    try:
        cur.execute('''
CREATE TABLE DESTINATIONS
(did char(32) NOT NULL PRIMARY KEY,
dname varchar NOT NULL,
area_of_campus varchar);''')
        conn.commit()
    except:
        raise

    try:
        cur.execute('''
CREATE TABLE FRIENDSHIPS
(userid1 varchar NOT NULL REFERENCES USERS(caseid),
userid2 varchar NOT NULL REFERENCES USERS(caseid),
PRIMARY KEY(userid1, userid2));''')
        conn.commit()
    except:
        raise
    try:
        cur.execute('''
CREATE TABLE BLOCKS
(userid1 varchar NOT NULL REFERENCES USERS(caseid),
userid2 varchar NOT NULL REFERENCES USERS(caseid),
PRIMARY KEY(userid1, userid2));''')
        conn.commit()
    except:
        raise
    try:
        cur.execute('''
CREATE TABLE TRIPS
(tripid char(32) NOT NULL PRIMARY KEY,
start_destination char(32) NOT NULL REFERENCES DESTINATIONS(did),
end_destination char(32) NOT NULL REFERENCES DESTINATIONS(did),
start_time timestamp NOT NULL,
number_participants integer NOT NULL);''')
        conn.commit()
    except:
        raise
    try:
        cur.execute('''
CREATE TABLE MEMBERS
(tripid char(32) NOT NULL REFERENCES TRIPS(tripid),
caseid varchar NOT NULL REFERENCES USERS(caseid),
PRIMARY KEY(tripid, caseid));''')
        conn.commit()
    except:
        raise
    try:
        cur.execute('''
CREATE TABLE USERRATINGS
(raterid varchar NOT NULL REFERENCES USERS(caseid),
rateeid varchar NOT NULL REFERENCES USERS(caseid),
rating integer NOT NULL,
PRIMARY KEY (raterid, rateeid));''')
        conn.commit()
    except:
        raise
    conn.commit()
    try:
        cur.execute('''
CREATE TABLE TRIPRATINGS
(raterid varchar NOT NULL REFERENCES USERS(caseid),
tripid char(32) NOT NULL REFERENCES TRIPS(tripid),
PRIMARY KEY (raterid, tripid));''')
        conn.commit()
    except:
        raise
    conn.commit()
if __name__ == '__main__':
    import createConnection
    createAll(*createConnection.createNewConnection())