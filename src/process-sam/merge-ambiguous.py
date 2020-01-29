from collections import defaultdict


def main():
    ambiguous_file = "hESC_r1_1_m20_ambiguous.output"
    sam_file = "hESC_r1_1.sam"
    output_sam_file = "hESC_r1_1_merged.sam"

    ambiguous_dic = {}

    with open(ambiguous_file) as f:
        for line in f:
            read_id = line.split()[0]
            ambiguous_dic[read_id] = line

    output_sam = open(output_sam_file, "w")

    with open(sam_file) as f:
        for _ in range(27):
            output_sam.write(f.readline())
        for line in f:
            read_id = line.split()[0]

            if read_id in ambiguous_dic:
                output_sam.write(ambiguous_dic[read_id])
            else:
                output_sam.write(line)

    output_sam.close()


if __name__ == '__main__':
    main()
