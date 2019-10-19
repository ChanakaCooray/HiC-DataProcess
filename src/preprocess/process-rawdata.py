import numpy as np


def main(data):
    # chrm_list = list(range(1, 23))
    chrm_list = list(range(1, 20))
    chrm_list.append("X")

    for chr_n in chrm_list:
        chrm = "chr" + str(chr_n)

        rawdata_file = "RAWdata/" + data + "/50kb_resolution_intrachromosomal/" + chrm + "/MAPQGE30/" + chrm + "_50kb.RAWobserved"
        norm_file = "RAWdata/" + data + "/50kb_resolution_intrachromosomal/" + chrm + "/MAPQGE30/" + chrm + "_50kb.KRnorm"
        bin_size = 50000
        line_output_file = "output/" + data + "/50kb_resolution_intrachromosomal/line-input/" + chrm + ".output"
        deepwalk_output_file = "output/" + data + "/50kb_resolution_intrachromosomal/deepwalk-input/" + chrm + ".output"

        line_out = open(line_output_file, "w")
        deepwalk_out = open(deepwalk_output_file, "w")

        process_method1(rawdata_file,norm_file, bin_size, line_out, deepwalk_out)

        line_out.close()
        deepwalk_out.close()


def process_method1(rawdata_file, norm_file, bin_size, line_out, deepwalk_out):
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

            if index1 == index2 or abs(index2 - index1) > 20:
                continue

            new_value = "NaN"
            if norm_map[index1] != "NaN" and norm_map[index2] != "NaN":
                new_value = value / (float(norm_map[index1]) * float(norm_map[index1]))

            if new_value != "NaN":
                line_out.write("{} {} {}\n".format(index1, index2, new_value))
                deepwalk_out.write("{} {} {}\n".format(index1, index2, new_value))
                if index1 != index2:
                    line_out.write("{} {} {}\n".format(index2, index1, new_value))


def process_method2(rawdata_file, norm_file, bin_size, line_out, deepwalk_out):

    values = []

    with open(rawdata_file) as f:
        for line in f:
            splitLine = line.split()
            bin1 = int(splitLine[0])
            bin2 = int(splitLine[1])

            index1 = int((bin1 / bin_size) + 1)
            index2 = int((bin2 / bin_size) + 1)

            if index1 == index2:
                continue

            value = float(splitLine[2])
            values.append(value)

    values = np.array(values)
    median = np.median(values)
    mean = np.mean(values)

    print("Median: " + str(median))
    print("Mean: " + str(mean))

    count = 0
    count_output = 0
    with open(rawdata_file) as f:
        for line in f:
            splitLine = line.split()

            bin1 = int(splitLine[0])
            bin2 = int(splitLine[1])
            new_value = float(splitLine[2])

            index1 = int((bin1 / bin_size) + 1)
            index2 = int((bin2 / bin_size) + 1)

            if index1 == index2:
                continue

            count += 1

            if new_value > median:
                count_output += 1
                line_out.write("{} {} {}\n".format(index1, index2, new_value))
                deepwalk_out.write("{} {} {}\n".format(index1, index2, new_value))
                if index1 != index2:
                    line_out.write("{} {} {}\n".format(index2, index1, new_value))

    print(count)
    print(count_output)


if __name__ == '__main__':
    main("CH12-LX")
