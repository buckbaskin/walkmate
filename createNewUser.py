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
    uuuid = uuid.uuid.uuid4().hex
    now = datetime.datetime.utcnow()
    date_joined = str(now.year)+'-'+str(now.month)+'-'+str(now.day)
    query = "INSERT INTO USERS
    cur.execute(query,data)
    
    cur.commit()
    cur.close()
def main():


if __name__ == '__main__':
    main()
