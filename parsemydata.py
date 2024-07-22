import re

# Function to extract username from Jenkins output
def extract_username_from_jenkins_output(filename):
    try:
        with open(filename, 'r') as file:
            jenkins_output = file.read()
            # Use regular expression to find username
            match = re.search(r'Started by user (\w+)', jenkins_output)
            if match:
                username = match.group(1)
                return username
            else:
                print("Username not found in Jenkins output.")
                return None
    except FileNotFoundError:
        print(f"Error: File '{filename}' not found.")
        return None

# Example usage
filename = 'output.txt'
username = extract_username_from_jenkins_output(filename)
if username:
    print(f"The username is: {username}")
