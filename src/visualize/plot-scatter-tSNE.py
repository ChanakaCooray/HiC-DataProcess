import numpy as np
from sklearn.manifold import TSNE
import matplotlib.pyplot as plt
import sys
from collections import defaultdict


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

        label_file = "output/domain-data/chrm/50kb-bin-labels/" + chrm + "-bin-labels.txt"

        label_map = {}

        with open(label_file) as f:
            for line in f:
                splitLine = line.split()

                bin_n = int(splitLine[0])
                label = [abs(int(splitLine[1]))]
                if len(splitLine) > 2:
                    label.append(abs(int(splitLine[2])))

                if label[0] in top_domains_map:
                    label_map[bin_n] = top_domains_map[label[0]]
                elif len(label) > 1:
                    if label[1] in top_domains_map:
                        label_map[bin_n] = top_domains_map[label[1]]
                    else:
                        label_map[bin_n] = "grey"
                else:
                    label_map[bin_n] = "grey"

        # print(label_map)

        # tSNE_output = "output/100kb_resolution_intrachromosomal/line-output-128/tSNE/" + chrm + "-tSNE.txt"
        tSNE_output = "output/50kb_resolution_intrachromosomal/deepwalk-output-128/tSNE/" + chrm + "-tSNE.txt"
        # tSNE_output = "output/100kb_resolution_intrachromosomal/chr22-dim2.emb"

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
        plt.show()

        # sys.exit(0)

        plt.savefig("output/graphs-50kb-128dim/BANE/" + chrm + ".png")
        # plt.savefig("output/graphs-100kb-128dim/deepwalk/" + chrm + ".png")


if __name__ == '__main__':
    main()
