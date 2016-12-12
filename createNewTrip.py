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

def createNewTrip(uuuid,start_destination,end_destination,start_time):
    tripid = uuid.uuid4().hex
    errorflag = False
    try:
        query1 = "INSERT INTO TRIPS (tripid, start_destination, end_destination, start_time, number_partipants)"
        data1 = (tripid, start_destination, end_destination, start_time, 1)
        cur.execute(query1,data1)
    except:
        print('Database insertion error, most likely not uuid collision')
        errorflag = True
        raise
    try:
        query2 = "INSERT INTO ONTRIP (tripid, uuuid)"
        data2 = (tripid, uuid)
    except:    
        print('Database insertion error, most likely not uuid collision')
        errorflag = True
        raise
    if not errorflag:
        conn.commit()
        cur.close()
    
