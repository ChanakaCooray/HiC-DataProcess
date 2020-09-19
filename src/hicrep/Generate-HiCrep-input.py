import h5py
import numpy as np
from argparse import ArgumentParser, ArgumentDefaultsHelpFormatter


def main(type, merged):
    filename = '/Users/bcchanaka/PycharmProjects/HiC-DataProcess/Contact-Matrix/' + merged + '/' + type + '-heatmap-res-1M.hdf5'
    output_file = '/Users/bcchanaka/PycharmProjects/HiC-DataProcess/Contact-Matrix/' + merged + '/out-hicrep/' + type + '-1M.npy'
    resolution = 1000000

    with h5py.File(filename, 'r') as f:
        a = (f.get(list(f)[4]))

        bin_start = f.get(list(f)[1])

        np_bin_starts = np.array(bin_start)

        np_arr = np.array(a)
        # print(np_arr)

        mat = np.empty(shape=(np_arr.shape[0], 2))
        chr_arr = []

        for i in range(0, np_arr.shape[0]):
            chr = np.searchsorted(np_bin_starts, i, side='right')

            if chr == 23:
                chr_str = 'chrX'
            elif chr == 24:
                chr_str = 'chrY'
            elif chr == 25:
                chr_str = 'chrM'
            else:
                chr_str = 'chr' + str(chr)

            chr_arr.append(chr_str)
            mat[i, 0] = i * resolution
            mat[i, 1] = mat[i, 0] + resolution

        chr_np = np.array(chr_arr)
        chr_np = np.reshape(chr_np, (chr_np.shape[0], 1))
        mat_2 = np.concatenate((chr_np, mat), 1)
        final_mat = np.append(mat_2, np_arr, 1)

        # np.save(output_file, final_mat)
        # np.savetxt(output_file+".txt",final_mat,fmt='%s')

        np.savetxt(output_file + '.txt', final_mat, delimiter=" ", fmt="%s")


if __name__ == '__main__':
    parser = ArgumentParser("Generate-HiCrep",
                            formatter_class=ArgumentDefaultsHelpFormatter,
                            conflict_handler='resolve')
    parser.add_argument("--input", default='None')
    parser.add_argument("--type", default='None')
    args = parser.parse_args()
    input_f = args.input
    type_f = args.type

    # main(input_f, type_f)
    main('hESC-r2', 'Original')
