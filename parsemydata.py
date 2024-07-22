def parse_jenkins_output(output_file):
    with open(output_file, 'r') as file:
        lines = file.readlines()
        # Example parsing logic
        for line in lines:
            if 'Error' in line:
                # Example: Print or handle error information
                print("Error found:", line.strip())

# Call the parsing function with the Jenkins-generated output file
parse_jenkins_output('output.txt')
