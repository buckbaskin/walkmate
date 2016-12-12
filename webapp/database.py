import uuid
import psycopg2
def getAllDestinations(conn):
    cur = conn.cursor()
    cur.execute('SELECT * FROM DESTINATIONS')
    return cur.fetchall()
# Git anchor
def createNewTrip(conn, caseid,start_destination,end_destination,start_time):
    cur = conn.cursor()
    tripid = uuid.uuid4().hex
    errorflag = False
    try:
        query1 = "INSERT INTO TRIPS (tripid, start_destination, end_destination, start_time, number_participants) VALUES (%s,%s,%s,%s,%s)"
        data1 = (tripid, start_destination, end_destination, start_time, 1)
        cur.execute(query1,data1)
    except psycopg2.Error as e:
        if e.pgcode == '42P01':
            createTables.createAll()
            cur.execute(query1,data1)
        elif e.pgcode == '23505':
            tripid = uuid.uuid.uuid4().hex
            data1 = (tripid, start_destination, end_destination, start_time, 1)
            try:
                cur.execute(query1,data1)
            except:
                errorflag =True
                raise
        else:
            errorflag = True
            raise
    try:
        query2 = "INSERT INTO MEMBERS (tripid, caseid) VALUES (%s, %s)"
        data2 = (tripid, caseid)
        cur.execute(query2,data2)
    except:    
        print('Database insertion error, most likely not uuid collision')
        errorflag = True
        raise
    if not errorflag:
        conn.commit()
        cur.close()
    return tripid

# Git anchor

def getAllTrips(conn, size):
    cur = conn.cursor()
    cur.execute('''
        SELECT T.tripid, D1.dname, D2.dname, T.start_time
        FROM TRIPS as T, Destinations as D1, Destinations as D2
        WHERE D1.did = T.start_destination AND D2.did = T.end_destination''')
    for tuple_ in cur.fetchmany(size):
        yield (tuple_[0], tuple_[1], tuple_[2], tuple_[3], tuple_[-1].hour, tuple_[-1].minute)

# Git anchor

def getOneTrip(conn, tripid):
    cur = conn.cursor()
    cur.execute('''
        SELECT T.tripid, D1.dname, D2.dname, T.start_time
        FROM TRIPS as T, Destinations as D1, Destinations as D2
        WHERE T.tripid = %s''', (tripid,))
    tuple_ = cur.fetchone()
    if tuple_ is None:
        return []
    print('trippy tuple: %s' % (tuple_,))

    num_participants = 0

    yield (tuple_[0], tuple_[1], tuple_[2], tuple_[3], num_participants, tuple_[3].hour, tuple_[3].minute)

# Git anchor

def getUser(conn, caseid):
    cur = conn.cursor()
    cur.execute('''
        SELECT *
        FROM USERS
        WHERE caseid = %s
        ''', (caseid,))
    return cur.fetchone()

# Git anchor

def getUserTrips(conn, caseid):
    cur = conn.cursor()
    cur.execute('''
        SELECT T.*
        FROM TRIPS as T, MEMBERS as M
        WHERE M.tripid = T.tripid AND M.caseid = %s
        ''', (caseid,))
    return cur.fetchall()

# Git anchor

def checkTripExists(conn, tripid):
    cur = conn.cursor()
    cur.execute('''SELECT * FROM TRIPS WHERE tripid = %s''',
        (tripid,))
    trip_exists = len(cur.fetchmany(1)) > 0
    return trip_exists

# Git anchor

def addToTrip(conn, tripid, caseid):
    cur = conn.cursor()
    #  TODO ... implement
    return True

# Git anchor

def getSpecificTrips(conn, size, start_destination, end_destination, start_time, end_time):
    cur = conn.cursor()
    cur.execute('''
        SELECT T.tripid, D1.dname, D2.dname, T.start_time
        FROM TRIPS as T, Destinations as D1, Destinations as D2
        WHERE D1.did = T.start_destination AND D2.did = T.end_destination AND T.start_destination = %s AND T.end_destination = %s AND T.start_time > %s AND T.start_time < %s''', (start_destination, end_destination, start_time, end_time)
    for tuple_ in cur.fetchmany(size):
        yield (tuple_[0], tuple_[1], tuple_[2], tuple_[3], tuple_[-1].hour, tuple_[-1].minute)

# Git anchor