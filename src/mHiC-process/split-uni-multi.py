import os
from argparse import ArgumentParser, ArgumentDefaultsHelpFormatter


def main():
    parser = ArgumentParser("Generate-s3-mHiC",
                            formatter_class=ArgumentDefaultsHelpFormatter,
                            conflict_handler='resolve')
    parser.add_argument("--input", default='None')
    parser.add_argument("--output", default='None')
    args = parser.parse_args()
    input_file = args.input
    output_dir = args.output

    # fragment_file = "/Users/bcchanaka/PycharmProjects/HiC-DataProcess/HiC-RAW/Digest_hg18_HindIII_None_00-37-56_30-11-2019.txt"

    # input_file = "/Users/bcchanaka/PycharmProjects/HiC-DataProcess/mHiC-data/hESC-r2.validpairs"
    # output_dir = "/Users/bcchanaka/PycharmProjects/HiC-DataProcess/mHiC-data/temp"

    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    output_uni = open(output_dir + "/validpair.uni", "w")
    output_multi = open(output_dir + "/validpair.multi", "w")

    with open(input_file) as f:
        for line in f:
            if "MULTI" in line:
                output_multi.write(line)
            if "UNI" in line:
                output_uni.write(line)

    output_uni.close()
    output_multi.close()


if __name__ == '__main__':
    main()
