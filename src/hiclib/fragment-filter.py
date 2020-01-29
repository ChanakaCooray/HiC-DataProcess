from hiclib import fragmentHiC
from mirnylib import genome


def main():
    # Create a HiCdataset object.
    resolution_size = 1000000
    resolution_str = '1M'

    genome_db = genome.Genome('../../chromosomes/')
    fragments = fragmentHiC.HiCdataset(
        filename='fragment_dataset.hdf5',
        genome=genome_db,
        maximumMoleculeLength=500,
        mode='w', enzymeName='HindIII')

    # Load the parsed reads into the HiCdataset. The dangling-end filter is applied
    # at this stage, with maximumMoleculeLength specified at the initiation of the
    # object.
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
