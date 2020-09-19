#!/bin/bash

for i in hESC-r1 hESC-r2 IMR90-r1 IMR90-r2; do
  fithic -r 40000 -l "$i" -f Original/frag-40k.txt.gz -i Original/krnorm/$i-interact-40k.txt.KRnorm.gz -L 50000 -U 5000000 -b 100 -p 1 -o ../fithic-krnorm-bias/fithic-res-Original/$i -t Original/krnorm/$i-interact-40k.txt.KRnorm.bias.gz
done

for i in hESC-r1 hESC-r2 IMR90-r1 IMR90-r2; do
  fithic -r 40000 -l "$i" -f Original/frag-40k.txt.gz -i Merged/krnorm/$i-interact-40k.txt.KRnorm.gz -L 50000 -U 5000000 -b 100 -p 1 -o ../fithic-krnorm-bias/fithic-res-Merged/$i -t Merged/krnorm/$i-interact-40k.txt.KRnorm.bias.gz
done