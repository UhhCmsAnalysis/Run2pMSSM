#!/usr/bin/env python

import math
import ROOT as rt

varCfg = {}
def addVar(var,title,nbin,min,max,options={}):
    key = var
    if options is not None:
        if "key" in options:
            key = options["key"]
            options.pop("key")
    varCfg.update({key:{"name":key,"var":var,"title":title,"binning":[nbin,min,max]}})
    if not "unit" in options:
        options["unit"] = "TeV"
    varCfg[key].update(options)
    return key

def addMass(var,title,nbin,min,max,options={}):
    key = var
    if options is not None:
        if "key" in options:
            key = options["key"]
            options.pop("key")
    varCfg.update({key:{"name":key,"var":var + "/1000","title":title,"binning":[nbin,min,max]}})
    if not "unit" in options:
        options["unit"] = "TeV"
    varCfg[key].update(options)
    return key

def addLogVar(var,title,nbin,min,max,options=None):
    key = addVar(var,title,nbin,min,max,options)
    # reset binnging
    varCfg[key].pop("binning")
    logmin = math.log(min,10)
    logmax = math.log(max,10)
    binning = [pow(10,logmin + i*(logmax - logmin)/nbin) for i in range(nbin+1)]
    varCfg[key].update([["customBinning",binning]])
    return key

# pMSSM parameters;
addVar("tanb","tan#beta",20,0,60,{"unit":""})
addVar("M1/1000","M_{1}",20,-3,3,{"key":"M1"})
addVar("M2/1000","M_{2}",20,-3,3,{"key":"M2"})
addVar("M3/1000","M_{3}",20,0,3,{"key":"M3"}) 
addVar("At/1000","A_{T}",20,-7,7,{"key":"At"})
addVar("Ab/1000","A_{b}",20,-7,7,{"key":"Ab"})
addVar("Al/1000","A_{#tau}",20,-7,7,{"key":"Al"})
addVar("mu/1000","#mu",20,-3,3,{"key":"mu"})
addVar("mA_pole/1000","A mass",20,0,3,{"key":"mA_pole"})
addVar("Ml1/1000","#tilde{L}_{1,2}",20,0,3,{"key":"Ml1"})
addVar("Ml3/1000","#tilde{L}_{3}",20,0,3,{"key":"Ml3"})
addVar("Mr1/1000","#tilde{E}_{1,2}",20,0,3,{"key":"Mr1"})
addVar("Mr3/1000","#tilde{E}_{3}",20,0,3,{"key":"Mr3"})
addVar("Mq1/1000","#tilde{Q}_{1,2}",20,0,3,{"key":"Mq1"})
addVar("Mq3/1000","#tilde{Q}_{3}",20,0,3,{"key":"Mq3"})
addVar("Mu1/1000","#tilde{U}_{1,2}",20,0,3,{"key":"Mu1"})
addVar("Mu3/1000","#tilde{U}_{3}",20,0,3,{"key":"Mu3"})
addVar("Md1/1000","#tilde{D}_{1,2}",20,0,3,{"key":"Md1"})
addVar("Md3/1000","#tilde{D}_{3}",20,0,3,{"key":"Md3"})

# masses
addVar("TMath::Sqrt(mt1*mt2)/1000","M_{SUSY}",20,0,3,{"key":"M_SUSY"})
addVar("mdL/1000","#tilde{d}_{L}, #tilde{s}_{L} mass",20,0,3,{"key":"mdL"})
addVar("mdR/1000","#tilde{d}_{R}, #tilde{s}_{R} mass",20,0,3,{"key":"mdR"})
addVar("muL/1000","#tilde{u}_{L}, #tilde{c}_{L} mass",20,0,3,{"key":"muL"})
addVar("muR/1000","#tilde{u}_{R}, #tilde{c}_{R} mass",20,0,3,{"key":"muR"})
addVar("mb1/1000","#tilde{b}_{1} mass",20,0,3,{"key":"mb1"})
addVar("mb2/1000","#tilde{b}_{2} mass",20,0,3,{"key":"mb2"})
addVar("mt1/1000","#tilde{t}_{1} mass",20,0,3,{"key":"mt1"})
addVar("mt2/1000","#tilde{t}_{2} mass",20,0,3,{"key":"mt2"})
addVar("meL/1000","#tilde{e}_{L}, #tilde{#mu}_{L} mass",20,0,3,{"key":"meL"})
addVar("meR/1000","#tilde{e}_{R}, #tilde{#mu}_{R} mass",20,0,3,{"key":"meR"})
addVar("min(meL,meR)/1000","min(#tilde{e}_{L}, #tilde{#mu}_{L}, #tilde{e}_{R}, #tilde{#mu}_{R} mass)",20,0,3,{"key":"min_meLmeR"})
addVar("mneute/1000","#tilde{#nu}_{e,#mu} mass",20,0,3,{"key":"mneute"})
addVar("mtau1/1000","#tilde{#tau}_{1} mass",20,0,3,{"key":"mtau1"})
addVar("mtau2/1000","#tilde{#tau}_{2} mass",20,0,3,{"key":"mtau2"})
addVar("mneuttau/1000","#tilde{#nu}_{#tau} mass",20,0,3,{"key":"mneuttau"})
addVar("mg/1000","#tilde{g} mass",20,0,3,{"key":"mg"})
addVar("fabs(mz1)/1000","#tilde{#chi}^{0}_{1} mass",20,0,1.5,{"key":"mz1"})
addVar("fabs(mz2)/1000","#tilde{#chi}^{0}_{2} mass",20,0,3,{"key":"mz2"})
addVar("fabs(mz3)/1000","#tilde{#chi}^{0}_{3} mass",20,0,3,{"key":"mz3"})
addVar("fabs(mz4)/1000","#tilde{#chi}^{0}_{4} mass",20,0,3,{"key":"mz4"})
addVar("fabs(mw1)/1000","#tilde{#chi}^{#pm}_{1} mass",20,0,3,{"key":"mw1"})
addVar("fabs(mw2)/1000","#tilde{#chi}^{#pm}_{2} mass",20,0,3,{"key":"mw2"})

# extra masses
addVar("min(mg,min(mdL,min(mdR,min(muL,min(muR,min(mb1,min(mb2,min(mt1,mt2))))))))/1000","LCSP mass",20,0,3,{"key":"mLCSP"})
addVar("min(mdL,min(mdR,min(muL,min(muR,min(mb1,mb2)))))","mass of lightest squark (1st, 2nd gen, #tilde{b}_{1})",20,0,3,{"key":"massLightestSquark12b"})
addVar("min(mdL,min(mdR,min(muL,muR)))","mass of lightest squark (1st, 2nd gen)",20,0,3,{"key":"massLightestSquark12"})

# mass difference, sparticle LSP
def AddMassDiff(key1,key2):
    addVar("({0} - {1})/1000".format(varCfg[key1]["var"],varCfg[key2]["var"]),"{0} - {1}".format(varCfg[key1]["title"].replace("mass",""),varCfg[key2]["title"]),20,0,3,{"key":"{0}_M_{1}".format(varCfg[key1]["name"],varCfg[key2]["name"])})
