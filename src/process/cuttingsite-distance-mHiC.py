import bisect
from argparse import ArgumentParser, ArgumentDefaultsHelpFormatter
from collections import defaultdict


def main():
    parser = ArgumentParser("process-split-files",
                            formatter_class=ArgumentDefaultsHelpFormatter,
                            conflict_handler='resolve')
    parser.add_argument("--input", default='None')
    parser.add_argument("--output1", default='None')
    parser.add_argument("--output2", default='None')
    parser.add_argument("--unimulti", default='None')

    args = parser.parse_args()
    input_file = args.input
    output_file1 = args.output1
    output_file2 = args.output2
    unimulti = args.unimulti

    fragment_file = "/Users/bcchanaka/PycharmProjects/HiC-DataProcess/HiC-RAW/Digest_hg18_HindIII_None_00-37-56_30-11-2019.txt"

    input_file = "/Users/bcchanaka/PycharmProjects/HiC-DataProcess/mHiC-data/hESC-r2.validpairs"
    output_file1 = "/Users/bcchanaka/PycharmProjects/HiC-DataProcess/mHiC-data/1"
    output_file2 = "/Users/bcchanaka/PycharmProjects/HiC-DataProcess/mHiC-data/2"

    fragment_dic = defaultdict(list)

    with open(fragment_file) as f:
        next(f)
        next(f)
        for line in f:
            fragment_info = line.split()

            if fragment_info[1] != "1":
                fragment_dic[fragment_info[0]].append(int(fragment_info[1]))

    output_f1 = open(output_file1, "w")
    output_f2 = open(output_file2, "w")

    with open(input_file) as f:
        for line in f:
            if unimulti in line:
                (dist1, dist2) = process_read(line, fragment_dic)
                output_f1.write("{}\n".format(dist1))
                output_f2.write("{}\n".format(dist2))

    output_f1.close()
    output_f2.close()


def process_read(read, fragment_dic):
    read_info = read.split()
    dist1 = get_fragment_diff(read_info[1], read_info[2], fragment_dic)
    dist2 = get_fragment_diff(read_info[6], read_info[7], fragment_dic)
    return (dist1, dist2)


# def process_sam(sam_dic, fragment_dic, output_sam):
#     # print(len(sam_dic))
#     count_unique = 0
#     count_all = 0
#     for key, value in sam_dic.items():
#         count_all += 1
#         if len(value) == 1:
#             output_sam.write(value[0])
#             continue
#
#         frag_diff_dic = defaultdict(list)
#         # fragment_diff = get_fragment_diff_both(value[0], fragment_dic)
#
#         min_diff = None
#         for read in value:
#             fragment_diff = get_fragment_diff_both(read, fragment_dic)
#
#             frag_diff_dic[fragment_diff].append(read)
#
#             if not min_diff:
#                 min_diff = fragment_diff
#             elif min_diff > fragment_diff:
#                 min_diff = fragment_diff
#
#         # print(frag_diff_dic[min_diff])
#         if len(frag_diff_dic[min_diff]) == 1:
#             output_sam.write(frag_diff_dic[min_diff][0].replace("MULTI", "UNI"))
#             count_unique += 1
#
#     print("Multi Processed count: " + str(count_unique))
#     print("All count: " + str(count_all))


def get_fragment_diff_both(read, fragment_dic):
    read_info = read.split()
    return get_fragment_diff(read_info[1], read_info[2], fragment_dic) + get_fragment_diff(read_info[6], read_info[7],
                                                                                           fragment_dic)


def get_fragment_diff(chr, pos, fragment_dic):
    fragments = fragment_dic[chr]
    read_value = int(float(pos))

    # idx = np.searchsorted(fragments, read_value, side='left')
    idx = bisect.bisect_left(fragments, read_value)

    # print(idx)

    if idx == 0:
        fragment_index_diff = fragments[idx] - read_value
    elif idx == len(fragments):
        fragment_index_diff = read_value - fragments[idx - 1]
    else:
        if (read_value - fragments[idx - 1]) < (fragments[idx] - read_value):
            fragment_index_diff = (read_value - fragments[idx - 1])
        else:
            fragment_index_diff = (fragments[idx] - read_value)

    return fragment_index_diff


if __name__ == '__main__':
    main()
