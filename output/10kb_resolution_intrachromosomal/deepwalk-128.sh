#!/bin/bash
for i in {1..22}
do
   deepwalk --input deepwalk-input/chr${i}.output --output deepwalk-output-128/chr${i}.emb --format edgelist --representation-size 128
done
