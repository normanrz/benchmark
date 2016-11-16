#!/bin/bash

set -e

if [[ -e results/tpcc_single_run/\{\}/None/ab.log ]]; then
  rm results/tpcc_single_run/\{\}/None/ab.log
fi
for i in {1..32}
do
  echo $i threads
  python exp_tpcc_single_run.py --ab=/home/Norman.Rzepka/tpcc/queries_gen/10W_1M.txt --clients=10 --threads=$i --abCore=22 --port=5222 --tabledir=/home/Norman.Rzepka/tpcc/10W-tables/ --duration=60 --verbose=1 --stdout --stderr
#  mv results/tpcc_single_run/\{\}/None/ab.log results/tpcc_single_run/\{\}/None/ab_threads_$i.log
  rm results/tpcc_single_run/\{\}/None/ab.log
done

