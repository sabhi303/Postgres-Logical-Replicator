

# this will be used to select the tables for publication..

class tableSelector:

    allTables: list
    conn : None
    
    # constructor
    def __init__(self, conn) -> None:

        self.conn = conn
        pass


    # display the tables in the database
    def displayTables(self):
        
        try :

            query = "select relname from pg_class where relkind='r' and relname !~ '^(pg_|sql_)'"

            # create a cursor
            cur = self.conn.cursor()
            
            # execute a statement
            cur.execute(query)

            # Checking success status -- this needs to be changed lol
            self.allTables = [ result[0] for result in cur.fetchall() ]

            # if query return no tables
            if not self.allTables :
                    print("We didn't find ant tables/relations in your current database! \n\nConsider changing it and try again..\n")
            
            else :
                
                # printing available tables
                print("Tables in your current database : ")

                for table in self.allTables :
                    print(table)
                print("\n***\n")
                pass

            # close the communication with the PostgreSQL
            cur.close()

        except Exception as error :
            
            print(error)
            print("Something went write while writing in the file, please try again")

        pass


    # select required tables
    def selectTables(self):
        
        # Display all tables..
        self.displayTables()

        selectedTables = input("Enter table names to replicate (space seperated) [ All tables ] =>\n")
        
        # if user provides table names
        if selectedTables :
            # seperate the list  by space 
            selectedTables = selectedTables.split(" ")
        else :
            selectedTables = self.allTables

        return selectedTables


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
    tableSelector = tableSelector(connObj.getConnection())
    tableSelector.displayTables()
    tempList = tableSelector.selectTables()
    print("Selected Tables : ", tempList)

    

    print("\n**Thanks!**\n")

# *** TESTED OK! ***
