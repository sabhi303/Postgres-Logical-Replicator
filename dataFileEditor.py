
# class
from dataLocations import postgreDataLocations

#for copying files
import shutil

#import os for deleting and renaming
import os

#importing the regex module
import re

#defining the replace method
def replace(filePath, text, subs, flags=0):
    with open(filePath, "r+") as file:
        #read the file contents
        file_contents = file.read()
        text_pattern = re.compile(re.escape(text), flags)
        file_contents = text_pattern.sub(subs, file_contents)
        file.seek(0)
        file.truncate()
        file.write(file_contents)




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

            file_path=sqllocation
            text="#wal_level ="
            subs="wal_level = logical #"

            # calling the replace method
            replace(file_path, text, subs)

            text="wal_level ="
            subs="wal_level = logical #"

            # calling the replace method
            replace(file_path, text, subs)

        except Exception as error :
            
            # deleting old file if exists in case of error
            if os.path.exists(sqllocation):
                os.remove(sqllocation)
                os.rename(sqllocation+".bkp", sqllocation)

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



