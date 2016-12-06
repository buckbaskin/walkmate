import psycopg2
import uuid
import datetime

# make a connection
try:
    conn = psycopg2.connect(database='postgres', user='postgres', password='economicalchinchillacorndog', host='localhost')
    cur = conn.cursor()
except:
    print('Database Connection Failed')
    raise

def joinTrip(did,uuuid):
    try:
        query = 'INSERT INTO MEMBERS(did, uuuid) Values (%s,%s)';
        data = (did, uuuid)
    except:
        
