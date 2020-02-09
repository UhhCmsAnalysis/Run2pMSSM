#!/usr/bin/env python

# read variables from variables.cfg.py
from variables_cfg import varCfg
import copy

# create plot cfg
plotCfg = []

# 1D plots for all Z
for key in sorted(varCfg.keys()):
    if key.find("Z_100") > 0:
        plotCfg.append([varCfg[key]])

# 2D plots for combined Z
from plotDef_sel_cfg import keys
varCfg_Z = copy.deepcopy(varCfg["SUS12024_SUS12011_SUS13012_SUS16033_Z_100"])
varCfg_Z["name"] = varCfg_Z["name"] + "_finebin"
varCfg_Z["binning"][0] = 120
done = []
for key in keys:
    if 'xsect_8TeV'==key: continue #sam skippe this because _varCfg had no key called "binning"
    pos = key.find("_rebin")
    if pos > 0:
        key = key[:pos]
    if key in done:
        continue
    done.append(key)
    key = key.replace("_rebin","")
    _varCfg = copy.deepcopy(varCfg[key])
    _varCfg["name"] = _varCfg["name"] + "_finebin"
    print '=='*10, key
    print 'having a nice look at _varCfg', _varCfg
    _varCfg["binning"][0] = 120
    plotCfg.append([_varCfg,varCfg_Z])
    


