import os


def main(file1, file2, output_file):
    os.makedirs(os.path.dirname(output_file), exist_ok=True)

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

    output = open(output_file, "w")
    for i in common:
        output.write("{} {} {} {}\n".format(i[0], i[1], i[2], i[3]))

    for i in f1_uni:
        output.write("{} {} {} {}\n".format(i[0], i[1], i[2], i[3]))

    for i in f2_uni:
        output.write("{} {} {} {}\n".format(i[0], i[1], i[2], i[3]))

    output.close()


if __name__ == '__main__':
    # file_path1 = '/Users/bcchanaka/PycharmProjects/HiC-DataProcess/fithic-krnorm-bias/fithic-res-Original/Processed-0.01/hESC-r1.txt'
    # file_path2 = '/Users/bcchanaka/PycharmProjects/HiC-DataProcess/fithic-krnorm-bias/fithic-res-Original/Processed-0.01/hESC-r2.txt'
    # output_file = '/Users/bcchanaka/PycharmProjects/HiC-DataProcess/fithic-krnorm-bias/fithic-res-Original/Processed-0.01/merged/hESC.txt'
    #
    # main(file_path1, file_path2, output_file)

    # for j in ('fithic-intra', 'fithic-krnorm-bias'):
    #     for l in ('hESC', 'IMR90'):
    #         for k in ('fithic-res-Original', 'fithic-res-Merged'):
    #             for i in (0.05, 0.01):
    #                 file_path1 = '/Users/bcchanaka/PycharmProjects/HiC-DataProcess/' + j + '/' + k + '/Processed-' + str(
    #                     i) + '/' + l + '-r1.txt'
    #                 file_path2 = '/Users/bcchanaka/PycharmProjects/HiC-DataProcess/' + j + '/' + k + '/Processed-' + str(
    #                     i) + '/' + l + '-r2.txt'
    #                 output_file = '/Users/bcchanaka/PycharmProjects/HiC-DataProcess/' + j + '/' + k + '/Processed-' + str(
    #                     i) + '/merged/' + l + '.txt'
    #                 main(file_path1, file_path2, output_file)
    #
    #         for k in ('fithic-mHiC-unique', 'fithic-mHiC-our', 'fithic-mHiC'):
    #             for i in (0.05, 0.01):
    #                 file_path1 = '/Users/bcchanaka/PycharmProjects/HiC-DataProcess/' + j + '/' + k + '/Processed-' + str(
    #                     i) + '/' + l + '_r1.txt'
    #                 file_path2 = '/Users/bcchanaka/PycharmProjects/HiC-DataProcess/' + j + '/' + k + '/Processed-' + str(
    #                     i) + '/' + l + '_r2.txt'
    #                 output_file = '/Users/bcchanaka/PycharmProjects/HiC-DataProcess/' + j + '/' + k + '/Processed-' + str(
    #                     i) + '/merged/' + l + '.txt'
    #                 main(file_path1, file_path2, output_file)

    for j in ('fithic-krnorm-bias',):
        for l in ('hESC', 'IMR90'):
            for k in ('fithic-hiclib-random', 'fithic-mHiC-random'):
                for i in (0.05, 0.01):
                    file_path1 = '/Users/bcchanaka/PycharmProjects/HiC-DataProcess/' + j + '/' + k + '/Processed-' + str(
                        i) + '/' + l + '_r1.txt'
                    file_path2 = '/Users/bcchanaka/PycharmProjects/HiC-DataProcess/' + j + '/' + k + '/Processed-' + str(
                        i) + '/' + l + '_r2.txt'
                    output_file = '/Users/bcchanaka/PycharmProjects/HiC-DataProcess/' + j + '/' + k + '/Processed-' + str(
                        i) + '/merged/' + l + '.txt'
                    main(file_path1, file_path2, output_file)
