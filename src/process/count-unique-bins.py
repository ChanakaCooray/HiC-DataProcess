import gzip


def main(file):
    print(file)

    set_bins = set()

    with gzip.open(file, 'r') as f:
        for line in f:
            parts = line.split()

            set_bins.add((parts[0], parts[1]))
            set_bins.add((parts[2], parts[3]))

    print(len(set_bins))


if __name__ == '__main__':
    # for i in ('Original', 'Merged'):
    #     for j in ('hESC-r1', 'hESC-r2', 'IMR90-r1', 'IMR90-r2'):
    #         main('fithic-res/' + i + '/' + j + '-interact-40k.txt.gz')

    for j in ('hESC_r1', 'hESC_r2', 'IMR90_r1', 'IMR90_r2'):
        main('fithic-res-mHiC/' + j + '.validPairs.binPairCount.uniMulti.gz')

    for i in ('fithic-our-mHiC', 'fithic-mHiC-uni'):
        for j in ('hESC_r1', 'hESC_r2', 'IMR90_r1', 'IMR90_r2'):
            main(i + '/' + j + '.validPairs.binPairCount.uni.gz')
