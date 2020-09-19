import os
from argparse import ArgumentParser, ArgumentDefaultsHelpFormatter
from collections import defaultdict
from concurrent.futures import ThreadPoolExecutor

import numpy as np


def main():
    parser = ArgumentParser("Generate-s3-mHiC",
                            formatter_class=ArgumentDefaultsHelpFormatter,
                            conflict_handler='resolve')
    parser.add_argument("--input", default='None')
    parser.add_argument("--output", default='None')
    args = parser.parse_args()
    input_file = args.input
    output_dir = args.output

    fragment_file = "/Users/bcchanaka/PycharmProjects/HiC-DataProcess/HiC-RAW/Digest_hg18_HindIII_None_00-37-56_30-11-2019.txt"

    input_file = "/Users/bcchanaka/PycharmProjects/HiC-DataProcess/mHiC-data/hESC-r2.validpairs"
    output_dir = "/Users/bcchanaka/PycharmProjects/HiC-DataProcess/mHiC-data/temp"

    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    fragment_dic = defaultdict(list)

    with open(fragment_file) as f:
        next(f)
        next(f)
        for line in f:
            fragment_info = line.split()

            if fragment_info[1] != "1":
                fragment_dic[fragment_info[0]].append(int(fragment_info[1]))

    sam_dic = defaultdict(list)

    with open(input_file) as f:
        for line in f:
            read_id = line.split()[0]
            sam_dic[read_id].append(line)

    dic_list = split_dict(sam_dic)

    i = 1
    for dic in dic_list:
        output_sam = open(output_dir + "/validpairs_multi_" + str(i), "w")

        for key, value in dic.items():
            for entry in value:
                output_sam.write(entry)

        output_sam.close()
        i += 1

    # output_sam = open(output_sam_file, "w")
    # process_sam(sam_dic, fragment_dic, output_sam)
    # output_sam.close()


def split_dict(dic):
    inc = int(len(dic) / 20)

    dic_list = []
    i = 0
    while i < len(dic):
        dic_list.append(dict(list(dic.items())[i:(i + inc)]))
        i += inc

    return dic_list


if __name__ == '__main__':
    main()
