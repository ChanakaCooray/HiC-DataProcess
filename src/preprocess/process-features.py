import sys
import numpy as np
import pandas as pd


def main():
    chrm_list = list(range(1, 23))
    chrm_list.append("X")

    for chr_n in chrm_list:
        chrm = "chr" + str(chr_n)

        domain_list_file = "output/domain-data/chrm/50kb-bin-labels/domain-list/" + chrm + "-domains.txt"
        bin_labels_file = "output/domain-data/chrm/50kb-bin-labels/" + chrm + "-bin-labels.txt"

        feature_out_file = "output/50kb_resolution_intrachromosomal/features/" + chrm + "-features.csv"

        KRNorm_file = "RAWdata/50kb_resolution_intrachromosomal/" + chrm + "/MAPQGE30/" + chrm + "_50kb.KRnorm"

        bin_list_file = "output/50kb_resolution_intrachromosomal/bin-list/" + chrm + "-bins.txt"

        bin_list = []
        with open(bin_list_file) as f:
            for line in f:
                bin_list.append(int(line.rstrip('\n')))

        num_bins = sum(1 for line in open(KRNorm_file))
        num_domains = sum(1 for line in open(domain_list_file))

        print(num_domains)
        print(num_bins)
        print(len(bin_list))

        features_matrix = np.zeros((num_bins, num_domains), dtype=np.int)

        print(features_matrix.shape)

        feature_out = open(feature_out_file, "w")

        with open(bin_labels_file) as f:
            for line in f:
                splitLine = line.split()

                bin_n = int(splitLine[0])
                label = abs(int(splitLine[1]))

                features_matrix[bin_n - 1, label - 1] = 1

                if len(splitLine) > 2:
                    label2 = abs(int(splitLine[2]))
                    features_matrix[bin_n - 1, label2 - 1] = 1

        feature_out.write("id")
        for x in range(0, num_domains):
            feature_out.write(",x_{}".format(x + 1))
        feature_out.write("\n")

        for y in range(0, num_bins):
            if (y+1) not in bin_list:
                continue
            feature_out.write("{}".format(bin_list.index(y + 1)))
            for z in range(0, num_domains):
                feature_out.write(",{}".format(features_matrix[y, z]))
            feature_out.write("\n")

        feature_out.close()


if __name__ == '__main__':
    main()
