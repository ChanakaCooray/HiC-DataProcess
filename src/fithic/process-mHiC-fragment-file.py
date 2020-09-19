import gzip
from collections import defaultdict


def main(file_path, output_file, fragment_file):
    frag_counts = defaultdict(int)
    with gzip.open(file_path, 'r') as f:
        for line in f:
            parts = line.split()

            chr1 = parts[0].decode("utf-8")
            frag1 = int(parts[1].decode("utf-8"))
            chr2 = parts[2].decode("utf-8")
            frag2 = int(parts[3].decode("utf-8"))
            count = int(parts[4].decode("utf-8"))

            if chr1 == chr2 and frag1 == frag2:
                frag_counts[(chr1, frag1)] = frag_counts[(chr1, frag1)] + count
            else:
                frag_counts[(chr1, frag1)] = frag_counts[(chr1, frag1)] + count
                frag_counts[(chr2, frag2)] = frag_counts[(chr2, frag2)] + count

    f_output = open(output_file, "w")

    with gzip.open(fragment_file, 'r') as f:
        for line in f:
            parts = line.split()

            chr = parts[0].decode("utf-8")
            part1 = int(parts[1].decode("utf-8"))
            part2 = int(parts[2].decode("utf-8"))

            part4 = int(parts[4].decode("utf-8"))

            f_output.write("{} {} {} {} {}\n".format(chr, part1, part2, frag_counts[(chr, part2)], part4))

            # if (chr, part2) in frag_counts:
            #     f_output.write("{} {} {} {} {}\n".format(chr, part1, part2, frag_counts[(chr, part2)], part4))
            # else:
            #     f_output.write("{} {} {} {} {}".format(chr, part1, part2, 0, part4))

    f_output.close()


if __name__ == '__main__':
    name = 'hESC_r2'
    file_path = '/Users/bcchanaka/PycharmProjects/HiC-DataProcess/fithic-res-mHiC/' + name + '.validPairs.binPairCount.uniMulti.gz'
    output_file = '/Users/bcchanaka/PycharmProjects/HiC-DataProcess/fithic-res-mHiC/' + name + '.uni.fragments.mHiC'
    fragment_file = '/Users/bcchanaka/PycharmProjects/HiC-DataProcess/fithic-res-mHiC/temp-frag/' + name + '.uni.fragments.mHiC.gz'
    main(file_path, output_file, fragment_file)
