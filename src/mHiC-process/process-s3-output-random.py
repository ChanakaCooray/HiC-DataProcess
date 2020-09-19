import random
from argparse import ArgumentParser, ArgumentDefaultsHelpFormatter


def main():
    parser = ArgumentParser("process-split-files",
                            formatter_class=ArgumentDefaultsHelpFormatter,
                            conflict_handler='resolve')
    parser.add_argument("--input", default='None')
    parser.add_argument("--output", default='None')
    args = parser.parse_args()
    input_file = args.input
    output_file = args.output

    curr_read = ""
    curr_reads = []

    output_f = open(output_file, "w")

    count_unique = 0
    count_all = 0

    with open(input_file) as f:
        for line in f:
            read_id = line.split()[0]
            if curr_read == "":
                curr_reads.append(line)
                curr_read = read_id
            elif curr_read == read_id:
                curr_reads.append(line)
            elif curr_read != read_id:
                count_all += 1
                result = process_read(curr_reads, output_f)

                if result:
                    count_unique += 1

                curr_read = read_id
                curr_reads = [line]

    count_all += 1
    result = process_read(curr_reads, output_f)

    if result:
        count_unique += 1

    # process_sam(sam_dic, fragment_dic, output_file)
    output_f.close()

    print("Multi Processed count: " + str(count_unique))
    print("All count: " + str(count_all))


def process_read(reads, output_sam):
    if len(reads) == 1:
        output_sam.write(reads[0])
        return False

    output_sam.write(random.choice(reads).replace("MULTI", "UNI"))
    return True


if __name__ == '__main__':
    main()
