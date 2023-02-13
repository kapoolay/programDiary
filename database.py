import sqlite3

# this is the connection to the data store
connection = sqlite3.connect("data.db")
connection.row_factory = sqlite3.Row  # Returns your rows as a dictionary rather than a tuple


## Function to create the table and data.db if it doesn't exist
def create_table():
    with connection:        # context manager automatically commits the changes
        connection.execute(
            "CREATE TABLE IF NOT EXISTS entries (content TEXT, date TEXT)"
        )


## Function to add an entry to the db
def add_entry(entry_content, entry_date):
    with connection: 
        connection.execute(
            "INSERT INTO entries VALUES(?, ?);", (entry_content, entry_date)    
        )


## Function to return values in the db
## If there are no changes, you won't need the context manager --> 'with connection:'
## '.execute' automatically creates a cursor()
def get_entries():
    cursor = connection.execute("SELECT * FROM entries;")
    return cursor