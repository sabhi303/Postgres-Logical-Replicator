

class helpGuide :

    def getPostLogiHelp(self):

        str = """
        Logical replication is a method of replicating data objects and their changes, 
        based upon their replication identity (usually a primary key). 
        
        We use the term logical in contrast to physical replication, 
        which uses exact block addresses and byte-by-byte replication.
        PostgreSQL supports both mechanisms concurrently.

        Logical replication allows fine-grained control over both data replication and security.

        Logical replication uses a publish and subscribe model with one or more subscribers subscribing 
        to one or more publications on a publisher node. Subscribers pull data from the publications
        they subscribe to and may subsequently re-publish data to allow cascading 
        replication or more complex configurations.

        """
        
        print("\n","="*50,"\n")
        print(str)
        print("\n","="*50,"\n")

    def getPubHelp(self):

        str="""
        A publication can be defined on any physical replication master. 
        The node where a publication is defined is referred to as publisher. 
        A publication is a set of changes generated from a table or a group of tables, 
        and might also be described as a change set or replication set. 
        Each publication exists in only one database.

        Publications are different from schemas and do not affect how the table is accessed. 
        Each table can be added to multiple publications if needed. 
        Publications may currently only contain tables. Objects must be added explicitly, 
        except when a publication is created for ALL TABLES.

        Publications can choose to limit the changes they produce to any combination of INSERT, 
        UPDATE, and DELETE, similar to how triggers are fired by particular event types. 
        By default, all operation types are replicated.
        """

        print("\n","="*50,"\n")
        print(str)
        print("\n","="*50,"\n")

    def getSubHelp(self):

        str="""
        A subscription is the downstream side of logical replication. 
        The node where a subscription is defined is referred to as the subscriber. 
        A subscription defines the connection to another database and set of 
        publications (one or more) to which it wants to subscribe.

        The subscriber database behaves in the same way as any other PostgreSQL instance and 
        can be used as a publisher for other databases by defining its own publications.

        A subscriber node may have multiple subscriptions if desired. 
        It is possible to define multiple subscriptions between a single publisher-subscriber pair, 
        in which case care must be taken to ensure that the subscribed publication objects don't overlap.
        """

        print("\n","="*50,"\n")
        print(str)
        print("\n","="*50,"\n")


def helpMenu():
    
    print("\n[ HELP ]\n")
    
    switcher = {
        1: helpGuide().getPostLogiHelp,
        2: helpGuide().getPubHelp,
        3: helpGuide().getSubHelp,
    }

    try :
        # handle this
        choice = int(input("\n\t  1. About PostgreSQL Logical Replication \n\t  2. About Publisher \n\t  3. About Subsriber\n\t  4. Exit to Main-Menu \nChoice\t: "))
        print("\n","="*50,"\n")
        

        # p00r attempt 0f sw1tch case :x ...
        if( choice < 4 and choice > 0 ):
            print(switcher[choice]())

        elif choice==4 :
            return
        else :
            print("Please Enter valid choice")
        
        helpMenu()

    # Now handling very generic, but can be improved later
    except Exception as error :
        print ( "\n" , error , "\n")
        print ( "Something went wrong! Please try again! \n" )
        helpMenu()
