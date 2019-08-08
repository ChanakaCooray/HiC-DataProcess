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

        label_file = "output/domain-data/chrm/100kb-bin-labels/" + chrm + "-bin-labels.txt"

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

        tSNE_output_1 = "output/100kb_resolution_intrachromosomal/deepwalk-output-128/tSNE/" + chrm + "-tSNE.txt"
        tSNE_output_2 = "output/100kb_resolution_intrachromosomal/line-output-128/tSNE/" + chrm + "-tSNE.txt"

        X1 = []
        Y1 = []
        col1 = []

        with open(tSNE_output_1) as f:
            next(f)
            for line in f:
                splitLine = line.split()

                X1.append(float(splitLine[1]))
                Y1.append(float(splitLine[2]))

                col1.append(label_map[int(splitLine[0])])

        X2 = []
        Y2 = []
        col2 = []

        with open(tSNE_output_2) as f:
            # next(f)
            for line in f:
                splitLine = line.split()

                X2.append(float(splitLine[1]))
                Y2.append(float(splitLine[2]))

                col2.append(label_map[int(splitLine[0])])

        fig = plt.figure(figsize=(20, 6))
        sub1 = fig.add_subplot(121)
        sub1.set_title('Deepwalk\'s Embeddings')
        sub1.set_xlabel('First Dimension of tSNE')
        sub1.set_ylabel('Second Dimension of tSNE')
        sub1.scatter(X1, Y1,color=col1,s=10)
        sub2 = fig.add_subplot(122)
        sub2.set_title('LINE\'s Embeddings')
        sub2.set_xlabel('First Dimension of tSNE')
        sub2.set_ylabel('Second Dimension of tSNE')
        sub2.scatter(X2, Y2,color=col2,s=10)
        plt.tight_layout()
        # plt.show()

        # plt.scatter(X1, Y1, color=col1)
        # plt.show()

        plt.savefig("output/graphs-100kb-128dim/" + chrm + ".png")


if __name__ == '__main__':
    main()
