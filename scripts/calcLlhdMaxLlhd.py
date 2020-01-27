#!/usr/bin/env python

import os
import sys
import math
import ROOT as rt
from mytools import slurptable

# +/- precision of maximum likelihood values
epsilon = 0.005

countypoo = {}
countypoo['totes'] = 0.0
countypoo['goods'] = 0.0

path_maxllhd = sys.argv[1]
path_llhd = sys.argv[2]

# read in the maximized likelihoods
maxllhd_ci,maxllhd = slurptable(path_maxllhd)
_id_ci = maxllhd_ci["ID"]
_ntot_ci = maxllhd_ci["N_TOT"]
_maxllhd_000_ci = maxllhd_ci["maxllhd_000"]
_maxllhd_050_ci = maxllhd_ci["maxllhd_050"]
_maxllhd_100_ci = maxllhd_ci["maxllhd_100"]
_maxllhd_150_ci = maxllhd_ci["maxllhd_150"]
_maxllhd_ci = maxllhd_ci["maxllhd"]

# file for likelihoods
LLHD = open(path_llhd,'w')
LLHD.write("ID\tN_TOT\t\tllhd_000\tllhd_050\tllhd_100\tllhd_150\tT_000\tT_050\tT_100\tT_150\n")



    
# function to calculate llhd
def calcLlhd(maxllhd,maxllhd_mu,id,tag):

    # require a non-problematic fit with mu floated
    if maxllhd==0 or maxllhd==1e+30:
        print "ERROR: llhd_max=",maxllhd,"for id",id
        sys.exit()

    # set llhd for problematic fits with fixed mu to 0  
    if maxllhd_mu == 0 or maxllhd_mu == 1e+30:
        return -1e+30,-2*(-1e+30 - maxllhd)

    # calc test stat
    T_ori = -2*(maxllhd_mu - maxllhd)
    T = T_ori
    
    # the fit with mu floating should give the highest likelihood
    # if not, due to limited fit precision (?), give it a bit extra
    if T_ori < epsilon:
        #print "WARNING: llhd_max={0}, llhd_max_{1}={2}, T_{1}={3}, for id={4}".format(maxllhd,tag,maxllhd_mu,T_ori,id)
        #print "         set T = T+",epsilon
        T = epsilon
    else:
        countypoo['goods']+=1

    #if maxllhd_mu - maxllhd >= 0:
    #sys.exit()

    # calculate the likelihood
    llhd = -0.5*math.log(2*math.pi) - 0.5*math.log(T) - 0.5*T
    countypoo['totes']+=1
    return llhd,T_ori

# loop over maximzied likelihoods
for _maxllhd in maxllhd:
    

    
    _id = _maxllhd[_id_ci]
    _ntot = _maxllhd[_ntot_ci]
    _maxllhd_000 = _maxllhd[_maxllhd_000_ci]
    _maxllhd_050 = _maxllhd[_maxllhd_050_ci]
    _maxllhd_100 = _maxllhd[_maxllhd_100_ci]
    _maxllhd_150 = _maxllhd[_maxllhd_150_ci]
    __maxllhd = _maxllhd[_maxllhd_ci]

    llhd_000,T_000 = calcLlhd(__maxllhd,_maxllhd_000,_id,"000")
    llhd_050,T_050 = calcLlhd(__maxllhd,_maxllhd_050,_id,"050")
    llhd_100,T_100 = calcLlhd(__maxllhd,_maxllhd_100,_id,"100")
    llhd_150,T_150 = calcLlhd(__maxllhd,_maxllhd_150,_id,"150")

    LLHD.write("{0}\t{1}\t\t{2:>.8}\t\t{3:>.8}\t\t{4:>.8}\t\t{5:>.8}\t{6:>.8}\t{7:>.8}\t{8:>.8}\t{9:>.8}\n".format(_id,_ntot,llhd_000,llhd_050,llhd_100,llhd_150,T_000,T_050,T_100,T_150))

# closing
LLHD.close()

print 'looks like', countypoo['goods'], 'fits out of', countypoo['totes'], "succeeded", countypoo['goods']/countypoo['totes']


