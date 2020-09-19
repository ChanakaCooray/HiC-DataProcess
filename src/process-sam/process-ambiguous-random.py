import random
from argparse import ArgumentParser, ArgumentDefaultsHelpFormatter
from collections import defaultdict


def main():
    parser = ArgumentParser("Process-ambi",
                            formatter_class=ArgumentDefaultsHelpFormatter,
                            conflict_handler='resolve')
    parser.add_argument("--input", default='None')
    parser.add_argument("--output", default='None')
    args = parser.parse_args()
    sam_file = args.input
    output_sam_file = args.output

    # fragment_file = "/Users/bcchanaka/PycharmProjects/HiC-DataProcess/HiC-RAW/Digest_hg18_HindIII_None_00-37-56_30-11-2019.txt"
    # fragment_file = "/Users/bcchanaka/PycharmProjects/HiC-DataProcess/HiC-RAW/test-fragment"
    sam_file = "/Users/bcchanaka/PycharmProjects/HiC-DataProcess/HiC-RAW/hESC-r1-1-m20.sam"

    output_sam_file = "/Users/bcchanaka/PycharmProjects/HiC-DataProcess/HiC-RAW/hESC-r1-1-m20-output-unique.sam"

    sam_dic = defaultdict(list)

    with open(sam_file) as f:
        for line in f:
            read_id = line.split()[0]
            sam_dic[read_id].append(line)

    output_sam = open(output_sam_file, "w")
    process_sam(sam_dic, output_sam)
    output_sam.close()


def process_sam(sam_dic, output_sam):
    print(len(sam_dic))
    count_unique = 0
    for key, value in sam_dic.items():
        if len(value) == 1:
            print(value[0])
            continue

        output_sam.write(random.choice(value))
        count_unique += 1

    print(count_unique)


if __name__ == '__main__':
    main()
