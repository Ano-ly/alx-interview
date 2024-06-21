#!/usr/bin/env python3
"""Log parsing"""
import re
import sys


counter = 0
file_size = 0
stats_list = []
regex = r'^([0-9]{1,3}\.){3}[0-9]{1,3} - \[[^\]]*\] "GET \/projects\/260 HTTP\/1\.1" [0-9]{3} [0-9]+$'


def print_vals(file_size, stats_list):
    """Print logs"""

    tup_val = (200, 301, 400, 401, 403, 404, 405, 500)
    print("File size: {}".format(file_size))
    stats_list = [item for item in stats_list if type(item) is int]
    stats_list.sort()
    travs = []
    for stat in stats_list:
        if stat in tup_val and stat not in travs:
            print("{}: {}".format(stat, stats_list.count(stat)))
            travs.append(stat)


try:
    for line in sys.stdin:
        if counter == 10:
            counter = 0
            print_vals(file_size, stats_list)
            file_size = 0
            stats_list = []
        line = line.rstrip()
        counter += 1
        if re.fullmatch(regex, line):
            divs = line.split()
            file_size += int(divs[8])
            stats_list.append(int(divs[7]))

except KeyboardInterrupt:
    print_vals(file_size, stats_list)
