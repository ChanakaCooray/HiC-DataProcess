#!/bin/bash
for i in {1..22}
do
   /Users/bcchanaka/Desktop/RA/tools/LINE/linux/line-mac -train line-input/chr${i}.output -output line-output-128/chr${i}.emb -size 128
done

/Users/bcchanaka/Desktop/RA/tools/LINE/linux/line-mac -train line-input/chrX.output -output line-output-128/chrX.emb -size 128
