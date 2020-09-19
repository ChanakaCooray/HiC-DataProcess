#!/bin/bash

for i in hESC-r1 hESC-r2 IMR90-r1 IMR90-r2; do
  fithic -r 40000 -l "$i" -f Original/frag-40k.txt.gz -i Original/$i-interact-40k.txt.gz -L 50000 -U 5000000 -b 100 -p 1 -o ../fithic-intra-bias/fithic-res-Original/$i -t Original/$i-bias.gz
done

for i in hESC-r1 hESC-r2 IMR90-r1 IMR90-r2; do
  fithic -r 40000 -l "$i" -f Merged/frag-40k.txt.gz -i Merged/$i-interact-40k.txt.gz -L 50000 -U 5000000 -b 100 -p 1 -o ../fithic-intra-bias/fithic-res-Merged/$i -t Merged/$i-bias.gz
done