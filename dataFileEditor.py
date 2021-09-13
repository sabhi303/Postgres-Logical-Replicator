
# class
from dataLocations import postgreDataLocations

#for copying files
import shutil

#import os for deleting and renaming
import os


class dataFileEditor :

    conn : None
    locationGetter : None

    # constructor
    def __init__(self, conn) -> None:
        self.conn = conn

        # object for getting data files paths
        self.locationGetter = postgreDataLocations(self.conn)
        pass

    def backupFile(self, filename):
        # handle exceptions
        shutil.copy(filename, filename+".bkp")
        pass

    def hbaEditor(self,userName):

        hbalocation = self.locationGetter.getHbaConfFile()
        print("hab File location : ", hbalocation)
        self.backupFile(hbalocation)

        #Adding hostNames 
        hostName = ["0.0.0.0/0", "localhost"]
        # hyat subscriber ch lagato ka kai sure naiye
        # bghava lagel
        hostName.append(input("Enter address of the subscriber machine : "))


        try : 
            fileHandler = open(hbalocation, "a")
            #ikde md5 kra, bt for a time being its okay
            #edit section
            
            
            fileHandler.write("\n# Following are the connections that are updated by replication tool\n")
            fileHandler.write("\n# You can find the original file with .bkp extension\n")

            for i in hostName :
                fileHandler.write("host  all        " + userName + "            " + i + "                 trust\n")
            pass
            
            fileHandler.close()

        except Exception as error :
            
            # deleting old file if exists in case of error
            if os.path.exists(hbalocation):
                os.remove(hbalocation)
                os.rename(hbalocation+".bkp", hbalocation)

            print(error)
            print("Something went write while writing in the file, please try again")
            fileHandler.close()
        


    def sqlEditor(self):

        sqllocation = self.locationGetter.getSqlConfFile()
        print("SQLconf File : ", sqllocation)
        self.backupFile(sqllocation)

        try :

            #Setting wal_level to logical via query


            query = "ALTER SYSTEM SET wal_level = logical"

            # create a cursor
            cur = self.conn.cursor()

            # Commiting previous changes
            cur.execute("COMMIT")
            
            # execute a statement
            cur.execute(query)

            # Checking success status
            if "ALTER" in cur.statusmessage:
                
                cur.execute("COMMIT")

                if "COMMIT" in cur.statusmessage:

                        print("Changed wal_level to logical!\n\n***Restart your Database to apply the changes !***\n\n")
                else:
                    print("wal_level updation failed at COMMIT..\n Something went wrong with database while committing..\n")


            # close the communication with the PostgreSQL
            cur.close()

        except Exception as error :
            
            print(error)
            print("Something went write while writing in the file, please try again")


        pass

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
    dataFileEditor = dataFileEditor(connObj.getConnection())
    dataFileEditor.hbaEditor("replicator")
    dataFileEditor.sqlEditor()

    print("\n**Thanks!**\n")



