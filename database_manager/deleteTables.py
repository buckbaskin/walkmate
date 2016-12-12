import psycopg2

def deleteAll(conn, cur):
    for table in ['FRIENDSHIPS', 'BLOCKS',  'MEMBERS', 'RATINGS','TRIPS', 'USERS', 'DESTINATIONS']:
        try:
            cur.execute('DROP TABLE IF EXISTS '+ table + ';')
            conn.commit()
        except psycopg2.ProgrammingError:
            raise
if __name__ == '__main__':
    import createConnection
    deleteAll(*createConnection.createNewConnection())