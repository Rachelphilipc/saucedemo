import re
import mysql.connector
from datetime import datetime

# Function to parse Jenkins console output
def parse_jenkins_console(console_output):
    data = {}
    lines = console_output.splitlines()

    # Find and extract data
    for line in lines:
        if line.startswith("Started by"):
            data['started_by'] = line.split("Started by ")[1].strip()
        elif line.startswith("Started at"):
            data['start_time'] = datetime.strptime(line.split("Started at ")[1].split('.')[0].strip(), '%Y-%m-%d %H:%M:%S')
        elif line.startswith("Finished at"):
            data['end_time'] = datetime.strptime(line.split("Finished at ")[1].split('.')[0].strip(), '%Y-%m-%d %H:%M:%S')
        elif line.startswith("Ran "):
            match = re.search(r'Ran (\d+) tests in (.*)s', line)
            if match:
                data['test_count'] = int(match.group(1))
                data['time_taken'] = float(match.group(2))
        elif line.startswith("FAILED"):
            match = re.search(r'FAILED \(errors=(\d+), skipped=(\d+)\)', line)
            if match:
                data['error_count'] = int(match.group(1))
                data['skip_count'] = int(match.group(2))

    return data

# Function to connect to MySQL and store data
def store_in_mysql(data):
    try:
        conn = mysql.connector.connect(
            host='localhost:3306',
            database='test_results_db',
            user='root',
            password='Test@1234'
        )

        cursor = conn.cursor()

        # Create table if it doesn't exist
        create_table_query = """
        CREATE TABLE IF NOT EXISTS jenkins_runs (
            id INT AUTO_INCREMENT PRIMARY KEY,
            started_by VARCHAR(255),
            start_time DATETIME,
            end_time DATETIME,
            time_taken FLOAT,
            error_count INT,
            skip_count INT
        )
        """
        cursor.execute(create_table_query)
        conn.commit()

        # Prepare SQL query to insert data into the table
        insert_query = """
        INSERT INTO jenkins_runs (started_by, start_time, end_time, time_taken, error_count, skip_count)
        VALUES (%s, %s, %s, %s, %s, %s)
        """
        values = (data['started_by'], data['start_time'], data['end_time'], data['time_taken'], data['error_count'], data['skip_count'])

        # Execute SQL query to insert data
        cursor.execute(insert_query, values)
        conn.commit()

        print("Data inserted successfully")

    except mysql.connector.Error as error:
        print(f"Error inserting data into MySQL: {error}")

    finally:
        if conn.is_connected():
            cursor.close()
            conn.close()

if __name__ == "__main__":
    # Read Jenkins output from a file (output.txt)
    with open('output.txt', 'r') as file:
        console_output = file.read()

    # Parse Jenkins console output
    parsed_data = parse_jenkins_console(console_output)

    # Store parsed data in MySQL
    store_in_mysql(parsed_data)
