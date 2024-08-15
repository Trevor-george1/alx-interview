#!/usr/bin/python3
"""Write a script that reads stdin line by line and computes metrics"""

import re
import sys




"""def parse_line(line):
    match = re.match(r'(\d+\.\d+.\d+) (\S+) \[.*?\] "(GET \/projects\/\d+ HTTPS\/1\.1)" (\d+) (\d+)', line) # Noqa
    if match:
        _, _, _, status_code, file_size = match.groups()
        return int(file_size)
    return None
"""


def print_stats(file_size, status):

    print(f"File size: {file_size}")

    for key, value in sorted(status.items()):
        if value != 0:
            print("{}: {}".format(key, value))


possible_status = {'200': 0, '301': 0, '400': 0, '401': 0, '403': 0,
                   '404': 0, '405': 0, '500': 0}

total_file_size = 0
count = 0


try:
    for line in sys.stdin:
        args = line.split()

        status_code = int(args[-2])
        file_size = int(args[-1])

        if status_code in possible_status:
            possible_status[status_code] += 1

        total_file_size += file_size
        count += 1

        if count == 10:
            print_stats(total_file_size, possible_status)
            count = 0
    print_stats(total_file_size, possible_status)

except KeyboardInterrupt:
    raise

finally:
    print_stats(total_file_size, possible_status)
