import sqlite3

try:
    # Establish a database connection
    connection = sqlite3.connect('store_transaction.db')
    
    # Create a cursor object
    cursor = connection.cursor()
    
    # Create the STORES table if it does not exist
    command1 = """
    CREATE TABLE IF NOT EXISTS stores (
        stores_id INTEGER PRIMARY KEY, 
        location TEXT
    )
    """
    cursor.execute(command1)
    
    # Create the purchases table if it does not exist
    command2 = """
    CREATE TABLE IF NOT EXISTS purchases (
        purchase_id INTEGER PRIMARY KEY, 
        store_id INTEGER, 
        total_cost FLOAT, 
        FOREIGN KEY(store_id) REFERENCES stores(stores_id)
    )
    """
    cursor.execute(command2)
    
    # Insert data into the stores table
    try:
        cursor.execute("INSERT INTO stores VALUES (21, 'Minneapolis')")
        cursor.execute("INSERT INTO stores VALUES (95, 'Chicago')")
        cursor.execute("INSERT INTO stores VALUES (64, 'Iowa City')")
    except sqlite3.IntegrityError as e:
        print(f"IntegrityError occurred while inserting into stores: {e}")
    
    # Insert data into the purchases table
    try:
        cursor.execute("INSERT INTO purchases VALUES (54, 21, 15.49)")
        cursor.execute("INSERT INTO purchases VALUES (23, 64, 21.12)")
    except sqlite3.IntegrityError as e:
        print(f"IntegrityError occurred while inserting into purchases: {e}")
    
    # Fetch and print all records from the purchases table
    cursor.execute("SELECT * FROM purchases")
    results = cursor.fetchall()
    print(results)
    
    # Update a record in the purchases table
    cursor.execute("UPDATE purchases SET total_cost = 3.67 WHERE purchase_id = 54")
    
    # Delete a record from the purchases table
    cursor.execute("DELETE FROM purchases WHERE purchase_id = 54")
    
    # Commit the transaction
    connection.commit()
    
except sqlite3.Error as e:
    print(f"An error occurred: {e}")
finally:
    # Close the database connection
    if connection:
        connection.close()
