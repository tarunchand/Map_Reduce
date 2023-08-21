import sys
import numpy as np
from prettytable import PrettyTable


def get_average_distance(file_name):
    with open(file_name, 'r') as f:
        lines = f.readlines()
    # Omitting the first two lines since first line consists of Input Path and second line consists of Key class
    lines = lines[2:-1]
    distances = []
    for line in lines:
        parts = line.strip().split()
        distance = float(parts[6])
        distances.append(distance)
    return np.sum(np.array(distances))/len(distances)


def plot_table(index):
    # Variables
    distances = ['CosineDistanceMeasure', 'EuclideanDistanceMeasure', 'ManhattanDistanceMeasure']
    distance_measure = distances[index - 1]
    k_s = range(1, 21)
    average_distance_to_centroids = []
    for k in k_s:
        points_dump_file = f"{distance_measure}-k{k}-points.txt"
        average_distance_to_centroids.append(get_average_distance(points_dump_file))

    # Print Values
    print('\nTable for : ', distance_measure)
    table = PrettyTable(['K-Value', 'Avg Distance To Centroids'])
    index = 0
    for k in k_s:
        table.add_row([k, average_distance_to_centroids[index]])
        index += 1
    print(table)


def main():
    plot_type = input('[?] Select distance measure - Cosine(1), Euclidean(2), Manhattan(3) : ')
    try:
        plot_type = int(plot_type)
        if plot_type == 1:
            plot_table(1)
        elif plot_type == 2:
            plot_table(2)
        elif plot_type == 3:
            plot_table(3)
        else:
            print('[!] Invalid Option.')
            sys.exit(1)
    except ValueError:
        print('[!] Invalid Input.')
        sys.exit(1)
    except (OSError, KeyboardInterrupt, Exception):
        print('[!] An Error Occurred')
        sys.exit(1)


if __name__ == '__main__':
    main()
