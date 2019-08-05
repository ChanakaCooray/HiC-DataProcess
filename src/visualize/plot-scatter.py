import numpy as np
from sklearn.manifold import TSNE
import matplotlib.pyplot as plt
import sys


def main():
    chrm_list = list(range(1, 23))
    chrm_list.append("X")

    for chr_n in chrm_list:
        chrm = "chr" + str(chr_n)

        top_domains_file = "output/domain-data/chrm/top-domains/" + chrm + "-topdomains.txt"

        top_domains_map = {}
        color_list = ["blue", "red", "green", "yellow", "orange"]

        i = 0
        with open(top_domains_file) as f:
            for line in f:
                top_domains_map[(int(line.rstrip('\n')))] = color_list[i]
                i += 1

        # print(top_domains_map)

        label_file = "output/domain-data/chrm/10kb-bin-labels/" + chrm + "-bin-labels.txt"

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

        # tSNE_output = "output/10kb_resolution_intrachromosomal/line-output-128/tSNE/" + chrm + "-tSNE.txt"
        tSNE_output = "output/10kb_resolution_intrachromosomal/deepwalk-output-128/tSNE/" + chrm + "-tSNE.txt"

        X = []
        Y = []
        col = []

        with open(tSNE_output) as f:
            for line in f:
                splitLine = line.split()

                X.append(float(splitLine[1]))
                Y.append(float(splitLine[2]))

                col.append(label_map[int(splitLine[0])])

        plt.figure(figsize=(20, 12))
        plt.scatter(X, Y, color=col)
        # plt.show()

        # plt.savefig("output/graphs-10kb-128dim/line/" + chrm + ".png")
        plt.savefig("output/graphs-10kb-128dim/deepwalk/" + chrm + ".png")


if __name__ == '__main__':
    main()
