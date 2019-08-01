import sys


def main():
    rawdata_file = "RAWdata/10kb_resolution_intrachromosomal/chr1/MAPQGE30/chr1_10kb.RAWobserved"
    norm_file = "RAWdata/10kb_resolution_intrachromosomal/chr1/MAPQGE30/chr1_10kb.KRnorm"
    bin_size = 10000
    output_file = "output/10kb_resolution_intrachromosomal/chr1/chr1_10kb.line_output"

    out = open(output_file, "w")

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
                out.write("{} {} {}\n".format(index1, index2, new_value))
                if index1 != index2:
                    out.write("{} {} {}\n".format(index2, index1, new_value))

    out.close()


if __name__ == '__main__':
    main()
