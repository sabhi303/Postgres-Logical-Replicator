
from publisher import publisherMenu
from subscriber import subscriberMenu
from help import helpMenu

# Header -- create beutiful logo for this
def header():
    print("\n","*"*50,"\n")
    print("\t POSTGRESQL LOGICAL REPLICATOR")
    print("\n","*"*50,"\n")
    return


# Main Menu
def mainMenu():
    
    print("\n[ MAIN-MENU ]\n")

    switcher = {
        1: publisherMenu,
        2: subscriberMenu,
        3: helpMenu,
    }


    try :
        # handle this
        choice = int(input("\n\t  1. Configure Publisher \n\t  2. Configure Subsriber \n\t  3. Help \n\t  4. Exit \nChoice\t: "))
        
        print("\n","="*50,"\n")

        # p00r attempt 0f sw1tch case :x ...
        if( choice < 4 and choice > 0 ):
            switcher[choice]()

        elif choice==4 :
            return
        else :
            print("Please Enter valid choice")

        mainMenu()

    except Exception as error :
        print ( "\n" , error , "\n")
        print ( "Something went wrong! Please try again! \n" )
        mainMenu()

    


# main function
def main():
    
    header()
    mainMenu()
    header()

    exit()


if __name__ == '__main__':
    # calling main function
    main()


