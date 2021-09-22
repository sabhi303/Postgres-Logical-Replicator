
#==========================================================================================================================#
# To Do                                                                                                                    #
#                                                                                                                          #
# What publisher or source does :                                                                                          #
#       1. User and authentication setup                                                                                   #
#       2. wal_level configuration                                                                                         #
#       3. CREATE PUBLICATION                                                                                              #
#       4. Grant rights to User                                                                                            #     
# Meaning,                                                                                                                 # 
#       1.  psql # CREATE ROLE replicator REPLICATION LOGIN PASSWORD 'Mandakini@4'; ---done                                #     
#                                                                                                                          #     
#       2.  Edit pg_hba.conf file & make user to eleble for REPLICATION             ---done                                #                 
#            Add line :                                                                                                    #             
#           host    all replicator localhost    md5                                                                        #     
#       3. set wal level in conf file                                           --- done                                   #     
#           wal_level = logical                                                                                            #     
#       4. psql # CREATE PUBLICATION classpub FOR TABLE classroom;              --- done                                   #     
#           COULD HAVE DONE FOR ALL TABLES AND STUFF    [ this is remaining, though current scene willl work, still lets   # 
#                                                       optimize it and create one FOR ALL TABLE wali query ]              #     
#       5. psql # GRANT ALL ON classroom TO replicator;                                                                    #     
#                                                       [ function has been written in userCreator check its validity and  #     
#                                                         add respective methods in this class ]                           #         
#                                                                                                                          #
#==========================================================================================================================#

from userCreator import userCreator

from publicationCreator import publicationCreator


class publisher :
    
    conn : None
    publisherName : str
    publicationName : str

    def __init__(self, conn = None) -> None:
        
        self.conn = conn
        pass

    def setConn(self,conn) :
        self.conn = conn
        pass
    

    ######### USER FOR PUBLICATION #########
    
    def createRoleForReplication(self):
        
        uc = userCreator( self.conn )
        
        # self exlplanotory
        self.publisherName = uc.createRoleForReplication()

        return self.publisherName or "Something went wrong, please try again later.."

    # Get publisher Name
    def getPublisherName(self):

        return self.publisherName if self.publisherName != "" else "Publisher hasn't been created yet!"

    #######################################


    ############ PUBLICATION ##############
    
    def createPublication(self):

        pc = publicationCreator(self.conn)
        self.publicationName = pc.generatePub()

        return self.publicationName or None

    # get publication name
    def getPublicationName(self):

        return self.publicationName or None

    #######################################

    
    # destructor 
    def __del__(self):        
        pass




# I may not need this bt jaane do abhi seperate handler likhne ke alava let it be
'''
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

'''

# *** TESTED OK! ***

# For establishing connection
from connection import dbConnection


def addPublisherDatabase():

     # Establishing Database Connection
    connObj = dbConnection()
    connObj.getDbDetails()
    connObj.connect()
    # connection object
    return connObj.getConnection()



# publisher object 
pub = publisher()

# Publisher Menu

def publisherMenu():
    
    global pub
    print("\n[ PUBLISHER-MENU ]\n")
    
    try :

        # handle this
        choice = int(input("\n\t  1. Configure Publisher Database \n\t  2. Create Publication Role \n\t  3. Configure Publication \n\t  4. Exit to Main Menu \nChoice\t: "))
        
        print("\n","="*50,"\n")

        # p00r attempt 0f sw1tch case :x ...
        
        if choice == 1 :
            # Set the connection
            pub.setConn(addPublisherDatabase())
            if ( pub.conn ) : print("\nPublisher database added successfully!")
            else : "We were unable to configure the database, please try again!"
        
        elif choice == 2 :
            # create publication role
            if ( pub.createRoleForReplication() ) : print ( " Role : ",pub.publisherName," is created successfully!")
            else : "Something went wrong! Please try again.."

        elif choice == 3 :
            if( pub.createPublication() ) :  print ( " Publication : ",pub.publicationName," is created successfully!")
            else : "Something went wrong! Please try again.."
    

        elif choice == 4 :
            # return to main menu
            return 

        else :
            print("Please Enter valid choice")
        
        publisherMenu()

    except Exception as error :
        print ( "\n" , error , "\n")
        print ( "Something went wrong! Please try again! \n" )
        publisherMenu()

    pass
