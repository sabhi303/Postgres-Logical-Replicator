
#==========================================================================================================================#
#  to-do :
#     1. try to copy table schema
#     2. adhi basics krun gheuyat
#==========================================================================================================================#

from userCreator import userCreator

from subscriptionCreator import subscriptionCreator

from sql import listAllUsers, listAllPublications, listAllSubscriptions


class subsriber :
    
    conn : None
    subscriberName : str
    subsriptionName : str

    def __init__(self, conn = None) -> None:
        
        self.conn = conn
        pass

    def setConn(self,conn) :
        self.conn = conn
        pass
    

    ######### Subscription Role #######
    
    def createRoleForReplication(self):
        
        uc = userCreator( self.conn )
        
        # self exlplanotory
        self.subscriberName = uc.createRoleForReplication()

        return self.subscriberName or "Something went wrong, please try again later.."

    # Get publisher Name
    def getSubscriberName(self):

        return self.subscriberName if self.subscriberName != "" else "Subscriber hasn't been created yet!"

    #################################


    ############ Subscription ##############
    
    def createSubscription(self, connectionStr, publicationName):

        sc = subscriptionCreator(self.conn)
        self.subsriptionName = sc.generateSub(connectionStr, publicationName)

        return self.subsriptionName or None

    # get publication name
    def getSubsriptionName(self):

        return self.subsriptionName or None

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


def addSubscriberDatabase():

     # Establishing Database Connection
    connObj = dbConnection()
    connObj.getDbDetails()
    connObj.connect()
    # connection object
    return connObj.getConnection()



# publisher object 
sub = subsriber()
pubObj = dbConnection()

# Publisher Menu

def subscriberMenu( choice = None ):
    
    global sub
    print("\n[ SUBSCRIBER-MENU ]\n")
    
    try :

        # handle this
        if not choice :
            choice = int(input("\n\t  1. Configure Subscriber Database \n\t  2. Create Subscrition Role \n\t  3. Configure Subscription \n\t  4. Exit to Main Menu \nChoice\t: "))
        
        print("\n","="*50,"\n")

        # p00r attempt 0f sw1tch case :x ...
        
        if choice == 1 :
            # Set the connection
            sub.setConn(addSubscriberDatabase())
            if ( sub.conn ) : print("\nSubscriber database added successfully!")
            else : "We were unable to configure the database, please try again!"
        
        elif choice == 2 :
           
            # create publication role
            print("\n[ SUBSCRIPTION ROLE CREATION ]\n")

            choice = int(input("\n\t  1. List All Database roles \n\t  2. Create New Subscription Role  \n\t  3. Exit to Subscription Menu \nChoice\t: "))
            print("\n","="*50,"\n")

            if choice == 1 :
                listAllUsers( sub.conn , True)

            elif choice == 2 : 
                if ( sub.createRoleForReplication() ) : print ( " Role : ",sub.subscriberName," is created successfully!")
                else : "Something went wrong! Please try again.."


            elif choice == 3 :
                pass
               
            else :
                print("Please Enter valid choice!")
                pass
           
        
        elif choice == 3 :
            print("\n[ SUBSCRIPTION CREATION ]\n")

            choice = int(input("\n\t  1. List All Subscriptions \n\t  2. Create New Subscription  \n\t  3. Exit to Subscription Menu \nChoice\t: "))
            print("\n","="*50,"\n")

            if choice == 1 :
                listAllSubscriptions( sub.conn , True)
                pass

            elif choice == 2 :
                
                # ithe publication details ghayachet
                            
                # Publisher details
                print("\nEnter Publisher Details..\n")

                dbServer = input("Server [ localhost ] : ") or "localhost"
                dbName = input("Database [ postgres ] : ") or "postgres"
                dbPort = input("Port [ 5432 ] : ") or "5432"
                dbUserName = input("Username [ postgres ] : ") or "postgres"
                #Hidden kra he
                dbPassword = input("Password : ")
                

                # list publications
                pubObj.setDbDetails(dbServer, dbName, dbPort, dbUserName, dbPassword)
                pubObj.connect()

                print("")
                listAllPublications(pubObj.getConnection() ,True)
                pubs = input("Enter Publications from above list [space seperated] : ").split(" ")


                connstr = "host={} dbname={} port={} user={} password={}".format(dbServer, dbName, dbPort, dbUserName, dbPassword)

                # list publications on that server over here..
                
                if( sub.createSubscription(connstr, pubs) ) :  print ( " Subscription : ",sub.getSubsriptionName()," is created successfully!")
                else : "Something went wrong! Please try again.."
                pass
            
            elif choice == 3 :
                pass

            else :
                print("Please Enter valid choice!")
                pass

        elif choice == 4 :
            # return to main menu
            return 

        else :
            print("Please Enter valid choice!")
        
        # Loop instead of this to optimize... and adjust menu accordingly
        subscriberMenu()

    except Exception as error :
        print ( "\n" , error , "\n")
        print ( "Something went wrong! Please try again! \n" )
        subscriberMenu()

    pass
