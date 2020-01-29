import h5py


def main():
    filename = '/Users/bcchanaka/PycharmProjects/HiC-DataProcess/HiCLib-res/contact-maps/heatmap-res-1M.hdf5'

    with h5py.File(filename, 'r') as f:
        # List all groups
        print("Keys: %s" % f.keys())
        a = (f.get(list(f)[4]))
        # print(a)
        n1 = f.get(list(f)[1])
        print(type(a))

        total_inter = 0
        for i in range(0, a.shape[0]):
            for j in range(0, a.shape[1]):
                total_inter += a[i][j]
                # print(a[i][j])

        print(total_inter)

        # print(f[list(f)[1]])
        # a_group_key = list(f.keys())[0]

        # Get the data
        # data = list(f[a_group_key])

        # print(data)


if __name__ == '__main__':
    main()

# Keys: [u'_self_key', u'chrms1', u'chrms2', u'cuts1', u'cuts2', u'downrsites1', u'downrsites2', u'misc', u'rfragIdxs1', u'rfragIdxs2', u'rsites1', u'rsites2', u'strands1', u'strands2', u'uprsites1', u'uprsites2']
