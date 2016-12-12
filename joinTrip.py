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

def joinTrip(tripid,uuuid):
    query = 'INSERT INTO MEMBERS(tripid, caseid) Values (%s,%s)';
    data = (tripid, uuuid)
    try:
        cur.execute(query,data)
    except pyscopg2.Error as e:
        if e.pgcode == '42P01':
            createTables.createAll()
            cur.execute(query,data)
            conn.commit()
        else:
            raise
    try:
        query2 = '''UPDATE TRIPS SET number_users = number_users + 1 WHERE tripid = %s'''
        data2 = (tripid,)
        cur.execute(query2,data2)
        conn.commit()
    except:
        raise
    conn.close()