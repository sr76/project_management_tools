#!/usr/bin/python
import os

os.system("rm -f *.OUT*")
os.system("rm -f STM*")
os.system("rm -f VCL*")
os.system("rm -f stm*")
os.system("rm -f PLOT.*")
os.system("rm -f .INFO*")
os.system("rm -f info*")
os.system("rm -f dos.xml")
os.system("rm -f info.xml")

os.system("mkdir tmp")
os.system("cp * tmp")

os.system("rm -f *.e*")
os.system("rm -f *.o*")

