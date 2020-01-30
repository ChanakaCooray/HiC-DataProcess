import matplotlib

matplotlib.use('agg')
import h5py
import matplotlib.pyplot as plt
import numpy as np
from argparse import ArgumentParser, ArgumentDefaultsHelpFormatter


def main(type):
    # type = "Merged/hESC-r1"
    resolution = "1M"

    filename = '/Users/bcchanaka/PycharmProjects/HiC-DataProcess/Contact-Matrix/' + type + '-heatmap-res-' + resolution + '.hdf5'

    with h5py.File(filename, 'r') as f:
        print("Keys: %s" % f.keys())
        contact_matrix = (f.get(list(f)[4]))
        np_arr = np.array(contact_matrix)
        # np.fill_diagonal(np_arr, 0)

        # plt.imshow(np.clip(np.log(np_arr), a_min=0, a_max=np.inf), cmap='Reds')
        plt.imshow(np.log(np_arr), cmap='Reds')
        # plt.imshow(np.clip(np_arr, a_min=0, a_max=10), cmap='Reds')
        # plt.imshow(np.log(np_arr), cmap='Reds')
        plt.colorbar()

        # plt.show()
        plt.savefig(
            "/Users/bcchanaka/PycharmProjects/HiC-DataProcess/HeatMap/" + resolution + "/" + type + "-heatmap.png",
            dpi=300)


if __name__ == '__main__':
    parser = ArgumentParser("Visualize-Heatmap",
                            formatter_class=ArgumentDefaultsHelpFormatter,
                            conflict_handler='resolve')
    parser.add_argument("--type", required=True)
    args = parser.parse_args()
    type = args.type
    main(type)
