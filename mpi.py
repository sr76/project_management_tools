#!/usr/bin/python
import os
import sys
import socket

narg=len(sys.argv)

if narg != 3:
    print "Number of arguments different from 2. \n Usage:\n $>mpi.py NP NNODE\nThis will execute the command 'mpirun -np NP excitingmpi' in machine solNNODE.physik.hu-berlin.de\nExit without executing"
    sys.exit()

scwd = str(os.getcwd()).split("/")
if len(scwd[-1])!=13 and scwd[-2]!="runs":
    print "You must be inside the run directory where the input.xml is located to run this script. Exiting without executing."
    sys.exit()

np=sys.argv[1]
node_name="sol"+sys.argv[2]


hostname = socket.gethostname()

exciting_root="/home1/srigamonti/exciting"


pbs_str="""#!/bin/bash
#PBS -l nodes=NNODE:ppn=NP
#PBS -N NAME
scdir=/home1/srigamonti/excitingruns/$PBS_JOBID
mkdir -p $scdir
cp $PBS_O_WORKDIR/* $scdir
COPYLINE
cp -r /home1/srigamonti/exciting/species $scdir
cd $scdir
RUNLINE
cp -r * $PBS_O_WORKDIR
"""
pbs_str=pbs_str.replace("NNODE",node_name)
pbs_str=pbs_str.replace("NP",np)
pbs_str=pbs_str.replace("NAME",scwd[-1])
if np>1:
    pbs_str=pbs_str.replace("RUNLINE","mpirun -np %s excitingmpi > RUN.OUT"%(np))
    pbs_str=pbs_str.replace("COPYLINE","cp /home1/srigamonti/exciting/bin/excitingmpi $scdir")
if np==1:
    pbs_str=pbs_str.replace("RUNLINE","excitingser > RUN.OUT"%(np))
    pbs_str=pbs_str.replace("COPYLINE","cp /home1/srigamonti/exciting/bin/excitingser $scdir")

print pbs_str

f=open("RUN.sh","w")
f.write(pbs_str)
f.close()

os.system("chmod +x+u RUN.sh")
os.system("qsub RUN.sh")