AddMassDiff("mg","mz1")
AddMassDiff("muL","mz1")
AddMassDiff("muR","mz1")
AddMassDiff("mdL","mz1")
AddMassDiff("mdR","mz1")
AddMassDiff("mb1","mz1")
AddMassDiff("mt1","mz1")
AddMassDiff("mt1","mz1")
AddMassDiff("mz2","mz1")
AddMassDiff("mz3","mz1")
AddMassDiff("mz4","mz1")
AddMassDiff("mw1","mz1")
AddMassDiff("mw2","mz1")
AddMassDiff("mLCSP","mz1")


# cross sections
addLogVar("(xsect_7TeV_pb*1000.)","signal cross section for #sqrt{s}=7 TeV",26,1e-4,1e7,{"logScale":1,"key":"xsect_7TeV","unit":"fb"})
addLogVar("(xsect_8TeV_pb*1000.)","signal cross section for #sqrt{s}=8 TeV",26,1e-4,1e7,{"logScale":1,"key":"xsect_8TeV","unit":"fb"})
addLogVar("(xsect_8TeV_pb*20000./10000.)","event weight for 20 fb^{-1} at 8 TeV",26,2e-8,2e5,{"logScale":1,"key":"weight8TeV"})
addLogVar("(xsect_7TeV_pb*5000./10000.)","event weight for 20 fb^{-1} at 8 TeV",26,2e-8,2e5,{"logScale":1,"key":"weight7TeV"})

addVar("TMath::Log10(xsect_7TeV_pb*1000.)","log_{10}(#sigma^{7 TeV}_{SUSY})",26,-4,7,{"key":"log10_xsect_7TeV","unit":"log_{10}(fb)"})
addVar("TMath::Log10(xsect_8TeV_pb*1000.)","log_{10}(#sigma^{8 TeV}_{SUSY})",26,-4,7,{"key":"log10_xsect_8TeV","unit":"log_{10}(fb)"})
addVar("TMath::Log10(xsect_8TeV_pb*20000./10000.)","log_{10}(event weight for 20 fb^{-1} at 8 TeV)",26,-9,6,{"key":"log10_weight8TeV"})
addVar("TMath::Log10(xsect_7TeV_pb*5000./10000.)","log_{10}(event weight for 20 fb^{-1} at 7 TeV)",26,-9,6,{"key":"log10_weight7TeV"})

# SM parameters and observables
addVar("mh","h mass",40,115,135,{"unit":"GeV"})
addVar("alpha_s","#alpha_{s}(m_{Z})",20,0.115,0.121,{"unit":""})
addVar("mbmb","m_{b}(m_{b})",20,3.8,5,{"unit":"GeV"})
addVar("Bsmumu*1.077586","BR(B_{s}#rightarrow#mu^{+}#mu^{-})^{exp}",20,0,0.00000001,{"key":"Bsmumu_exp","unit":""})
addVar("bsgamma","BR(b#rightarrow s#gamma)",20,0.0002,0.0005,{"unit":""})
addVar("mt","t mass",20,166,180,{"unit":"GeV"})
addVar("muon_gm2","g_{#mu} - 2",20,-0.000000001,0.000000005,{"unit":""})

# DM related parameters and observables
addLogVar("(sigSD)","#xi#sigma^{SD}(p#tilde{#chi}_{1}^{0})",20,1e-12,1e-1,{"logScale":1,"key":"sigSD","unit":"pb"})
addLogVar("(sigSI)","#xi#sigma^{SI}(p#tilde{#chi}_{1}^{0})",20,1e-14,1e-4,{"logScale":1,"key":"sigSI","unit":"pb"})
addLogVar("(omg)","#Omega_{#tilde{#chi}^{0}_{1}}h^{2}",20,1e-4,1e4,{"logScale":1,"key":"omgh2","unit":""})
addVar("TMath::Log10(sigSD)","log_{10}(#xi#sigma^{SD}(p#tilde{#chi}_{1}^{0}))",20,-12.,-1.,{"key":"log10_sigSD","unit":"log_{10}(pb)"})
addVar("TMath::Log10(sigSI)","log_{10}(#xi#sigma^{SI}(p#tilde{#chi}_{1}^{0}))",20,-15.,-4.,{"key":"log10_sigSI","unit":"log_{10}(pb)"})
addVar("TMath::Log10(omg)","log_{10}(#Omega_{#tilde{#chi}^{0}_{1}}h^{2})",20,-4,4,{"key":"log10_omgh2","unit":""})
addVar("(At - tb/mu)/sqrt(mt1*mt2)","(A_{t} - (#mu/tan#beta)) / #sqrt{m_{#tilde{t}_{1}}m_{#tilde{t}_{2}}}",20,-4,4,{"key":"XtDms","unit":""})

# LND chi, 1D
addVar("((fabs(M1) < min(fabs(M2),fabs(mu)))? mw1 : mw2)/1000","LND #chi^{#pm} mass",20,0,3,{"key":"mLNDw"})
addVar("((fabs(mu) < min(fabs(M1),fabs(M2)))? mz3 : mz2)/1000","LND #chi^{0} mass",20,0,3,{"key":"mLNDz"})
addVar("min((fabs(mu) < min(fabs(M1),fabs(M2)))? mz3 : mz2,(fabs(M1) < min(fabs(M2),fabs(mu)))? mw1 : mw2)/1000", "LND #chi mass",20,0,3,{"key":"mLNDv"})

addVar("min((fabs(M1) < min(fabs(M2),fabs(mu)))? mw1 : mw2,meL)/1000","lightest(LND #tilde{#chi}^{#pm}, #tilde{e}_{L}, #tilde{#mu}_{L}) mass",20,0,3,{"key":"minmLNDwmeL"})
addVar("min((fabs(M1) < min(fabs(M2),fabs(mu)))? mw1 : mw2,min(meL,mtau1))/1000","lightest(LND #tilde{#chi}^{#pm}, #tilde{e}_{L}, #tilde{#mu}_{L}, #tilde{#tau}_{1}) mass",20,0,3,{"key":"minLNDwmeLmtau1"})
addVar("min((fabs(mu) < min(fabs(M1),fabs(M2)))? mz3 : mz2,min((fabs(M1) < min(fabs(M2),fabs(mu)))? mw1 : mw2,meL))/1000", "lightest(LND #chi, #tilde{e}_{L}, #tilde{#mu}_{L}) mass",20,0,3,{"key":"minmLNDvmeL"})
addVar("min((fabs(mu) < min(fabs(M1),fabs(M2)))? mz3 : mz2,min((fabs(M1) < min(fabs(M2),fabs(mu)))? mw1 : mw2,min(meL,mtau1)))/1000","lightest(LND #tilde{#chi}, #tilde{e}_{L}, #tilde{#mu}_{L}, #tilde{#tau}_{1}) mass",20,0,3,{"key":"minLNDvmeLmtau1"})

