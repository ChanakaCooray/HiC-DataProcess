import sys
import statistics
import matplotlib.pyplot as plt
import numpy as np

def main():
    compartment_file = "metadata/GSE63525_GM12878_subcompartments.bed"
    bin_size = 10000

    list_range = []

    with open(compartment_file) as f:
        next(f)
        for line in f:
            splitLine = line.split()

            chrm1 = splitLine[0]
            comp_start1 = int(splitLine[1])
            comp_end1 = int(splitLine[2])

            list_range.append(comp_end1 - comp_start1)

    print(max(list_range))
    print(min(list_range))
    print(statistics.median(list_range))

    plt.hist(list_range,bins=100)
    plt.show()


if __name__ == '__main__':
    main()
