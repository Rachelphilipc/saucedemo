def extract_counts_from_file(filename):
    try:
        with open(filename, 'r') as file:
            output = file.read().strip()  # Read the file and strip any leading/trailing whitespace
            
            # Split the output string by commas and spaces
            counts = output.split(', ')
            
            # Extract numbers from each part
            passed = counts[0].split()[1]  # "passed 1" -> split by space and take the second part
            failed = counts[1].split()[1]  # "failed 4" -> split by space and take the second part
            skipped = counts[2].split()[1]  # "skipped 1" -> split by space and take the second part
            
            return passed, failed, skipped
        
    except FileNotFoundError:
        print(f"Error: File '{filename}' not found.")
        return None, None, None
    except IndexError:
        print(f"Error: Unexpected format in '{filename}'.")
        return None, None, None

# Example usage
filename = 'output.txt'
passed, failed, skipped = extract_counts_from_file(filename)

if passed is not None and failed is not None and skipped is not None:
    print(f"Passed: {passed}")
    print(f"Failed: {failed}")
    print(f"Skipped: {skipped}")
