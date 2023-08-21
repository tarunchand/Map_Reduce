#!/usr/bin/env python3
import sys

for line in sys.stdin:
    try:
        columns = line.strip().split(',')
        day = columns[1]
        wind_speed = int(columns[12])
        print('%s\t%s' % (day, wind_speed))
    except (ValueError, OSError, IndexError, Exception):
        pass
