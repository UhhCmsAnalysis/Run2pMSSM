#!/usr/bin/env python

SMALL = 30
MEDIUM = 35
LARGE = 45


import sys
sys.argv.append("-b")
import ROOT as rt,os
from legendTitles import *
import array
from variables_cfg import varCfg

# which files?
tfile = rt.TFile.Open("odata/hist_Z/preCMS.root")
odir = "odata/distributions_Z"
if not os.path.isdir(odir):
    os.mkdir(odir)

# canvas
c = rt.TCanvas('c', 'c', 600, 600)
c.SetBottomMargin(0.15)
c.SetLeftMargin(0.17)
c.SetRightMargin(0.19)
c.SetTopMargin(0.14)

# a box
# a box
box = rt.TPaveText(0.10,0.89,1.-c.GetRightMargin()+0.04,0.91+30./800,"NDC")
box.SetFillStyle(0)
box.SetTextFont(134)
box.SetTextSize(LARGE)
box.SetBorderSize(0)
box.SetTextAlign(31)
box.AddText("CMS, pMSSM")

# the legend
legend =  rt.TLegend(0.15, 0.87,1.-c.GetRightMargin(), 0.87);
legend.SetNColumns(2)
legend.SetBorderSize(0);
legend.SetFillStyle(0000);
legend.SetTextFont(134);
legend.SetTextSize(SMALL)
legend.SetTextAlign(32)

# create palette
NRGBs = 5
NCont = 255
stops = array.array('d', [ 0.00, 0.34, 0.61, 0.84, 1.00 ])
red   = array.array('d', [ 0.50, 0.50, 1.00, 1.00, 1.00 ])
green = array.array('d', [ 0.50, 1.00, 1.00, 0.60, 0.50 ])
blue  = array.array('d', [ 1.00, 1.00, 0.50, 0.40, 0.50 ])
rt.TColor.CreateGradientColorTable(NRGBs, stops, red, green, blue, NCont)


for key in tfile.GetListOfKeys():
    name = key.GetName()
    print name
    if not name.find("_VS_SUS12024_SUS12011_SUS13012_SUS16033_Z_100_finebin") > 0:
        continue


    hist  = tfile.Get(name)
    hist.SetTitle("")
    hist.SetStats(0)
        
    # underflow bin
    hist.SetBinContent(1,hist.GetBinContent(0)+hist.GetBinContent(1))
    hist.SetBinContent(0,0)

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
    #hist.GetYaxis().SetNdivisions(0,0,0)
    #hist.Scale(1/hist.Integral(0,hist.GetNbinsX()+1))
    # z-axis
    hist.SetTitleFont(134,"Z")
    hist.SetTitleSize(LARGE,"Z")
    hist.SetLabelFont(134,"Z")
    hist.SetLabelSize(MEDIUM,"Z")
    hist.SetTitleOffset(1.1,"Z")
    hist.GetZaxis().CenterTitle()
    pos1 = name.find("_VS_")
    _key = name[:pos1].replace("_finebin","")
    title = "non-DCS prior prob. dens."
    if "unit" in varCfg[_key] and varCfg[_key]["unit"] != "":
        unit = varCfg[_key]["unit"]
        title += " / " + unit 
    hist.SetZTitle(title)

    # add to legend
    pos2 = name.find("_Z_100_")
    _key = name[pos1+4:pos2]
    _legend = legend.Clone()
    _legend.SetHeader(legendTitle[_key])
        

    hist.Draw("COLZ")

    rt.gPad.Update()
    zaxis = hist.GetListOfFunctions().FindObject("palette")
    zaxis.SetTitleOffset(1.1)
    
    # draw legend
    _legend.Draw()

    box.Draw()
    
    ofile = odir + "/" +  name + ".pdf"
    print 'creating', ofile
    rt.gPad.Print(ofile)
