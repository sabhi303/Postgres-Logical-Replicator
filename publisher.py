

# To Do

# What publisher or source does :
#       1. User and authentication setup
#       2. wal_level configuration
#       3. CREATE PUBLICATION
#       4. Grant rights to User
# Meaning,
#       1.  psql # CREATE ROLE replicator REPLICATION LOGIN PASSWORD 'Mandakini@4'; ---done

#       2.  Edit pg_hba.conf file & make user to eleble for REPLICATION             ---done
#            Add line : 
#           host    all replicator localhost    md5
#       3. set wal level in conf file                                           ---done
#           wal_level = logical
#       4. psql # CREATE PUBLICATION classpub FOR TABLE classroom;              
#           COULD HAVE DONE FOR ALL TABLES AND STUFF
#       5. psql # GRANT ALL ON classroom TO replicator;



# Class for New User Creation
class userCreator :
    
    # Connection Object
    conn : None
    userName : None
    userPass : None

    def __init__(self, conn) -> None:
        
        self.conn = conn
        pass

    def getCredentials(self, default="newUser" ) -> None:
        
        self.userName = input("Enter Username for Replicator [ "+ default +" ] : ") or default        
        #parat he field hidden kra
        self.userPass = ""
        while(self.userPass == ""):
            self.userPass = input("Enter Password for "+self.userName+" : ")
         

    def createRoleForReplication(self) :
        
        # get credentials for new replicator
        self.getCredentials( "replicator" )

        query = "CREATE ROLE " + self.userName + " REPLICATION LOGIN PASSWORD '" + self.userPass +"'"

        # init cursor
        cur = self.conn.cursor()

        try : 
            # execute query
            cur.execute(query)

            # do exception handling over this
            if "CREATE" in cur.statusmessage:
                
                cur.execute("COMMIT")

                if "COMMIT" in cur.statusmessage:

                        print("User creation Successful ! ")
                else:
                    print("User creation Failed at COMMIT..\n Something went wrong with database while committing..\n")

        except Exception as error :
            print(error)
            print("User creation Failed! \nTry again with different username..\n")

            # close cursor
        cur.close()

        return self.userName or ""
        
    # destructor 
    def __del__(self):        
        pass

class publisher :
    
    conn : None
    publisherName : str

    def __init__(self, conn) -> None:
        
        self.conn = conn
        pass

    def createRoleForReplication(self):
        
        uc = userCreator( self.conn )
        
        # self exlplanotory
        self.publisherName = uc.createRoleForReplication()
        pass

    # Get publisher Name
    def getPublisherName(self):
        return self.publisherName if self.publisherName != "" else "Publisher hasn't been created yet!"



# I may not need this bt jaane do abhi seperate handler likhne ke alava let it be
from connection import dbConnection

if __name__ == '__main__':
    

    # Establishing Database Connection
    connObj = dbConnection()
    connObj.getDbDetails()
    connObj.connect()


    # Now Objects of this class
    publisher = publisher(connObj.getConnection())
    publisher.createRoleForReplication()
    

    print("\n**Thanks!**\n")

# *** TESTED OK! ***
