#!/bin/bash
for i in {1..22}
do
   python __main__.py --data chr${i}
done

python __main__.py --data chrX