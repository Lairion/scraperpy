import os
import settings 
import sqlite3
from sqlite3 import Error
 
def create_db(name):
    """ create a database connection to a database that resides
        in the memory
    """
    try:
        conn = sqlite3.connect(os.path.join(settings.PROJECT_DIR,name+".sqlite3"))
        print(sqlite3.version)
        cursor = conn.cursor()
        cursor.execute("""CREATE TABLE combinations(id INTEGER NOT NULL PRIMARY KEY autoincrement, comb varchar(4))""")
        cursor.execute("""CREATE TABLE hints(id INTEGER NOT NULL PRIMARY KEY autoincrement, combination_id int NOT NULL, item varchar)""")
    except Error as e:
        print(e)
    finally:
        conn.close()

create_db(input("Input name for db: "))
