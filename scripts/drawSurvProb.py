#!/usr/bin/env python

import sys,glob,os,math,shutil

SMALL = 30
MEDIUM = 35
LARGE = 45

# command line arguments
IDIR = sys.argv[1]
CFG = sys.argv[2]
ODIR = sys.argv[3]
FORMAT = "pdf"

sys.argv.append("-b")
import ROOT as rt

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
legend = rt.TLegend(0.18,0.88,0.6,0.88)
legend.SetFillStyle(0)
legend.SetBorderSize(0)
legend.SetTextFont(134)
legend.SetTextSize(SMALL)
legend.SetMargin(0.25)
legend.SetTextAlign(12)

# line legend
lines = []
lineLegend = rt.TLegend(0.189,0.88,0.6,0.88)
lineLegend.SetNColumns(len(lineLayout))
for key in ["050","100","150"]:
    lines.append(rt.TLine())
    lines[-1].SetLineStyle(lineLayout[key]["linestyle"])
    lines[-1].SetLineWidth(lineLayout[key]["linewidth"])
    lines[-1].SetLineColor(lineLayout[key]["linecolor"])
    lineLegend.AddEntry(lines[-1],lineLayout[key]["linetitle"],"l")
lineLegend.SetFillStyle(0)
lineLegend.SetBorderSize(0)
lineLegend.SetTextFont(134)
lineLegend.SetTextSize(SMALL)
lineLegend.SetMargin(0.35)
lineLegend.SetTextAlign(12)

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
    hist.SetMinimum(0)

    # x-axis
    hist.SetTitleFont(134,"X")
    hist.SetTitleSize(LARGE,"X")
    hist.SetLabelFont(134,"X")
    hist.SetLabelSize(MEDIUM,"X")
    hist.SetTitleOffset(1.0,"X")
    hist.GetXaxis().CenterTitle()
    # y-axis
    hist.SetTitleFont(134,"Y")
    hist.SetTitleSize(LARGE,"Y")
    hist.SetTitleOffset(1.2,"Y")
    hist.SetLabelFont(134,"Y")
    hist.SetLabelSize(MEDIUM,"Y")
    hist.GetYaxis().SetTitle("survival probability")
    hist.GetYaxis().CenterTitle()
    hist.GetYaxis().SetNdivisions(10,0,0)
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

# read histogram paths
preCMSfile_path = IDIR + "/preCMS.root"
histName = []
file_preCMS = rt.TFile.Open(preCMSfile_path)
for key in file_preCMS.GetListOfKeys():
    if key.GetClassName() == "TH1D":
        histName.append(key.GetName())
        file_preCMS.Get(histName[-1])
print histName
#sys.exit()

def getError(sumw,sumw2):
    Q = 0
    tau = 2.67442025444541689e-07
    if sumw > 1e-150:
        Q = sumw*sumw/sumw2
        tau = sumw/Q
    Ql = 0.5*rt.TMath.ChisquareQuantile(0.16,Q*2)
    Qu = 0.5*rt.TMath.ChisquareQuantile(0.84,Q*2+2)
    dQ = max(Q-Ql,Qu-Q)
    #print Ql,"<",Q,"<",Qu
    #print "sw:{0} sqrt(sw2):{1} Q:{2} dQ:{3} dsw:{4}".format(sumw,math.sqrt(sumw2),Q,dQ,dQ*tau)
    #if sumw > 0:
    #    print sumw/rt.TMath.Sqrt(sumw2),Q/dQ
    return dQ*tau

