import gzip
import os

import h5py
import numpy as np


def main(name, type):
    # file_path = type + '/' + name + '.validPairs.binPairCount.uniMulti.gz'
    file_path = type + '/' + name + '.validPairs.binPairCount.uni.gz'
    bin_file = 'hESC-r1-heatmap-res-40k.hdf5'
    resolution = 40000

    output_dir = type + '/hicrep-res/' + name + '/'

    # if not os.path.exists(output_dir):
    #     os.makedirs(output_dir)

    # with h5py.File(bin_file, 'r') as f:
    #     bin_start = f.get(list(f)[1])
    #     np_bin_starts = np.array(bin_start)
    #
    # chr_mats = {}
    # curr_index = 0
    # for i in range(1, len(np_bin_starts)):
    #     next_index = np_bin_starts[i]
    #     size = next_index - curr_index
    #
    #     if i == 23:
    #         chr_str = 'chrX'
    #     elif i == 24:
    #         chr_str = 'chrY'
    #     elif i == 25:
    #         chr_str = 'chrM'
    #     else:
    #         chr_str = 'chr' + str(i)
    #
    #     # chr_mats[chr_str] = np.empty((size, size))
    #     chr_mats[chr_str] = np.zeros(shape=(size, size), dtype=np.int)
    #     curr_index = next_index

    with gzip.open(file_path, 'r') as f:
        for line in f:
            parts = line.split()
            chr1 = parts[0].decode("utf-8")
            chr2 = parts[2].decode("utf-8")
            if chr1 != chr2:
                continue

            if chr1 == 'chr22' or chr1 == 'chrY':
                print(file_path)
                print(line)

            # chr = parts[0].decode("utf-8")
            # mat = chr_mats[chr]
            #
            # mid1 = int(parts[1].decode("utf-8"))
            # mid2 = int(parts[3].decode("utf-8"))
            #
            # count = int(parts[4].decode("utf-8"))
            #
            # bin1 = int((mid1 - (resolution / 2)) / resolution)
            # bin2 = int((mid2 - (resolution / 2)) / resolution)
            #
            # mat[bin1][bin2] = count
            # mat[bin2][bin1] = count
            #
            # chr_mats[chr] = mat

    # for c, m in chr_mats.items():
    #     mat_temp = np.empty(shape=(m.shape[0], 2))
    #     chr_arr = []
    #
    #     for j in range(0, m.shape[0]):
    #         chr_arr.append(c)
    #         mat_temp[j, 0] = j * resolution
    #         mat_temp[j, 1] = mat_temp[j, 0] + resolution
    #
    #     chr_np = np.array(chr_arr)
    #     chr_np = np.reshape(chr_np, (chr_np.shape[0], 1))
    #     mat_2 = np.concatenate((chr_np, mat_temp), 1)
    #     final_mat = np.append(mat_2, m, 1)
    #
    #     np.savetxt(output_dir + name + '-' + c + '-40k.txt', final_mat, delimiter=" ", fmt="%s")


if __name__ == '__main__':
    # for i in ('hESC_r1', 'hESC_r2', 'IMR90_r1', 'IMR90_r2'):
    #     for j in ('fithic-our-mHiC', 'fithic-res-mHiC', 'fithic-mHiC-uni'):
    #         main(i, j)

    for i in ('hESC_r1', 'hESC_r2', 'IMR90_r1', 'IMR90_r2'):
        for j in ('fithic-our-mHiC', 'fithic-mHiC-uni'):
            main(i, j)
