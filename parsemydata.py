import mysql.connector

def extract_counts_from_output(output):
    try:
        # Split the output string by commas and spaces
        counts = output.split(', ')
        
        # Extract numbers from each part
        passed = int(counts[0].split()[1])  # "passed 1" -> split by space and take the second part
        failed = int(counts[1].split()[1])  # "failed 4" -> split by space and take the second part
        skipped = int(counts[2].split()[1])  # "skipped 1" -> split by space and take the second part
        
        return passed, failed, skipped
    
    except IndexError:
        print("Error: Unexpected format in output.")
        return None, None, None
    except ValueError:
        print("Error: Unable to convert count to integer.")
        return None, None, None

def insert_into_mysql(passed, failed, skipped):
    try:
        # Connect to MySQL
        conn = mysql.connector.connect(
            host='localhost',
            port=3306,
            database='test_results_db',
            user='root',
            password='Test@1234'
        )
        
        # Create a cursor object using the cursor() method
        cursor = conn.cursor()
        
        # Prepare SQL query to INSERT a record into the database
        sql = "INSERT INTO test_2 (test_name,total, passed, failed, skipped) VALUES (%s, %s, %s, %s, %s)"
        data = ("Log In Test",total, passed, failed, skipped)
        
        # Execute the SQL command
        cursor.execute(sql, data)
        
        # Commit your changes in the database
        conn.commit()
        
        print("Record inserted successfully into MySQL database")
        
    except mysql.connector.Error as e:
        print(f"Error: {e}")
        
    finally:
        # Close cursor and connection
        if 'conn' in locals() and conn.is_connected():
            cursor.close()
            conn.close()
            print("MySQL connection is closed")

# Example usage
filename = 'output.txt'
with open(filename, 'r') as file:
    output = file.read().strip()

passed, failed, skipped = extract_counts_from_output(output)

if passed is not None and failed is not None and skipped is not None:
    insert_into_mysql(passed, failed, skipped)
