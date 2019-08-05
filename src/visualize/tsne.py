import numpy as np
from sklearn.manifold import TSNE
import matplotlib.pyplot as plt
import sys


def main():
    # file = "output/10kb_resolution_intrachromosomal/chr1/deepwalk.embeddings"
    file = "output/10kb_resolution_intrachromosomal/chr1/line.emb"

    # tSNE_output = "output/10kb_resolution_intrachromosomal/chr1/tSNE/deepwalk-tSNE.txt"
    tSNE_output = "output/10kb_resolution_intrachromosomal/chr1/tSNE/line-tSNE.txt"
    out = open(tSNE_output, "w")


    bin_list = []

    with open(file) as f:
        first_line = f.readline()
        splitLine = first_line.split()
        np_data = np.zeros(shape=(int(splitLine[0]), int(splitLine[1])))
        index = 0
        for line in f:
            splitLine = line.split()
            bin_list.append(int(splitLine[0]))

            for i in range(1,len(splitLine)):
                np_data[index][i-1] = float(splitLine[i])


    # X = np.array([[0, 0, 0], [0, 1, 1], [1, 0, 1], [1, 1, 1]])
    X_embedded = TSNE(n_components=2).fit_transform(np_data)

    rows = X_embedded.shape[0]
    cols = X_embedded.shape[1]

    # print(X_embedded)

    for x in range(0, rows):
        out.write("{}".format(bin_list[x]))
        for y in range(0, cols):
            out.write(" {}".format(X_embedded[x,y]))
        out.write("\n")

    out.close()

    print(X_embedded.shape)
    print("\n")
    # print(X_embedded)

    # plt.scatter(X_embedded[:, 0], X_embedded[:, 1])
    # plt.show()


if __name__ == '__main__':
    main()
