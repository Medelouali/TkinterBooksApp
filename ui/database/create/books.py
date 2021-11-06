
def books():
    query=""""
        CREATE TABLE books(
            title TEXT NOT NULL,
            pages INTEGER DEFAULT 0,
            writerEmail TEXT,
            FOREIGN KEY(writerEmail) REFERENCES authors(email)
        )
    """
    return query