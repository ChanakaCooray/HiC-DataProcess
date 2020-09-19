import bisect
import re
import timeit
from collections import defaultdict


def atoi(text):
    return int(text) if text.isdigit() else text


def natural_keys(text):
    return [atoi(c) for c in re.split('(\d+)', text)]


def main_perlabel(file_path, fithic_file):
    print(file_path)
    print(fithic_file)
    # file_path = '/Users/bcchanaka/PycharmProjects/HiC-DataProcess/annotations-process/wgEncodeBroadHmmH1hescHMM-hg18.bed'
    # file_path = '/Users/bcchanaka/PycharmProjects/HiC-DataProcess/annotations-process/segway_h1hesc-hg18.bed'

    # fithic_file = '/Users/bcchanaka/PycharmProjects/HiC-DataProcess/fithic-intra/fithic-res-Original/Processed-0.01/hESC-r1.txt'

    # if not os.path.exists(output_dir):
    #     os.makedirs(output_dir)

    # output_file = ''
    # f_output = open(output_file, "w")

    annot_map = defaultdict()
    annot_stat = {}
    # annot_total = {}

    with open(file_path, 'r') as f:
        for line in f:
            parts = line.split()

            chr = parts[0]
            start = int(parts[1])
            end = int(parts[2])
            annot = parts[3]

            if chr not in annot_map:
                annot_map[chr] = ([annot], [start], [end])
            else:
                annot_map[chr][0].append(annot)
                annot_map[chr][1].append(start)
                annot_map[chr][2].append(end)

            if parts[3] not in annot_stat:
                annot_stat[parts[3]] = 0
                # annot_total[parts[3]] = 0
            # else:
            #     annot_total[parts[3]] += 1

    # print(len(annot_map))
    # print(sorted(annot_map.keys()))

    start = timeit.default_timer()

    countlines = 0
    with open(fithic_file, 'r') as f:
        for line in f:
            countlines += 1
            if countlines % 10000 == 0:
                print(countlines, end='\r')

            parts = line.split()

            if parts[0] != parts[2]:
                print(line)

            if parts[0] == '24' or parts[0] == 'chrY':
                continue

            if 'chr' not in parts[0]:
                if parts[0] == '23':
                    chr = 'chrX'
                else:
                    chr = 'chr' + parts[0]

            start1 = int(parts[1]) - 20000
            end1 = int(parts[1]) + 20000

            start2 = int(parts[3]) - 20000
            end2 = int(parts[3]) + 20000

            # count = int(parts[4])

            annot_arr = annot_map[chr][0]
            start_arr = annot_map[chr][1]
            end_arr = annot_map[chr][2]

            idx1 = bisect.bisect_right(start_arr, start1) - 1

            find_annot = []

            for i in range(idx1, len(start_arr)):
                annot = annot_arr[i]

                if annot in find_annot:
                    continue

                st = start_arr[i]
                ed = end_arr[i]

                if st <= start1 < ed:
                    annot_stat[annot] += 1
                    find_annot.append(annot)
                elif st <= end1 < ed:
                    find_annot.append(annot)
                    annot_stat[annot] += 1
                elif start1 < st and ed <= end1:
                    find_annot.append(annot)
                    annot_stat[annot] += 1

                if end1 < st:
                    break

            idx2 = bisect.bisect_right(start_arr, start2) - 1

            for i in range(idx2, len(start_arr)):
                annot = annot_arr[i]

                if annot in find_annot:
                    continue

                st = start_arr[i]
                ed = end_arr[i]

                if st <= start2 < ed:
                    annot_stat[annot] += 1
                    find_annot.append(annot)
                elif st <= end2 < ed:
                    find_annot.append(annot)
                    annot_stat[annot] += 1
                elif start2 < st and ed <= end2:
                    find_annot.append(annot)
                    annot_stat[annot] += 1

                if end2 < st:
                    break

    # for key,value in annot_map.items():
    #     print(key+" "+str(len(value)))

    # print(annot_stat)
    # print(len(annot_stat))

    for key in sorted(annot_stat.keys(), key=natural_keys):
        print("{}".format(annot_stat[key] / countlines))

    # stop = timeit.default_timer()
    # print('Time: ', stop - start)
    # print()


