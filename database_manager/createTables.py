import psycopg2
def createAll(conn, cur):
    print('createAll')
    try:
        cur.execute('''
CREATE TABLE USERS
(caseid varchar NOT NULL PRIMARY KEY,
hashed_raiseword varchar NOT NULL,
first_name varchar NOT NULL,
last_name varchar NOT NULL,
date_joined timestamp NOT NULL);''')
        conn.commit()
        cur.execute('SELECT * FROM USERS')
        print(cur.fetchone())
    except:
        raise
    try:
        cur.execute('''
CREATE TABLE DESTINATIONS
(did uuid NOT NULL PRIMARY KEY,
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
(tripid uuid NOT NULL PRIMARY KEY,
start_destination uuid NOT NULL REFERENCES DESTINATIONS(did),
end_destination uuid NOT NULL REFERENCES DESTINATIONS(did),
start_time timestamp NOT NULL,
number_participants integer NOT NULL);''')
        conn.commit()
    except:
        raise
    try:
        cur.execute('''
CREATE TABLE MEMBERS
(tripid uuid NOT NULL REFERENCES TRIPS(tripid),
uuuid varchar NOT NULL REFERENCES USERS(caseid),
PRIMARY KEY(tripid, uuuid));''')
        conn.commit()
    except:
        raise
    try:
        cur.execute('''
CREATE TABLE RATINGS
(raterid varchar NOT NULL REFERENCES USERS(caseid),
rateeid varchar NOT NULL REFERENCES USERS(caseid),
rating integer NOT NULL,
PRIMARY KEY (raterid, rateeid));''')
        conn.commit()
    except:
        raise
    conn.commit()
if __name__ == '__main__':
    import createConnection
    createAll(*createConnection.createNewConnection())