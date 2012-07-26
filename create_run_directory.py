import time
import os
import sys

def create_run_directory():
    scwd = str(os.getcwd())

    sscwd = scwd.split("/")
    if sscwd[len(sscwd)-1]!="runs":
        print "You are not in a runs directory"
        sys.exit()

    sstamp = str(int(time.time()*1000))
    srundir = scwd+"/"+sstamp
    os.system("mkdir %s"%(srundir))
    return sstamp,srundir



