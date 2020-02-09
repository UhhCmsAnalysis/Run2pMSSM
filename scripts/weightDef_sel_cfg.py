#!/usr/bin/env python
	       
import sys,copy



weightCfg = []
weightCfg.append(["preCMS",["all_OK","lhratio_preCMS"]])
#weightCfg.append(["preCMS_higgs",["all_OK","lhratio_preCMS*TMath::Exp(lilith_llhd)"]])

def addLhdAna(analist,ext=""):
    for ana in analist:
        for sr in ana[1]:
            for s in ["050","100","150"]:
                key = "{0}{1}{2}_lhd_{3}".format(ana[0],sr,ext,s)
                value = "lhratio_preCMS*TMath::Exp({0}{1}{2}_llhd_{3})".format(ana[0],sr,ext,s)
                weightCfg.append([key,["all_OK",value]])
                
ana = [
    ["SUS12011",[""]],#sam added
    ["SUS13012",[""]],
    ["SUS16033",[""]],#sam added
    ["SUS12024_SUS12011_SUS13012_SUS16033",[""]],#sam added
    ]

addLhdAna(ana)

def addZAna(analist,ext="",extracond=None):
    for ana in analist:
        for sr in ana[1]:
            for s in ["050","100","150"]:
                key = "{0}{1}{2}_surv_{3}".format(ana[0],sr,ext,s)
                value1 = "all_OK"
                if extracond is not None:
                    value1 += "*" + extracond
                value2 = "lhratio_preCMS*({0}{1}_Z_{2} >= -1.64)".format(ana[0],sr,s)
                weightCfg.append([key,[value1,value2]])

ana = [
    ["SUS12024_SUS12011_SUS13012_SUS16033",[""]]
    ]

addZAna(ana)

for e in range(0,len(weightCfg)):
    key = weightCfg[e][0]
    key += "_higgs"
    condition = weightCfg[e][1][0]
    weight = weightCfg[e][1][1]
    weight += "*TMath::Exp(lilith_llhd)"
    weightCfg.append([key,[condition,weight]])

    key += "_123mh128_"
    weight = weightCfg[e][1][1]
    weight += "*TMath::Exp(lilith_llhd)*(123 < mh)*(mh < 128)"
    weightCfg.append([key,[condition,weight]])
    
