import argparse
import benchmark
import os

from benchmark.bench_mixed import MixedWLBenchmark


aparser = argparse.ArgumentParser(description='Python implementation of the TPC-C Benchmark for HYRISE')
aparser.add_argument('--duration', default=300, type=int, metavar='D',
                     help='How long to run the benchmark in seconds')
aparser.add_argument('--clients', default=-1, type=int, metavar='N',
                     help='The number of blocking clients to fork (note: this overrides --clients-min/--clients-max')
aparser.add_argument('--clients-min', default=1, type=int, metavar='N',
                     help='The minimum number of blocking clients to fork')
aparser.add_argument('--clients-max', default=1, type=int, metavar='N',
                     help='The maximum number of blocking clients to fork')
aparser.add_argument('--no-load', action='store_true',
                     help='Disable loading the data')
aparser.add_argument('--no-execute', action='store_true',
                     help='Disable executing the workload')
aparser.add_argument('--port', default=5001, type=int, metavar="P",
                     help='Port on which HYRISE should be run')
aparser.add_argument('--threads', default=0, type=int, metavar="T",
                     help='Number of server threadsto use')
aparser.add_argument('--warmup', default=5, type=int,
                     help='Warmuptime before logging is activated')
aparser.add_argument('--manual', action='store_true',
                     help='Do not build and start a HYRISE instance (note: a HYRISE server must be running on the specified port)')
aparser.add_argument('--stdout', action='store_true',
                     help='Print HYRISE server\'s stdout to console')
aparser.add_argument('--stderr', action='store_true',
                     help='Print HYRISE server\'s stderr to console')
aparser.add_argument('--rebuild', action='store_true',
                     help='Force `make clean` before each build')
aparser.add_argument('--regenerate', action='store_true',
                     help='Force regeneration of TPC-C table files')
aparser.add_argument('--perfdata', default=True, action='store_true',
                     help='Collect additional performance data. Slows down benchmark.')
aparser.add_argument('--json', default=False, action='store_true',
                     help='Use JSON queries instead of stored procedures.')
args = vars(aparser.parse_args())

s1 = benchmark.Settings("Standard", PERSISTENCY="NONE", COMPILER="autog++")

kwargs = {
    "port"              : args["port"],
    "manual"            : args["manual"],
    "warmuptime"        : args["warmup"],
    "runtime"           : args["duration"],
    "benchmarkQueries"  : ("xselling",),
    "prepareQueries"    : ("preload_vbap",),
    "showStdout"        : args["stdout"],
    "showStderr"        : args["stderr"],
    "rebuild"           : args["rebuild"],
    "regenerate"        : args["regenerate"],
    "noLoad"            : args["no_load"],
    "serverThreads"     : args["threads"],
    "collectPerfData"   : args["perfdata"],
    "useJson"           : args["json"],
    "hyriseDBPath"      : "/home/Johannes.Wust/hyrise-benchmark/hyrise/test/",
    "scheduler"         : "CoreBoundQueuesScheduler",
    "serverThreads"     : 22
}

runId = str(1)
kwargs["numUsers"] = 30
b1 = MixedWLBenchmark("MixedWLBenchmark", runId, s1, **kwargs)
b1.run()
plotter = benchmark.Plotter("MixedWLBenchmark")
plotter.printStatistics()

kwargs["scheduler"]="WSCoreBoundQueuesScheduler"
runId = str(2)
b2 = MixedWLBenchmark("MixedWLBenchmark", runId, s1, **kwargs)
b2.run()
plotter = benchmark.Plotter("MixedWLBenchmark")
plotter.printStatistics()

kwargs["scheduler"]="CentralScheduler"
runId = str(3)
b3 = MixedWLBenchmark("MixedWLBenchmark", runId, s1, **kwargs)
b3.run()
plotter = benchmark.Plotter("MixedWLBenchmark")
plotter.printStatistics()


kwargs["scheduler"]="ThreadPerTaskScheduler"
runId = str(4)
b4 = MixedWLBenchmark("MixedWLBenchmark", runId, s1, **kwargs)
b4.run()
plotter = benchmark.Plotter("MixedWLBenchmark")
plotter.printStatistics()


#num_clients = args["clients"]
#minClients = args["clients_min"]
#maxClients = args["clients_max"]
#
#
#
#
#if args["clients"] > 0:
#    minClients = args["clients"]
#    maxClients = args["clients"]
#
#for num_clients in xrange(minClients, maxClients+1):
#    runId = "numClients_%s" % num_clients
#    kwargs["numUsers"] = num_clients
#
#    b1 = benchmark.TPCCBenchmark(groupId, runId, s1, **kwargs)
#    b2 = benchmark.TPCCBenchmark(groupId, runId, s2, **kwargs)
#    #b3 = TPCCBenchmark(groupId, runId, s3, **kwargs)
#
#    b1.run()
#    # b2.run()
#    # b3.run()
#
#    if os.path.exists("/mnt/pmfs/hyrise_tpcc"):
#        os.remove("/mnt/pmfs/hyrise_tpcc")
#
##plotter = benchmark.Plotter(groupId)
##plotter.printStatistics()
#
#
