
# this is for executing and seperating sql statements


def queryExecutor(conn, sql, getColNames = False):
        
        try :   

            # create a cursor
            cur = conn.cursor()
            
            # execute a statement
            cur.execute(sql)

            # Checking success status -- this needs to be changed lol
            res = cur.fetchall()

            
            colnames = ""
            if getColNames :
                colnames = [desc[0] for desc in cur.description]
            cur.close()
            
            
            return res if not getColNames else (res, colnames)

        except Exception as error :
            
            print(error)
            print("Something went write while writing in the file, please try again")
            return ""



# list all publications
def listAllPublications( conn, display = False ) :

    if conn :
        sql = "select pubname, puballtables, pubowner from pg_publication"
        res = queryExecutor(conn, sql)
        
        # iterating over result
        if res != "" : 
            
            if display : 
                print("\n[ PUBLICATIONS ]\n")
                print("Publication\t\tAll tables?\tOwnerID")
                print(len("Publication             All tables?     OwnerID") * "=")

                for row in res: 
                    print( row[0] , "\t\t" , row[1] , "\t\t" , row[2] )

                print("\n***\n")

            return res

        else :
            print(" Sorry, the query failed! ")

    else :
        print("You are not connected to the database ! ")

    return
    
def listAllSubscriptions(conn, display = False):
    if conn :
        sql = "select subname, subenabled, subowner from pg_subscription"
        res = queryExecutor(conn, sql)
        
        # iterating over result
        if res != "" : 
            
            if display : 
                print("\n[ SUBSCRIPTIONS ]\n")
                print("Subscription\t\tEnabled?\tOwnerID")
                print(len("Subscription             All tables?     OwnerID") * "=")

                for row in res: 
                    print( row[0] , "\t\t" , row[1] , "\t\t" , row[2] )

                print("\n***\n")

            return res

        else :
            print(" Sorry, the query failed! ")

    else :
        print("You are not connected to the database ! ")

    return


# list all database users
def listAllUsers (conn, display = False):
    if conn :
        sql = '''SELECT usename AS role_name,
            CASE 
            WHEN usesuper AND usecreatedb THEN 
            CAST('superuser, create database' AS pg_catalog.text)
            WHEN usesuper THEN 
            CAST('superuser' AS pg_catalog.text)
            WHEN usecreatedb THEN 
            CAST('create database' AS pg_catalog.text)
            ELSE 
            CAST('' AS pg_catalog.text)
            END role_attributes
            FROM pg_catalog.pg_user
            ORDER BY role_name desc;'''
        
        res = queryExecutor(conn, sql)
        
        # iterating over result
        if res != "" : 
            
            if display :
                print("\n[ DATABASE USERS ]\n")
                print("User\t\t\tRoles")
                print( len("postgres                 superuser, create database") * "=" )
                
                for row in res: 
                    print( row[0],"\t\t", row[1])
                
                print("\n***\n")

            return res

        else :
            print(" Sorry, the query failed! ")
    
    else :
        print("You are not connected to the database ! ")
    
    return


# get all tables under a publication
# select * from pg_publication_tables where pubname='pmrvq2i19mpub';
def getPublicationTables(conn, pubName, display = False):
    
    if conn :
        sql = "select schemaname,tablename  from pg_publication_tables where pubname='%s'" % pubName
        res = queryExecutor(conn, sql)
        
        # iterating over result
        if res != "" : 
            
            if display : 
                print( "\n[ TABLES UNDER %s ]\n" % pubName )
                print("Schema\t\tTable Name")
                print(len("Publication             All tables?     OwnerID") * "=")

                for row in res: 
                    print( row[0], "\t\t", row[1])

                print("\n***\n")

            return res

        else :
            print(" Sorry, the query failed! ")

    else :
        print("You are not connected to the database ! ")

    return
    pass


# get table schema
def getTableDescription(conn, tableName, display = False):
    if conn :
        sql = '''SELECT * FROM information_schema.columns
                WHERE TABLE_NAME = '%s';''' % tableName
        
        res, colNames = queryExecutor(conn, sql, True)

        
        # iterating over result
        if res != "" : 
            if display:
        
                print("colnames : ", colNames)

                print("\n[ TABLE DESCRIPTION ]\n")
                print("Table schema")
                for row in res: 
                    print( row )
                
                print("\n***\n")
            
            return res

        else :
            print(" Sorry, the query failed! ")
    
    else :
        print("You are not connected to the database ! ")
    
    return






# I may not need this bt jaane do abhi seperate handler likhne ke alava let it be
from connection import dbConnection

if __name__ == '__main__':
    
    connObj = dbConnection()
    connObj.getDbDetails()
    connObj.connect()

    print("\n**Thanks!**\n")

    # res = listAllUsers(connObj.getConnection(), True)
    # res = listAllPublications(connObj.getConnection())

    # res = getTableDescription(connObj.getConnection(), 'testtable',True)

    # res = listAllUsers(connObj.getConnection())

    res = getPublicationTables(connObj.getConnection(), 'puzcimnn93pub', True)


# *** TESTED OK! ***