def main_persite(file_path, fithic_file):
    print(file_path)
    print(fithic_file)
    # file_path = '/Users/bcchanaka/PycharmProjects/HiC-DataProcess/annotations-process/wgEncodeBroadHmmH1hescHMM-hg18.bed'
    # file_path = '/Users/bcchanaka/PycharmProjects/HiC-DataProcess/annotations-process/segway_h1hesc-hg18.bed'

    # fithic_file = '/Users/bcchanaka/PycharmProjects/HiC-DataProcess/fithic-intra/fithic-res-Original/Processed-0.01/hESC-r1.txt'

    # if not os.path.exists(output_dir):
    #     os.makedirs(output_dir)

    # output_file = ''
    # f_output = open(output_file, "w")

    annot_map = defaultdict()
    annot_stat = {}
    annot_total = {}

    with open(file_path, 'r') as f:
        for line in f:
            parts = line.split()

            chr = parts[0]
            start = int(parts[1])
            end = int(parts[2])
            annot = parts[3]

            if chr not in annot_map:
                annot_map[chr] = ([annot], [start], [end])
            else:
                annot_map[chr][0].append(annot)
                annot_map[chr][1].append(start)
                annot_map[chr][2].append(end)

            if parts[3] not in annot_stat:
                annot_stat[parts[3]] = 0
                annot_total[parts[3]] = 0
            else:
                annot_total[parts[3]] += 1

    start = timeit.default_timer()

    countlines = 0
    with open(fithic_file, 'r') as f:
        for line in f:
            countlines += 1
            if countlines % 10000 == 0:
                print(countlines, end='\r')

            parts = line.split()

            if parts[0] != parts[2]:
                print(line)

            if parts[0] == '24' or parts[0] == 'chrY':
                continue

            if 'chr' not in parts[0]:
                if parts[0] == '23':
                    chr = 'chrX'
                else:
                    chr = 'chr' + parts[0]

            start1 = int(parts[1]) - 20000
            end1 = int(parts[1]) + 20000

            start2 = int(parts[3]) - 20000
            end2 = int(parts[3]) + 20000

            # count = int(parts[4])

            annot_arr = annot_map[chr][0]
            start_arr = annot_map[chr][1]
            end_arr = annot_map[chr][2]

            idx1 = bisect.bisect_right(start_arr, start1) - 1

            # find_annot = []

            for i in range(idx1, len(start_arr)):
                annot = annot_arr[i]

                # if annot in find_annot:
                #     continue

                st = start_arr[i]
                ed = end_arr[i]

                if st <= start1 < ed:
                    annot_stat[annot] += 1
                    # find_annot.append(annot)
                elif st <= end1 < ed:
                    # find_annot.append(annot)
                    annot_stat[annot] += 1
                elif start1 < st and ed <= end1:
                    # find_annot.append(annot)
                    annot_stat[annot] += 1

                if end1 < st:
                    break

            idx2 = bisect.bisect_right(start_arr, start2) - 1

            for i in range(idx2, len(start_arr)):
                annot = annot_arr[i]

                # if annot in find_annot:
                #     continue

                st = start_arr[i]
                ed = end_arr[i]

                if st <= start2 < ed:
                    annot_stat[annot] += 1
                    # find_annot.append(annot)
                elif st <= end2 < ed:
                    # find_annot.append(annot)
                    annot_stat[annot] += 1
                elif start2 < st and ed <= end2:
                    # find_annot.append(annot)
                    annot_stat[annot] += 1

                if end2 < st:
                    break

    for key in sorted(annot_stat.keys(), key=natural_keys):
        print("{}".format(annot_stat[key] / annot_total[key]))

    # stop = timeit.default_timer()
    # print('Time: ', stop - start)
    # print()


