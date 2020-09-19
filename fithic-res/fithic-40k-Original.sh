#!/bin/bash

for i in hESC-r1 hESC-r2 IMR90-r1 IMR90-r2; do
  fithic -r 40000 -l "$i" -f Original/frag-40k.txt.gz -i Original/$i-interact-40k.txt.gz -L 50000 -U 5000000 -b 100 -p 1 -o ../fithic-intra/fithic-res-Original/$i
done
