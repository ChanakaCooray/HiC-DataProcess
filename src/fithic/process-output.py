import gzip
import os


def main(name, threshold, type):
    print("Processing " + name + ", " + str(threshold) + ", " + type)
    # file_path = '/Users/bcchanaka/PycharmProjects/HiC-DataProcess/fithic-res/fithic-out/out-40k/' + type + '/' + name + '/' + name + '.spline_pass1.res40000.significances.txt.gz'
    # output_dir = '/Users/bcchanaka/PycharmProjects/HiC-DataProcess/fithic-res/fithic-out/out-40k/Processed-' + str(
    #     threshold) + '/' + type
    # file_path = '/Users/bcchanaka/PycharmProjects/HiC-DataProcess/fithic-mHiC-uni/fithic-out/' + name + '/' + name + '.spline_pass1.res40000.significances.txt.gz'
    # output_dir = '/Users/bcchanaka/PycharmProjects/HiC-DataProcess/fithic-mHiC-uni/fithic-out/Processed-' + str(threshold)

    # file_path = '/Users/bcchanaka/PycharmProjects/HiC-DataProcess/hic-explorer/hESC-r1/hESC-r1.spline_pass1.res40000.significances.txt.gz'
    # output_dir = '/Users/bcchanaka/PycharmProjects/HiC-DataProcess/hic-explorer/temp/out'

    # file_path = '/Users/bcchanaka/PycharmProjects/HiC-DataProcess/fithic-mHiC-uni/fithic-out/' + name + '/' + name + '.spline_pass1.res40000.significances.txt.gz'
    # output_dir = '/Users/bcchanaka/PycharmProjects/HiC-DataProcess/fithic-mHiC-uni/fithic-out/Processed-' + str(threshold)

    # file_path = '/Users/bcchanaka/PycharmProjects/HiC-DataProcess/fithic-res/fithic-out/out-40k/Original/hESC-r1/hESC-r1.spline_pass1.res40000.significances.txt.gz'
    # output_dir = '/Users/bcchanaka/PycharmProjects/HiC-DataProcess/fithic-res/fithic-out/out-40k/Processed-' + str(
    #     threshold) + '/Original'

    file_path = '/Users/bcchanaka/PycharmProjects/HiC-DataProcess/fithic-krnorm-bias/' + type + '/' + name + '/' + name + '.spline_pass1.res40000.significances.txt.gz'
    output_dir = '/Users/bcchanaka/PycharmProjects/HiC-DataProcess/fithic-krnorm-bias/' + type + '/Processed-' + str(
        threshold)

    # file_path = '/Users/bcchanaka/PycharmProjects/HiC-DataProcess/fithic-res/Original/krnorm/fithic-out-2/FitHiC.spline_pass1.res40000.significances.txt.gz'
    # output_dir = '/Users/bcchanaka/PycharmProjects/HiC-DataProcess/fithic-res/Original/krnorm/fithic-out-2/Processed-' + str(threshold)

    output_file = output_dir + '/' + name + '.txt'

    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    f_output = open(output_file, "w")

    with gzip.open(file_path, 'r') as f:
        next(f)
        for line in f:
            parts = line.split()
            q_value = parts[6]

            # if float(q_value)==0:
            #     print(parts[0].decode("utf-8"))
            #     print(parts[1])

            if float(q_value) < threshold:
                # if parts[0].decode("utf-8") != 'chrM' and parts[2].decode("utf-8") != 'chrM':
                f_output.write(line.decode("utf-8"))

    f_output.close()


if __name__ == '__main__':
    # for i in ('hESC-r1', 'hESC-r2', 'IMR90-r1', 'IMR90-r2'):
    #     for k in (0.01, 0.001, 0.0001, 0.00001):
    #         main(i, k, 'fithic-res-Original')
    #         main(i, k, 'fithic-res-Merged')
    #
    # for i in ('hESC_r1', 'hESC_r2', 'IMR90_r1', 'IMR90_r2'):
    #     for k in (0.01, 0.001, 0.0001, 0.00001):
    #         main(i, k, 'fithic-mHiC')
    #         main(i, k, 'fithic-mHiC-our')
    #         main(i, k, 'fithic-mHiC-unique')

    # for i in ('hESC-r1', 'hESC-r2', 'IMR90-r1', 'IMR90-r2'):
    #     for k in (0.05,):
    #         main(i, k, 'fithic-res-Original')
    #         main(i, k, 'fithic-res-Merged')

    for i in ('hESC_r1', 'hESC_r2', 'IMR90_r1', 'IMR90_r2'):
        for j in (0.05, 0.01, 0.001, 0.0001, 0.00001):
            for k in ('fithic-hiclib-random', 'fithic-mHiC-random'):
                main(i, j, k)

    # main('hESC-r1', 0.01, 'aaa')
