all: run1 

run1:
	python3 cache_simulator.py -s 128 -a 16 -b 64 -file 400.perlbench-41B.trace.txt
	python3 cache_simulator.py -s 128 -a 16 -b 64 -file 401.bzip2-226B.trace.txt
	python3 cache_simulator.py -s 128 -a 16 -b 64 -file 403.gcc-16B.trace.txt
	python3 cache_simulator.py -s 128 -a 16 -b 64 -file 410.bwaves-1963B.trace.txt
	python3 cache_simulator.py -s 128 -a 16 -b 64 -file 416.gamess-875B.trace.txt
	python3 cache_simulator.py -s 128 -a 16 -b 64 -file 429.mcf-184B.trace.txt
	python3 cache_simulator.py -s 128 -a 16 -b 64 -file 433.milc-127B.trace.txt
	python3 cache_simulator.py -s 128 -a 16 -b 64 -file 435.gromacs-111B.trace.txt
	python3 cache_simulator.py -s 128 -a 16 -b 64 -file 436.cactusADM-1804B.trace.txt
	python3 cache_simulator.py -s 128 -a 16 -b 64 -file 437.leslie3d-134B.trace.txt
	python3 cache_simulator.py -s 128 -a 16 -b 64 -file 444.namd-120B.trace.txt
	python3 cache_simulator.py -s 128 -a 16 -b 64 -file 445.gobmk-17B.trace.txt
	python3 cache_simulator.py -s 128 -a 16 -b 64 -file 450.soplex-247B.trace.txt
	python3 cache_simulator.py -s 128 -a 16 -b 64 -file 453.povray-887B.trace.txt
	python3 cache_simulator.py -s 128 -a 16 -b 64 -file 454.calculix-104B.trace.txt
	python3 cache_simulator.py -s 128 -a 16 -b 64 -file 456.hmmer-191B.trace.txt
	python3 cache_simulator.py -s 128 -a 16 -b 64 -file 458.sjeng-1088B.trace.txt
	python3 cache_simulator.py -s 128 -a 16 -b 64 -file 459.GemsFDTD-1169B.trace.txt
	python3 cache_simulator.py -s 128 -a 16 -b 64 -file 462.libquantum-1343B.trace.txt
	python3 cache_simulator.py -s 128 -a 16 -b 64 -file 464.h264ref-30B.trace.txt
	python3 cache_simulator.py -s 128 -a 16 -b 64 -file 465.tonto-1769B.trace.txt
	python3 cache_simulator.py -s 128 -a 16 -b 64 -file 470.lbm-1274B.trace.txt
	python3 cache_simulator.py -s 128 -a 16 -b 64 -file 471.omnetpp-188B.trace.txt
	python3 cache_simulator.py -s 128 -a 16 -b 64 -file 473.astar-153B.trace.txt
	python3 cache_simulator.py -s 128 -a 16 -b 64 -file 481.wrf-1170B.trace.txt
	python3 cache_simulator.py -s 128 -a 16 -b 64 -file 482.sphinx3-1100B.trace.txt
	python3 cache_simulator.py -s 128 -a 16 -b 64 -file 483.xalancbmk-127B.trace.txt
