# Higgs stuff

addVar("RgghZZ","#mu_{gg}(ZZ)",20,0.5,1.4,{"unit":""})
addVar("RgghAA","#mu_{gg}(#gamma#gamma)",20,0.5,1.4,{"unit":""})
addVar("Rgghbb","#mu_{gg}(bb)",20,0.5,1.4,{"unit":""})
addVar("RVBFhZZ","#mu_{VBF}(ZZ)",20,0.5,1.4,{"unit":""})
addVar("RVBFhAA","#mu_{VBF}(#gamma#gamma)",20,0.5,1.4,{"unit":""})
addVar("RVBFhbb","#mu_{VBF}(bb)",20,0.5,1.4,{"unit":""})

addLogVar("(zn13*zn13+zn14*zn14)","higgsino fraction of #tilde{#chi}^{0}_{1}",20,0.0001,1,{"logScale":1,"key":"hinofrac","unit":""})
addLogVar("(zn11*zn11)","bino fraction of #tilde{#chi}^{0}_{1}",20,0.00001,1,{"logScale":1,"key":"binofrac","unit":""})
addLogVar("(zn12*zn12)","wino fraction of #tilde{#chi}^{0}_{1}",20,0.0000000001,1,{"logScale":1,"key":"winofrac","unit":""})
addVar("MH3/1000","A mass",20,0,3,{"key":"MH3"})
addVar("mHc/1000","H^{#pm} mass",20,0,3,{"key":"mHc"})
addVar("mHh/1000","H^{0} mass",20,0,3,{"key":"mHh"})

addVar("H0SUSY","BR(H #rightarrow SUSY)",20,0,1,{"unit":""})
addVar("HpmSUSY","BR(H^{#pm} #rightarrow SUSY)",20,0,1,{"unit":""})
addVar("hASUSY","BR(A #rightarrow SUSY)",20,0,1,{"unit":""})
addVar("TMath::Log10(hSUSY)","Log_{10}(BR(h #rightarrow SUSY))",33,-15,0,{"unit":"","key":"log10_hSUSY"})
addVar("TMath::Log10(hSUSY)","Log_{10}(BR(h #rightarrow SUSY))",16,-4,0,{"unit":"","key":"log10_hSUSY_zoom"})
addVar("hSUSY","BR(h #rightarrow SUSY)",9,.01,1,{"unit":"","key":"hSUSY_zoom"})


import sys,copy
FILE = open("scripts/analyses.cfg.py")
exec(FILE)
FILE.close()

def addZ(analist):
    for ana in analist:
        for sr in ana[1]:
            key = ana[0] + sr + "_Z_100"
            varCfg.update({key:{"name":key,"var":key,"title":"Z","binning":[20,-5,5],"unit":"","underflowbin":True}})
            key_rebin = key + "_rebin"
            #print key_rebin
            _bins = range(-21,-9,3)
            _bins += range(-9,-3,2)
            while _bins[-1] < 5:
                _bins.append(_bins[-1] + 0.5)
            varCfg.update({key_rebin:{"name":key_rebin,"var":key,"title":"Z","customBinning":_bins,"unit":""}})

#addZ(ana7)
#addZ(ana8)
#addZ(ana7z)
#addZ(ana8z)
addZ(ana13z)
#addZ(ana7n8n13z)
#addZ(ana7n8n13lossyz)

logXsectBinning = [-3,-2,-1.5,-1,-.5,0.,0.333,0.666,1.,1.333,1.666,2,2.333,2.666,3.,3.333,3.666,4,5,6]
#[-6,-5,-4,-3,-2.5,-2,-1.5,-1,-.5,0.,0.333,0.666,1.,1.333,1.666,2,2.333,2.666,3.,3.333,3.666,4,5,6]
# final state stuff
# met
addVar("fs_met","average E_{T}^{missing}",20,0,500,{"customBinning":[0,20,40,60,80,100,150,200,250,300,400,500,600,700,800]})
# met35
addVar("fs_frac_met35","#epsilon (E_{T}^{missing} > 35 GeV)",20,0,1)
addVar("TMath::Log10(fs_frac_met35*xsect_8TeV_pb*1000)","log_{10}#left[#sigma^{SUSY}_{8 TeV,pp}#upoint A [fb]#right]",20,0,1,{"extralabel":"E_{T}^{missing} > 35 GeV","customBinning":logXsectBinning,"key":"fs_A_met35","unit":""})
# met80
addVar("fs_frac_met80","#epsilon (E_{T}^{missing} > 80 GeV)",20,0,1)
addVar("TMath::Log10(fs_frac_met80*xsect_8TeV_pb*1000)","log_{10}#left[#sigma^{SUSY}_{8 TeV,pp}}#upoint A [fb]#right]",20,0,1,{"extralabel":"E_{T}^{missing} > 80 GeV","customBinning":logXsectBinning,"key":"fs_A_met80","unit":""})
# met200
addVar("fs_frac_met200","#epsilon (E_{T}^{missing} > 200 GeV)",20,0,1)
addVar("TMath::Log10(fs_frac_met200*xsect_8TeV_pb*1000)","log_{10}#left[#sigma^{SUSY}_{8 TeV,pp}#upoint A [fb]#right]",20,0,1,{"extralabel":"E_{T}^{missing} > 200 GeV","customBinning":logXsectBinning,"key":"fs_A_met200","unit":""})
# met300
addVar("fs_frac_met300","#epsilon (E_{T}^{missing} > 300 GeV)",20,0,1)
addVar("TMath::Log10(fs_frac_met300*xsect_8TeV_pb*1000)","log_{10}#left[#sigma^{SUSY}_{8 TeV,pp}#upoint A [fb]#right]",20,0,1,{"extralabel":"E_{T}^{missing} > 300 GeV","customBinning":logXsectBinning,"key":"fs_A_met300","unit":""})
# met450
addVar("fs_frac_met450","#epsilon (E_{T}^{missing} > 450 GeV)",20,0,1)
addVar("TMath::Log10(fs_frac_met450*xsect_8TeV_pb*1000)","log_{10}#left[#sigma^{SUSY}_{8 TeV,pp}#upoint A [fb]#right]",20,0,1,{"extralabel":"E_{T}^{missing} > 450 GeV","customBinning":logXsectBinning,"key":"fs_A_met450","unit":""})
# met600
addVar("fs_frac_met600","#epsilon (E_{T}^{missing} > 600 GeV)",20,0,1)
addVar("TMath::Log10(fs_frac_met600*xsect_8TeV_pb*1000)","log_{10}#left[#sigma^{SUSY}_{8 TeV,pp}#upoint A [fb]#right]",20,0,1,{"extralabel":"E_{T}^{missing} > 600 GeV","customBinning":logXsectBinning,"key":"fs_A_met600","unit":""})