if __name__ == '__main__':
    # fithic_file = '/Users/bcchanaka/PycharmProjects/HiC-DataProcess/fithic-krnorm-bias/fithic-res-Original/Processed-0.01/merged/hESC.txt'
    file_path1 = '/Users/bcchanaka/PycharmProjects/HiC-DataProcess/annotations-process/wgEncodeBroadHmmH1hescHMM-hg18.bed'
    file_path2 = '/Users/bcchanaka/PycharmProjects/HiC-DataProcess/annotations-process/segway_h1hesc-hg18.bed'
    file_path3 = '/Users/bcchanaka/PycharmProjects/HiC-DataProcess/annotations-process/E017_15_coreMarks_mnemonics-hg18.bed'
    # #
    # main_persite(file_path3, fithic_file)

    # for i in (0.05, 0.01):
    #     for j in ('fithic-intra', 'fithic-krnorm-bias'):
    #         for k in ('fithic-res-Original', 'fithic-res-Merged', 'fithic-mHiC', 'fithic-mHiC-our', 'fithic-mHiC-unique'):
    #             fithic_file = '/Users/bcchanaka/PycharmProjects/HiC-DataProcess/' + j + '/' + k + '/Processed-' + str(
    #                 i) + '/merged/IMR90.txt'
    #             # main_persite(file_path3, fithic_file)
    #             main_perlabel(file_path3, fithic_file)

    # for l in (file_path1, file_path2):
    # for l in (file_path1,):
    #     for i in (0.01,):
    #         for j in ('fithic-krnorm-bias',):
    #             for k in (
    #             'fithic-res-Original', 'fithic-res-Merged', 'fithic-mHiC', 'fithic-mHiC-our', 'fithic-mHiC-unique'):
    #                 fithic_file = '/Users/bcchanaka/PycharmProjects/HiC-DataProcess/' + j + '/' + k + '/Processed-' + str(
    #                     i) + '/merged/hESC.txt'
    #                 main_persite(l, fithic_file)
    # main_perlabel(l, fithic_file)

    # print("per label ---------------------------------------------------------------------------------------------------------")

    # for l in (file_path3,):
    #     for i in (0.05, 0.01):
    #         for j in ('fithic-intra', 'fithic-krnorm-bias'):
    #             for k in (
    #             'fithic-res-Original', 'fithic-res-Merged', 'fithic-mHiC', 'fithic-mHiC-our', 'fithic-mHiC-unique'):
    #                 fithic_file = '/Users/bcchanaka/PycharmProjects/HiC-DataProcess/' + j + '/' + k + '/Processed-' + str(
    #                     i) + '/merged/IMR90.txt'
    #                 # main_persite(l, fithic_file)
    #                 main_perlabel(l, fithic_file)

    # for i in (0.05, 0.01):
    #     j = 'hESC'
    #     fithic_file = 'fithic-comparison/krnorm/mHiC-mHiCour/mHiC-mHiCour/Processed-' + str(
    #         i) + '/' + j + '-' + j + '-common.txt'
    #     main_perlabel(file_path1, fithic_file)
    #
    #     fithic_file = 'fithic-comparison/krnorm/mHiC-mHiCour/mHiC-mHiCour/Processed-' + str(
    #         i) + '/' + j + '-mHiC-unique.txt'
    #     main_perlabel(file_path1, fithic_file)
    #
    #     fithic_file = 'fithic-comparison/krnorm/mHiC-mHiCour/mHiC-mHiCour/Processed-' + str(
    #         i) + '/' + j + '-mHiCour-unique.txt'
    #     main_perlabel(file_path1, fithic_file)
    #
    #     j = 'IMR90'
    #     fithic_file = 'fithic-comparison/krnorm/mHiC-mHiCour/mHiC-mHiCour/Processed-' + str(
    #         i) + '/' + j + '-' + j + '-common.txt'
    #     main_perlabel(file_path3, fithic_file)
    #
    #     fithic_file = 'fithic-comparison/krnorm/mHiC-mHiCour/mHiC-mHiCour/Processed-' + str(
    #         i) + '/' + j + '-mHiC-unique.txt'
    #     main_perlabel(file_path3, fithic_file)
    #
    #     fithic_file = 'fithic-comparison/krnorm/mHiC-mHiCour/mHiC-mHiCour/Processed-' + str(
    #         i) + '/' + j + '-mHiCour-unique.txt'
    #     main_perlabel(file_path3, fithic_file)

    for i in ('fithic-hiclib-random', 'fithic-mHiC-random'):
        for j in (0.05, 0.01):
            fithic_file = 'fithic-krnorm-bias/' + i + '/Processed-' + str(j) + '/merged/hESC.txt'
            main_persite(file_path1, fithic_file)
            main_persite(file_path2, fithic_file)

            fithic_file = 'fithic-krnorm-bias/' + i + '/Processed-' + str(j) + '/merged/IMR90.txt'
            main_persite(file_path3, fithic_file)
