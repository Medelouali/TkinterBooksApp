from sqlite3 import *

def users():
    query="""
        CREATE TABLE users(
            username text NOT NULL,
            email text PRIMARY KEY,
            password text NOT NULL
        )
    """
    return query