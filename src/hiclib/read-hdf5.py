import h5py
import numpy as np


def main(name, type):
    filename = '/Users/bcchanaka/PycharmProjects/HiC-DataProcess/Contact-Matrix/' + type + '/' + name + '-heatmap-res-40k.hdf5'
    # output_file = '/Users/bcchanaka/PycharmProjects/HiC-DataProcess/Contact-Matrix/Original/hESC-r1-40k.npy'
    resolution = 40000

    with h5py.File(filename, 'r') as f:
        a = (f.get(list(f)[4]))

        bin_start = f.get(list(f)[1])

        np_bin_starts = np.array(bin_start)

        np_arr = np.array(a)
        np_arr = np_arr[0:77021, 0:77021]

        a_triu = np.triu(np_arr, k=0)

        print("line count: " + name + " " + type + " " + str(np.count_nonzero(a_triu)))

        print("total: " + name + " " + type + " " + str(np.sum(a_triu)))

        # mat = np.empty(shape=(np_arr.shape[0], 2))
        # chr_arr = []

        # for i in range(0, np_arr.shape[0]):
        #     chr = np.searchsorted(np_bin_starts, i, side='right')
        #
        #     if chr == 23:
        #         chr_str = 'chrX'
        #     elif chr == 24:
        #         chr_str = 'chrY'
        #     elif chr == 25:
        #         chr_str = 'chrM'
        #     else:
        #         chr_str = 'chr' + str(chr)
        #
        #     chr_arr.append(chr_str)
        #     mat[i, 0] = i * resolution
        #     mat[i, 1] = mat[i, 0] + resolution
        #
        # chr_np = np.array(chr_arr)
        # chr_np = np.reshape(chr_np, (chr_np.shape[0], 1))
        # mat_2 = np.concatenate((chr_np,mat),1)
        # final_mat = np.append(mat_2, np_arr, 1)

        # np.save(output_file, final_mat)
        # np.savetxt(output_file+".txt",final_mat,fmt='%s')

        # np.savetxt(output_file+'.txt', final_mat, delimiter=" ", fmt="%s")


if __name__ == '__main__':
    for i in ('IMR90-r1',):
        for j in ('Original', 'Merged'):
            main(i, j)
