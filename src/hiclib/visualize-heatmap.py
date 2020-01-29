import h5py
import matplotlib.pyplot as plt
import numpy as np


def main():
    type = "Original/hESC-r1"

    filename = '/Users/bcchanaka/PycharmProjects/HiC-DataProcess/Contact-Matrix/' + type + '-heatmap-res-40k.hdf5'

    with h5py.File(filename, 'r') as f:
        print("Keys: %s" % f.keys())
        contact_matrix = (f.get(list(f)[4]))
        np_arr = np.array(contact_matrix)

        plt.imshow(np.clip(np.log(np_arr), a_min=0, a_max=np.inf), cmap='Reds')
        # plt.imshow(np.log(np_arr), cmap='Reds')
        plt.colorbar()

        # plt.show()
        plt.savefig("/Users/bcchanaka/PycharmProjects/HiC-DataProcess/HeatMap/"+type+"-heatmap.png",
                    dpi=300)


if __name__ == '__main__':
    main()
