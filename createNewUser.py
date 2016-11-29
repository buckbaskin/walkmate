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

def createNewUser(username, hashed_password, first_name, last_name):
    try:
        uuuid = uuid.uuid.uuid4().hex
        date_joined = datetime.datetime.utcnow()
        query = "INSERT INTO USERS (uuuid, username, hashed_password, first_name, last_name, date_joined) VALUES (%s, %s, %s, %s, %s, %s);"
        data = (uuuid, username, hashed_password, first_name, last_name, date_joined)
        cur.execute(query,data)
    except:
        print('Possible uuid error, trying again')
        try:
            uuuid = uuid.uuid.uuid4().hex
            query = "INSERT INTO USERS (uuuid, username, hashed_password, first_name, last_name, date_joined) VALUES (%s, %s, %s, %s, %s, %s);"
            data = (uuuid, username, hashed_password, first_name, last_name, date_joined)
            cur.execute(query,data)
        except:
            print('Database insertion error, most likely not uuid collision')
            raise
    
    cur.commit()
    cur.close()


if __name__ == '__main__':
    main()

