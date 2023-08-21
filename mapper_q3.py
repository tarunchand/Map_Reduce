#!/usr/bin/env python3
import sys

for line in sys.stdin:
    try:
        columns = line.strip().split(',')
        day = columns[1]
        dew_point_temperature = int(columns[9])
        print('%s\t%s' % (day, dew_point_temperature))
    except (ValueError, OSError, IndexError, Exception):
        pass
