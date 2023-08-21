import sys
import matplotlib.pyplot as plt
import numpy as np
from scipy.signal import gaussian


def calculate_total_wcss_score(file_name):
    with open(file_name, 'r') as f:
        lines = f.readlines()
    # Omitting the first two lines since first line consists of Input Path and second line consists of Key class
    lines = lines[2:-1]
    wcss_values = []
    for line in lines:
        parts = line.strip().split()
        distance = float(parts[6])
        wcss_values.append(distance * distance)
    return np.sum(np.array(wcss_values))


def plot_elbow_graph(index):
    # Variables
    distances = ['CosineDistanceMeasure', 'EuclideanDistanceMeasure', 'ManhattanDistanceMeasure']
    distance_measure = distances[index - 1]
    k_s = range(1, 28)
    wcss_scores = []
    for k in k_s:
        points_dump_file = f"{distance_measure}-k{k}-points.txt"
        wcss_scores.append(calculate_total_wcss_score(points_dump_file))
    
    wcss_scores = np.array(wcss_scores)
    
    '''
        Smoothen the elbow graph with the help of Gaussian Smoothing
    '''
    # Define the width of the Gaussian kernel
    kernel_width = 5

    # Define the Gaussian kernel
    kernel = gaussian(kernel_width, kernel_width/3)
    
    # Convolve the WCSS vector with the Gaussian kernel
    smoothed_wcss = np.convolve(wcss_scores, kernel, mode='same') / sum(kernel)

    # Plot Graph
    k = np.arange(1, len(wcss_scores) + 1)
    fig, ax = plt.subplots()
    ax.plot(k, smoothed_wcss, 'bx-')
    ax.set_xticks(k)
    ax.set_xlabel('K')
    ax.set_ylabel('WCSS')
    ax.set_title('Elbow Graph for {}.'.format(distance_measure))
    plt.show()


def main():
    plot_type = input('[?] Select distance measure - Cosine(1), Euclidean(2), Manhattan(3) : ')
    try:
        plot_type = int(plot_type)
        if plot_type == 1:
            plot_elbow_graph(1)
        elif plot_type == 2:
            plot_elbow_graph(2)
        elif plot_type == 3:
            plot_elbow_graph(3)
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
