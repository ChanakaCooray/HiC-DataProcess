#!/bin/bash
for i in {1..22}
do
   python /Users/bcchanaka/Desktop/RA/tools/TADW/src/main.py --edge-path TADW-BANE-input/chr${i}-output.csv --feature-path features/chr${i}-features.csv --output-path TADW-output-2/chr${i}.csv --features dense --dimensions 1
done

python /Users/bcchanaka/Desktop/RA/tools/TADW/src/main.py --edge-path TADW-BANE-input/chrX-output.csv --feature-path features/chrX-features.csv --output-path TADW-output-2/chrX.csv --features dense --dimensions 1