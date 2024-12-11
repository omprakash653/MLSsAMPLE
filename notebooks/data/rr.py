import pandas as pd
import mysql.connector

# MySQL connection details
db_config = {
    'user': 'root',
    'password': r'@shivam35',
    'host': 'localhost',  # or your host address
    'database': 'gemstone_data'
}

# Path to your CSV file
csv_file_path = r'C:\Users\shivo\OneDrive\Desktop\FSDS\project\Ml\project11\notebooks\data\gemstone.csv'

# MySQL table name
table_name = "diamonds"

def export_csv_to_mysql(csv_file, table_name, db_config):
    try:
        # Read the CSV file into a DataFrame
        data = pd.read_csv(csv_file)
        
        # Establish connection to MySQL
        connection = mysql.connector.connect(**db_config)
        cursor = connection.cursor()

        # Generate the SQL query for data insertion
        columns = ", ".join([f"`{col}`" for col in data.columns])  # Wrap column names in backticks
        placeholders = ", ".join(["%s"] * len(data.columns))
        insert_query = f"INSERT INTO {table_name} ({columns}) VALUES ({placeholders})"

        # Insert each row from the DataFrame into the table
        for row in data.itertuples(index=False, name=None):
            cursor.execute(insert_query, row)

        # Commit the transaction
        connection.commit()
        print(f"Data exported successfully to {table_name} table.")
    
    except Exception as e:
        print(f"An error occurred: {e}")
    
    finally:
        if connection.is_connected():
            cursor.close()
            connection.close()

# Call the function
export_csv_to_mysql(csv_file_path, table_name, db_config)
