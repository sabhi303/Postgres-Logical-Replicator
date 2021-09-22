
# Class for publication creator
from tableSelector import tableSelector

# for random string generator
import random, string


class subscriptionCreator:

    conn: None
    publicationName : str

    def __init__(self, conn) -> None:
        
        self.conn = conn
        pass


    def queryGenerator(self, connectionString, publicationName):


        # get publication name from user or generate random
        # for a time being, lets make a random one
        self.publicationName = 'S'+''.join(random.choice(string.ascii_uppercase + string.digits) for _ in range(9))
        
        '''
        CREATE SUBSCRIPTION mysub
         CONNECTION 'host=192.168.1.50 port=5432 user=foo dbname=foodb'
        PUBLICATION mypublication, insert_only;
        '''

        ret =  "CREATE SUBSCRIPTION " + self.publicationName + " CONNECTION '" + connectionString
        ret += "' PUBLICATION "
        for pub in publicationName:
            ret += pub + " "
        
        return ret


    def generateSub(self, connectionString, pubNames):
        query = self.queryGenerator( connectionString, pubNames)
        
        try :
            # create a cursor
            cur = self.conn.cursor()

            # Commiting previous changes
            cur.execute("COMMIT")
            
            # execute a statement
            cur.execute(query)

            # Checking success status
            if "CREATE" in cur.statusmessage:
                    
                cur.execute("COMMIT")

                if "COMMIT" in cur.statusmessage:

                        print("Subscription created!")
                else:
                    print("Subscription creation failed while committing!\n")


           
        
        except Exception as error :
            
            print(error)
            print("Something went wrong!\nPlease try again..\n\n")

        # return publication name
        finally :
            
            # closing the cursor
            cur.close()

            return self.publicationName
    

    # destructor 
    def __del__(self):        
        pass


# I may not need this bt jaane do abhi seperate handler likhne ke alava let it be
from connection import dbConnection

if __name__ == '__main__':
    

    # Establishing Database Connection
    connObj = dbConnection()
    connObj.getDbDetails()
    connObj.connect()


    # Now Objects of this class
    generateObj = publicationCreator(connObj.getConnection())
    
    # Publisher details
    dbServer = input("Server [ localhost ] : ") or "localhost"
    dbName = input("Database [ postgres ] : ") or "postgres"
    dbPort = input("Port [ 5432 ] : ") or "5432"
    dbUserName = input("Username [ postgres ] : ") or "postgres"
    #Hidden kra he
    dbPassword = input("Password : ")
    
    '''
        CREATE SUBSCRIPTION mysub
         CONNECTION 'host=192.168.1.50 port=5432 user=foo dbname=foodb'
        PUBLICATION mypublication, insert_only;
    '''

    connstr = "host={} dbname={} port={} user={} password={}".format(dbServer, dbName, dbPort, dbUserName, dbPassword)
    
    generateObj.generateSub(connstr, ["puzcimnn93pub"])
     
    print("\n**Thanks!**\n")

# *** TESTED OK! ***

