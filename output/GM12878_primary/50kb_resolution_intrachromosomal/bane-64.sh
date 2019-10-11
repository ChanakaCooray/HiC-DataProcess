#!/bin/bash
for i in {18..22}
do
   python /Users/bcchanaka/Desktop/RA/tools/BANE/src/main.py --edge-path TADW-BANE-input/chr${i}-output.csv --feature-path features/chr${i}-features.csv --output-path BANE-output-64/chr${i}.csv --features dense --dimensions 64
done

python /Users/bcchanaka/Desktop/RA/tools/BANE/src/main.py --edge-path TADW-BANE-input/chr13-output.csv --feature-path features/chr13-features.csv --output-path BANE-output-64/chr13.csv --features dense --dimensions 64