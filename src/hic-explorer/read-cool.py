import cooler


def main():
    filename = '/Users/bcchanaka/PycharmProjects/HiC-DataProcess/hic-explorer/hESC-r1-40k.cool'
    output = '/Users/bcchanaka/PycharmProjects/HiC-DataProcess/hic-explorer/hESC-r1-interact-40k-wochrM.txt'

    # with h5py.File(filename, 'r') as f:
    #     a = (f.get(list(f)[4]))
    #
    #     print(a)

    mat = cooler.Cooler(filename).matrix(balance=False, as_pixels=True, join=True)
    df = mat[:]

    df = df[(df.chrom1 != 'chrM') & (df.chrom2 != 'chrM')]

    df['fragmentMid1'] = (df['start1'] + df['end1']) / 2
    df['fragmentMid2'] = (df['start2'] + df['end2']) / 2

    new_df = df[['chrom1', 'fragmentMid1', 'chrom2', 'fragmentMid2', 'count']].copy()

    new_df.to_csv(output, sep=" ", float_format='%d', header=False, index=False)

    # print(df['count'].sum())

    # with cooler.Cooler.open(cooler.Cooler(filename), 'r') as f:
    #     a = (f.get(list(f)[4]))
    #
    #     print(a)


if __name__ == '__main__':
    main()
