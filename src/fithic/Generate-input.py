import h5py
import numpy as np


def generate_input(filename, output_interact, resolution):
    # chrom_size_file = '/Users/bcchanaka/PycharmProjects/HiC-DataProcess/metadata/hg18_chrom_sizes.txt'
    # chrm_size = {}
    # with open(chrom_size_file) as f:
    #     for line in f:
    #         (key, val) = line.split()
    #         chrm_size[key] = int(val)

    with h5py.File(filename, 'r') as f:
        print("Keys: %s" % f.keys())
        mat = (f.get(list(f)[4]))
        bin_start = f.get(list(f)[1])

        np_contact_mat = np.array(mat)
        np_bin_starts = np.array(bin_start)

    np_contact_mat = np.triu(np_contact_mat, k=0)

    np_sum = np.sum(np_contact_mat, axis=1)

    # f_output_frag = open(output_frag, "w")

    bin_map = {}

    for i in range(0, np_sum.shape[0]):
        val = np_sum[i]
        chr = np.searchsorted(np_bin_starts, i, side='right')
        bin_idx = i - np_bin_starts[chr - 1]
        mid = bin_idx * resolution + resolution / 2

        if chr == 23:
            chr_str = 'chrX'
        elif chr == 24:
            chr_str = 'chrY'
        elif chr == 25:
            chr_str = 'chrM'
        else:
            chr_str = 'chr' + str(chr)

        if chr == len(np_bin_starts):
            print(chr)
            pass
        # elif i == np_bin_starts[chr] - 1:
        #     size = chrm_size[chr_str]
        #     mid = (bin_idx * resolution + size) / 2
        #     f_output_frag.write("{} {} {} {} {}\n".format(chr, 0, int(mid), val, 0))
        else:
            bin_map[i] = (chr_str, int(mid))
            # f_output_frag.write("{} {} {} {} {}\n".format(chr, 0, int(mid), val, 0))

    # f_output_frag.close()

    f_output_interact = open(output_interact, "w")

    for i in range(0, np_contact_mat.shape[0]):
        for j in range(0, np_contact_mat.shape[1]):
            if np_contact_mat[i][j] != 0:
                f_output_interact.write(
                    "{} {} {} {} {}\n".format(bin_map[i][0], bin_map[i][1], bin_map[j][0], bin_map[j][1],
                                              np_contact_mat[i][j]))

    f_output_interact.close()


def main():
    resolution = 40000
    # for i in ('Original', 'Merged'):
    #     for j in ('hESC-r1', 'hESC-r2', 'IMR90-r1', 'IMR90-r2'):
    #         filename = '/Users/bcchanaka/PycharmProjects/HiC-DataProcess/Contact-Matrix/' + i + '/' + j + '-heatmap-res-40k.hdf5'
    #         output_frag = 'fithic-res/' + i + '/' + j + '-frag-40k.txt'
    #         output_interact = 'fithic-res/' + i + '/' + j + '-interact-40k.txt'
    #
    #         generate_input(filename, output_frag, output_interact, resolution)

    # for i in ('Original', 'Merged'):
    #     j = 'IMR90-r1'
    #     filename = '/Users/bcchanaka/PycharmProjects/HiC-DataProcess/Contact-Matrix/' + i + '/' + j + '-heatmap-res-40k.hdf5'
    #     # output_frag = 'fithic-res/' + i + '/' + j + '-frag-40k.txt'
    #     output_interact = 'fithic-res/' + i + '/' + j + '-interact-40k-new.txt'
    #
    #     generate_input(filename, output_interact, resolution)

    for j in ('hESC_r1', 'hESC_r2', 'IMR90_r1', 'IMR90_r1'):
        filename = 'Contact-Matrix/random/' + j + '-heatmap-res-40k.hdf5'
        output_interact = 'fithic-hiclib-random/' + j + '.validPairs.binPairCount.uni'
        generate_input(filename, output_interact, resolution)


if __name__ == '__main__':
    main()
