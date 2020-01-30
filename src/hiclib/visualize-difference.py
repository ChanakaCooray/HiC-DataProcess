import matplotlib

matplotlib.use('agg')
import h5py
import matplotlib.pyplot as plt
import numpy as np
from argparse import ArgumentParser, ArgumentDefaultsHelpFormatter

def main(type):
    resolution = "1M"
    original_file = "/Users/bcchanaka/PycharmProjects/HiC-DataProcess/Contact-Matrix/Original/"+type+"-heatmap-res-"+resolution+".hdf5"
    merged_file = "/Users/bcchanaka/PycharmProjects/HiC-DataProcess/Contact-Matrix/Merged/"+type+"-heatmap-res-"+resolution+".hdf5"

    with h5py.File(original_file, 'r') as f:
        print("Keys: %s" % f.keys())
        a = (f.get(list(f)[4]))
        np_arr_orig = np.array(a)

    with h5py.File(merged_file, 'r') as f:
        print("Keys: %s" % f.keys())
        a = (f.get(list(f)[4]))
        np_arr_merg = np.array(a)

    np_diff = np.subtract(np_arr_merg,np_arr_orig)

    # plt.imshow(np.clip(np.log(np_diff), a_min=0, a_max=np.inf), cmap='Reds')
    plt.imshow(np.log(np_diff), cmap='Reds')
    plt.colorbar()
    # plt.show()
    plt.savefig(
        "/Users/bcchanaka/PycharmProjects/HiC-DataProcess/HeatMap/" + resolution + "/Difference/" + type + "-heatmap.png",
        dpi=300)

if __name__ == '__main__':
    parser = ArgumentParser("Visualize-Heatmap",
                            formatter_class=ArgumentDefaultsHelpFormatter,
                            conflict_handler='resolve')
    parser.add_argument("--type", required=True)
    args = parser.parse_args()
    type = args.type
    main(type)