# ht
addVar("fs_ht","average HT",20,0,500,{"customBinning":[0,20,40,60,80,100,150,200,300,400,500,600,700,800,900,1000,1200]})
#
addVar("fs_frac_ht80","#epsilon (HT > 80 GeV)",20,0,1)
addVar("TMath::Log10(fs_frac_ht80*xsect_8TeV_pb*1000)","log_{10}#left[#sigma^{SUSY}_{8 TeV,pp}#upoint A [fb]#right]",20,0,1,{"extralabel":"HT > 80 GeV","customBinning":logXsectBinning,"key":"fs_A_ht80","unit":""})
#
addVar("fs_frac_ht300","#epsilon (HT > 300 GeV)",20,0,1)
addVar("TMath::Log10(fs_frac_ht300*xsect_8TeV_pb*1000)","log_{10}#left[#sigma^{SUSY}_{8 TeV,pp}#upoint A [fb]#right]",20,0,1,{"extralabel":"HT > 300 GeV","customBinning":logXsectBinning,"key":"fs_A_ht300","unit":""})
#
addVar("fs_frac_ht500","#epsilon (HT > 500 GeV)",20,0,1)
addVar("TMath::Log10(fs_frac_ht500*xsect_8TeV_pb*1000)","log_{10}#left[#sigma^{SUSY}_{8 TeV,pp}#upoint A [fb]#right]",20,0,1,{"extralabel":"HT > 500 GeV","customBinning":logXsectBinning,"key":"fs_A_ht500","unit":""})
#
addVar("fs_frac_ht800","#epsilon (HT > 800 GeV)",20,0,1)
addVar("TMath::Log10(fs_frac_ht800*xsect_8TeV_pb*1000)","log_{10}#left[#sigma^{SUSY}_{8 TeV,pp}#upoint A [fb]#right]",20,0,1,{"extralabel":"HT > 800 GeV","customBinning":logXsectBinning,"key":"fs_A_ht800","unit":""})
#
addVar("fs_frac_ht1000","#epsilon (HT > 1000 GeV)",20,0,1)
addVar("TMath::Log10(fs_frac_ht1000*xsect_8TeV_pb*1000)","log_{10}#left[#sigma^{SUSY}_{8 TeV,pp}#upoint A [fb]#right]",20,0,1,{"extralabel":"HT > 1000 GeV","customBinning":logXsectBinning,"key":"fs_A_ht1000","unit":""})
#
addVar("fs_frac_ht1250","#epsilon (HT > 1250 GeV)",20,0,1)
addVar("TMath::Log10(fs_frac_ht1250*xsect_8TeV_pb*1000)","log_{10}#left[#sigma^{SUSY}_{8 TeV,pp}#upoint A [fb]#right]",20,0,1,{"extralabel":"HT > 1250 GeV","customBinning":logXsectBinning,"key":"fs_A_ht1250","unit":""})
#
addVar("fs_frac_ht1500","#epsilon (HT > 1500 GeV)",20,0,1)
addVar("TMath::Log10(fs_frac_ht1500*xsect_8TeV_pb*1000)","log_{10}#left[#sigma^{SUSY}_{8 TeV,pp}#upoint A [fb]#right]",20,0,1,{"extralabel":"HT > 1500 GeV","customBinning":logXsectBinning,"key":"fs_A_ht1500","unit":""})
# jets
addVar("fs_njet","average N^{jet 1}",16,0,8,{"unit":""})
addVar("fs_ptjet1","average p_{T}^{jet}",20,0,500,{"customBinning":[0,20,40,60,80,100,150,200,250,300,400,500,600,700,800]})
####
addVar("fs_frac_jet1pt30","#epsilon (p_{T}^{jet 1} > 30 GeV)",20,0,1,{"unit":""})
addVar("TMath::Log10(fs_frac_jet1pt30*xsect_8TeV_pb*1000)","log_{10}#left[#sigma^{SUSY}_{8 TeV,pp}#upoint A [fb]#right]",20,0,1,{"extralabel":"p_{T}^{jet 1} > 30 GeV","customBinning":logXsectBinning,"key":"fs_A_jet1pt30","unit":""})
#
addVar("fs_frac_jet1pt50","#epsilon (p_{T}^{jet 1} > 50 GeV)",20,0,1,{"unit":""})
addVar("TMath::Log10(fs_frac_jet1pt50*xsect_8TeV_pb*1000)","log_{10}#left[#sigma^{SUSY}_{8 TeV,pp}#upoint A [fb]#right]",20,0,1,{"extralabel":"p_{T}^{jet 1} > 50 GeV","customBinning":logXsectBinning,"key":"fs_A_jet1pt50","unit":""})
#
addVar("fs_frac_jet1pt80","#epsilon (p_{T}^{jet 1} > 80 GeV)",20,0,1,{"unit":""})
addVar("TMath::Log10(fs_frac_jet1pt80*xsect_8TeV_pb*1000)","log_{10}#left[#sigma^{SUSY}_{8 TeV,pp}#upoint A [fb]#right]",20,0,1,{"extralabel":"p_{T}^{jet 1} > 80 GeV","customBinning":logXsectBinning,"key":"fs_A_jet1pt80","unit":""})
#
addVar("fs_frac_jet1pt100","#epsilon (p_{T}^{jet 1} > 100 GeV)",20,0,1,{"unit":""})
addVar("TMath::Log10(fs_frac_jet1pt100*xsect_8TeV_pb*1000)","log_{10}#left[#sigma^{SUSY}_{8 TeV,pp}#upoint A [fb]#right]",20,0,1,{"extralabel":"p_{T}^{jet 1} > 100 GeV","customBinning":logXsectBinning,"key":"fs_A_jet1pt100","unit":""})
#
addVar("fs_frac_jet1pt200","#epsilon (p_{T}^{jet 1} > 200 GeV)",20,0,1,{"unit":""})
addVar("TMath::Log10(fs_frac_jet1pt200*xsect_8TeV_pb*1000)","log_{10}#left[#sigma^{SUSY}_{8 TeV,pp}#upoint A [fb]#right]",20,0,1,{"extralabel":"p_{T}^{jet 1} > 200 GeV","customBinning":logXsectBinning,"key":"fs_A_jet1pt200","unit":""})
#
#addVar("fs_frac_jet1pt400","#epsilon (p_{T}^{jet 1} > 400 GeV)",20,0,1,{"unit":""})
#addVar("TMath::Log10(fs_frac_jet1pt400*xsect_8TeV_pb*1000)","log_{10}#left[#sigma^{SUSY}_{8 TeV,pp}#upoint A [fb]#right]",20,0,1,{"extralabel":"p_{T}^{jet 1} > 400 GeV","customBinning":logXsectBinning,"key":"fs_A_jet1pt400","unit":""})
#
addVar("fs_frac_jet1pt500","#epsilon (p_{T}^{jet 1} > 500 GeV)",20,0,1,{"unit":""})
addVar("TMath::Log10(fs_frac_jet1pt500*xsect_8TeV_pb*1000)","log_{10}#left[#sigma^{SUSY}_{8 TeV,pp}#upoint A [fb]#right]",20,0,1,{"extralabel":"p_{T}^{jet 1} > 500 GeV","customBinning":logXsectBinning,"key":"fs_A_jet1pt500","unit":""})
####
#addVar("fs_frac_jet2pt30","#epsilon (p_{T}^{jet 2} > 30 GeV)",20,0,1,{"unit":""})
#addVar("TMath::Log10(fs_frac_jet2pt30*xsect_8TeV_pb*1000)","log_{10}#left[#sigma^{SUSY}_{8 TeV,pp}(p_{T}^{jet 2} > 30 GeV) [fb]#right]",20,0,1,{"customBinning":logXsectBinning,"key":"fs_A_jet2pt30","unit":""})
#
addVar("fs_frac_jet2pt50","#epsilon (p_{T}^{jet 2} > 50 GeV)",20,0,1,{"unit":""})
addVar("TMath::Log10(fs_frac_jet2pt50*xsect_8TeV_pb*1000)","log_{10}#left[#sigma^{SUSY}_{8 TeV,pp}#upoint A [fb]#right]",20,0,1,{"extralabel":"p_{T}^{jet 2} > 50 GeV","customBinning":logXsectBinning,"key":"fs_A_jet2pt50","unit":""})
#
addVar("fs_frac_jet2pt80","#epsilon (p_{T}^{jet 2} > 80 GeV)",20,0,1,{"unit":""})
addVar("TMath::Log10(fs_frac_jet2pt80*xsect_8TeV_pb*1000)","log_{10}#left[#sigma^{SUSY}_{8 TeV,pp}#upoint A [fb]#right]",20,0,1,{"extralabel":"p_{T}^{jet 2} > 80 GeV","customBinning":logXsectBinning,"key":"fs_A_jet2pt80","unit":""})
#
addVar("fs_frac_jet2pt100","#epsilon (p_{T}^{jet 2} > 100 GeV)",20,0,1,{"unit":""})
addVar("TMath::Log10(fs_frac_jet2pt100*xsect_8TeV_pb*1000)","log_{10}#left[#sigma^{SUSY}_{8 TeV,pp}#upoint A [fb]#right]",20,0,1,{"extralabel":"p_{T}^{jet 2} > 100 GeV","customBinning":logXsectBinning,"key":"fs_A_jet2pt100","unit":""})
#
addVar("fs_frac_jet2pt200","#epsilon (p_{T}^{jet 2} > 200 GeV)",20,0,1,{"unit":""})
addVar("TMath::Log10(fs_frac_jet2pt200*xsect_8TeV_pb*1000)","log_{10}#left[#sigma^{SUSY}_{8 TeV,pp}#upoint A [fb]#right]",20,0,1,{"extralabel":"p_{T}^{jet 2} > 200 GeV","customBinning":logXsectBinning,"key":"fs_A_jet2pt200","unit":""})
#
addVar("fs_frac_jet2pt400","#epsilon (p_{T}^{jet 2} > 400 GeV)",20,0,1,{"unit":""})
addVar("TMath::Log10(fs_frac_jet2pt400*xsect_8TeV_pb*1000)","log_{10}#left[#sigma^{SUSY}_{8 TeV,pp}#upoint A [fb]#right]",20,0,1,{"extralabel":"p_{T}^{jet 2} > 400 GeV","customBinning":logXsectBinning,"key":"fs_A_jet2pt400","unit":""})
#
addVar("fs_frac_jet2pt500","#epsilon (p_{T}^{jet 2} > 500 GeV)",20,0,1,{"unit":""})
addVar("TMath::Log10(fs_frac_jet2pt500*xsect_8TeV_pb*1000)","log_{10}#left[#sigma^{SUSY}_{8 TeV,pp}#upoint A [fb]#right]",20,0,1,{"extralabel":"p_{T}^{jet 2} > 500 GeV","customBinning":logXsectBinning,"key":"fs_A_jet2pt500","unit":""})
####
#
addVar("fs_frac_jet4pt50","#epsilon (p_{T}^{jet 4} > 50 GeV)",20,0,1,{"unit":""})
addVar("TMath::Log10(fs_frac_jet4pt50*xsect_8TeV_pb*1000)","log_{10}#left[#sigma^{SUSY}_{8 TeV,pp}#upoint A [fb]#right]",20,0,1,{"extralabel":"p_{T}^{jet 4} > 50 GeV","customBinning":logXsectBinning,"key":"fs_A_jet4pt50","unit":""})
#
addVar("fs_frac_jet6pt50","#epsilon (p_{T}^{jet 6} > 50 GeV)",20,0,1,{"unit":""})
addVar("TMath::Log10(fs_frac_jet6pt50*xsect_8TeV_pb*1000)","log_{10}#left[#sigma^{SUSY}_{8 TeV,pp}#upoint A [fb]#right]",20,0,1,{"extralabel":"p_{T}^{jet 6} > 50 GeV","customBinning":logXsectBinning,"key":"fs_A_jet6pt50","unit":""})
#
addVar("fs_frac_jet8pt50","#epsilon (p_{T}^{jet 8} > 50 GeV)",20,0,1,{"unit":""})
addVar("TMath::Log10(fs_frac_jet8pt50*xsect_8TeV_pb*1000)","log_{10}#left[#sigma^{SUSY}_{8 TeV,pp}#upoint A [fb]#right]",20,0,1,{"extralabel":"p_{T}^{jet 8} > 50 GeV","customBinning":logXsectBinning,"key":"fs_A_jet8pt50","unit":""})

