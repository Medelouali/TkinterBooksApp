
def editors():
    query=""""
        CREATE TABLE editors(
            name TEXT DEFAULT "Unkown",
            email TEXT NOT NULL PRIMARY KEY,
            address TEXT DEFAULT "Unkown",
            phone TEXT DEFAULT "Unkown",
            manager TEXT NOT NULL,
            websiteUrl TEXT DEFAULT "",
            stars INTEGER DEFAULT 0,
            FOREIGN KEY(manager) REFERENCES users(email)
        )
    """
    return query