#!/bin/bash

for i in hESC-r1 hESC-r2 IMR90-r1 IMR90-r2; do
  python ../../fithic/fithic/utils/HiCKRy.py -f Original/frag-40k.txt.gz -i Original/$i-interact-40k.txt.gz -o Original/$i-bias.gz
done

for i in hESC-r1 hESC-r2 IMR90-r1 IMR90-r2; do
  python ../../fithic/fithic/utils/HiCKRy.py -f Merged/frag-40k.txt.gz -i Merged/$i-interact-40k.txt.gz -o Merged/$i-bias.gz
done