import sys


def main():
    chrm_list = list(range(1, 23))
    chrm_list.append("X")

    for chr_n in chrm_list:
        chrm = "chr" + str(chr_n)

        rawdata_file = "RAWdata/10kb_resolution_intrachromosomal/" + chrm + "/MAPQGE30/" + chrm + "_10kb.RAWobserved"
        norm_file = "RAWdata/10kb_resolution_intrachromosomal/" + chrm + "/MAPQGE30/" + chrm + "_10kb.KRnorm"
        bin_size = 10000
        line_output_file = "output/10kb_resolution_intrachromosomal/line-input/" + chrm + ".output"
        deepwalk_output_file = "output/10kb_resolution_intrachromosomal/deepwalk-input/" + chrm + ".output"

        line_out = open(line_output_file, "w")
        deepwalk_out = open(deepwalk_output_file, "w")

        i = 1
        norm_map = {}
        with open(norm_file) as f:
            for line in f:
                norm_map[i] = line.rstrip('\n')
                i += 1

        print(i)

        count = 0
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
                    line_out.write("{} {} {}\n".format(index1, index2, new_value))
                    deepwalk_out.write("{} {} {}\n".format(index1, index2, new_value))
                    if index1 != index2:
                        line_out.write("{} {} {}\n".format(index2, index1, new_value))

        line_out.close()
        deepwalk_out.close()


if __name__ == '__main__':
    main()
