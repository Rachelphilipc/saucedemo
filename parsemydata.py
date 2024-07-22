import re

def extract_username_from_jenkins_output(filename):
    try:
        with open(filename, 'r') as file:
            jenkins_output = file.read()
            
            # Try to find the username using different patterns
            # Pattern 1: Started by user <username>
            match = re.search(r'Passed (\w+)', jenkins_output)
            if match:
                return match.group(1)
            
            # Pattern 2: Started by user <username> Obtained Jenkinsfile
            match = re.search(r'Started by user (\w+)', jenkins_output)
            if match:
                return match.group(1)
            
            # If no pattern matches
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
