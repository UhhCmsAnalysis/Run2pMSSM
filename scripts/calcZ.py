#!/usr/bin/env python

from mytools import slurptable
import sys,os,math
from optparse import OptionParser


########################
# read from command line
########################
path_llhd = sys.argv[1]
path_Z = path_llhd.replace("llhd","Z")

########################
# load llhds
########################
print "reading llhd from",path_llhd
llhd_ci,llhd = slurptable(filenames=path_llhd)
_ID_ci = llhd_ci["ID"]
_llhd_000_ci = llhd_ci["llhd_000"]
_llhd_050_ci = None
_llhd_100_ci = llhd_ci["llhd_100"]
_llhd_150_ci = None
if "llhd_050" in llhd_ci:
    _llhd_050_ci = llhd_ci["llhd_050"]
if "llhd_150" in llhd_ci:
    _llhd_150_ci = llhd_ci["llhd_150"]

########################
# calc and write Z
########################
print "writing Z to",path_Z
FILE = open(path_Z,"w")
FILE.write("ID\tZ_050\tZ_100\tZ_150\n")

for entry in llhd:

    ID = entry[_ID_ci]

    lnB10_050 = entry[_llhd_050_ci] - entry[_llhd_000_ci]
    Z_050 = 0
    if lnB10_050 != 0:
        Z_050 = lnB10_050/abs(lnB10_050)*math.sqrt(2*abs(lnB10_050))

    lnB10_100 = entry[_llhd_100_ci] - entry[_llhd_000_ci]
    Z_100 = 0
    if lnB10_100 != 0:
        Z_100 = lnB10_100/abs(lnB10_100)*math.sqrt(2*abs(lnB10_100))

    lnB10_150 = entry[_llhd_150_ci] - entry[_llhd_000_ci]
    Z_150 = 0
    if lnB10_150 != 0:
        Z_150 = lnB10_150/abs(lnB10_150)*math.sqrt(2*abs(lnB10_150))

    FILE.write(str(int(ID)) + "\t" + str(Z_050) + "\t" + str(Z_100) + "\t" + str(Z_150) + "\n")

FILE.close()
