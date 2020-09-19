#!/bin/bash

for i in hESC_r1 hESC_r2 IMR90_r1 IMR90_r2; do
  fithic -r 40000 -l "$i" -f $i.uni.fragments.mHiC.gz -i krnorm/$i.validPairs.binPairCount.uni.KRnorm.gz -L 50000 -U 5000000 -b 100 -p 1 -o ../fithic-krnorm-bias/fithic-mHiC/$i -t krnorm/$i.validPairs.binPairCount.uni.KRnorm.bias.gz
done