addVar("fs_frac_dphijet1mht","#epsilon (#Delta#phi(jet^{1},MHT))",20,0,1,{"unit":""})
addVar("TMath::Log10(fs_frac_dphijet1mht*xsect_8TeV_pb*1000)","log_{10}#left[#sigma^{SUSY}_{8 TeV,pp}#upoint A [fb]#right]",20,0,1,{"extralabel":"#Delta#phi(jet^{1},MHT)","customBinning":logXsectBinning,"key":"fs_A_dphijet1mht","unit":""})
addVar("fs_dphijet1mht","#Delta#phi(jet^{1},MHT)",20,2,3,{"unit":""})



logXsectBinning2 = [-6,-5.5,-5,-4.5,-4,-3.5,-3,-2.5,-2.,-1.5,-1,0,1,2]
# bjets
addVar("fs_nbjet","average N^{b-jet 1}",8,0,4,{"unit":""})
addVar("fs_ptbjet1","average p_{T}^{b-jet}",20,10,100,{"customBinning":[0,20,40,60,80,100,150,200,250,300,350]})
####
#
addVar("fs_frac_bjet1pt30","#epsilon (p_{T}^{b-jet 1} > 30 GeV)",20,0,1,{"unit":""})
addVar("TMath::Log10(fs_frac_bjet1pt30*xsect_8TeV_pb*1000)","log_{10}#left[#sigma^{SUSY}_{8 TeV,pp}#upoint A [fb]#right]",20,0,1,{"extralabel":"p_{T}^{b-jet 1} > 30 GeV","customBinning":logXsectBinning,"key":"fs_A_bjet1pt30","unit":""})
#
addVar("fs_frac_bjet1pt50","#epsilon (p_{T}^{b-jet 1} > 50 GeV)",20,0,1,{"unit":""})
addVar("TMath::Log10(fs_frac_bjet1pt50*xsect_8TeV_pb*1000)","log_{10}#left[#sigma^{SUSY}_{8 TeV,pp}#upoint A [fb]#right]",20,0,1,{"extralabel":"p_{T}^{b-jet 1} > 50 GeV","customBinning":logXsectBinning,"key":"fs_A_bjet1pt50","unit":""})
#
addVar("fs_frac_bjet1pt80","#epsilon (p_{T}^{b-jet 1} > 80 GeV)",20,0,1,{"unit":""})
addVar("TMath::Log10(fs_frac_bjet1pt80*xsect_8TeV_pb*1000)","log_{10}#left[#sigma^{SUSY}_{8 TeV,pp}#upoint A [fb]#right]",20,0,1,{"extralabel":"p_{T}^{b-jet 1} > 80 GeV","customBinning":logXsectBinning,"key":"fs_A_bjet1pt80","unit":""})
#
addVar("fs_frac_bjet1pt100","#epsilon (p_{T}^{b-jet 1} > 100 GeV)",20,0,1,{"unit":""})
addVar("TMath::Log10(fs_frac_bjet1pt100*xsect_8TeV_pb*1000)","log_{10}#left[#sigma^{SUSY}_{8 TeV,pp}#upoint A [fb]#right]",20,0,1,{"extralabel":"p_{T}^{b-jet 1} > 100 GeV","customBinning":logXsectBinning,"key":"fs_A_bjet1pt100","unit":""})
#
addVar("fs_frac_bjet1pt200","#epsilon (p_{T}^{b-jet 1} > 200 GeV)",20,0,1,{"unit":""})
addVar("TMath::Log10(fs_frac_bjet1pt200*xsect_8TeV_pb*1000)","log_{10}#left[#sigma^{SUSY}_{8 TeV,pp}#upoint A [fb]#right]",20,0,1,{"extralabel":"p_{T}^{b-jet 1} > 200 GeV","customBinning":logXsectBinning,"key":"fs_A_bjet1pt200","unit":""})
#
addVar("fs_frac_bjet1pt400","#epsilon (p_{T}^{b-jet 1} > 400 GeV)",20,0,1,{"unit":""})
addVar("TMath::Log10(fs_frac_bjet1pt400*xsect_8TeV_pb*1000)","log_{10}#left[#sigma^{SUSY}_{8 TeV,pp}#upoint A [fb]#right]",20,0,1,{"extralabel":"p_{T}^{b-jet 1} > 400 GeV","customBinning":logXsectBinning,"key":"fs_A_bjet1pt400","unit":""})
#
addVar("fs_frac_bjet1pt500","#epsilon (p_{T}^{b-jet 1} > 500 GeV)",20,0,1,{"unit":""})
addVar("TMath::Log10(fs_frac_bjet1pt500*xsect_8TeV_pb*1000)","log_{10}#left[#sigma^{SUSY}_{8 TeV,pp}#upoint A [fb]#right]",20,0,1,{"extralabel":"p_{T}^{b-jet 1} > 500 GeV","customBinning":logXsectBinning,"key":"fs_A_bjet1pt500","unit":""})
####
#
#addVar("fs_frac_bjet2pt30","#epsilon (p_{T}^{b-jet 2} > 30 GeV)",20,0,1,{"unit":""})
#addVar("TMath::Log10(fs_frac_bjet2pt30*xsect_8TeV_pb*1000)","log_{10}#left[#sigma^{SUSY}_{8 TeV,pp}(p_{T}^{b-jet 2} > 30 GeV) [fb]#right]",20,0,1,{"customBinning":logXsectBinning,"key":"fs_A_bjet2pt30","unit":""})
#
addVar("fs_frac_bjet2pt50","#epsilon (p_{T}^{b-jet 2} > 50 GeV)",20,0,1,{"unit":""})
addVar("TMath::Log10(fs_frac_bjet2pt50*xsect_8TeV_pb*1000)","log_{10}#left[#sigma^{SUSY}_{8 TeV,pp}#upoint A [fb]#right]",20,0,1,{"extralabel":"p_{T}^{b-jet 2} > 50 GeV","customBinning":logXsectBinning,"key":"fs_A_bjet2pt50","unit":""})
#
addVar("fs_frac_bjet2pt80","#epsilon (p_{T}^{b-jet 2} > 80 GeV)",20,0,1,{"unit":""})
addVar("TMath::Log10(fs_frac_bjet2pt80*xsect_8TeV_pb*1000)","log_{10}#left[#sigma^{SUSY}_{8 TeV,pp}#upoint A [fb]#right]",20,0,1,{"extralabel":"p_{T}^{b-jet 2} > 80 GeV","customBinning":logXsectBinning,"key":"fs_A_bjet2pt80","unit":""})
#
addVar("fs_frac_bjet2pt100","#epsilon (p_{T}^{b-jet 2} > 100 GeV)",20,0,1,{"unit":""})
addVar("TMath::Log10(fs_frac_bjet2pt100*xsect_8TeV_pb*1000)","log_{10}#left[#sigma^{SUSY}_{8 TeV,pp}#upoint A [fb]#right]",20,0,1,{"extralabel":"p_{T}^{b-jet 2} > 100 GeV","customBinning":logXsectBinning,"key":"fs_A_bjet2pt100","unit":""})
#
addVar("fs_frac_bjet2pt200","#epsilon (p_{T}^{b-jet 2} > 200 GeV)",20,0,1,{"unit":""})
addVar("TMath::Log10(fs_frac_bjet2pt200*xsect_8TeV_pb*1000)","log_{10}#left[#sigma^{SUSY}_{8 TeV,pp}#upoint A [fb]#right]",20,0,1,{"extralabel":"p_{T}^{b-jet 2} > 200 GeV","customBinning":logXsectBinning,"key":"fs_A_bjet2pt200","unit":""})
#
addVar("fs_frac_bjet2pt400","#epsilon (p_{T}^{b-jet 2} > 400 GeV)",20,0,1,{"unit":""})
addVar("TMath::Log10(fs_frac_bjet2pt400*xsect_8TeV_pb*1000)","log_{10}#left[#sigma^{SUSY}_{8 TeV,pp}#upoint A [fb]#right]",20,0,1,{"extralabel":"p_{T}^{b-jet 2} > 400 GeV","customBinning":logXsectBinning,"key":"fs_A_bjet2pt400","unit":""})
#
addVar("fs_frac_bjet2pt500","#epsilon (p_{T}^{b-jet 2} > 500 GeV)",20,0,1,{"unit":""})
addVar("TMath::Log10(fs_frac_bjet2pt500*xsect_8TeV_pb*1000)","log_{10}#left[#sigma^{SUSY}_{8 TeV,pp}#upoint A [fb]#right]",20,0,1,{"extralabel":"p_{T}^{b-jet 2} > 500 GeV","customBinning":logXsectBinning,"key":"fs_A_bjet2pt500","unit":""})

