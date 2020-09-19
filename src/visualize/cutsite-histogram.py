import statistics

import matplotlib.pyplot as plt


def histogram():
    filepath = "hESC-r1-1-uni"
    input_file = "/Users/bcchanaka/PycharmProjects/HiC-DataProcess/mHiC-data/bowtie/" + filepath

    count_1000 = 0

    distance_list = []
    with open(input_file) as f:
        for line in f:
            dist = int(line)
            # distance_list.append(int(line))
            if dist > 10000:
                count_1000 = count_1000 + 1
            else:
                distance_list.append(int(line))

    print(len(distance_list))
    print(count_1000)

    plt.hist(distance_list, bins=20)
    plt.ylabel('Count')
    plt.xlabel('Distance')
    # plt.show()
    plt.savefig("/Users/bcchanaka/PycharmProjects/HiC-DataProcess/mHiC-data/bowtie/" + filepath + "-10000.png")


def calc_stats():
    # filepath = "IMR90_r1.uni.2"
    filepath = "hESC_r2_2_uni"
    # input_file = "/Users/bcchanaka/PycharmProjects/HiC-DataProcess/mHiC-data/our-approach/" + filepath
    input_file = "/Users/bcchanaka/PycharmProjects/HiC-DataProcess/mHiC-data/bowtie/" + filepath

    distance_list = []
    with open(input_file) as f:
        for line in f:
            distance_list.append(int(line))

    print(filepath)
    print("Min: {}".format(min(distance_list)))
    print("Max: {}".format(max(distance_list)))
    print("Average: {}".format(statistics.mean(distance_list)))
    print("Median: {}".format(statistics.median(distance_list)))


if __name__ == '__main__':
    calc_stats()
    # histogram()
