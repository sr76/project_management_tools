#!/usr/bin/python
import create_run_directory
import sys
import runsarr
import os
from lxml import etree

scwd = str(os.getcwd()).split("/")
if scwd[len(scwd)-1]!="runs":
    print "You are not in a runs directory"
    sys.exit()

narg=len(sys.argv)

if narg > 2:
    print "Number of arguments greater than 1"
    sys.exit()

runs=runsarr.runsarr()

for run in runs:
    s_project=run[0]
    s_tstamp=run[1]
    index=int(run[2])
    s_description=run[3]
    s_path=run[4]
    s_status=run[5]
    s_importance=run[6]

    if index==int(sys.argv[1]):
        print "********** CLONE FROM *****************"
        print "PROJECT:",s_project
        print "TSTAMP:",s_tstamp
        print "INDEX:",index
        print "DESCRIPTION:", s_description
        print "PATH:", s_path
        print "***************************************\n"

        tstamp,srundir = create_run_directory.create_run_directory()

        if os.path.isfile(s_path+"/input.xml"):
            #os.system("cp %s/input.xml %s"%(s_path,srundir))
            name=s_path+"/input.xml"
            root = etree.parse(name).getroot()
            for child in root:
                if child.tag=="keywords":
                    child.text=s_description+"\n*** Run cloned from %s ***\n"%(s_path)
            s_input=etree.tostring(root, pretty_print="true")
            f=open(srundir+"/input.xml","w")
            f.write(s_input)
            f.close()
        else:
            description="NO INPUT.XML FILE"

        sys.exit()
