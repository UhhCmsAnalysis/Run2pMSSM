#!/usr/bin/env python

SMALL = 30
MEDIUM = 35
LARGE = 45

import sys,os,shutil,array
from legendTitles import *

IDIR = sys.argv[1]
ODIR = sys.argv[2]
option = None
if len(sys.argv) >= 4:
    option = sys.argv[3]
print option
test = (option == "test")
do_sp = (option == "sp")
do_ratio = (option == "ratio")

sys.argv.append("-b")
import ROOT as rt

FORMAT = "pdf"



do_sp = True

showBCR = False
#rt.TGaxis.SetMaxDigits(3)

#o_preCMS_lhd = {"mode":"preCMS_lhd","ztitle":"p(#theta) / p(#theta)^{max}"}
#o_preCMS_lhdHw = {"mode":"preCMS_lhdHw"}
#o_lhd = {"mode":"lhd","ztitle":"p(#theta) / p(#theta)^{max}"}
#o_zlhd = {"mode":"zlhd","ztitle":"p(#theta) / p(#theta)^{max}"}
o_preCMS_lhd = {"mode":"preCMS_lhd","ztitle":"probability density"}
o_preCMS_123mh128_lhd = {"mode":"preCMS_123mh128_lhd","ztitle":"p^{non-DCS}(#theta)"}
o_lhd = {"mode":"lhd",
         "do_ratio":True,
         "ztitle":"probability density",
         "ztitle_ratio":"p(#theta|D^{CMS}) / p^{non-DCS}(#theta)",
         "preCMSKey":"preCMS"
         }
o_zlhd = {"mode":"zlhd",
          "do_sp":True,
          "do_ratio":True,
          "ztitle":"probability density",
          "ztitle_sp":"survival probability",
          "ztitle_ratio":"p(#theta|Z^{CMS}>-1.64) / p^{non-DCS}(#theta)",
          "preCMSKey":"preCMS",}
o_zlhd_123mh128 = {"mode":"zlhd_123mh128",
                   "do_sp":True,
                   "do_ratio":True,
                   "ztitle":"p(#theta|Z^{CMS}>-1.64)",
                   "ztitle_sp":"survival probability",
                   "ztitle_ratio":"p(#theta|Z^{CMS}>-1.64) / p^{non-DCS}(#theta)",
                   "preCMSKey":"preCMS_123mh128"}
#o_zlhdHw = {"mode":"zlhdHw"}
#o_invZlhd = {"mode":"invZlhd"}

ratiotitle = "p(#theta|D^{CMS}) / p^{non-DCS}(#theta)"

# read variables from variables.cfg.py
from variables_cfg import varCfg

combination = [
    ############################
    # llhds
    ############################
    ["preCMS" , o_preCMS_lhd],    
    #["preCMS_123mh128" , o_preCMS_123mh128_lhd],    
    # SUS12003
    #["SUS12003_1BL_lhd_100" , o_lhd],
    #["SUS12003_1BT_lhd_100" , o_lhd],
    #["SUS12003_2BL_lhd_100" , o_lhd],
    #["SUS12003_2BT_lhd_100" , o_lhd],
    #["SUS12003_3BL_lhd_100" , o_lhd],
    # SUS12006
    #["SUS12006_lhd_100" , o_lhd],
    # SUS12011
    #["SUS12011_lhd_100" , o_lhd],
    # SUS12024
    #["SUS12024_lhd_100" , o_lhd],
    # SUS13006
    #["SUS13006_lhd_100" , o_lhd],
    # SUS13012
    #["SUS13012_lhd_100" , o_lhd],
    #["SUS13019_lhd_100",o_lhd]
    # SUS12006 SUS13006
    #["SUS12006_SUS13006_lhd_100" , o_lhd],
    # SUS12011 SUS13012
    #["SUS12011_SUS13012_lhd_100" , o_lhd],
    #["combined7and8and13TeV_surv_100" , o_zlhd],
    ["SUS12024_SUS12011_SUS13012_SUS16033_lhd_100" , o_zlhd],
    #["combined7and8TeV_123mh128_surv_100" , o_zlhd_123mh128],
    #["EXO11059_EXO12048_SUS13009_surv_100", o_zlhd],
]

if test:
    combination = [combination[0],combination[1],combination[-1]]

# the canvas
c = rt.TCanvas('c', 'c', 800, 800)
c.SetBottomMargin(0.15)
c.SetLeftMargin(0.17)
c.SetRightMargin(0.19)
c.SetTopMargin(0.14)
if showBCR:
    c.SetTopMargin(0.16)

