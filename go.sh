#!/bin/bash

./run_threads_benchmark.sh | tee >(gzip --stdout > logs/output_`git rev-parse HEAD`.log.gz) | grep -E "threads|PID|Complete|Non-2xx"