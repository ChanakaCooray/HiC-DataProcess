#!/bin/bash

for i in hESC_r1 hESC_r2 IMR90_r1 IMR90_r2; do
  fithic -r 40000 -l "$i" -f $i.uni.fragments.mHiC.gz -i $i.validPairs.binPairCount.uni.gz -L 50000 -U 5000000 -b 100 -p 1 -o ../fithic-intra-common-bias/fithic-mHiC-unique/$i -t common-bias.gz
done
