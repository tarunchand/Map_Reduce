#!/usr/bin/env python3
import sys

for line in sys.stdin:
    try:
        columns = line.strip().split(',')
        day = columns[1]
        relative_humidity = int(columns[11])
        print('%s\t%s' % (day, relative_humidity))
    except (ValueError, OSError, IndexError, Exception):
        pass
