import sys
import numpy as np


def main():
    chrm_list = list(range(1, 23))
    chrm_list.append("X")

    for chr_n in chrm_list:
        chrm = "chr" + str(chr_n)

        rawdata_file = "RAWdata/50kb_resolution_intrachromosomal/" + chrm + "/MAPQGE30/" + chrm + "_50kb.RAWobserved"
        norm_file = "RAWdata/50kb_resolution_intrachromosomal/" + chrm + "/MAPQGE30/" + chrm + "_50kb.KRnorm"
        bin_size = 50000
        # line_output_file = "output/50kb_resolution_intrachromosomal/line-input/" + chrm + ".output"
        # deepwalk_output_file = "output/50kb_resolution_intrachromosomal/deepwalk-input/" + chrm + ".output"
        new_tools_output_file = "output/50kb_resolution_intrachromosomal/TADW-BANE-input/" + chrm + "-output.csv"
        bin_list_file = "output/50kb_resolution_intrachromosomal/bin-list/" + chrm + "-bins.txt"

        # line_out = open(line_output_file, "w")
        # deepwalk_out = open(deepwalk_output_file, "w")

        new_tools_out = open(new_tools_output_file, "w")

        i = 1
        norm_map = {}
        with open(norm_file) as f:
            for line in f:
                norm_map[i] = line.rstrip('\n')
                i += 1

        print(i)

        count = 0
        edge_map = {}
        value_list = []

        with open(rawdata_file) as f:
            for line in f:
                splitLine = line.split()

                bin1 = int(splitLine[0])
                bin2 = int(splitLine[1])
                value = float(splitLine[2])

                index1 = int((bin1 / bin_size) + 1)
                index2 = int((bin2 / bin_size) + 1)

                new_value = "NaN"
                if norm_map[index1] != "NaN" and norm_map[index2] != "NaN":
                    new_value = value / (float(norm_map[index1]) * float(norm_map[index1]))

                if new_value != "NaN":
                    edge_map[(index1, index2)] = new_value
                    # new_tools_out.write("{},{}\n".format(index1, index2))
                    value_list.append(new_value)

        percentile_5 = np.percentile(value_list, 5)

        bin_list_out = open(bin_list_file, "w")
        bin_list = set()

        edge_list = []

        new_tools_out.write("{},{}\n".format("bin1", "bin2"))
        for key, value in edge_map.items():
            if value > percentile_5:
                bin_list.add(key[0])
                bin_list.add(key[1])

                edge_list.append((key[0], key[1]))

                # if key[0] not in bin_list:
                #     bin_list.append(key[0])
                # if key[1] not in bin_list:
                #     bin_list.append(key[1])

        bin_list = list(bin_list)
        bin_list.sort()

        bin_map = {}
        cou = 0
        for binn in bin_list:
            bin_map[binn] = cou
            cou += 1

        for ed in edge_list:
            new_tools_out.write("{},{}\n".format(bin_map[ed[0]], bin_map[ed[1]]))

        # for key, value in edge_map.items():
        #     if value > percentile_5:
        #         new_tools_out.write("{},{}\n".format(bin_list.index(key[0]), bin_list.index(key[1])))

        print(len(bin_list))

        for bi in bin_list:
            bin_list_out.write("{}\n".format(bi))

        bin_list_out.close()

        # line_out.close()
        # deepwalk_out.close()

        new_tools_out.close()


if __name__ == '__main__':
    main()
