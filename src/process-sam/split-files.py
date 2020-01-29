from collections import defaultdict


def main():
    sam_file = "/Users/bcchanaka/PycharmProjects/HiC-DataProcess/HiC-RAW/hESC-r1-1-m20.sam"
    output_sam_prefix = "/Users/bcchanaka/PycharmProjects/HiC-DataProcess/HiC-RAW/hESC-r1-1-m20"
    sam_dic = defaultdict(list)

    header = []

    count_sam = 0
    with open(sam_file) as f:
        for _ in range(27):
            header.append(f.readline())
        for line in f:
            read_id = line.split()[0]
            sam_dic[read_id].append(line)
            count_sam += 1

    print(count_sam)

    process_sam(sam_dic, output_sam_prefix)
    # output_sam.close()


def process_sam(sam_dic, output_sam_prefix):
    output_dic = {}

    print(len(sam_dic))
    count_unique = 0
    count_all = 0
    for key, value in sam_dic.items():
        if len(value) == 1:
            continue
        i = count_unique // 2000000
        output_sam_file = output_sam_prefix + "-part-" + str(i)
        if not (output_sam_file in output_dic):
            output_dic[output_sam_file] = open(output_sam_file, "w")

        output_sam = output_dic[output_sam_file]

        for read in value:
            output_sam.write(read)
            count_all+=1

        count_unique += 1

    for key, value in output_dic.items():
        value.close()

    print(count_unique)
    print(count_all)


if __name__ == '__main__':
    main()
