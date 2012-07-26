#!/usr/bin/python

import os
from lxml import etree

projectsdir="/home1/srigamonti/projects"

iruns=[]
for root, dirs, files in os.walk(projectsdir):
    sroot=root.split("/")
    srootlen=len(sroot)
    if sroot[srootlen-1]=="runs":
        for run in dirs:
            if len(run)==13:
                iruns.append(int(run))
iruns.sort()

runsi={}
runst={}
for i,r in enumerate(iruns):
    runst[str(r)]=i
    runsi[i]=str(r)

runsarr=[]

for root, dirs, files in os.walk(projectsdir):
    sroot=root.split("/")
    srootlen=len(sroot)
    
    #Create symbolic links to run directories
    if sroot[srootlen-1]=="runs":
        for run in dirs:
            if len(run)==13:
                print root
                print root+"/"+run
                print root+"/"+str(runst[str(run)])
                cmds="ln -sfn %s/ %s"%(root+"/"+run,root+"/"+str(runst[str(run)]))
                print cmds
                os.system(cmds)


#    if sroot[srootlen-1]=="projects":
#        projects=dirs


    if sroot[srootlen-2]=="runs":
        print "***************************"
        name=root+"/input.xml"
        if os.path.isfile(name):
            tree = etree.parse(name)
            description=tree.xpath('/input/keywords')[0].text
        else:
            description="NO INPUT.XML FILE"

        tstamp=int(sroot[srootlen-1])
        
        s_project=sroot[srootlen-3]
        s_tstamp=str(tstamp)
        s_index=runst[str(tstamp)]
        s_description=description

        print "PROJECT:",s_project
        print "TSTAMP:",s_tstamp
        print "INDEX:",s_index
        print "DESCRIPTION:", s_description

        print "***************************\n"
        runsarr.append([s_project,s_tstamp,s_index,s_description])


#    print root, dirs, files


