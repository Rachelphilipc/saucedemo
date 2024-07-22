import re
from datetime import datetime

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
            match = re.search(r'FAILED \(errors=(\d+)', line)
            if match:
                data['error_count'] = int(match.group(1))
        elif line.startswith("skipped"):
            match = re.search(r'skipped=(\d+)', line)
            if match:
                data['skip_count'] = int(match.group(1))

    return data
