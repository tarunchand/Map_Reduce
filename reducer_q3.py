#!/usr/bin/env python3
import sys

'''
    Variance is calculated using this another formula => σ² = ((Σ x²) / N) - μ²
    x is the observation
    N is the total observations count
    μ is the Mean
'''

total_sum = 0
total_sum_square = 0
count = 1
current_day = None

for line in sys.stdin:
    day, dew_point_temperature = line.strip().split('\t')
    dew_point_temperature = int(dew_point_temperature)
    if current_day != day:
        if current_day is not None:
            mean = total_sum / count
            variance = (total_sum_square / count) - (mean * mean)
            print(f"{day}\t{mean}\t{variance}")
        current_day = day
        total_sum = dew_point_temperature
        total_sum_square = (dew_point_temperature * dew_point_temperature)
        count = 1
    else:
        total_sum += dew_point_temperature
        total_sum_square += (dew_point_temperature * dew_point_temperature)
        count += 1

if current_day is not None:
    mean = total_sum / count
    variance = (total_sum_square / count) - (mean * mean)
    print(f"{current_day}\t{mean}\t{variance}")