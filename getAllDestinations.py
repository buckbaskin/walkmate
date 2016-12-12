import psycopg2

# make a connection
try:
    conn = psycopg2.connect(database='postgres', user='postgres', password='economicalchinchillacorndog', host='localhost')
    cur = conn.cursor()
except:
    print('Database Connection Failed')
    raise
def getALLDestinations():
    cur.execute('SELECT * FROM DESTINATIONS')
    return cur.fetchAll()