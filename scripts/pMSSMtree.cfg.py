FILE = open("scripts/analyses.cfg.py")
exec(FILE)
FILE.close()

#################################
# parameters, masses, etc
#################################
treeCfg = [
    [ "params",
      {"files":"idata/parameters/params_batch*.txt","base":""}],
    [ "moreparams",
      {"files":"idata/moreparams/moreparams.txt","base":""}],
    [ "fs",
      {"files":"idata/fs/fs.txt","base":"fs"}],
    [ "lilith",
      {"files":"idata/moreparams/lilith.txt"}],
#    [ "xsect13",
#      {"files":"idata/xsect/xsect_13*txt","base":"","skip_ID":[],"skip_col":"pointName"}],
    [ "xsect8",
      {"files":"idata/xsect/xsect_8*txt","base":"","skip_ID":[2321,8344,6640],"skip_col":"pointName"}],
    [ "xsect7",
      {"files":"idata/xsect/xsect_7*txt","base":"","skip_ID":[2321,8344,6640]}],
    ]
datadir = "idata"
#################################
# likelihoods
#################################
def addLlhd2Cfg(anaList,ext=""):
    for ana in anaList:
        for sr in ana[1]:
            base = ana[0]
            base += sr
            base += ext.replace(".","")
            key = base + "_llhd"
            files = datadir + "/" + ana[0] + "/llhd" + sr + ext + ".txt"
            treeCfg.append([key,{"files":files,"base":base}])

addLlhd2Cfg(ana7)
addLlhd2Cfg(ana8)
addLlhd2Cfg(ana13)
addLlhd2Cfg(ana7n8n13)

#################################
# Z-values
#################################

def addZ2Cfg(anaList,ext=""):
    for ana in anaList:
        for sr in ana[1]:
            base = ana[0]
            base += sr
            base += ext.replace(".","_")
            key = base + "_Z"
            files = datadir + "/" + ana[0] + "/Z" + sr + ext + ".txt"
            treeCfg.append([key,{"files":files,"base":base}])           
            #addZ2Cfg(ana7)
#addZ2Cfg(ana8)
#addZ2Cfg(ana7n8)
addZ2Cfg(ana7z)
addZ2Cfg(ana8z)
addZ2Cfg(ana13z)
addZ2Cfg(ana7n8n13z)
addZ2Cfg(ana7n8n13lossyz)


################################
# print
################################

#for entry in treeCfg:
#    print entry[0],entry[1]
