import sqlite3

# the query function lets us interact with the db in a friendly way
# query_t => refers to the sql query
# data => refers to the list of items to process 
# doesReturn => indicates if the query does return something
# howMany => lets us controll how many items we want to fetch

def query(query_t, data=None, doesReturn=False, howMany=None):
    response=[]
    connection=sqlite3.connect('library.db')
    cursor=connection.cursor()
    if(not data):
        cursor.execute(query_t)
    else:
        cursor.executemany(query_t, data)
    if(doesReturn):
        if(howMany):
            if(howMany==1):
                response=cursor.fetchone()
            else:
                response=cursor.fetchmany(howMany)
        else:
            response=cursor.fetchall()
    connection.commit()
    cursor.close()
    if(doesReturn):
        return response