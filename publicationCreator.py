
# Class for publication creator
from tableSelector import tableSelector

# for random string generator
import random, string


class publicationCreator:

    conn: None
    pubName : str

    def __init__(self, conn) -> None:
        self.conn = conn
        pass


    def queryGenerator(self):

        # get required table names from user
        ts = tableSelector(self.conn)
        tableList =  ts.selectTables()
        tableList = ", ".join(tableList)


        # get publication name from user or generate random
        # for a time being, lets make a random one
        self.pubName = ''.join(random.choice(string.ascii_uppercase + string.digits) for _ in range(10))
        

        return "CREATE PUBLICATION " + self.pubName + "pub FOR TABLE " + tableList


    def generatePub(self):

        query = self.queryGenerator()
        
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

                        print("Publication created!")
                else:
                    print("Publication creation failed while committing!\n")


            # closing the cursor
            cur.close()
        
        except Exception as error :
            
            print(error)
            print("Something went wrong!\nPlease try again..\n\n")
        

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
    generateObj.generatePub()
     
    print("\n**Thanks!**\n")

# *** TESTED OK! ***

