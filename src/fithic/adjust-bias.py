def main():
    file_path = '/Users/bcchanaka/PycharmProjects/HiC-DataProcess/fithic-res/Original/hESC-r1-bias'
    output_file = '/Users/bcchanaka/PycharmProjects/HiC-DataProcess/fithic-res/Original/common-bias'

    output = open(output_file, 'w')
    with open(file_path, 'r') as f:
        for line in f:
            parts = line.split()
            output.write("{}\t{}\t{}\n".format(parts[0], parts[1], 1))

    output.close()


if __name__ == '__main__':
    main()
