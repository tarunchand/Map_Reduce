#!/usr/bin/env python3
import sys

for line in sys.stdin:
    try:
        columns = line.strip().split(',')
        date = columns[1]
        month = date[4:6]
        relative_humidity = int(columns[11])
        wind_speed = int(columns[12])
        dry_bulb_temp = int(columns[8])
        print('%s\t%s\t%s\t%s' % (month, relative_humidity, wind_speed, dry_bulb_temp))
    except (ValueError, OSError, IndexError, Exception):
        pass
