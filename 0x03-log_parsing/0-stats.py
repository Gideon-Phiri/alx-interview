#!/usr/bin/python3
import sys
import re
from collections import defaultdict

# Regular expression for parsing the log lines
log_regex = r'(\S+) - \[(.*?)\] "GET /projects/260 HTTP/1.1" (\d{3}) (\d+)'

# Initialize metrics
total_file_size = 0
status_code_counts = defaultdict(int)
line_count = 0

def print_metrics():
    """ Function to print the current metrics. """
    print("File size: {}".format(total_file_size))
    for code in sorted(status_code_counts.keys()):
        if status_code_counts[code] > 0:
            print("{}: {}".format(code, status_code_counts[code]))

try:
    for line in sys.stdin:
        line_count += 1
        match = re.match(log_regex, line)
        if match:
            status_code = match.group(3)
            file_size = int(match.group(4))
            
            # Update total file size
            total_file_size += file_size
            
            # Update status code count
            status_code_counts[status_code] += 1
        
        # Print metrics every 10 lines
        if line_count % 10 == 0:
            print_metrics()

except KeyboardInterrupt:
    # Handle Ctrl+C
    print_metrics()
    sys.exit(0)

# Final print after reading all lines
print_metrics()

