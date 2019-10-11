#!/bin/bash
for i in {1..22}
do
   deepwalk --input deepwalk-input/chr${i}.output --output deepwalk-output-2/chr${i}.emb --format edgelist --representation-size 2
done

deepwalk --input deepwalk-input/chrX.output --output deepwalk-output-2/chrX.emb --format edgelist --representation-size 2