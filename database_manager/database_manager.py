import createConnection
import createTables
import deleteTables
import populateTables

def prepareDatabase():
    conn, cur = createConnection.createNewConnection()
    deleteTables.deleteAll(conn, cur)
    conn.commit()
    createTables.createAll(conn, cur)
    conn.commit()
    populateTables.populateAll(conn, cur)
    conn.commit()
    cur.close()
if __name__ == '__main__':
    prepareDatabase()