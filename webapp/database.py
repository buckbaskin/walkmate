import uuid
import psycopg2
import datetime

def commit_me(func):
    def replacement(conn, *args, **kwargs):
        result = func(conn, *args, **kwargs)
        conn.commit()
        return result
    replacement.__name__ = func.__name__
    return replacement

def getAllDestinations(conn):
    cur = conn.cursor()
    cur.execute('SELECT * FROM DESTINATIONS')
    return cur.fetchall()

# Git anchor
@commit_me
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
    print('getUserTrips(%s)' % (caseid,))
    cur = conn.cursor()
    cur.execute('''
        SELECT T.tripid, D1.dname, D2.dname
        FROM USERS as U, TRIPS as T, MEMBERS as M, DESTINATIONS as D1, DESTINATIONS as D2
        WHERE U.caseid = %s AND M.tripid = T.tripid AND U.caseid = M.caseid AND T.start_destination = D1.did AND T.end_destination = D2.did
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

@commit_me
def addToTrip(conn, tripid, caseid):
    print('addToTrip(%s, %s)' % (tripid, caseid,))
    cur = conn.cursor()
    try:
        cur.execute('''INSERT INTO MEMBERS(tripid, caseid) VALUES(%s, %s)''', (tripid, caseid,))
    except psycopg2.IntegrityError:
        return False
    return True

# Git anchor

def getSpecificTrips(conn, size, start_destination, end_destination, start_time, end_time):
    cur = conn.cursor()
    cur.execute('''
        SELECT T.tripid, D1.dname, D2.dname, T.start_time
        FROM TRIPS as T, Destinations as D1, Destinations as D2
        WHERE D1.did = T.start_destination AND D2.did = T.end_destination AND T.start_destination = %s AND T.end_destination = %s AND T.start_time > %s AND T.start_time < %s''', (start_destination, end_destination, start_time, end_time))
    
    
    for tuple_ in cur.fetchmany(size):
        yield (tuple_[0], tuple_[1], tuple_[2], tuple_[3], tuple_[-1].hour, tuple_[-1].minute)


# Git Anchor

def getUserByTrip(conn, tripid):
    cur = conn.cursor()
    cur.execute('''
        SELECT U.*
        FROM USERS as U, TRIPS as T, MEMBERS as M
        WHERE T.tripid = %s AND M.tripid = T.tripid AND U.caseid = M.caseid
        ''', (tripid,))

    return cur.fetchall()
# Git anchor

def getTripMembers(conn, tripid):
    cur = conn.cursor()
    cur.execute('''SELECT COUNT(*) FROM MEMBERS WHERE tripid = %s'''(tripid,))
    return cur.fetchall()

# Git anchor

def getTripInfo(conn, tripid):
    cur = conn.cursor()
    cur.execute('''SELECT * FROM TRIPS WHERE tripid = %s'''(tripid,))
    return trip_info

# Git Anchor
def getSpecificFriendsTrips(conn, size, start_destination, end_destination, start_time, end_time, caseid):
    cur = conn.cursor()
    cur.execute('''
        SELECT T.tripid, D1.dname, D2.dname, T.start_time
        FROM TRIPS as T, Destinations as D1, Destinations as D2
        WHERE D1.did = T.start_destination AND D2.did = T.end_destination AND T.start_destination = %s AND T.end_destination = %s AND T.start_time > %s AND T.start_time < %s AND EXISTS(SELECT M.caseid FROM MEMBERS AS M, FRIENDSHIPS AS F WHERE M.caseid = F.userid1 AND M.tripid = T.tripid AND F.userid2 = %s)''', (start_destination, end_destination, start_time, end_time, caseid,))
    
    
    for tuple_ in cur.fetchmany(size):
        yield (tuple_[0], tuple_[1], tuple_[2], tuple_[3], tuple_[-1].hour, tuple_[-1].minute)


# Git Anchor

@commit_me
def blockUser(conn, user1, user2):
    # make this mutual
    cur = conn.cursor()
    cur.execute('''INSERT INTO BLOCKS(userid1, userid2) VALUES(%s, %s)''', (user1, user2))
    conn.commit()
    cur.execute('''INSERT INTO BLOCKS(userid1, userid2) VALUES(%s, %s)''', (user2, user1))
    conn.commit()
    return True

# Git Anchor

def checkBlocked(conn, user1, blocked_by):
    cur = conn.cursor()
    result = cur.execute('''
        SELECT COUNT(*)
        FROM BLOCKS 
        WHERE userid1=%s AND userid2=%s''', (user1, blocked_by,))
    return result is not None

# Git Anchor

@commit_me
def makeFriends(conn, user1, user2):
    cur = conn.cursor()
    if not checkBlocked(conn, user1, user2):
        try:
            cur.execute('''
                INSERT INTO FRIENDSHIPS(userid1, userid2)
                VALUES(%s, %s)''', (user1, user2))
            conn.commit()
        except psycopg2.IntegrityError:
            pass

        # print('friends of %s\n%s' % (user1, list(listFriends(conn, user1)),))

        return True
    return False

# Git Anchor

def listFriends(conn, caseid):
    cur = conn.cursor()
    cur.execute(
        '''
        SELECT U.caseid, U.first_name, U.last_name
        FROM FRIENDSHIPS as F, USERS as U
        WHERE F.userid1 = %s AND U.caseid = F.userid2 AND
            NOT EXISTS (
                SELECT *
                FROM BLOCKS as B
                WHERE B.userid1 = F.userid2 AND B.userid2 = F.userid1
            )
        ''', (caseid,))
    return cur.fetchmany(10)

# Git Anchor

def countLikes(conn, caseid):
    cur = conn.cursor()
    result = cur.execute(
        '''
        SELECT COUNT(*)
        FROM USERRATINGS
        WHERE rateeid = %s
        ''', (caseid,))
    if result is None:
        return 0
    else:
        return result[0]

def rateTrip(conn, tripid,caseid):
    cur = conn.cursor()
    try:
        cur.execute('INSERT INTO TRIPRATINGS(tripid,caseid) VALUES (%s, %s)',(tripid,caseid,))
    except psycopg2.IntegrityError as e:
        pass
    tripMembers = getTripMembers(conn,tripid)
    for tuple_ in tripMemebers:
        rateUsers(conn,caseid,tuple_[0])
    return True
def rateUsers(conn,userid1,userid2):
    cur.execute(
        '''
        SELECT *
        FROM USERRATINGS AS U
        WHERE U.raterid = %s AND U.rateeid = %s''',(userid1,userid2,))
    result = cur.fetchone()
    if result is None:
        cur.execute('INSERT INTO USERRATINGS(raterid,rateeid,rating) VALUES (%s, %s)',(userid1,userid2,1,))
        conn.commit()
    else:
        cur.execute('UPDATE USERRATINGS AS U SET rating = rating +1 WHERE U.raterid = %s AND U.rateeid = %s', (userid1,userid2,))
        conn.commit()

def verifyCaseid(conn,caseid):
    cur = conn.cursor()
    cur.execute(
        '''
        SELECT *
        FROM USERS as U
        WHERE U.caseid = %s
        ''',(caseid,))
    userexists = cur.fetchone()
    if userexists is not None:
        return True
    else:
        return False

def addUser(caseid,hashed_password,first_name,last_name):
    query = 'INSERT INTO USERS (caseid, hashed_password, first_name, last_name, date_joined) VALUES (%s, %s, %s, %s, %s)'
    date_joined = datetime.datetime.utcnow()
    data = (caseid, hashed_password, first_name, last_name, date_joined)
    try:
        cur.execute(query,data)
        conn.commit()
        return True
    except psycopg2.IntegrityError as e:
        return False
