#!/usr/bin/env python

import sys,os,shutil,array

SMALL = 30
MEDIUM = 35
LARGE = 45

IDIR = sys.argv[1]
CFG = sys.argv[2]
ODIR = sys.argv[3]
FORMAT = "pdf"

sys.argv.append("-b")
import ROOT as rt
print rt.TGaxis.GetMaxDigits()
rt.TGaxis.SetMaxDigits(4)

# read variables from variables.cfg.py
from variables_cfg import varCfg

# read in combinations
FILE = open(CFG)
exec(FILE)
FILE.close()

# the canvas
c = rt.TCanvas('c', 'c', 800, 800)
c.SetBottomMargin(0.15)
c.SetLeftMargin(0.14)

# the legend
legend = rt.TLegend(0.18,0.85,0.6,0.88)
legend.SetFillStyle(0)
legend.SetBorderSize(0)
legend.SetTextFont(134)
legend.SetTextSize(SMALL)
legend.SetMargin(0.25)
legend.SetTextAlign(12)

# line legend
lines = []
lineLegend = None
if 'lineLayout' in locals() and lineLayout is not None:
    lineLegend = rt.TLegend(0.189,0.88,0.65,0.88)
    lineLegend.SetNColumns(len(lineLayout))
    for key in ["050","100","150"]:
        lines.append(rt.TLine())
        lines[-1].SetLineStyle(lineLayout[key]["linestyle"])
        lines[-1].SetLineWidth(lineLayout[key]["linewidth"])
        lineLegend.AddEntry(lines[-1],lineLayout[key]["linetitle"],"l")
    lineLegend.SetFillStyle(0)
    lineLegend.SetBorderSize(0)
    lineLegend.SetTextFont(134)
    lineLegend.SetTextSize(SMALL) # 30
    #lineLegend.SetMargin(0.35)
    lineLegend.SetTextAlign(12)

# extra lines
boxXtra = rt.TPaveText(0.17,0.88,0.65,0.88,"NDC")
boxXtra.SetFillStyle(0)
boxXtra.SetBorderSize(0)
boxXtra.SetTextFont(134)
boxXtra.SetTextSize(SMALL) #23
boxXtra.SetTextAlign(12)
#boxXtra.SetMargin(0.35)

# a box
box = rt.TPaveText(0.10,0.89,0.93,0.91+30./800,"NDC")
box.SetFillStyle(0)
box.SetTextFont(134)
box.SetTextSize(LARGE)
box.SetBorderSize(0)
box.SetTextAlign(31)
box.AddText("CMS, pMSSM")


# the histogram layout
def doLayout(hist,options,var):

    hist.SetStats(0)
    hist.SetTitle("")

    # x-axis
    hist.SetTitleFont(134,"X")
    hist.SetTitleSize(LARGE,"X") # 30
    hist.SetLabelFont(134,"X")
    hist.SetLabelSize(MEDIUM,"X") # 25
    hist.SetTitleOffset(1.0,"X")
    hist.GetXaxis().CenterTitle()
    #hist.GetXaxis().SetNoExponent(True)
    # y-axis
    hist.SetTitleFont(134,"Y")
    hist.SetTitleSize(LARGE,"Y") # 30
    hist.SetTitleOffset(1.2,"Y")
    hist.SetLabelFont(134,"Y")
    hist.SetLabelSize(MEDIUM,"Y") # 25
    hist.GetYaxis().CenterTitle()
    hist.GetYaxis().SetNdivisions(10,0,0)
    if "ytitle" in options:
        _title = options["ytitle"]
        if "unit" in var and var["unit"] != "":
            _title += " / " + var["unit"]
        hist.SetYTitle(_title)
    # normalisation
    if "normalise" in options and options["normalise"]:
        hist.Scale(1./hist.Integral(0,hist.GetNbinsX()+1))
    else:
        _int = hist.Integral(0,hist.GetNbinsX()+1)
        hist.Scale(hist.GetEntries()/_int)
    # /bin -> /unit
    for b in range(1,hist.GetNbinsX()+1):
        _bc = hist.GetBinContent(b)/hist.GetBinWidth(b)
        hist.SetBinContent(b,_bc)
    # colors
    if "linecolor" in options:
        hist.SetLineColor(options["linecolor"])
    if "markerstyle" in options:
        hist.SetMarkerStyle(options["markerstyle"])
        hist.SetMarkerSize(1.8)
    if "markercolor" in options:
        hist.SetMarkerColor(options["markercolor"])
    if "fillcolor" in options:
        hist.SetFillColor(options["fillcolor"])
    # line width
    if "linewidth" in options:
        hist.SetLineWidth(options["linewidth"])
    if "linestyle" in options:
        hist.SetLineStyle(options["linestyle"])
        
