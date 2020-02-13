#!/usr/bin/env python

import os,glob
import sys
import math

#this is the version of the script where analyses have provided raw number of simulated counts - then we apply xsec, lumi and so forth
# the 2017 version assumes the analyses have applied all weights, and is a bit configurable. 

from mytools import slurptable

# options
from optparse import OptionParser
parser = OptionParser()
parser.add_option("--start", dest="start", type="int",
                  help="start from entry N", metavar="N",default=0)
parser.add_option("--nentries", dest="nentries", type="int",
                  help="only process N first entries", metavar="N")
parser.add_option("--numeric",
                  action="store_true", dest="numeric", default=False,
                  help="calculate llhds numerically")
parser.add_option("--sr",dest="sr",type="string",
                  help="list of names of signal regions to consider, default: all signal regions are consider",metavar="SR1,SR10,...")
parser.add_option("--2D",
                  action="store_true", dest="twoD", default=False,
                  help="calculate llhds 2D")
parser.add_option("--bkgScale",
                  action="store", dest="bkgScale", default=0,type='float',
                  help="scale up all bkg estimates with N sigma",metavar="N")


# read input directory from the command line
path_counts = sys.argv[1]
path_data_bg = sys.argv[2]
path_llhd = sys.argv[3]
print "counts:",path_counts
print "databg:",path_data_bg

# read other command line options
(options, args) = parser.parse_args()

# load root in batch mode
sys.argv = ["-b"]
import ROOT as rt

# check presence of expected files
dir = os.path.split(path_counts)[0] + "/"
if dir == "/":
    dir = "./"

path_lumi = dir + "/lumi.txt"
path_cme = dir + "/cme.txt"
    
if not os.path.isfile(path_data_bg):
    print "ERROR: expecting a file:",path_data_bg
    sys.exit()
if not os.path.isfile(path_counts):
    print "ERROR: expecting a file:",path_counts
    sys.exit()
if not os.path.isfile(path_lumi):
    print "ERROR: file not found:",path_lumi
    sys.exit()
if not os.path.isfile(path_cme):
    print "ERROR: file not found:",path_cme
    sys.exit()

# read cme
CME = open(path_cme)
line = CME.readline().strip()
elements = line.split()
cme = int(elements[0])

# which signal regions to consider
sr_name = None
if options.sr is not None:
    sr_name = options.sr.split(",")
    
# read in the data and bg predictions
data_bg_ci,data_bg = slurptable(path_data_bg)
N = []
B = []
dB = []
Q = []
K = []
sr = []
for entry in data_bg:
    _sr_name = entry[data_bg_ci["SR_NAME"]]
    if sr_name == None or _sr_name in sr_name:
        sr.append(entry[data_bg_ci["SR_NAME"]])
        N.append(int(entry[data_bg_ci["N"]]))
        B.append(float(entry[data_bg_ci["B"]]))
        dB.append(float(entry[data_bg_ci["dB"]]))
        if(options.bkgScale != 0):
            B[-1] = max(0,B[-1] + dB[-1]*options.bkgScale)
        Q.append(B[-1]*B[-1]/dB[-1]/dB[-1])
        K.append(B[-1]/dB[-1]/dB[-1])
print len(sr) 

print "included signal regions:",",".join(sr)
  
# read in the integrated luminosity
LUMI = open(path_lumi)
line = LUMI.readline().strip()
elements = line.split("/")
lumi = -999
if not len(elements)==2:
    print "ERROR in",path_lumi,": provide units for lumi: '/pb' or '/fb'"
    sys.exit()
if elements[1] == "fb":
    lumi = float(elements[0].strip())*1000
elif elements[1] == "pb":
    lumi = float(elements[0].strip())
else:
    print "ERROR in",path_lumi,": provide units for lumi: '/pb' or '/fb'"
    sys.exit()
LUMI.close()

# read in cross signal xsections
path_xsect = glob.glob("idata/xsect/xsect_{0}TeV*.txt".format(cme))
path_xsect = ",".join(path_xsect)
xsection_ci,xsection = slurptable(path_xsect,True)
_xsection_ci = xsection_ci["xsect_{0}TeV_pb".format(cme)]

# create a file to store the log likelihoods
#llhddir = os.path.split(path_llhd)[0]
#if not os.path.isdir(llhddir):
#    os.makedirs(llhddir)
print "writing likelihoods to",path_llhd
LLHD = open(path_llhd,"w")
LLHD.write("ID\tN_TOT\tllhd_000\tllhd_050\tllhd_100\tllhd_150\n")

# define the single count likelihood functions
rt.gROOT.ProcessLine(".L scripts/calcLlhdSingleCount.C+")
def myllhd(_N,_S,_B,_dB,w=1):
    if options.numeric:
        return rt.llhd(_N,_S*w,_B,_dB)
    elif options.twoD:
        return rt.llhd2D(_N,_B,_dB,_S,w)
    else:
        return rt.llhdAna(_N,_S*w,_B,_dB)

# add the bkg-only hypothesis to the llhd file

# read in the predicted signal counts
counts_ci,counts = slurptable(path_counts)
id_ci = counts_ci["ID"]##sam: don't we need slurptable in dictmode for this?
N_TOT_ci = counts_ci["N_TOT"]
sr_ci = []
for _sr in sr:
    sr_ci.append(counts_ci["N_" + _sr])

#add the signal + bkg hypothesis to the llhd file
start = options.start
stop = len(counts)
if options.nentries is not None:
    stop = min(len(counts),start + options.nentries)
for e in range(start,stop):
    #print "---------"
    if e%10 == 0:
        print "processing {0}/{1}".format(e,stop)
        sys.stdout.flush()
    entry = counts[e]
    _id = int(entry[id_ci])
    if counts[e][N_TOT_ci] == 0.0:
        continue
    #print "id",_id
    _xsection = xsection[_id][_xsection_ci]
    #print _xsection
    if math.isnan(_xsection) or _xsection < 0:
        continue
    _N_TOT = entry[N_TOT_ci]
    _llhd_000 = 0
    _llhd_050 = 0
    _llhd_100 = 0
    _llhd_150 = 0
    for r in range(0,len(sr)):
        w = 1./_N_TOT*lumi*_xsection
        S = entry[sr_ci[r]]
        # print N[r],B[r],dB[r],S,w
        _llhd_050 += myllhd(N[r],S,B[r],dB[r],w*0.5) - myllhd(N[r],0.,B[r],dB[r],w*0.5)
        _llhd_100 += myllhd(N[r],S,B[r],dB[r],w*1.) - myllhd(N[r],0.,B[r],dB[r],w*1.)
        _llhd_150 += myllhd(N[r],S,B[r],dB[r],w*1.5) -myllhd(N[r],0.,B[r],dB[r],w*1.5)

    # get rid of infinities
    if _llhd_000 < -1e30:
        _llhd_000 = -1e30
    if _llhd_050 < -1e30:
        _llhd_050 = -1e30
    if _llhd_100 < -1e30:
        _llhd_100 = -1e30
    if _llhd_150 < -1e30:
        _llhd_150 = -1e30


    line = str(_id) + "\t" + str(_N_TOT) + "\t" + str(_llhd_000) + "\t" + str(_llhd_050) + "\t" + str(_llhd_100) + "\t" + str(_llhd_150) + "\n"
    LLHD.write(line)
    LLHD.flush()

# close
print 'just created', path_llhd
LLHD.close()

