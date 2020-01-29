import matplotlib

matplotlib.use('agg')
import matplotlib.pyplot as plt
import numpy as np
from hiclib import binnedData
from mirnylib import genome
from mirnylib import h5dict
from mirnylib import plotting


def main():
    resolution_str = '1M'
    type = 'hESC-r1'

    genome_db = genome.Genome('../../chromosomes/')

    # Read resolution from the dataset.
    raw_heatmap = h5dict.h5dict('heatmap-res-' + resolution_str + '.hdf5', mode='r')
    resolution = int(raw_heatmap['resolution'])

    # Create a binnedData object, load the data.
    BD = binnedData.binnedData(resolution, genome_db)
    BD.simpleLoad('heatmap-res-' + resolution_str + '.hdf5', 'HindIII_GM_1')

    # Remove the contacts between loci located within the same bin.
    # BD.removeDiagonal()

    # Remove bins with less than half of a bin sequenced.
    BD.removeBySequencedCount(0.5)

    # Remove 1% of regions with low coverage.
    BD.removePoorRegions(cutoff=1)

    # Truncate top 0.05% of interchromosomal counts (possibly, PCR blowouts).
    BD.truncTrans(high=0.0005)

    # Perform iterative correction.
    BD.iterativeCorrectWithoutSS()

    # Save the iteratively corrected heatmap.
    BD.export('HindIII_GM_1', 'IC-heatmap-res-' + resolution_str + '.hdf5')

    # Plot the heatmap directly.
    print(BD.dataDict.keys())
    plotting.plot_matrix(np.log(BD.dataDict['HindIII_GM_1']))

    # plt.show()
    plt.savefig('heatmap-' + type + '-' + resolution_str + '.png')


if __name__ == '__main__':
    main()