# photons
addVar("fs_npho","average N^{#gamma}",16,0,2,{"unit":""})
addVar("fs_ptpho1","average p_{T}^{#gamma 1}",20,10,100)
#
addVar("fs_frac_pho1pt10","#epsilon (p_{T}^{#gamma 1} > 10 GeV)",20,0,1,{"unit":""})
addVar("TMath::Log10(fs_frac_pho1pt10*xsect_8TeV_pb*1000)","log_{10}#left[#sigma^{SUSY}_{8 TeV,pp}#upoint A [fb]#right]",20,0,1,{"extralabel":"p_{T}^{#gamma 1} > 10 GeV","customBinning":logXsectBinning,"key":"fs_A_pho1pt10","unit":""})
#
addVar("fs_frac_pho1pt25","#epsilon (p_{T}^{#gamma 1} > 25 GeV)",20,0,1,{"unit":""})
addVar("TMath::Log10(fs_frac_pho1pt25*xsect_8TeV_pb*1000)","log_{10}#left[#sigma^{SUSY}_{8 TeV,pp}#upoint A [fb]#right]",20,0,1,{"extralabel":"p_{T}^{#gamma 1} > 25 GeV","customBinning":logXsectBinning,"key":"fs_A_pho1pt25","unit":""})
#
addVar("fs_frac_pho1pt50","#epsilon (p_{T}^{#gamma 1} > 50 GeV)",20,0,1,{"unit":""})
addVar("TMath::Log10(fs_frac_pho1pt50*xsect_8TeV_pb*1000)","log_{10}#left[#sigma^{SUSY}_{8 TeV,pp}#upoint A [fb]#right]",20,0,1,{"extralabel":"p_{T}^{#gamma 1} > 50 GeV","customBinning":logXsectBinning,"key":"fs_A_pho1pt50","unit":""})
#
addVar("fs_frac_pho2pt10","#epsilon (p_{T}^{#gamma 2} > 10 GeV)",20,0,1,{"unit":""})
addVar("TMath::Log10(fs_frac_pho2pt10*xsect_8TeV_pb*1000)","log_{10}#left[#sigma^{SUSY}_{8 TeV,pp}#upoint A [fb]#right]",20,0,1,{"extralabel":"p_{T}^{#gamma 2} > 10 GeV","customBinning":logXsectBinning,"key":"fs_A_pho2pt10","unit":""})
#
addVar("fs_frac_pho2pt25","#epsilon (p_{T}^{#gamma 2} > 25 GeV)",20,0,1,{"unit":""})
addVar("TMath::Log10(fs_frac_pho2pt25*xsect_8TeV_pb*1000)","log_{10}#left[#sigma^{SUSY}_{8 TeV,pp}#upoint A [fb]#right]",20,0,1,{"extralabel":"p_{T}^{#gamma 2} > 25 GeV","customBinning":logXsectBinning,"key":"fs_A_pho2pt25","unit":""})
#
addVar("fs_frac_pho2pt50","#epsilon (p_{T}^{#gamma 2} > 50 GeV)",20,0,1,{"unit":""})
addVar("TMath::Log10(fs_frac_pho2pt50*xsect_8TeV_pb*1000)","log_{10}#left[#sigma^{SUSY}_{8 TeV,pp}#upoint A [fb]#right]",20,0,1,{"extralabel":"p_{T}^{#gamma 2} > 50 GeV","customBinning":logXsectBinning,"key":"fs_A_pho2pt50","unit":""})

