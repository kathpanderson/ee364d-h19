# to run this file in the command line type:
# python visualizing_cluster.py file_name.csv blob#
# this script will display the 3d image of the blobs at a frequency given by the user

import numpy as np
from sklearn.cluster import MeanShift
from sklearn.datasets import make_blobs
import csv
import sys, getopt
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
np.random.seed(1)
import pandas as pd


def get_file_import_data(file_name):

    clusterCenters = []
    with open(file_name, newline='') as csvfile:
        spamreader = csv.reader(csvfile, delimiter=',', quotechar='|')
        next(spamreader)
        next(spamreader)
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

            remove_commas = np.asarray(remove_commas)
            clusterCenters.append(remove_commas)
    print("finished editing incoming data")
    return clusterCenters


def create_3dgraph(clusterCenters, value):
    print("made it into create the 3d graph")
    # begin 1st function within a function #

    def update_annot(ind):  # update_annot is used to update the annotation as you hover over each cluster
        pos = sc.get_offsets()[ind["ind"][0]]
        annot.xy = pos
        text = "{}, {}, {}".format((" ".join([names[n, 0] for n in ind["ind"]])),   # display x
                                   (" ".join([names[n, 1] for n in ind["ind"]])),   # display y
                                   (" ".join([names[n, 2] for n in ind["ind"]])))   # display z
        annot.set_text(text)
        annot.get_bbox_patch().set_alpha(0.4)

    # end 1st function within a function #

    # begin 2nd function within a function #

    def hover(event):   # hover is the function that determines if the hover event occurs on the data or not
        vis = annot.get_visible()
        if event.inaxes == ax:
            cont, ind = sc.contains(event)
            if cont:    # if it occurs on the data it will go to the update_annot function and display the values
                update_annot(ind)
                annot.set_visible(True)
                fig.canvas.draw_idle()
            else:       # if it is not over data it will not display anything
                if vis:
                    annot.set_visible(False)
                    fig.canvas.draw_idle()

    # end 2nd function within a function #

    name1 = clusterCenters[value]    # this part is used to help us match the labels with the number
    name = np.round_(name1, 2)
    names = name.astype(str)
    c = np.random.randint(1, 6, size=15)

    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')

    sc = ax.scatter(clusterCenters[value][:, 0], clusterCenters[value][:, 1], clusterCenters[value][:, 2],  # scatterplot
                    marker="o", color='k', s=150, linewidths=5, zorder=10)

    plt.title(value)

    annot = ax.annotate("", xy=(0, 0), xytext=(20, 20), textcoords="offset points", # used to make the annotation
                        bbox=dict(boxstyle="round", fc="w"),
                        arrowprops=dict(arrowstyle="->"))
    annot.set_visible(False)

    fig.canvas.mpl_connect("motion_notify_event", hover)
    plt.show()


def determine_blob(clusterCenters, value):  # used to determine if the given blob number is within range

    if value > len(clusterCenters):
        print("Uh oh! This value is out of range")

    else:
        create_3dgraph(clusterCenters, value)


def main(argv):
    n = len(sys.argv)
    print("Total arguments passed:", n)
    print("\nName of Python script:", sys.argv[0])
    print("\nFilename that was sent:", sys.argv[1])
    print("\nBlob Number to analyze:", sys.argv[2])

    value = int(sys.argv[2])

    clusterCenters = get_file_import_data(sys.argv[1])
    determine_blob(clusterCenters, value)


if __name__ == "__main__":
   main(sys.argv[1:])

