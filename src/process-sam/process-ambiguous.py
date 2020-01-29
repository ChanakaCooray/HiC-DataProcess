from collections import defaultdict
import numpy as np
from argparse import ArgumentParser, ArgumentDefaultsHelpFormatter

def main():
    parser = ArgumentParser("EdgeDetector",
                            formatter_class=ArgumentDefaultsHelpFormatter,
                            conflict_handler='resolve')
    parser.add_argument("--input", default='None')
    parser.add_argument("--output", default='None')
    args = parser.parse_args()
    sam_file = args.input
    output_sam_file = args.output

    fragment_file = "/Users/bcchanaka/PycharmProjects/HiC-DataProcess/HiC-RAW/Digest_hg18_HindIII_None_00-37-56_30-11-2019.txt"
    # fragment_file = "/Users/bcchanaka/PycharmProjects/HiC-DataProcess/HiC-RAW/test-fragment"
    # sam_file = "/Users/bcchanaka/PycharmProjects/HiC-DataProcess/HiC-RAW/hESC-r1-1-m20.sam"

    # output_sam_file = "/Users/bcchanaka/PycharmProjects/HiC-DataProcess/HiC-RAW/hESC-r1-1-m20-output-unique.sam"

    fragment_dic = defaultdict(list)

    with open(fragment_file) as f:
        next(f)
        next(f)
        for line in f:
            fragment_info = line.split()

            if fragment_info[1] != "1":
                fragment_dic[fragment_info[0]].append(int(fragment_info[1]))

    sam_dic = defaultdict(list)

    header = []

    with open(sam_file) as f:
        # for _ in range(27):
        #     header.append(f.readline())
        for line in f:
            read_id = line.split()[0]
            sam_dic[read_id].append(line)

    output_sam = open(output_sam_file, "w")

    # for h in header:
    #     output_sam.write(h)

    process_sam(sam_dic, fragment_dic, output_sam)

    output_sam.close()


def process_sam(sam_dic, fragment_dic, output_sam):
    print(len(sam_dic))
    count_unique = 0
    for key, value in sam_dic.items():
        if len(value) == 1:
            continue

        # print(key)

        frag_diff_dic = defaultdict(list)
        fragment_diff = get_fragment_diff(value[0], fragment_dic)
        # print("Min diff: " + str(fragment_diff) + "\n")

        min_diff = fragment_diff
        for read in value:
            fragment_diff = get_fragment_diff(read, fragment_dic)

            frag_diff_dic[fragment_diff].append(read)

            if min_diff > fragment_diff:
                min_diff = fragment_diff

            # print("Min diff: " + str(fragment_diff))
            # print()

        if len(frag_diff_dic[min_diff]) == 1:
            output_sam.write(frag_diff_dic[min_diff][0])
            count_unique += 1

        # print("-----------------------------------------------------")
        # print(fragments)
        # break
        # break
    print(count_unique)


def get_fragment_diff(read, fragment_dic):
    read_info = read.split()
    fragments = fragment_dic[read_info[2]]
    read_value = int(read_info[3])

    # print(read)

    # fragment_index_diff = read_value - fragments[len(fragments)-1]

    # for i in range(0, len(fragments)):
    #     if fragments[i] >= read_value:
    #         prev_idx = fragments[i - 1]
    #         next_idx = fragments[i]
    #
    #         if (next_idx - read_value) < (read_value - prev_idx):
    #             fragment_index_diff = (next_idx - read_value)
    #         else:
    #             fragment_index_diff = (read_value - prev_idx)
    #
    #         print("Close fragments: "+str(prev_idx)+" "+str(next_idx))
    #         break

    idx = np.searchsorted(fragments, read_value, side='left')

    if idx == 0:
        fragment_index_diff = fragments[idx] - read_value
    elif idx == len(fragments):
        fragment_index_diff = read_value - fragments[idx - 1]
    else:
        if (read_value - fragments[idx - 1]) < (fragments[idx] - read_value):
            fragment_index_diff = (read_value - fragments[idx - 1])
        else:
            fragment_index_diff = (fragments[idx] - read_value)

    # print("Close fragments: " + str(fragments[idx - 1]) + " " + str(fragments[idx]))

    return fragment_index_diff


if __name__ == '__main__':
    main()