# leptons
addVar("fs_ptlep1","average p_{T}^{lepton 1}",20,10,100,{"customBinning":[0,20,40,60,80,100,150,200,250,300]})
addVar("fs_nlep","average N^{lep}",20,0,.5)
####
#
addVar("fs_frac_lep1pt5","#epsilon (p_{T}^{lep 1} > 10 GeV)",20,0,.4,{"unit":""})
addVar("TMath::Log10(fs_frac_lep1pt5*xsect_8TeV_pb*1000)","log_{10}#left[#sigma^{SUSY}_{8 TeV,pp}#upoint A [fb]#right]",20,0,1,{"extralabel":"p_{T}^{lep 1} > 5 GeV","customBinning":logXsectBinning,"key":"fs_A_lep1pt5","unit":""})
#
addVar("fs_frac_lep1pt10","#epsilon (p_{T}^{lep 1} > 10 GeV)",20,0,.4,{"unit":""})
addVar("TMath::Log10(fs_frac_lep1pt10*xsect_8TeV_pb*1000)","log_{10}#left[#sigma^{SUSY}_{8 TeV,pp}#upoint A [fb]#right]",20,0,1,{"extralabel":"p_{T}^{lep 1} > 10 GeV","customBinning":logXsectBinning,"key":"fs_A_lep1pt10","unit":""})
#
addVar("fs_frac_lep1pt25","#epsilon (p_{T}^{lep 1} > 25 GeV)",20,0,.4,{"unit":""})
addVar("TMath::Log10(fs_frac_lep1pt25*xsect_8TeV_pb*1000)","log_{10}#left[#sigma^{SUSY}_{8 TeV,pp}#upoint A [fb]#right]",20,0,1,{"extralabel":"p_{T}^{lep 1} > 25 GeV","customBinning":logXsectBinning,"key":"fs_A_lep1pt25","unit":""})
###
#
addVar("fs_frac_lep2pt5","#epsilon (p_{T}^{lep 2} > 5 GeV)",20,0,.1,{"unit":""})
addVar("TMath::Log10(fs_frac_lep2pt5*xsect_8TeV_pb*1000)","log_{10}#left[#sigma^{SUSY}_{8 TeV,pp}#upoint A [fb]#right]",20,0,1,{"extralabel":"p_{T}^{lep 2} > 5 GeV","customBinning":logXsectBinning,"key":"fs_A_lep2pt5","unit":""})
#
addVar("fs_frac_lep2pt10","#epsilon (p_{T}^{lep 2} > 10 GeV)",20,0,.1,{"unit":""})
addVar("TMath::Log10(fs_frac_lep2pt10*xsect_8TeV_pb*1000)","log_{10}#left[#sigma^{SUSY}_{8 TeV,pp}#upoint A [fb]#right]",20,0,1,{"extralabel":"p_{T}^{lep 2} > 10 GeV","customBinning":logXsectBinning,"key":"fs_A_lep2pt10","unit":""})
#
addVar("fs_frac_lep2pt25","#epsilon (p_{T}^{lep 2} > 25 GeV)",20,0,.1,{"unit":""})
addVar("TMath::Log10(fs_frac_lep2pt25*xsect_8TeV_pb*1000)","log_{10}#left[#sigma^{SUSY}_{8 TeV,pp}#upoint A [fb]#right]",20,0,1,{"extralabel":"p_{T}^{lep 2} > 25 GeV","customBinning":logXsectBinning,"key":"fs_A_lep2pt25","unit":""})
###
#
addVar("fs_frac_lep3pt5","#epsilon (p_{T}^{lep 3} > 5 GeV)",20,0,.1,{"unit":""})
addVar("TMath::Log10(fs_frac_lep3pt5*xsect_8TeV_pb*1000)","log_{10}#left[#sigma^{SUSY}_{8 TeV,pp}#upoint A [fb]#right]",20,0,1,{"extralabel":"p_{T}^{lep 3} > 5 GeV","customBinning":logXsectBinning,"key":"fs_A_lep3pt5","unit":""})
#
addVar("fs_frac_lep3pt10","#epsilon (p_{T}^{lep 3} > 10 GeV)",20,0,.1,{"unit":""})
addVar("TMath::Log10(fs_frac_lep3pt10*xsect_8TeV_pb*1000)","log_{10}#left[#sigma^{SUSY}_{8 TeV,pp}#upoint A [fb]#right]",20,0,1,{"extralabel":"p_{T}^{lep 3} > 10 GeV","customBinning":logXsectBinning,"key":"fs_A_lep3pt10","unit":""})
#
addVar("fs_frac_lep3pt25","#epsilon (p_{T}^{lep 3} > 25 GeV)",20,0,.1,{"unit":""})
addVar("TMath::Log10(fs_frac_lep3pt25*xsect_8TeV_pb*1000)","log_{10}#left[#sigma^{SUSY}_{8 TeV,pp}#upoint A [fb]#right]",20,0,1,{"extralabel":"p_{T}^{lep 3} > 25 GeV","customBinning":logXsectBinning,"key":"fs_A_lep3pt25","unit":""})

