
def authors():
    query=""""
        CREATE TABLE authors(
            username TEXT NOT NULL,
            email TEXT PRIMARY KEY,
            cityCountry TEXT DEFAULT "Unkown",
            branch TEXT DEFAULT "Unkown",
            stars INTEGER DEFAULT 0,
            bio TEXT DEFAULT "",
            birthday TEXT DEFAULT "Unkown"
        )
    """
    return query