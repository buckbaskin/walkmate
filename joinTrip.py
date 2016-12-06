import psycopg2
import uuid
import datetime
import createTables

# make a connection
try:
    conn = psycopg2.connect(database='postgres', user='postgres', password='economicalchinchillacorndog', host='localhost')
    cur = conn.cursor()
except:
    print('Database Connection Failed')
    raise

def joinTrip(did,uuuid):
    query = 'INSERT INTO MEMBERS(did, uuuid) Values (%s,%s)';
    data = (did, uuuid)
    errorflag = False
    try:
        cur.execute(query,data)
    except pyscopg2.Error as e:
        if e.pgcode == '42P01':
            createTables.createAll()
            cur.execute(query,data)
        else:
            raise
            errorflag = True
    try:
        query = '''UPDATE TRIPS 
