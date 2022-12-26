import sqlite3



# Creates The DB, or if already created then connects
def CreateorConnectDB(dbname, query):
    connection = sqlite3.connect(dbname)
    cursor = connection.cursor()
    SQLquery = query
    cursor.execute(SQLquery)
    connection.commit()

# Sends the given query to the DB given
def QueryToDB(dbname, query):
    connection = sqlite3.connect(dbname)
    cursor = connection.cursor()
    cursor.execute(query)
    connection.commit()

# Returns a list of the results in columnName
def AssignDBContenttoList(dbname, tableName, columnName):
    connection = sqlite3.connect(dbname)
    cursor = connection.cursor()
    LinksinDB_list = []
    query = 'SELECT {}'.format(columnName) + ' from {}'.format(tableName)
    for row in  cursor.execute(query):
        LinksinDB_list.append(row[0])
    return LinksinDB_list

# Sends the given query and returns a list of the result
def AssignDBContenttoListWithQuery(dbname, query):
    connection = sqlite3.connect(dbname)
    cursor = connection.cursor()
    LinksinDB_list = []
    for row in cursor.execute(query):
        LinksinDB_list.append(row[0])
    return LinksinDB_list