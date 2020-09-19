#!/bin/bash

for i in hESC_r1 hESC_r2 IMR90_r1 IMR90_r2; do
  python /gpfs1/scratch/chanaka.cooray/jobs/fastq-jobs/Contact-Matrix/mHiC/bin/KR_norm_mHiC.py -r 40000 -l /gpfs1/scratch/chanaka.cooray/jobs/fastq-jobs/Contact-Matrix/mHiC-res/metadata/hg18_chrom_sizes.txt -c whole -tr 10 -f $i.validPairs.binPairCount.uni -o krnorm
done
