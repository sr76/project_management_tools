import os
from lxml import etree
projectsdir="/home1/srigamonti/projects"


def runsarr():
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
                    cmds="ln -sfn %s/ %s"%(root+"/"+run,root+"/"+str(runst[str(run)]))
                    os.system(cmds)


    #    if sroot[srootlen-1]=="projects":
    #        projects=dirs

        status = ""
        importance = ""
        if sroot[srootlen-2]=="runs":
            name=root+"/input.xml"
            if os.path.isfile(name):
                tree = etree.parse(name)
                if tree.xpath('/input/keywords'):
                    description=tree.xpath('/input/keywords')[0].text
                    notes=""
                    if tree.xpath('/input/keywords/description'):
                        description=description + tree.xpath('/input/keywords/description')[0].text
                    if tree.xpath('/input/keywords/status'):
                        status=tree.xpath('/input/keywords/status')[0].text
                    if tree.xpath('/input/keywords/importance'):
                        importance=tree.xpath('/input/keywords/importance')[0].text
                    if tree.xpath('/input/keywords/notes'):
                        notes=notes + tree.xpath('/input/keywords/notes')[0].text
                else:
                    description="No metadata"
            else:
                description="NO INPUT.XML FILE"

            tstamp=int(sroot[srootlen-1])

            s_project=sroot[srootlen-3]
            s_tstamp=str(tstamp)
            s_index=runst[str(tstamp)]
            s_description=description
            s_path=root
            s_status=status.strip()
            s_importance=importance.strip()
            s_notes=notes

            runsarr.append([s_project,s_tstamp,s_index,s_description,s_path,s_status,s_importance,s_notes])

    return runsarr

    #    print root, dirs, files


