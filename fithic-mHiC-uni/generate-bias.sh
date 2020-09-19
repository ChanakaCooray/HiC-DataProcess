#!/bin/bash

for i in hESC_r1 hESC_r2 IMR90_r1 IMR90_r2; do
  python ../../fithic/fithic/utils/HiCKRy.py -f $i.uni.fragments.mHiC.gz -i $i.validPairs.binPairCount.uni.gz -o $i-bias.gz
done