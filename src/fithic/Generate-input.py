import h5py
import numpy as np


def main():
    resolution = 1000000
    filename = '/Users/bcchanaka/PycharmProjects/HiC-DataProcess/Contact-Matrix/Original/hESC-r1-heatmap-res-1M.hdf5'
    chrom_size_file = '/Users/bcchanaka/PycharmProjects/HiC-DataProcess/metadata/hg18_chrom_sizes.txt'

    chrm_size = {}
    with open(chrom_size_file) as f:
        for line in f:
            (key, val) = line.split()
            chrm_size[key] = int(val)

    with h5py.File(filename, 'r') as f:
        print("Keys: %s" % f.keys())
        mat = (f.get(list(f)[4]))
        bin_start = f.get(list(f)[1])

        np_contact_mat = np.array(mat)
        np_bin_starts = np.array(bin_start)

    np_sum = np.sum(np_contact_mat, axis=0)

    f_output_frag = open("fithic-res/fithic-frag-1M.txt", "w")

    bin_map = {}

    for i in range(0, np_sum.shape[0]):
        val = np_sum[i]
        chr = np.searchsorted(np_bin_starts, i, side='right')
        bin_idx = i - np_bin_starts[chr - 1]
        mid = bin_idx * resolution + resolution / 2

        if chr == 23:
            chr_str = 'X'
        elif chr == 24:
            chr_str = 'Y'
        elif chr == 25:
            chr_str = 'M'
        else:
            chr_str = str(chr)

        if chr == len(np_bin_starts):
            pass
        elif i == np_bin_starts[chr] - 1:
            size = chrm_size[chr_str]
            mid = (bin_idx * resolution + size) / 2

        bin_map[i] = (chr, int(mid))

        f_output_frag.write("{} {} {} {} {}\n".format(chr, 0, int(mid), val, 0))

    f_output_frag.close()

    f_output_interact = open("fithic-res/fithic-interact-1M.txt", "w")

    for i in range(0, np_contact_mat.shape[0]):
        for j in range(0, np_contact_mat.shape[1]):
            if np_contact_mat[i][j] != 0:
                f_output_interact.write(
                    "{} {} {} {} {}\n".format(bin_map[i][0], bin_map[i][1], bin_map[j][0], bin_map[j][1],
                                              np_contact_mat[i][j]))

    f_output_interact.close()


if __name__ == '__main__':
    main()