# the legend
legend =  rt.TLegend(0.15, 0.80-1.15*2*30./800,1.-c.GetRightMargin(), 0.80);
legend.SetNColumns(2)
legend.SetBorderSize(0);
legend.SetFillStyle(0000);
legend.SetTextFont(134);
legend.SetTextSize(SMALL)
legend.SetTextAlign(32)
if not showBCR:
    legend.SetY1(0.905)

# a box
box = rt.TPaveText(0.10,0.89,1.-c.GetRightMargin()+0.04,0.91+30./800,"NDC")
box.SetFillStyle(0)
box.SetTextFont(134)
box.SetTextSize(LARGE)
box.SetBorderSize(0)
box.SetTextAlign(31)
box.AddText("CMS, pMSSM")

def doLayout2D(hist):
    hist.SetStats(0)
    hist.SetTitle("")
    hist.SetMinimum(0)

    # x-axis
    hist.SetTitleFont(134,"X")
    hist.SetTitleSize(LARGE,"X")
    hist.SetLabelFont(134,"X")
    hist.SetLabelSize(MEDIUM,"X")
    hist.SetTitleOffset(1.1,"X")
    hist.GetXaxis().CenterTitle()
    # y-axis
    hist.SetTitleFont(134,"Y")
    hist.SetTitleSize(LARGE,"Y")
    hist.SetLabelFont(134,"Y")
    hist.SetLabelSize(MEDIUM,"Y")
    hist.SetTitleOffset(1.3,"Y")
    hist.GetYaxis().CenterTitle()
    # z-axis
    hist.SetTitleFont(134,"Z")
    hist.SetTitleSize(LARGE,"Z")
    hist.SetLabelFont(134,"Z")
    hist.SetLabelSize(MEDIUM,"Z")
    hist.SetTitleOffset(3,"Z")
    hist.GetZaxis().CenterTitle()


def normaliseToUnitArea(hist):
    # scale
    hist.Scale(1./hist.Integral(0,hist.GetNbinsX()+2,0,hist.GetNbinsY()))
    ax = hist.GetXaxis()
    ay = hist.GetYaxis()
    for bx in range(1,hist.GetNbinsX()+1):
        for by in range(1,hist.GetNbinsY()+1):
            bc = hist.GetBinContent(bx,by)/ax.GetBinWidth(bx)/ay.GetBinWidth(by)
            hist.SetBinContent(bx,by,bc)
    _max = hist.GetMaximum()
    if _max < 0.0001:
        hist.Scale(1000000)
        return -6
    elif _max < 0.01:
        hist.Scale(1000)
        return -3
    else:
        return 0
    #hist.SetBinContent(bx,by,_bc)
    # give color to empty bins
    #or bx in range(1,hist.GetNbinsX()+1):
    #   for by in range(1,hist.GetNbinsY()+1):
    #       hist.Fill(ax.GetBinCenter(bx),ay.GetBinCenter(by),0.00000000000001)
    

def setZTitle(hist,option,var1,var2):
    if "ztitle" in option:
        _title = option["ztitle"]
        unit = []
        if "unit" in var1 and var1["unit"] != "":
            unit.append(var1["unit"])
        if "unit" in var2 and var2["unit"] != "":
            unit.append(var2["unit"])
        if len(unit) > 0:
            _title += " / " + unit[0]
        if len(unit) > 1:
            if unit[0] != unit[1]:
                _title += " #upoint " + unit[1]
            else:
                _title += "^{2}"
    hist.SetZTitle(_title)

rt.gStyle.SetNumberContours(100)            
# create palette
NRGBs = 5
NCont = 255
stops = array.array('d', [ 0.00, 0.34, 0.61, 0.84, 1.00 ])
red   = array.array('d', [ 0.50, 0.50, 1.00, 1.00, 1.00 ])
green = array.array('d', [ 0.50, 1.00, 1.00, 0.60, 0.50 ])
blue  = array.array('d', [ 1.00, 1.00, 0.50, 0.40, 0.50 ])
rt.TColor.CreateGradientColorTable(NRGBs, stops, red, green, blue, NCont)

"""
if do_ratio:
    # create palette
    print "!!!"
    NRGBs = 2
    NCont = 100
    stops = array.array('d', [ 0.0, 1.00 ])
    red   = array.array('d', [ 1, 0.8 ])
    green = array.array('d', [ 0.8, 0.0 ])
    blue  = array.array('d', [ 0.8, 0.0 ])
    rt.TColor.CreateGradientColorTable(NRGBs, stops, red, green, blue, NCont)
"""

