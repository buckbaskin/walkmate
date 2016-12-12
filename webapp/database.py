def getALLDestinations(conn, cur):
    cur.execute('SELECT * FROM DESTINATIONS')
    return cur.fetchAll()