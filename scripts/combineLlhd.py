#!/usr/bin/env python

from mytools import slurptable
import copy,sets,os,sys

ifiles = sys.argv[1].strip(",").split(",")
ofile = sys.argv[2]

def combine(ifiles,ofile):
    print "combining likelihoods in " + " ".join(ifiles)
    print "writing to " + ofile

    # read in data
    data = []
    ci = []
    for ifile in ifiles:
        filename = ifile
        _ci,_data = slurptable(filenames=filename,dictMode=True)
        ci.append(_ci)
        data.append(_data)

    # create exaustive list of IDs
    ID = sets.Set()
    for _data in data:
        _ID = sets.Set(_data.keys())
        ID = _ID|ID
    ID = sorted(list(ID))

    # check header compatibility
    header = None
    for i in range(0,len(data)):
        _header = []
        for entry in sorted(ci[i].keys()):
            if entry.find("llhd") == 0:
                _header.append(entry)
        if header == None:
            header= _header
        elif header != _header:
            print "BAM!"
            sys.exit()
            

    # open output file
    odir = os.path.split(ofile)[0]
    if not os.path.isdir(odir):
        os.makedirs(odir)
    OFILE = open(ofile,"w")
    OFILE.write("ID\t{0}\n".format("\t".join(header)))
    for id in ID:
        llhd = [0]*len(header)
        for d in range(0,len(data)):
            if not id in data[d]:
                llhd = None
                break
            _data = data[d][id]
            _ci = ci[d]
            # add llhds
            for h in range(len(header)):
                j = ci[d][header[h]]
                _llhd = data[d][id][j]
                llhd[h] += _llhd
        if llhd != None:
            OFILE.write("{0}\t{1}\n".format(int(id),"\t".join([str(x) for x in llhd])))
    OFILE.close()
                        

combine(ifiles,ofile)
print 'just created', ofile
