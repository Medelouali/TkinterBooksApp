
def copies():
    query=""""
        CREATE TABLE copies(
            title TEXT NOT NULL,
            writerEmail TEXT NOT NULL,
            description TEXT DEFAULT "",
            editionHouse TEXT NOT NULL,
            editionDate TEXT DEFAULT "Unkown",
            editorEmail TEXT NOT NULL,
            FOREIGN KEY(writerEmail) REFERENCES authors(email)
            FOREIGN KEY(editorEmail) REFERENCES editors(email)
        )
    """
    return query