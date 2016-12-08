import psycopg2

def deleteAll(cur):
    query = 'DROP TABLE USERS;'
    cur.execute(query)
    query = 'DROP TABLE FRIENDSHIPS;'
    cur.execute(query)
    query = 'DROP TABLE BLOCKS;'
    cur.execute(query)
    query = 'DROP TABLE TRIPS;'
    cur.execute(query)
    query = 'DROP TABLE MEMBERS;'
    cur.execute(query)
    query = 'DROP TABLE DESTINATIONS;'
    cur.execute(query)
    query = 'DROP TABLE RATINGS;'
    cur.execute(query)
    cur.commit
