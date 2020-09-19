def main():
    chrLens ="/Users/bcchanaka/PycharmProjects/HiC-DataProcess/metadata/chrom.sizes.test"
    with open(chrLens, 'r') as infile:
        for line in infile:
            ## for each chromosome
            chrom, chrL = line.split()
            print(chrom,chrL)


if __name__ == '__main__':
    main()
