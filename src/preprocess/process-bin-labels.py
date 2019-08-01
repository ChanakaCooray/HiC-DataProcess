import sys
import statistics
import matplotlib.pyplot as plt
import numpy as np
from operator import itemgetter
import os
from collections import defaultdict


def main():
    bin_size = 10000
    num_bins = 24950
    chrm = "chr1"

    domain_file = "output/domain-data/chrm/merged/" + chrm + "-domainlist-merged.txt"

    output_file = "output/domain-data/chrm/10kb-bin-labels/" + chrm + "-bin-labels.txt"

    out = open(output_file, "w")

    domain_map = {}

    with open(domain_file) as f:
        for line in f:
            splitLine = line.split()

            domain_index = int(splitLine[0])
            domain_start = int(splitLine[1])
            domain_end = int(splitLine[2])

            domain_map[domain_index] = (domain_start, domain_end)

    for i in range(0, num_bins):
        start_bin_index = i * bin_size
        end_bin_index = start_bin_index + 10000
        label = 0
        for key, value in domain_map.items():
            if value[0] <= start_bin_index <= value[1] and value[0] <= end_bin_index <= value[1]:
                label = key
                break
            elif value[0] < start_bin_index < value[1] or value[0] < end_bin_index < value[1]:
                label = key*(-1)
                break

        out.write("{} {}\n".format(i+1, label))
    out.close()


if __name__ == '__main__':
    main()
