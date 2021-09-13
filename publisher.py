

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


from userCreator import userCreator

from publicationCreator import publicationCreator


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
