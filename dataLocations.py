
class postgreDataLocations :

    # data_directory for the database
    dataDirectory : str
    # pg_hba.conf
    hbaConfFilelocation : str
    # postgresql.conf
    sqlConfFileLocation : str
    #db connection
    conn : None
    
    def __init__(self, conn):
        self.conn = conn

    def getDataDirectory(self) :

        # create a cursor
        cur = self.conn.cursor()
        
        # execute a statement
        print('PostgreSQL Data Directory:')
        cur.execute('show data_directory')

        # get the PostgreSQL database's data directory
        # retruns tuple so fetch the first element
        self.dataDirectory = cur.fetchone()[0]
        print(self.dataDirectory)
    
        # close the communication with the PostgreSQL
        cur.close()
        # return(self.dataDirectory)

    def getHbaConfFile(self) :

        # Assuming that the file is always name 'pg_hba.conf'
        self.hbaConfFilelocation = self.dataDirectory + "pg_hba.conf"
        
        # print("HBA Conf File Location : ", self.hbaConfFilelocation)

        return self.hbaConfFilelocation

    def getSqlConfFile(self) :
        
        # Assuming that the file is always name 'postgresql.conf'
        self.sqlConfFileLocation = self.dataDirectory + "postgresql.conf"
        
        # print("SQL Conf File Location : ", self.sqlConfFileLocation)

        return self.sqlConfFileLocation

    # destructor
    def __del__(self):
        pass


#This is this file specific can be used for unit testing

# I may not need this bt jaane do abhi seperate handler likhne ke alava let it be
from connection import dbConnection

if __name__ == '__main__':
    

    # Establishing Database Connection
    connObj = dbConnection()
    connObj.getDbDetails()
    connObj.connect()


    # Now Objects of this class
    locationGetter = postgreDataLocations(connObj.getConnection())
    locationGetter.getDataDirectory()
    locationGetter.getHbaConfFile()
    locationGetter.getSqlConfFile()

    print("\n**Thanks!**\n")

# *** TESTED OK! ***

