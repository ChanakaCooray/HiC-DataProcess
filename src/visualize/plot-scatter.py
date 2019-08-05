import numpy as np
from sklearn.manifold import TSNE
import matplotlib.pyplot as plt
import sys


def main():
    top_domains_file = "output/domain-data/chrm/top-domains/chr1-topdomains.txt"

    top_domains_map = {}
    color_list = ["blue", "red", "green", "yellow", "orange"]

    i = 0
    with open(top_domains_file) as f:
        for line in f:
            top_domains_map[(int(line.rstrip('\n')))] = color_list[i]
            i += 1

    # print(top_domains_map)

    label_file = "output/domain-data/chrm/10kb-bin-labels/chr1-bin-labels.txt"

    label_map = {}

    with open(label_file) as f:
        for line in f:
            splitLine = line.split()

            bin = int(splitLine[0])
            label = abs(int(splitLine[1]))

            if label in top_domains_map:
                label_map[bin] = top_domains_map[label]
            else:
                label_map[bin] = "grey"

    # print(label_map)

    # tSNE_output = "output/10kb_resolution_intrachromosomal/chr1/tSNE/deepwalk-tSNE.txt"
    tSNE_output = "output/10kb_resolution_intrachromosomal/chr1/tSNE/line-tSNE.txt"

    X = []
    Y = []
    col = []

    with open(tSNE_output) as f:
        for line in f:
            splitLine = line.split()

            X.append(float(splitLine[1]))
            Y.append(float(splitLine[2]))

            col.append(label_map[int(splitLine[0])])

    plt.scatter(X, Y, color=col)
    plt.show()


if __name__ == '__main__':
    main()
