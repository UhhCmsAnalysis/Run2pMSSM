import copy,sys
from legendTitles import *
import ROOT as rt

# the preCMS color
col = rt.TColor();
col.SetRGB(102./255.0, 153./255.0, 204./255.0);
preCMScolor = rt.TColor.GetColor(150./255.0, 190./255.0, 230./255.0)

# line style and width
lineLayout = {
    "050":{"linestyle":2,"linewidth":2,"linetitle":"#mu=0.5"},
    "100":{"linestyle":1,"linewidth":4,"linetitle":"#mu=1.0"},
    "150":{"linestyle":3,"linewidth":2,"linetitle":"#mu=1.5"}
}

# define draw options
options_method = {
    "lhd":{
        "ytitle":"prob. dens.",
        "normalise":1},
    }
options_method.update([["zlhd",options_method["lhd"]]])
                     
# preCMS distributions
preCMSlayout = {"linecolor":preCMScolor,"fillcolor":preCMScolor,"legendoption":"f","legendtitle":"Prior from non-DCS data"}

preCMS_lhd_cfg = ["preCMS",{"normalise":1}]
preCMS_lhd_cfg[1].update(options_method["lhd"])
preCMS_lhd_cfg[1].update(preCMSlayout)

##########################################
# define the combinations
##########################################
colors = [rt.kBlue,rt.kRed,rt.kBlack]
combinations = []

def getAnaComb(ana,color,method):
    # distribution key
    _comb = []
    distrKey = method
    if distrKey == "zlhd":
        distrKey = "surv"
    # first part of legend title
    #legendTitlePrefix = "p(#theta|D^{CMS})"
    #if distrKey == "surv":
    #    legendTitlePrefix = "p(#theta|Z^{CMS}>-1.64)"
    for s in ["050","100","150"]:
        _comb.append([ana  + "_" + distrKey + "_" + s,copy.copy(options_method[method])])
        _comb[-1][1].update(lineLayout[s])
        _comb[-1][1]["linecolor"] = color
        if s == "100":
            #_comb[-1][1]["legendtitle"] = legendTitlePrefix + " " + legendTitle[ana.replace("_123mh128","")]
            _comb[-1][1]["legendtitle"] = legendTitle[ana.replace("_123mh128","")]
            _comb[-1][1]["legendoption"] = "l"
    return _comb

def addCombination(key,analyses,method,extraLegendLines=None):
    combinations.append([key,[]])
    # first add preCMS distribtution
    combinations[-1][1].append(preCMS_lhd_cfg)
    # then add CMS distributions
    for a in range(len(analyses)):
        combinations[-1][1].extend(getAnaComb(analyses[a],colors[a],method))
    # extra options
    combinations[-1].append({})
    if not extraLegendLines is None:
        combinations[-1][-1]["extraLegendLines"] = extraLegendLines


combinations = []

preDefComb = {}
# hadronic inclusive
preDefComb["SUS12011"] = getAnaComb("SUS12011",rt.kBlue,"lhd")
preDefComb["SUS13012"] = getAnaComb("SUS13012",rt.kRed,"lhd")
preDefComb["SUS16033"] = getAnaComb("SUS16033",rt.kOrange+1,"lhd")#sam added
preDefComb["SUS12024_SUS12011_SUS13012_SUS16033"] = getAnaComb("SUS12024_SUS12011_SUS13012_SUS16033",rt.kOrange+1,"lhd")


#preDefComb["combined7TeV"] = getAnaComb("combined7TeV",rt.kRed,"zlhd")
#preDefComb["combined8TeV"] = getAnaComb("combined8TeV",rt.kBlue,"zlhd")
preDefComb["combined7and8and13TeV"] = getAnaComb("combined7and8and13TeV",rt.kBlack,"zlhd")

def addCombination2(name,predefs):
    combinations.append([name,[],{}])
    combinations[-1][1].append(preCMS_lhd_cfg)
    for ana in predefs:
        combinations[-1][1].extend(preDefComb[ana])


#addCombination2("combined",["combined7TeV","combined7and8TeV"])
#run 1 and run 2
addCombination2("inclusiveRun1-2",["SUS12011","SUS13012","SUS12024_SUS12011_SUS13012_SUS16033"]) #sam added

combined = combinations[-1]

combinations.append(copy.deepcopy(combined))
combinations[-1][0] = "combined_higgs"
combination = combinations[-1]
combination[1].append(copy.deepcopy(combination[1][5]))
combination[1][-1][0] += "_higgs"
combination[1][-1][1]["drawstyle"] = "P0"
combination[1][-1][1]["linewidth"] = 1
combination[1][-1][1]["showStatUncert"] = False
combination[1][-1][1]["denom"] = "preCMS_higgs"
combination[1][-1][1]["markerstyle"] = 33
combination[1][-1][1]["markercolor"] = rt.kOrange + 7
combination[1][-1][1]["legendoption"] = "p"
combination[1][-1][1]["legendtitle"] += ", LHC Higgs data"
combined_higgs = combinations[-1]

print combinations[-1]

#combined7and8TeV_zlhd =combinations[-1]
