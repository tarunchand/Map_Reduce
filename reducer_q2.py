#!/usr/bin/env python3
import sys

current_day = None
min_relative_humidity = None

for line in sys.stdin:
    day, relative_humidity = line.strip().split('\t')
    relative_humidity = int(relative_humidity)
    if current_day != day:
        if current_day is not None:
            print('%s\t%s' % (current_day, min_relative_humidity))
        current_day = day
        min_relative_humidity = relative_humidity
    else:
        min_relative_humidity = min(min_relative_humidity, relative_humidity)

if current_day is not None:
    print('%s\t%s' % (current_day, min_relative_humidity))
