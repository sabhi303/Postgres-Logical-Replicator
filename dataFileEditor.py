
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
            
            
            fileHandler.write("\# Following are the connections that are updated by replication tool\n")
            fileHandler.write("\# You can find the original file with .bkp extension\n")

            for i in hostName :
                fileHandler.write("host    all             " + userName + "      " + i + "			trust\n")
            pass
        
        except Exception as error :
            
            # deleting old file if exists in case of error
            if os.path.exists(hbalocation):
                os.remove(hbalocation)
                os.rename(hbalocation+".bkp", hbalocation)

            print(error)
            print("Something went write while writing in the file, please try again")
        


    def sqlEditor(self):

        sqllocation = self.locationGetter.getSqlConfFile()
        print("SQLconf File : ", sqllocation)
        self.backupFile(sqllocation)

        try :
            fileHandler = open(sqllocation,'r')
            fileData = fileHandler.read()

            # setting wal_level to logical to enable replication
            fileData.replace('wal_level =', 'wal_level = logical #')
            fileData.replace('#wal_level =', 'wal_level = logical #')
        
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



