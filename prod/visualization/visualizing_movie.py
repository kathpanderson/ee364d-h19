# to run this code in the command line type:
# python visualizing_movie.py data_file_name.csv movie_name.mp4
# this will produce a movie that iterates through all the blobs 

import matplotlib.animation as animation
import numpy as np
import matplotlib
import matplotlib.pyplot as plt
from matplotlib import cm
from matplotlib.colors import BoundaryNorm
from matplotlib.colors import ListedColormap, LinearSegmentedColormap
import math
import sys, getopt
from numpy.random import seed
from numpy.random import rand
from matplotlib.ticker import MaxNLocator
from matplotlib import animation
import csv
seed(1)


def format_data(file_name):
    clusterCenters = []
    with open(file_name, newline='') as csvfile:
        min_x = min_y = max_x = max_y = 0
        spamreader = csv.reader(csvfile, delimiter=',', quotechar='|')
        next(spamreader)
        minima = float(next(spamreader)[0])
        for row in spamreader:
            remove_commas = []
            for i in range(0, len(row)):
                if row[i]:
                    remove_commas.append(row[i].split())
                    length = len(row[i].split())
                    if length == 3:
                        remove_commas[i][0] = remove_commas[i][0].replace('[', '')
                        remove_commas[i][2] = remove_commas[i][2].replace(']', '')

                    if len(remove_commas[i]) == 4 and remove_commas[i][3] == ']':
                        remove_commas[i][0] = remove_commas[i][0].replace('[', '')
                        remove_commas[i].pop()

                    if len(remove_commas[i]) == 4 and remove_commas[i][0] == '[':
                        remove_commas[i].pop(0)
                        remove_commas[i][2] = remove_commas[i][2].replace(']', '')

                    if len(remove_commas[i]) == 5:
                        remove_commas[i].pop(0)
                        remove_commas[i].pop(3)

                    for l in range(0, 3):
                        remove_commas[i][l] = float(remove_commas[i][l])
                else:
                    break

                if remove_commas[i][0] < min_x:
                    min_x = remove_commas[i][0]

                if remove_commas[i][1] < min_y:
                    min_y = remove_commas[i][1]

                if remove_commas[i][0] > max_x:
                    max_x = remove_commas[i][0]

                if remove_commas[i][1] > max_y:
                    max_y = remove_commas[i][1]

            remove_commas = np.asarray(remove_commas)
            clusterCenters.append(remove_commas)

    return clusterCenters, minima, min_x, min_y, max_x, max_y


def create_animated_graph(clusterCenters, minima, min_x, min_y, max_x, max_y, movie_name):

    # begin function within a function #
    def animate(i):
        ax.clear()
        ax.scatter(clusterCenters[i][:, 0], clusterCenters[i][:, 1], c=mapper.to_rgba(clusterCenters[i][:, 2]))
        ax.set(xlim=(min_x, max_x), ylim=(min_y, max_y))
        plt.title(i)
        return

    # end function within a function #

    maxima = 0
    norm = matplotlib.colors.Normalize(vmin=minima, vmax=maxima, clip=True)
    mapper = cm.ScalarMappable(norm=norm, cmap='seismic')

    Writer = animation.writers['ffmpeg']
    writer = Writer(fps=5, metadata=dict(artist='Me'), bitrate=1800)
    filename = movie_name

    fig, ax = plt.subplots()
    plt.colorbar(mapper)

    anim = animation.FuncAnimation(fig, animate, interval=100, frames=(len(clusterCenters)), repeat=False)

    plt.show()
    anim.save(filename, writer=writer)


def main(argv):

    clusterCenters, minima, min_x, min_y, max_x, max_y = format_data(sys.argv[1])
    create_animated_graph(clusterCenters, minima, min_x, min_y, max_x, max_y, sys.argv[2])


if __name__ == "__main__":
   main(sys.argv[1:])
