import os


def main(file1, file2, name1, name2, type1, type2, threshold):
    output_dir = "fithic-comparison/krnorm/mHiC-mHiCour/" + type1 + "-" + type2 + "/Processed-" + str(threshold)

    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    # dic_f1 = {}
    arr_f1 = set()
    with open(file1) as f:
        for line in f:
            split = line.split()
            key = (split[0], split[1], split[2], split[3])
            arr_f1.add(key)

    arr_f2 = set()
    with open(file2) as f:
        for line in f:
            split = line.split()
            key = (split[0], split[1], split[2], split[3])

            arr_f2.add(key)

    common = arr_f1.intersection(arr_f2)
    f1_uni = arr_f1.difference(arr_f2)
    f2_uni = arr_f2.difference(arr_f1)

    print("{} {} {} {} {}".format(type1, type2, name1, name2, threshold))
    print(len(common))
    print(len(f1_uni))
    print(len(f2_uni))

    output_file_common = open(output_dir + "/" + name1 + "-" + name2 + "-common.txt", "w")
    for i in common:
        output_file_common.write("{} {} {} {}\n".format(i[0], i[1], i[2], i[3]))
    output_file_common.close()

    output_file_f1uniq = open(output_dir + "/" + name1 + "-" + type1 + "-unique.txt", "w")
    for i in f1_uni:
        output_file_f1uniq.write("{} {} {} {}\n".format(i[0], i[1], i[2], i[3]))
    output_file_f1uniq.close()

    output_file_f2uniq = open(output_dir + "/" + name2 + "-" + type2 + "-unique.txt", "w")
    for i in f2_uni:
        output_file_f2uniq.write("{} {} {} {}\n".format(i[0], i[1], i[2], i[3]))
    output_file_f2uniq.close()

    print()


if __name__ == '__main__':
    # parser = ArgumentParser("compare-output",
    #                         formatter_class=ArgumentDefaultsHelpFormatter,
    #                         conflict_handler='resolve')
    # parser.add_argument("-f1", default='None')
    # parser.add_argument("-f2", default='None')
    # parser.add_argument("-n1", default='None')
    # parser.add_argument("-n2", default='None')
    # args = parser.parse_args()

    # f1 = args.f1
    # f2 = args.f2
    # n1 = args.n1
    # n2 = args.n2
    #
    # f1 = f1 + n1 + ".txt"
    # f2 = f2 + n2 + ".txt"
    #
    # main(f1, f2, n1, n2)

    # for i in (0.05, 0.01, 0.001, 0.0001, 0.00001):
    #     for j in ('hESC-r1', 'hESC-r2', 'IMR90-r1', 'IMR90-r2'):
    #         f1 = 'fithic-krnorm-bias/fithic-res-Original/Processed-' + str(i) + '/' + j + '.txt'
    #         f2 = 'fithic-krnorm-bias/fithic-res-Merged/Processed-' + str(i) + '/' + j + '.txt'
    #         main(f1, f2, j, j, 'original', 'merged', i)
    #
    #     for j in ('hESC_r1', 'hESC_r2', 'IMR90_r1', 'IMR90_r2'):
    #         f1 = 'fithic-krnorm-bias/fithic-mHiC-unique/Processed-' + str(i) + '/' + j + '.txt'
    #         f2 = 'fithic-krnorm-bias/fithic-mHiC/Processed-' + str(i) + '/' + j + '.txt'
    #         main(f1, f2, j, j, 'mHiC-unique', 'mHiC', i)
    #
    #         f1 = 'fithic-krnorm-bias/fithic-mHiC-unique/Processed-' + str(i) + '/' + j + '.txt'
    #         f2 = 'fithic-krnorm-bias/fithic-mHiC-our/Processed-' + str(i) + '/' + j + '.txt'
    #         main(f1, f2, j, j, 'mHiC-unique', 'mHiC-our', i)

    # for i in (0.05, 0.01, 0.001, 0.0001, 0.00001):
    #     for j in ('Original', 'Merged'):
    #         f1 = 'fithic-krnorm-bias/fithic-res-' + j + '/Processed-' + str(i) + '/hESC-r1.txt'
    #         f2 = 'fithic-krnorm-bias/fithic-res-' + j + '/Processed-' + str(i) + '/hESC-r2.txt'
    #         main(f1, f2, 'hESC-r1', 'hESC-r2', j, '', i)
    #
    #         f1 = 'fithic-krnorm-bias/fithic-res-' + j + '/Processed-' + str(i) + '/IMR90-r1.txt'
    #         f2 = 'fithic-krnorm-bias/fithic-res-' + j + '/Processed-' + str(i) + '/IMR90-r2.txt'
    #         main(f1, f2, 'IMR90-r1', 'IMR90-r2', j, '', i)
    #
    #     for j in ('mHiC', 'mHiC-our', 'mHiC-unique'):
    #         f1 = 'fithic-krnorm-bias/fithic-' + j + '/Processed-' + str(i) + '/hESC_r1.txt'
    #         f2 = 'fithic-krnorm-bias/fithic-' + j + '/Processed-' + str(i) + '/hESC_r2.txt'
    #         main(f1, f2, 'hESC_r1', 'hESC_r2', j, '', i)
    #
    #         f1 = 'fithic-krnorm-bias/fithic-' + j + '/Processed-' + str(i) + '/IMR90_r1.txt'
    #         f2 = 'fithic-krnorm-bias/fithic-' + j + '/Processed-' + str(i) + '/IMR90_r2.txt'
    #         main(f1, f2, 'IMR90_r1', 'IMR90_r2', j, '', i)

    for i in (0.05, 0.01):
        for j in ('hESC', 'IMR90'):
            f1 = 'fithic-krnorm-bias/fithic-mHiC/Processed-' + str(i) + '/merged/' + j + '.txt'
            f2 = 'fithic-krnorm-bias/fithic-mHiC-our/Processed-' + str(i) + '/merged/' + j + '.txt'
            main(f1, f2, j, j, 'mHiC', 'mHiCour', i)
