import sys
import statistics
import matplotlib.pyplot as plt
import numpy as np
from operator import itemgetter
import os
from collections import defaultdict


def main():
    bin_size = 100000
    # num_bins = 24950

    chrm_list = list(range(1, 23))
    chrm_list.append("X")

    print(chrm_list)

    for chr_n in chrm_list:
        chrm = "chr" + str(chr_n)

        KRNorm_file = "RAWdata/100kb_resolution_intrachromosomal/" + chrm + "/MAPQGE30/" + chrm + "_100kb.KRnorm"

        num_bins = sum(1 for line in open(KRNorm_file))

        domain_file = "output/domain-data/chrm/merged/" + chrm + "-domainlist-merged.txt"

        output_file = "output/domain-data/chrm/100kb-bin-labels/" + chrm + "-bin-labels.txt"

        out = open(output_file, "w")

        domain_map = {}

        with open(domain_file) as f:
            for line in f:
                splitLine = line.split()

                domain_index = int(splitLine[0])
                domain_start = int(splitLine[1])
                domain_end = int(splitLine[2])

                domain_map[domain_index] = (domain_start, domain_end)
        print(len(domain_map))
        co = 0
        for i in range(0, num_bins):
            start_bin_index = i * bin_size
            end_bin_index = start_bin_index + bin_size
            label = []
            co = 0
            for key, value in domain_map.items():

                if (value[1] - value[0]) < 100000:
                    continue
                else:
                    co += 1

                if value[0] <= start_bin_index <= value[1] and value[0] <= end_bin_index <= value[1]:
                    label.append(key)
                    # break
                elif value[0] < start_bin_index < value[1] or value[0] < end_bin_index < value[1]:
                    # label = key * (-1)
                    label.append(key)
                    # break

            if len(label) == 0:
                out.write("{} {}\n".format(i + 1, 0))
            else:
                out.write("{}".format(i + 1))
                for j in label:
                    out.write(" {}".format(j))
                out.write("\n")

        print(str(chr_n) + ": " + str(co))
        out.close()


if __name__ == '__main__':
    main()
