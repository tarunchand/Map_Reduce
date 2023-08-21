#!/usr/bin/env python3
import sys
import math

current_month = None

# Correlations
corr_relative_humidity_wind_speed = 0
corr_relative_humidity_dry_bulb_temp = 0
corr_wind_speed_dry_bulb_temp = 0

# Variables to calculate correlations
mul_relative_humidity_wind_speed = 1
mul_relative_humidity_dry_bulb_temp = 1
mul_wind_speed_dry_bulb_temp = 1

sum_relative_humidity = 0
sum_wind_speed = 0
sum_dry_bulb_temp = 0

sum_square_relative_humidity = 0
sum_square_wind_speed = 0
sum_square_bulb_temp = 0

count = 1


def get_pearson_corr_numerator(mul_x_y, sum_x, sum_y, count):
    return mul_x_y - ((sum_x * sum_y) / count)


def get_pearson_corr_denominator(sum_x, sum_y, sum_square_x, sum_square_y, count):
    return math.sqrt((sum_square_x - ((sum_x * sum_x)/count)) * (sum_square_y - ((sum_y * sum_y)/count)))


def print_matrix(matrix, names):
    row_names = col_names = names
    rows = len(matrix)
    cols = len(matrix[0])
    max_len = max(len(str(element)) for row in matrix for element in row)
    max_row_len = max(len(str(name)) for name in row_names)
    max_col_len = max(len(str(name)) for name in col_names)
    print(" " * max_row_len, end=" ")
    for j in range(cols):
        col_name = str(col_names[j]).rjust(max_col_len)
        print(col_name, end=" ")
    print()
    for i in range(rows):
        row_name = str(row_names[i]).rjust(max_row_len)
        print(row_name, end=" ")
        for j in range(cols):
            element = str(matrix[i][j]).rjust(max_len)
            print(element, end=" ")
        print()


for line in sys.stdin:
    month, relative_humidity, wind_speed, dry_bulb_temp = line.strip().split('\t')
    relative_humidity = int(relative_humidity)
    wind_speed = int(wind_speed)
    dry_bulb_temp = int(dry_bulb_temp)
    if current_month != month:
        if current_month is not None:
            # No need to handle this scenario since the dataset contains all columns with same month
            pass
        current_month = month
        count = 1
        sum_relative_humidity = relative_humidity
        sum_wind_speed = wind_speed
        sum_dry_bulb_temp = dry_bulb_temp
        sum_square_relative_humidity = relative_humidity * relative_humidity
        sum_square_wind_speed = wind_speed * wind_speed
        sum_square_bulb_temp = dry_bulb_temp * dry_bulb_temp
        mul_relative_humidity_dry_bulb_temp = relative_humidity * dry_bulb_temp
        mul_relative_humidity_wind_speed = relative_humidity * wind_speed
        mul_wind_speed_dry_bulb_temp = wind_speed * dry_bulb_temp
    else:
        count += 1
        sum_relative_humidity += relative_humidity
        sum_wind_speed += wind_speed
        sum_dry_bulb_temp += dry_bulb_temp
        sum_square_relative_humidity += relative_humidity * relative_humidity
        sum_square_wind_speed += wind_speed * wind_speed
        sum_square_bulb_temp += dry_bulb_temp * dry_bulb_temp
        mul_relative_humidity_dry_bulb_temp += relative_humidity * dry_bulb_temp
        mul_relative_humidity_wind_speed += relative_humidity * wind_speed
        mul_wind_speed_dry_bulb_temp += wind_speed * dry_bulb_temp


corr_relative_humidity_wind_speed = get_pearson_corr_numerator(
    mul_relative_humidity_wind_speed, sum_relative_humidity, sum_wind_speed, count)/get_pearson_corr_denominator(
    sum_relative_humidity, sum_wind_speed, sum_square_relative_humidity, sum_square_wind_speed, count)

corr_wind_speed_dry_bulb_temp = get_pearson_corr_numerator(
    mul_wind_speed_dry_bulb_temp, sum_wind_speed, sum_dry_bulb_temp, count)/get_pearson_corr_denominator(
    sum_wind_speed, sum_dry_bulb_temp, sum_square_wind_speed, sum_square_bulb_temp, count)

corr_relative_humidity_dry_bulb_temp = get_pearson_corr_numerator(
    mul_relative_humidity_dry_bulb_temp, sum_relative_humidity, sum_dry_bulb_temp, count)/get_pearson_corr_denominator(
    sum_relative_humidity, sum_dry_bulb_temp, sum_square_relative_humidity, sum_square_bulb_temp, count)

pearson_corr_matrix = [
    [1, corr_relative_humidity_wind_speed, corr_relative_humidity_dry_bulb_temp],
    [corr_relative_humidity_wind_speed, 1, corr_wind_speed_dry_bulb_temp],
    [corr_relative_humidity_dry_bulb_temp, corr_wind_speed_dry_bulb_temp, 1]
]
print_matrix(pearson_corr_matrix, ['Relative Humidity', 'Wind Speed', 'Dry Bulb Temp'])
