#!/usr/bin/python
import create_run_directory


tstamp, srundir = create_run_directory.create_run_directory()

print "Created run dir with \n tstamp %s \n in \n %s"%(tstamp,srundir)

