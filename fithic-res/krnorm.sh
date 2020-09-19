#!/bin/bash

for i in hESC-r1 hESC-r2 IMR90-r1 IMR90-r2; do
  python /Users/bcchanaka/PycharmProjects/mHiC/bin/KR_norm_mHiC.py -r 40000 -l /Users/bcchanaka/PycharmProjects/HiC-DataProcess/metadata/hg18_chrom_sizes-new.txt -c whole -tr 10 -f Original/$i-interact-40k.txt -o Original/krnorm
done

for i in hESC-r1 hESC-r2 IMR90-r1 IMR90-r2; do
  python /Users/bcchanaka/PycharmProjects/mHiC/bin/KR_norm_mHiC.py -r 40000 -l /Users/bcchanaka/PycharmProjects/HiC-DataProcess/metadata/hg18_chrom_sizes-new.txt -c whole -tr 10 -f Merged/$i-interact-40k.txt -o Merged/krnorm
done