#!/bin/bash


CLIENTS="10"
PORT="5222"
QUERYFILE="/home/Norman.Rzepka/tpcc/queries_gen/1W_neworder_1M.txt"
TABLEDIR="/home/Norman.Rzepka/tpcc/1W-tables/"
DURATION="300"
VERBOSE="1"
THREADS="10"
NODES="0"
MEMORY_NODES="0"
PARAMETER="--ab=$QUERYFILE --clients=$CLIENTS --threads=$THREADS --abCore=22 --port=$PORT --tabledir=$TABLEDIR --duration=$DURATION --verbose=$VERBOSE --stdout --stderr"
