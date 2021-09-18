
# Header -- create beutiful logo for this
def header():
    print("\n","*"*50,"\n")
    print("\t POSTGRESQL LOGICAL REPLICATOR")
    print("\n","*"*50,"\n")
    return


# Help Menu
def help():

    print("\n[ HELP ]")

    try :
        # handle this
        choice = int(input("\n\t  1. About PostgreSQL Logical Replication \n\t  2. About Publisher \n\t  3. About Subsriber\n\t  4. Exit to Main-Menu \nChoice\t: "))
        
        switcher = {
         0: "When deploying applications in a production environment, it is always good for you to have multiple copies of the database. After making the copies, you must ensure that they are all in sync. This process of keeping database copies in sync is known as replication.",
         1: "one",
         2: "two",
        
        }


    # Now handling very generic, but can be improved later
    except Exception as error :
        print ( "\n" , error , "\n")
        print ( "Something went wrong! Please try again! \n" )
        mainMenu()
    pass

# Main Menu
def mainMenu():
    print("[ MAIN-MENU ]")
    
    try :
        # handle this
        choice = int(input("\n\t  1. Configure Publisher \n\t  2. Configure Subsriber \n\t  3. Help \nChoice\t: "))
        #let it be for now
        print(choice)

    except Exception as error :
        print ( "\n" , error , "\n")
        print ( "Something went wrong! Please try again! \n" )
        mainMenu()


# main function
def main():
    
    header()
    mainMenu()

    header()

    pass


if __name__ == '__main__':
    # calling main function
    main()