if do_ratio or do_sp:
    # create palette
    print "!!!"
    NRGBs = 3
    NCont = 100
    stops = array.array('d', [ 0.0, 0.5, 1.00 ])
    red   = array.array('d', [ 255./255, 255./255,0.3 ])
    green = array.array('d', [ 175./255, 0.0     ,0.1 ])
    blue  = array.array('d', [ 0.,      0.0     ,0])
    rt.TColor.CreateGradientColorTable(NRGBs, stops, red, green, blue, NCont)

"""
if do_sp:
    # create palette
    print "!!!"
    NRGBs = 2
    NCont = 100
    stops = array.array('d', [ 0.0, 1.00 ])
    red   = array.array('d', [ 0.8, 0.0 ])
    green = array.array('d', [ 0.8, 0.0 ])
    blue  = array.array('d', [ 1., 0.8 ])
    rt.TColor.CreateGradientColorTable(NRGBs, stops, red, green, blue, NCont)
"""

# countour
def contour(hist,cred):
    _hist = hist.Clone()
    _hist.SetContour(2)
    # create a list of bins, ordered to decreasing bin content
    binlist = []
        # fill the list
    for ix in range(0,hist.GetNbinsX()+1):
        for iy in range(0,hist.GetNbinsY()+1):
            binlist.append([ix,iy,hist.GetBinContent(ix,iy)])
            _hist.SetBinContent(ix,iy,0)
        # order the list
        binlist.sort(key=lambda x: -x[2])
        int = hist.Integral(0,hist.GetNbinsX(),0,hist.GetNbinsY())
        sum = 0
        # fill contour histograms
        for b in binlist:
            sum += b[2]/int
            if sum < cred:
                _hist.SetBinContent(b[0],b[1],1)
            else:
                _hist.SetBinContent(b[0],b[1],0)            
    return _hist

# read 2D histogram names from preCMS file
histName = []
file_preCMS = rt.TFile.Open(IDIR + "/preCMS.root")
for key in file_preCMS.GetListOfKeys():
    if key.GetClassName() == "TH2D":
        histName.append(key.GetName())
#histName = ["mg_rebin_VS_mz1_rebin"]
#histName = ["mz1_rebin_VS_log10_omgh2_rebin"]
#histName = ["mt1_rebin_VS_XtDms_rebin"]

filedict = dict()
filedict.update([["preCMS",file_preCMS]])

