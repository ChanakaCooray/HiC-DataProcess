import logging

from hiclib import mapping
from mirnylib import h5dict, genome


# main func
def main():
    mapped_reads = h5dict.h5dict('mapped_reads.hdf5')
    logging.basicConfig(level=logging.DEBUG)

    genome_db = genome.Genome('../../chromosomes/')
    # a = hiclib.mapping.parse_sam('hESC_r1_1', 'hESC_r1_2', mapped_reads, genome_db,enzyme_name='HindIII')

    mapping.parse_sam(
        sam_basename1='hESC_r1_1',
        sam_basename2='hESC_r1_2',
        out_dict=mapped_reads,
        genome_db=genome_db,
        enzyme_name='HindIII')

    # print(a)


if __name__ == '__main__':
    main()
