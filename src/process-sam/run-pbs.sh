#!/bin/bash

for i in {1..16}
do
qsub python-process-ambiguous-$i.pbs
done
