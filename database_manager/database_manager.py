import createConnection
import createTables
import deleteTables
import populateTables

def prepareDatabase():
	cur = createConnection.createNewConnection()
	deleteTables.deleteAll(cur)
	createTables.createAll(cur)
	populateTables.populateAll(cur)
