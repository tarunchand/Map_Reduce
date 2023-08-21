#!/usr/bin/env python3
import sys

wind_speeds = {}

for line in sys.stdin:
    day, wind_speed = line.strip().split('\t')
    wind_speed = int(wind_speed)
    if day not in wind_speeds:
        wind_speeds[day] = dict()
        wind_speeds[day]['min'] = wind_speed
        wind_speeds[day]['max'] = wind_speed
    else:
        wind_speeds[day]['min'] = min(wind_speed, wind_speeds[day]['min'])
        wind_speeds[day]['max'] = max(wind_speed, wind_speeds[day]['max'])

for day, speeds in wind_speeds.items():
    diff = speeds['max'] - speeds['min']
    print('Date : {} , MaxMinWindSpeedDifference : {}'.format(day, diff))