for entry in combinations:
    combName = entry[0]
    comb = entry[1]
    print "###################################"
    print "  drawing for " + combName
    print "###################################"    

    # clean up and make output directory
    odir = ODIR + "/" + combName + "_sp"
    if os.path.exists(odir):
        shutil.rmtree(odir)
    os.makedirs(odir)
    
    # open root files
    print "#"
    filedict = dict()
    for entry in comb:
        print entry[0]
    print "#"
    for x in comb:
        print x[1]
    for distr in [x[0] for x in comb] + [x[1]["denom"] for x in comb]:
        if not distr in filedict:
            _file = rt.TFile.Open(IDIR + "/" + distr + ".root")
            for key in _file.GetListOfKeys():
                _file.Get(key.GetName())
            filedict.update([[distr,_file]])
    for key in filedict.keys():
        print key            
            
    # draw all 1D histograms
    for name in histName:

        _legend = legend.Clone()
        _lineLegend = lineLegend.Clone()
        histList = []
        histDrawOptionList = []
        graphList = []
        temp = []
        for d in range(0,len(comb)):
            distr = comb[d]
            key = distr[0]
            options = distr[1]
            _file = filedict[key]
            print 'fileeeeeeee', _file.GetName()
            _file_denom = filedict[options["denom"]]
            print 'attempting to grab', name, ' from fileeeeeeee_denom', _file_denom.GetName()
            hist = _file.Get(name)
            hist_denom = _file_denom.Get(name)
            doLayout(hist,options,varCfg[name])
            hist_num = hist.Clone()
            hist.Divide(hist_denom)
            histList.append(hist)
            histDrawOptionList.append("HIST")
            if "drawstyle" in options:
                histDrawOptionList[-1] = options["drawstyle"]
            # statistical uncertainty
            if "showStatUncert" in options and options["showStatUncert"] == True:
                g = rt.TGraphAsymmErrors()
                a = hist.GetXaxis()
                for b in range(1,a.GetNbins()+1):
                    #print "****",b
                    # x coordinates
                    x = a.GetBinCenter(b)
                    xl = a.GetBinLowEdge(b)
                    xu = a.GetBinUpEdge(b)
                    # y coordinates
                    y = hist.GetBinContent(b)
                    # pass 
                    Y1 = hist_num.GetBinContent(b)
                    dY1 = hist_num.GetBinError(b)
                    #print "before:", Y1,dY1
                    dY1 = getError(Y1,dY1*dY1)
                    #print "after:", Y1,dY1
                    # fail
                    Y0 = hist_denom.GetBinContent(b) - Y1

                    if math.pow(hist_denom.GetBinError(b),2) - math.pow(hist_num.GetBinError(b),2) < 0: 
                        print 'happening', math.pow(hist_denom.GetBinError(b),2),math.pow(hist_num.GetBinError(b),2), math.pow(hist_denom.GetBinError(b),2) - math.pow(hist_num.GetBinError(b),2)
                    #####dY0 = math.sqrt(math.pow(hist_denom.GetBinError(b),2) - math.pow(hist_num.GetBinError(b),2)) #sam going to change this line to avoid domain error
                    dY0 = math.sqrt(abs(math.pow(hist_denom.GetBinError(b),2) - math.pow(hist_num.GetBinError(b),2)))
                    #print "before:", Y0,dY0
                    dY0 = getError(Y0,dY0*dY0)
                    #print "after:", Y0,dY0
                    Y = Y0 + Y1
                    dy = 1
                    if not Y == 0:
                        dy = math.sqrt(
                            dY1*dY1*rt.TMath.Power(1/Y - Y1/Y/Y,2) + 
                            dY0*dY0*rt.TMath.Power(Y1/Y/Y,2)
                            )
                    else:
                        y = 0.
                    g.SetPoint(b-1,x,y)
                    g.SetPointError(b-1,x-xl,xu-x,dy,min(1-y,dy))
                g.SetFillColor(options["pb_fillcolor"])
                g.SetFillStyle(options["pb_fillstyle"])
                print "ding"
                graphList.append(g)
            
            # fill legend
            if "legendtitle" in options:
                temp.append(hist.Clone())
                if "showStatUncert" in options and options["showStatUncert"] == True:
                    temp[-1].SetFillStyle(options["pb_fillstyle"])
                    temp[-1].SetFillColor(options["pb_fillcolor"])
                _legend.AddEntry(temp[-1],options["legendtitle"],options["legendoption"])

        # log scale?
        if "logScale" in varCfg[name] and varCfg[name]["logScale"] == 1:
            rt.gPad.SetLogx()
        else:
            rt.gPad.SetLogx(0)
        # set max
        mymax = 0
        for hist in histList:
            _max = hist.GetMaximum()
            if _max > mymax:
                mymax = _max

        if len(graphList) > 0:
            graphList[0].SetMaximum(1.3666)
            graphList[0].SetMinimum(0)
        histList[0].SetMinimum(0.0)
        histList[0].SetMaximum(1.466)
        # draw
        for h in range(0,len(histList)):
            if h == 0:
                histList[h].Draw(histDrawOptionList[h])
            else:
                histList[h].Draw(histDrawOptionList[h] + ",HIST,SAME")
        for g in range(0,len(graphList)):
            graphList[g].Draw("2")
        for h in range(0,len(histList)):
            histList[h].Draw(histDrawOptionList[h]+",A,HIST,SAME")
        for h in range(0,len(histList)):
            histList[h].Draw(histDrawOptionList[h]+",A,HIST,SAME")
        histList[h].Draw("AXIS,SAME")
        # legends
        n = _legend.GetNRows()
        y1 = _legend.GetY2()-1.5*25./800*n
        _legend.SetY1(y1)
        _legend.Draw()
        _lineLegend.SetY1(y1-1.5*25./800)
        _lineLegend.SetY2(y1)
        _lineLegend.Draw()
        box.Draw()
        # print
        for format in FORMAT.split(","):
            rt.gPad.Print(odir + "/" + combName + "_sp_" + name + "." + format) 
        histList[0].SetMaximum(-1111)

    # close root files
    for file in filedict.values():
        file.Close()