# read 1D histogram names from preCMS file
histName = []

# loop over all combinations
for entry in combinations:
    rt.gPad.Clear()
    combName = entry[0]
    comb = entry[1]
    print "###################################"
    print "  drawing for " + combName
    print "###################################"    

    # clean up and make output directory
    odir = ODIR + "/" + combName
    if os.path.exists(odir):
        shutil.rmtree(odir)
    os.makedirs(odir)
    
    # open root files
    filedict = dict()
    for distr in comb:
        if not distr[0] in filedict:
            filedict.update([[distr[0],rt.TFile.Open(IDIR + "/" + distr[0] + ".root")]])

        if len(histName) == 0:
            for key in filedict[distr[0]].GetListOfKeys():
                if key.GetClassName() == "TH1D":
                    histName.append(key.GetName())

    
    # draw all 1D histograms
    for name in histName:
        _legend = legend.Clone()
        histList = []
        histDrawOptionList = []
        for distr in comb:
            key = distr[0]
            options = distr[1]
            _file = filedict[key]
            hist = _file.Get(name)
            doLayout(hist,options,varCfg[name])
            histList.append(hist)
            histDrawOptionList.append("HIST")
            if "drawstyle" in options:
                histDrawOptionList[-1] = options["drawstyle"]
            if "legendtitle" in options:
                _legend.AddEntry(hist,options["legendtitle"],options["legendoption"])
        _boxXtra = boxXtra.Clone()
        if len(entry) > 2 and "extraLegendLines" in entry[2]:
            for line in entry[2]["extraLegendLines"]:
                _boxXtra.AddText(line)

        # find max
        _max = 0
        for hist in histList:
            __max = hist.GetMaximum()
            if __max > _max:
                _max = __max
        # find min
        _min = None
        for hist in histList:
            for b1 in range(0,hist.GetNbinsX()):
                bc = hist.GetBinContent(b1)
                if bc > 0.:
                    if _min is None or _min > bc:
                        _min = bc
        if "logScale" in varCfg[name] and varCfg[name]["logScale"] == 1:
            if not "xLogScale" in varCfg[name] or varCfg[name]["xLogScale"]==1:
                rt.gPad.SetLogx()
            rt.gPad.SetLogy()
        else:
            rt.gPad.SetLogx(0)
            rt.gPad.SetLogy(0)
        if "SETLOGY" in locals() and SETLOGY:
            rt.gPad.SetLogy()            

        for h in range(0,len(histList)):
            if h == 0:
                if not rt.gPad.GetLogy():
                    histList[h].SetMinimum(0)
                    histList[h].SetMaximum(_max*1.5)
                else:
                    lmax = rt.TMath.Log10(_max)
                    lmin = rt.TMath.Log10(_min)
                    histList[h].SetMinimum(_min)
                    histList[h].SetMaximum(rt.TMath.Power(10,lmax + (lmax - lmin)*0.45))
                histList[h].Draw(histDrawOptionList[h])
            else:
                histList[h].Draw(histDrawOptionList[h]+",HIST,SAME")
        

        n = _legend.GetNRows()
        y1 = _legend.GetY2()-1.5*25./800*n
        _legend.SetY1(y1)
        _legend.Draw()
        if lineLegend is not None:
            _lineLegend = lineLegend.Clone()
            _lineLegend.SetY1(y1-1.5*25./800)
            _lineLegend.SetY2(y1)
            _lineLegend.Draw()
        _boxXtra.SetY1(y1-1.4*25./800)
        _boxXtra.SetY2(y1-2*1.4*25./800)
        _boxXtra.Draw()
        box.Draw()

        # extra labels
        extralabel = None
        if "extralabel" in varCfg[name]:
            extralabel = rt.TPaveText(0.7,0.8,0.6,0.8,"brNDC")
            extralabel.SetFillStyle(0)
            extralabel.SetBorderSize(0)
            extralabel.SetTextFont(134)
            extralabel.SetTextAlign(12)
            extralabel.SetTextSize(SMALL)
            extralabel.AddText(varCfg[name]["extralabel"])
        if extralabel is not None:
            extralabel.Draw()
            

        for format in FORMAT.split(","):
            rt.gPad.Print(odir + "/" + combName + "_" + name + "." + format) 
        rt.gPad.SetLogx(0)
        histList[0].SetMaximum(-1111)
    
    # close root files
    for file in filedict.values():
        file.Close()
    