preCMS = dict()
for [analysis,option] in combination:
    # clean up and make output directory
    odir = ODIR + "/" + analysis
    if os.path.exists(odir):
        shutil.rmtree(odir)
    os.makedirs(odir)

    # open root files if needed
    if not analysis in filedict:
        filedict.update([[analysis,rt.TFile.Open(IDIR + "/" + analysis + ".root")]])
    
    if analysis.find("preCMS")==0:
        preCMS.update([[analysis,dict()]])
    # draw all 2D histograms
    for name in histName:
        print 'now hoping to move into the file given by analysis', analysis, 'in the dict', filedict
        file = filedict[analysis]
        print  'shall now attempt to extract', name, 'from', file.GetName()
        histOri = file.Get(name)
        [name1,name2] = name.split("_VS_")
        
        if analysis.find("preCMS")==0:
            preCMS[analysis].update([[name,histOri]])


        #########################
        # the simple distributions
        #########################


        hist = histOri.Clone()
        doLayout2D(hist)
        _power = normaliseToUnitArea(hist)
        setZTitle(hist,option,varCfg[name1],varCfg[name2])
        
        hist.Draw("colz")
        rt.gPad.Update()
        zaxis = hist.GetListOfFunctions().FindObject("palette")
        zaxis.SetTitleOffset(1.1)
        
        """
        h_68 = contour(hist,0.68)
        h_68.SetLineColor(rt.kGray+1)
        h_68.SetLineWidth(4)
        h_95 = contour(hist,0.95)
        h_95.SetLineColor(rt.kBlack)
        h_95.SetLineWidth(4)
        if showBCR:
            h_68.Draw("CONT3,SAME")
            h_95.Draw("CONT3,SAME")
        """

        box.Draw()
        _legend = legend.Clone()
        _key = analysis.replace("_lhd_100","").replace("_excl_100","").replace("_surv_100","")
        _legend.SetHeader(legendTitle[_key])

        """
        if(showBCR):
            _legend.AddEntry(h_68,"68% BCR ", "l");
            _legend.AddEntry(h_95,"95% BCR ", "l");
        """

        _legend.Draw()

        boxPower = None
        if _power !=0:
            boxPower = rt.TPaveText(1.-c.GetRightMargin() + 0.05,1.-c.GetTopMargin()-0.03,1.,1.,"NDC")
            boxPower.SetFillStyle(0)
            boxPower.SetTextFont(134)
            boxPower.SetTextSize(MEDIUM)
            boxPower.SetBorderSize(0)
            boxPower.SetTextAlign(13)
            boxPower.SetMargin(0)
            boxPower.AddText("#times10^{{{0}}}".format(_power))
            boxPower.Draw()
            

        if "logScale" in varCfg[name1] and varCfg[name1]["logScale"] == 1:
            rt.gPad.SetLogx()
        else:
            rt.gPad.SetLogx(0)
        if "logScale" in varCfg[name2] and varCfg[name2]["logScale"] == 1:
            rt.gPad.SetLogy()
        else:
            rt.gPad.SetLogy(0)
        if rt.gPad.GetLogy() or rt.gPad.GetLogx():
            rt.gPad.SetLogz()
            _min = None
            for b1 in range(0,hist.GetNbinsX()):
                for b2 in range(0,hist.GetNbinsX()):
                    bc = hist.GetBinContent(b1,b2)
                    if bc > 0.:
                        if _min is None or _min > bc:
                            _min = bc
            hist.SetMinimum(_min)
        else:
            rt.gPad.SetLogz(0)


        if not do_sp and not do_ratio:
            for format in FORMAT.split(","):
                rt.gPad.Print(odir + "/" + analysis + "_" + name + "." + format) 
    
        
        if analysis.find("preCMS") == 0:
            continue

        ####################
        # the ratio
        ####################

        if do_ratio and "do_ratio" in option and option["do_ratio"]:
            
            hist_num = histOri.Clone()
            doLayout2D(hist_num)
            normaliseToUnitArea(hist_num)
            hist_num.SetZTitle(option["ztitle_ratio"])
            
            hist_denom = preCMS[option["preCMSKey"]][name].Clone()
            normaliseToUnitArea(hist_denom)
            hist_num.Divide(hist_denom)
            hist_num.SetMinimum(0.)

            hist_num.Draw("colz")
            rt.gPad.Update()
            zaxis = hist_num.GetListOfFunctions().FindObject("palette")
            zaxis.SetTitleOffset(1.2)
            _legend.Draw()
            box.Draw()
            for format in FORMAT.split(","):
                rt.gPad.Print(odir + "/" + analysis + "_" + name + "_ratio." + format) 
            
        ####################
        # the survival probability
        ####################
        if do_sp and "do_sp" in option and option["do_sp"]:
            
            hist_num = histOri.Clone()
            doLayout2D(hist_num)
            hist_num.SetZTitle(option["ztitle_sp"])
            
            hist_denom = preCMS[option["preCMSKey"]][name].Clone()
            hist_num.Divide(hist_denom)
            hist_num.SetMinimum(0.)
            hist_num.SetMaximum(1.)

            hist_num.SetMinimum(0)
            hist_num.SetMaximum(1)
            hist_num.Draw("colz")
            rt.gPad.Update()
            zaxis = hist_num.GetListOfFunctions().FindObject("palette")
            zaxis.SetTitleOffset(1.1)
            _legend.Draw()
            box.Draw()
            for format in FORMAT.split(","):
                rt.gPad.Print(odir + "/" + analysis + "_" + name + "_sp." + format) 

        """
            nb1 = histClone2.GetNbinsX()
        nb2 = histClone2.GetNbinsY()
        histClone2.Scale(histClone2.GetEntries()/histClone2.Integral(0,nb1+1,0,nb2+1))
        hist_denom = preCMS[option["preCMSKey"]][name].Clone()
        hist_denom.Scale(histClone2.GetEntries()/hist_denom.Integral(0,nb1+1,0,nb2+1))
        histClone2.Divide(hist_denom)
        #for b1 in range(0,nb1):
        #    for b2 in range(0,nb2):
        #        histClone2.SetBinContent(b1,b2,min(1.,histClone2.GetBinContent(b1,b2)))
        histClone2.Draw("colz")
        rt.gPad.Update()
        zaxis = histClone.GetListOfFunctions().FindObject("palette")
        zaxis.SetTitleOffset(1.2)
        _legend.Draw()
        box.Draw()
        for format in FORMAT.split(","):
            rt.gPad.Print(odir + "/" + analysis + "_" + name + "_sp." + format) 
        """
