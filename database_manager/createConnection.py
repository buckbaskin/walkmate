import psycopg2
def createNewConnection():
    try:
        conn = psycopg2.connect(database='postgres', user='postgres', password='economicalchinchillacorndog', host='localhost')
        cur = conn.cursor()
    except:
        print('Database Connection Failed')
        import sys
        sys.exit(1)
    return (conn, cur,)