
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
