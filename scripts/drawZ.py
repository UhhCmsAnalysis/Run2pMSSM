#!/usr/bin/env python

SMALL = 0.05
MEDIUM = 35
LARGE = 0.06
FONT = 42
import sys
sys.argv.append("-b")
import ROOT as rt,os
from legendTitles import *


# which files?
tfile = rt.TFile.Open("odata/hist_Z/preCMS.root")
odir = "odata/distributions_Z"
if not os.path.isdir(odir):
    os.mkdir(odir)

from draw1D_combinations_cfg import combinations,preDefComb
_combinations = {}
del combinations[-1]
for combination in combinations:
    _combinations.update({combination[0]:[]})
    for entry in combination[1]:
        key = entry[0]
        if key.find("050") > 0 or key.find("150") > 0 or key.find("preCMS") == 0:
            continue
        else:
            key = key.replace("lhd","Z").replace("surv","Z")
        #_combinations[combination[0]].append(key + "_rebin")
        _combinations[combination[0]].append(key)
#_combinations.update({"combined":["combined7TeV_Z_100_rebin","combined7and8TeV_Z_100_rebin"]},
#_combinations.update({"combined":["combined7TeV_Z_100","combined7and8TeV_Z_100"]},)
combinations = _combinations
print combinations

colors = [rt.kRed,rt.kBlue,rt.kGreen + 2]



c = rt.TCanvas('c', 'c', 800, 800)
c.SetBottomMargin(0.15)
c.SetLeftMargin(0.14)
c.SetLogy()

# a box
box = rt.TPaveText(0.10,0.89,0.93,0.91+30./800,"NDC")
box.SetFillStyle(0)
box.SetTextFont(FONT)
box.SetTextSize(LARGE)
box.SetBorderSize(0)
box.SetTextAlign(31)
box.AddText("CMS, pMSSM")

for key,combination in combinations.iteritems():
    hist = []

    legend = rt.TLegend(0.18,0.92,0.6,0.92)
    legend.SetFillStyle(0)
    legend.SetBorderSize(0)
    legend.SetTextFont(FONT)
    legend.SetTextSize(SMALL)

    print 'combination', combination
    for h in range(0,len(combination)):

        print 'attempting', h, combination[h], tfile.GetName()
        hist.append(tfile.Get(combination[h]))
        if hist[-1] == None:
            print combination[h],"causes trouble, hmmmmm"
        hist[h].SetTitle("")
        hist[h].SetStats(0)

        # layout
        hist[h].SetLineColor(colors[h])
        print key,combination[h]
        if key == "combined" and combination[h].find("combined7and8TeV")>=0:
            print "WTF"
            hist[h].SetLineColor(rt.kBlack)
        hist[h].SetLineWidth(4)
        
        # underflow bin
        hist[h].SetBinContent(1,hist[h].GetBinContent(0)+hist[h].GetBinContent(1))
        hist[h].SetBinContent(0,0)

        # overflow bin
        hist[h].SetBinContent(hist[h].GetNbinsX(),hist[h].GetBinContent(hist[h].GetNbinsX())+hist[h].GetBinContent(hist[h].GetNbinsX()+1))
        hist[h].SetBinContent(hist[h].GetNbinsX()+1,0)

        # x-axis
        hist[h].SetTitleFont(FONT,"X")
        hist[h].SetTitleSize(LARGE,"X")
        hist[h].SetLabelFont(FONT,"X")
        hist[h].SetLabelOffset(FONT,"X")
        hist[h].SetLabelSize(MEDIUM,"X")
        hist[h].SetTitleOffset(1.0,"X")
        hist[h].GetXaxis().CenterTitle()
        # y-axis
        hist[h].SetTitleFont(FONT,"Y")
        hist[h].SetTitleSize(LARGE,"Y")
        hist[h].SetLabelFont(FONT,"Y")
        hist[h].SetLabelSize(MEDIUM,"Y")
        hist[h].SetTitleOffset(1.2,"Y")
        hist[h].GetYaxis().CenterTitle()
        #hist[h].GetYaxis().SetNdivisions(0,0,0)
        hist[h].SetYTitle("non-DCS prior probability density")
        # normalisation
        hist[h].Scale(1/hist[h].Integral(0,hist[h].GetNbinsX()+1))
        # /bin -> /unit
        for b in range(1,hist[h].GetNbinsX()+1):
            _bc = hist[h].GetBinContent(b)/hist[h].GetBinWidth(b)
            hist[h].SetBinContent(b,_bc)

        # add to legend
        _key = combination[h].replace("_Z_100","").replace("_rebin","")
        legend.AddEntry(hist[h],legendTitle[_key],"l")
        

    # draw
    _max = max([x.GetMaximum() for x in hist])
    hist[0].SetMaximum(_max*10)
    hist[0].SetMinimum(0.0001)
    for h in range(0,len(hist)):
        if h == 0:
            hist[h].Draw("HIST")
        else:
            hist[h].Draw("HIST,same")

    # draw legend
    n = legend.GetNRows()
    y1 = legend.GetY2()-1.5*25./800*n
    legend.SetY1(y1)
    legend.Draw()
    box.Draw()

    rt.gPad.Print(odir + "/" +  key + ".pdf")
