import sys
import statistics
import matplotlib.pyplot as plt
import numpy as np
from operator import itemgetter
import os
from collections import defaultdict


def main():
    domain_file = "metadata/GSE63525_GM12878_primary+replicate_Arrowhead_domainlist.txt"

    output_dir = "output/domain-data/chrm/original"
    output_dir_merged = "output/domain-data/chrm/merged"
    output_dir_mapped = "output/domain-data/chrm/mapped"

    # list_range = []

    domain_map = defaultdict(list)

    with open(domain_file) as f:
        next(f)
        for line in f:
            splitLine = line.split()

            chrm = splitLine[0]
            domain_start = int(splitLine[1])
            domain_end = int(splitLine[2])

            domain_map[chrm].append((domain_start, domain_end))

            # list_range.append(domain_end1 - domain_start1)

    for key, value in domain_map.items():
        value.sort(key=itemgetter(1))

        out = open(os.path.join(output_dir, "chr" + key + "-domainlist.txt"), "w")
        out2 = open(os.path.join(output_dir_merged, "chr" + key + "-domainlist-merged.txt"), "w")
        out3 = open(os.path.join(output_dir_mapped, "chr" + key + "-domainlist-mapped.txt"), "w")

        length = int(value[-1][1] / 2500) + 2
        chrm_domain_list = [0] * length

        for val in value:
            start = int(val[0] / 2500)
            end = int(val[1] / 2500)

            for idx in range(start, end + 1):
                chrm_domain_list[idx] = 1

        prev = 0
        j = 0
        k = 1
        start_range = 0

        domain_map_internal = {}

        for idx in chrm_domain_list:
            if prev == 0 and idx == 1:
                start_range = j * 2500
            if prev == 1 and idx == 0:
                end_range = (j - 1) * 2500
                out2.write("{} {} {}\n".format(k, start_range, end_range))
                domain_map_internal[k] = (start_range, end_range)
                k += 1
            prev = idx
            j += 1

        i = 1
        domain_merge_map = defaultdict(list)
        # prev_value = 0
        for val in value:
            for k2, v2 in domain_map_internal.items():
                if v2[0] <= val[0] <= v2[1] and v2[0] <= val[1] <= v2[1]:
                    domain_merge_map[k2].append(i)

            out.write("{} {} {}\n".format(i, val[0], val[1]))
            # if val[0] % 5000 != 0 or val[1] % 5000 != 0:
            #     print("{} {} {}".format(key, val[0], val[1]))
            # prev_value = val[1]
            i += 1

        calculate_top_merged_domains(key, domain_merge_map, domain_map_internal)

        count_val = 0
        cnt = 0
        for k1, v1 in domain_merge_map.items():
            cnt += 1
            count_val += len(v1)
            out3.write("{}".format(k1))
            for t in v1:
                out3.write(" {}".format(t))
            out3.write("\n")

        # print(count_val)
        out.close()
        out2.close()
        out3.close()

    # print(max(list_range))
    # print(min(list_range))
    # print(statistics.median(list_range))
    #
    # plt.hist(list_range,bins=100)
    # plt.show()


def calculate_top_nonmerged_domains(chr, domain_merge_map, domain_map_internal):
    domain_range_list = []

    for key, value in domain_map_internal.items():
        domain_range_list.append((key, value[1] - value[0]))

    domain_range_list.sort(key=itemgetter(1), reverse=True)

    top_domain_list = []

    for domain in domain_range_list:
        if len(domain_merge_map[domain[0]]) == 1:
            top_domain_list.append(domain[0])
            if len(top_domain_list) == 5:
                break

    top_domain_file = "output/domain-data/chrm/top-domains/chr" + chr + "-topdomains.txt"
    out = open(top_domain_file, "w")

    for i in top_domain_list:
        out.write("{}\n".format(i))

    out.close()

def calculate_top_merged_domains(chr, domain_merge_map, domain_map_internal):
        domain_range_list = []

        for key, value in domain_map_internal.items():
            domain_range_list.append((key, value[1] - value[0]))

        domain_range_list.sort(key=itemgetter(1), reverse=True)

        top_domain_list = []

        for domain in domain_range_list:
            top_domain_list.append(domain[0])
            if len(top_domain_list) == 5:
                break

        top_domain_file = "output/domain-data/chrm/top-domains/chr" + chr + "-topdomains.txt"
        out = open(top_domain_file, "w")

        for i in top_domain_list:
            out.write("{}\n".format(i))

        out.close()

    # sys.exit(0)


if __name__ == '__main__':
    main()