addVar("fs_pdgidSusy","susy pdg id",40,0,40)


# rebin
defaultRebin = [0,0.15,0.3,0.450,0.600,0.750,0.900,1.050,1.200,1.400,1.600,1.800,2.100,2.400,2.700,3.000]
def rebin(key,binning=defaultRebin,newkey=None):
    _var = copy.copy(varCfg[key])
    _var["customBinning"] = binning
    _var["binning"] = binning # sam added to help crash in plotZ.py which wanted "binning" instead of "customBinning", but didn't work
    if newkey is None:
        newkey = key + "_rebin"
    _var["name"] = newkey
    varCfg.update([[newkey,_var]])
    
qrb2 = [0,0.200,0.400,0.600,0.800,1.000,1.200,1.500,1.800,2.100,2.400,2.700,3.000]
qrb3 = [0,.300,.600,.900,1.200,1.500,1.800,2.100,2.400,2.700,3.000]
sleptonRebin = [0,.150,.300,.450,.600,.800,1.000,1.200,1.500,1.800,2.100,2.400,2.700,3.000]
squark3Rebin = [0,.300,.600,.800,1.000,1.200,1.400,1.600,1.800,1.950,2.100,2.250,2.400,2.550,2.700,2.850,3.000]

rebin("mg")
rebin("mz1",[0,.075,.150,.225,.300,.375,.450,.525,.600,.675,.750,.900,1.050,1.200,1.350,1.500])
rebin("mz1",[0,.150,.300,.450,.600,.750,.900,1.050,1.200,1.350,1.500],newkey="mz1_rebin2")
#rebin("mz1",[0,20,40,60,80,100,120,140,160,225,300,375,450,525,600,675,750,900,1050,1200,1350,1500],newkey="mz1_rebin3")
rebin("mz1",[0,.020,.040,.060,.080,.100,.120,.140,.160,.180,.200],newkey="mz1_rebin3")
rebin("mz2",qrb2)
rebin("mz3",qrb2)
rebin("mz4",qrb2)
rebin("mw1",qrb2)
rebin("mw2",qrb2)
rebin("mh",[116,120,121,122,123,124,125,126,127,128,129,130,134])
#rebin("mh",defaultRebin)
rebin("mA_pole",qrb2)
rebin("mHc")
rebin("mHh")
rebin("mLNDz",qrb2)
rebin("mLNDw",qrb2)
rebin("muL",qrb2)
rebin("muR",qrb2)
rebin("mdL",qrb2)
rebin("mdR",qrb2)
rebin("mb1",qrb2)
rebin("mb2",qrb3)
rebin("mt1",qrb3)
rebin("mt2",qrb3)
rebin("meR",qrb2)
rebin("meL",qrb2)
rebin("min_meLmeR",qrb2)
rebin("mtau1",qrb2)
rebin("mtau2",qrb2)
#rebin("xsect_8TeV",[0.001,0.01,rt.TMath.Power(10,-1.666),rt.TMath.Power(10,-1.333),0.1,rt.TMath.Power(10,-.666),rt.TMath.Power(10,-.333),1,rt.TMath.Power(10,.333),rt.TMath.Power(10,.666),10,rt.TMath.Power(10,1.333),rt.TMath.Power(10,1.666),100,rt.TMath.Power(10,2.333),rt.TMath.Power(10,2.666),1000,10000,100000,1000000])
rebin("log10_xsect_8TeV",[-3,-2,-1.5,-1,-.5,0.,0.333,0.666,1.,1.333,1.666,2,2.333,2.666,3.,3.333,3.666,4,5,6])

addVar("MH3","A mass",15,0,3,{"key":"MH3_rebin"})
addVar("tanb","tan#beta",15,0,60,{"unit":"","key":"tanb_rebin"})
rebin("log10_sigSD",[-12,-11,-10,-9,-8.333,-7.666,-7.,-6.333,-5.666,-5,-4.333,-3.666,-3,-2,-1])
rebin("log10_sigSI",[-15,-14,-13,-12,-11.333,-10.666,-10,-9.5,-9.,-8.5,-8,-7.5,-7,-6.333,-5,-4])
addVar("TMath::Log10(omg)","log_{10}(#Omega_{#tilde{#chi}^{0}_{1}}h^{2})",16,-4,4,{"key":"log10_omgh2_rebin","unit":""})
addVar("(At - tb/mu)/sqrt(mt1*mt2)","(A_{t} - (#mu/tan#beta)) / #sqrt{m_{#tilde{t}_{1}}m_{#tilde{t}_{2}}}",16,-4,4,{"key":"XtDms_rebin","unit":""})
addVar("min(mg,min(mdL,min(mdR,min(muL,min(muR,min(mb1,min(mb2,min(mt1,mt2))))))))/1000","LCSP mass",16,0,2.500,{"key":"mLCSP_rebin"})


AddMassDiff("mg_rebin","mz1")
AddMassDiff("muL_rebin","mz1")
AddMassDiff("muR_rebin","mz1")
AddMassDiff("mdL_rebin","mz1")
AddMassDiff("mdR_rebin","mz1")
AddMassDiff("mb1_rebin","mz1")
AddMassDiff("mt1_rebin","mz1")
AddMassDiff("mt1_rebin","mz1")
AddMassDiff("mz2_rebin","mz1")
AddMassDiff("mw1_rebin","mz1")
AddMassDiff("mLCSP_rebin","mz1")
