def getAllDestinations(conn):
    cur = conn.cursor()
    cur.execute('SELECT * FROM DESTINATIONS')
    return cur.fetchall()

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