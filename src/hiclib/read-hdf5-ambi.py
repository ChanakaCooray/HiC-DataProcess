
import h5py
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns

def main():
    # filename = '/Users/bcchanaka/PycharmProjects/HiC-DataProcess/HiCLib-res/contact-maps/heatmap-res-1M.hdf5'
    # filename = '/Users/bcchanaka/PycharmProjects/HiC-DataProcess/HiCLib-res/contact-maps/IC-heatmap-res-1M.hdf5'
    filename = '/Users/bcchanaka/PycharmProjects/HiC-DataProcess/HiCLib-res/contact-maps/ambi/hESC_r1_heatmap-res-1M.hdf5'
    # filename = '/Users/bcchanaka/PycharmProjects/HiC-DataProcess/HiCLib-res/contact-maps/ambi/hESC_r1_IC-heatmap-res-1M.hdf5'

    with h5py.File(filename, 'r') as f:
        # List all groups
        print("Keys: %s" % f.keys())
        a = (f.get(list(f)[4]))
        # a = (f.get(list(f)[6]))
        # print(a)
        n1 = f.get(list(f)[1])
        # print(type(a))

        # total_inter = 0
        # for i in range(0, 4):
        #     print(a[i])
        #     for j in range(0, 4):
        #         print(a[i][j])
        #         total_inter += a[i][j]
        # print(a[i][j])
        # abc = np.array(n1)
        np_arr = np.array(a)

        # plt.imshow(np.clip(np_arr, a_min=0, a_max=50),interpolation='nearest')
        # plt.show()

        # print(np_arr.shape)

        # b = np.log(np_arr)

        # sns.heatmap(np.log(np_arr), cmap="Reds")

        # sns.heatmap(np.clip(np.log(np_arr), a_min=0, a_max=np.inf), cmap="Reds")

        # plt.imshow(np.clip(np.log(np_arr), a_min=0,a_max=np.inf))

        # plt.show()

        # plt.imshow(np_arr)

        plt.imshow(np.clip(np.log(np_arr), a_min=0, a_max=np.inf),cmap='Reds')
        plt.colorbar()
        # plt.ylim(np_arr.shape[0], 0)
        # plt.xlim(0, np_arr.shape[1])
        # plt.show()

        # ax = sns.heatmap(np_arr, linewidth=0.5)
        # plt.imshow(np_arr)
        plt.savefig("output-hESC-r1-merge-2.png", dpi=300)

        # df = pd.DataFrame(np_arr)

        # sns.plt.show()

        # Now if we normalize it by column:
        # df_norm_col = (df - df.mean()) / df.std()
        # sns.heatmap(df_norm_col, cmap='viridis')
        # plt.savefig("b.png")

        # a_triu = np.triu(np_arr, k=0)
        # np.sum(np_arr)
        # total_inter = sum(sum(a))
        # print(np.sum(a_triu))

        # print(f[list(f)[1]])
        # a_group_key = list(f.keys())[0]

        # Get the data
        # data = list(f[a_group_key])

        # print(data)


if __name__ == '__main__':
    main()

# Keys: [u'_self_key', u'chrms1', u'chrms2', u'cuts1', u'cuts2', u'downrsites1', u'downrsites2', u'misc', u'rfragIdxs1', u'rfragIdxs2', u'rsites1', u'rsites2', u'strands1', u'strands2', u'uprsites1', u'uprsites2']
