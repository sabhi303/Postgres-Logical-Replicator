
import psycopg2                 # for postgres connection


class dbConnection : 
    
    dbServer : str
    dbName : str
    dbPort : str
    dbUserName : str 
    dbPassword : str

    #Connection Object 
    conn : None

    #For getting connection details from user
    def getDbDetails(self):

        self.dbServer = input("Server [ localhost ] : ") or "localhost"
        self.dbName = input("Database [ postgres ] : ") or "postgres"
        self.dbPort = input("Port [ 5432 ] : ") or "5432"
        self.dbUserName = input("Username [ postgres ] : ") or "postgres"

        #Hidden kra he
        self.dbPassword = input("Password : ")

    #For Establishing connection 
    def connect(self):
        
        self.conn = None
        try:
            connectionDetails = {
                'host' : self.dbServer,
                'port' : self.dbPort,
                'database' : self.dbName,
                'user' : self.dbUserName,
                'password' : self.dbPassword
            }

            # connect to the PostgreSQL server
            print('Connecting to the PostgreSQL database...')
            self.conn = psycopg2.connect(**connectionDetails)
            
            # create a cursor
            cur = self.conn.cursor()
            
            # execute a statement
            print('PostgreSQL database version:')
            cur.execute('SELECT version()')

            # display the PostgreSQL database server version
            db_version = cur.fetchone()
            print(db_version)
        
            # close the communication with the PostgreSQL
            cur.close()

        except (Exception, psycopg2.DatabaseError) as error:
            print(error)

    #return connection object
    def getConnection(self):

        return self.conn

    # closing the connection if exists
    def closeConnection(self):        
        if self.conn is not None:
            self.conn.close()
            print('Database connection closed.')

    def __del__(self):
        
        self.closeConnection()
        pass


#This is this file specific can be used for unit testing
if __name__ == '__main__':
    
    connObj = dbConnection()
    connObj.getDbDetails()
    connObj.connect()

    print("\n**Thanks!**\n")

# *** TESTED OK! ***