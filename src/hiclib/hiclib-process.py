import logging

from hiclib import fragmentHiC
from hiclib import mapping
from mirnylib import h5dict, genome


# main func
def main():
    mapped_reads = h5dict.h5dict('mapped_reads.hdf5')
    logging.basicConfig(level=logging.DEBUG)

    genome_db = genome.Genome('../../chromosomes/')

    mapping.parse_sam(
        sam_basename1='hESC_r1_1',
        sam_basename2='hESC_r1_2',
        out_dict=mapped_reads,
        genome_db=genome_db,
        enzyme_name='HindIII')

    # Create a HiCdataset object.
    resolution_size = 40000
    resolution_str = '40k'

    fragments = fragmentHiC.HiCdataset(
        filename='fragment_dataset.hdf5',
        genome=genome_db,
        maximumMoleculeLength=500,
        mode='w', enzymeName='HindIII')

    fragments.parseInputData(
        dictLike='mapped_reads.hdf5')

    fragments.filterRsiteStart(offset=5)
    fragments.filterDuplicates()
    # fragments.filterLarge()
    fragments.filterExtreme(cutH=0.005, cutL=0)

    fragments.saveHeatmap('heatmap-res-' + resolution_str + '.hdf5', resolution=resolution_size)
    fragments.printMetadata(saveTo='statistics-' + resolution_str + '.txt')


if __name__ == '__main__':
    main()
