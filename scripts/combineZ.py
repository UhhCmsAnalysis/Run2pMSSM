#!/usr/bin/env python

#warning: all Z combinations produced here are lossy - the non-lossy method is to combine likelihood and then calcZ.sh

from mytools import slurptable
import copy,sets,os,sys

anadir = "idata/"

combination = []

# 7 TeV

combination.append(["lossycombined7and8and13TeV/Z.txt",[]]) #usually for overlapping signal regions, this is just an example
combination[-1][1].extend(["SUS12011/Z.txt"])
combination[-1][1].extend(["SUS13012/Z.txt"])
combination[-1][1].extend(["SUS16033/Z.txt"])

def combine(ofile,ifiles):
    # read in data
    data = []
    ci = []
    for ifile in ifiles:
        filename = ifile
        _ci,_data = slurptable(filenames=filename,dictMode=True)
        ci.append(_ci)
        data.append(_data)

    # create omnipresent list of IDs
    ID = None
    for _data in data:
        _ID = sets.Set(_data.keys())
        if ID == None:
            ID = _ID
        else:
            ID = ID.intersection(_ID)
    ID = sorted(list(ID))

    # check header compatibility
    header = None
    for i in range(0,len(data)):
        _header = []
        for entry in sorted(ci[i].keys()):
            if entry.find("Z") == 0:
                _header.append(entry)
        if header == None:
            header= _header
        elif header != _header:
            print "BAM!"
            sys.exit()

    # open output file
    c = "mkdir {0}".format(os.path.split(ofile)[0])
    if not os.path.exists("{0}".format(os.path.split(ofile)[0])): os.system(c)
    OFILE = open(ofile,"w")
    OFILE.write("ID\t{0}\n".format("\t".join(header)))
    for id in ID:
        Z = [0]*len(header)
        for d in range(0,len(data)):
            if not id in data[d]:
                llhd = None
                break
            _data = data[d][id]
            _ci = ci[d]
            # find the best for each column
            for h in range(len(header)):
                j = ci[d][header[h]]
                _Z = data[d][id][j]
                if Z[h] == None or abs(Z[h]) < abs(_Z):
                    Z[h] = _Z
        if Z != None:
            OFILE.write("{0}\t{1}\n".format(id,"\t".join([str(x) for x in Z])))
    OFILE.close()

for entry in combination:
    print "###",entry[0]
    ofile = anadir + entry[0]
    ifiles = [anadir + x for x in entry[1]]
    combine(ofile,ifiles)

    



                      
