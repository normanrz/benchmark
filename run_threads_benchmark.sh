#!/bin/bash

set -e

: ${LOWER_THREADS:=1}
: ${UPPER_THREADS:=$(($(nproc)/2))}

if [[ -e results/tpcc_single_run/\{\}/None/ab.log ]]; then
  rm results/tpcc_single_run/\{\}/None/ab.log
fi
for i in $(seq ${LOWER_THREADS} ${UPPER_THREADS})
do
  echo $i threads
  python exp_tpcc_single_run.py --ab=/home/Norman.Rzepka/tpcc/queries_gen/20W_1M.txt --clients=10000 --threads=$i --abCore=22 --port=5222 --tabledir=/home/Norman.Rzepka/tpcc/20W-tables/ --duration=60 --verbose=1 --stdout --stderr
  mv results/tpcc_single_run/\{\}/None/ab.log results/tpcc_single_run/\{\}/None/ab_threads_$(printf "%02d" $i).log
#  rm results/tpcc_single_run/\{\}/None/ab.log
done

