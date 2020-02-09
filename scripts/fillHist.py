#!/usr/bin/env python

import ROOT as rt
import sys,os,math,array
import json

ifile=sys.argv[1]
plotdef = sys.argv[2]
weightdef = sys.argv[3]
odir = sys.argv[4]

# odir
if not os.path.isdir(odir):
    os.makedirs(odir)

# read in plot and weight cfg
FILE = open(plotdef)
exec(FILE)    # plotCfg
FILE.close()

FILE = open(weightdef)
exec(FILE)    # weightCfg
FILE.close()

class PlotDef:

    def __init__(self,var1,var2=None):
        self.var1 = var1
        self.var2 = var2
        self.histType = "TH1D"
        self.name = self.var1["name"]
        if not self.var2 == None:
            self.histType = "TH2D"
            self.name += "_VS_" + self.var2["name"]
        self.fillHistString = "Fill({0},_weight+1e-160)".format(self.var1["var"])
        if not self.var2 == None:
            self.fillHistString = "Fill({0},{1},_weight+1e-160)".format(self.var1["var"],self.var2["var"])

    def histDeclaration(self):
        _str = ""
        binarg = ""
        # binning x
        if "customBinning" in self.var1:
            _str += "double xbinlimits_{0}[] = {{{1}}};\n".format(self.var1["name"],",".join([str(x) for x in self.var1["customBinning"]]))
            binarg += "{0},xbinlimits_{1}".format(len(self.var1["customBinning"])-1,self.var1["name"])
        else:
            binarg += ",".join([str(x) for x in self.var1["binning"]])
        # binning y
        if not self.var2 == None:
            if "customBinning" in self.var2:
                _str += "double xbinlimits_{0}[] = {{{1}}};\n".format(self.var2["name"],",".join([str(x) for x in self.var2["customBinning"]]))
                binarg += "," + "{0},xbinlimits_{1}".format(len(self.var2["customBinning"])-1,self.var2["name"])
            else:
                binarg += "," + ",".join([str(x) for x in self.var2["binning"]])
        # declaration
        _str  += "{type} * _h = new {type}(\"{name}\",\"{name}\",{binning});\n".format(type=self.histType,name=self.name,binning=binarg)
        # axis titles
        _xtitle = self.var1["title"]
        if "unit" in self.var1 and self.var1["unit"] != "":
            _xtitle = "{0} [{1}]".format(_xtitle,self.var1["unit"])
        _str += "      _h->SetXTitle(\"{0}\");\n".format(_xtitle)
        if not self.var2 == None:
            _ytitle = self.var2["title"]
            if "unit" in self.var2 and self.var2["unit"] != "":
                _ytitle = "{0} [{1}]".format(_ytitle,self.var2["unit"])
            _str += "      _h->SetYTitle(\"{0}\");\n".format(_ytitle)
        return _str
    def __str__(self):
        _str  = "PlotDef object\n"
        _str+="   name:" + self.name + "\n"
        _str+="   type:" + self.histType + "\n"
        _str+="   fill:" + self.fillHistString
        return _str

plotDef = []
for cfg in plotCfg:
    plotDef.append(PlotDef(*cfg))
        
# create c++ files to read the tree
file = rt.TFile.Open(ifile)
tree = file.Get("pMSSM")
tree.MakeClass("MyClass")
file.Close()

# replace the .cc file

# open the Loop function
cstr = """
#define MyClass_cxx
#include "MyClass.h"
#include "TMath.h"
#include <TH2D.h>
#include <TH1D.h>
#include <iostream>
using namespace std;


void MyClass::Loop()
{{


   if (fChain == 0) return;

   TH1::SetDefaultSumw2();

   Long64_t nentries = fChain->GetEntriesFast();

   int nWeight = {nWeight};
   double condition[{nWeight}];
   double weight[{nWeight}];
   string filename[{nWeight}];
""".format(nWeight=len(weightCfg))

# init filenames
for w in range(len(weightCfg)):
    cstr += "   filename[{0}] = \"{1}/{2}.root\";\n".format(w,odir,weightCfg[w][0])

# histogram arrays
for _def in plotDef:
    cstr += """
   {histType} * histarr_{plotName}[nWeight];
   for(int w = 0;w<nWeight;++w){{
      {histDeclaration}
      histarr_{plotName}[w] = _h;
   }}""".format(histType=_def.histType,plotName=_def.name,histDeclaration=_def.histDeclaration().rstrip("\n"))

# open the tree loop
cstr += """
   Long64_t nbytes = 0, nb = 0;
   for (Long64_t jentry=0; jentry<nentries;jentry++) {
      Long64_t ientry = LoadTree(jentry);
      if (ientry < 0) break;
      nb = fChain->GetEntry(jentry);   nbytes += nb;
"""

# update the weight array
for w in range(0,len(weightCfg)):
    cstr += "      condition[{0}] = {1};\n".format(w,weightCfg[w][1][0])
    cstr += "      weight[{0}] = {1};\n".format(w,weightCfg[w][1][1])
# fill histograms
cstr += "      for(int w = 0;w<nWeight;++w){;\n"
cstr += "         double & _weight = weight[w];\n"
cstr += "         if(!condition[w]) continue;\n"
for _def in plotDef:
    cstr+= "      histarr_{plotName}[w]->{fill};\n".format(plotName=_def.name,fill=_def.fillHistString)
cstr += "      }\n"

# close the tree loop
cstr +="   }\n"

# write histograms
cstr += "   for(int w = 0;w<nWeight;++w){;\n"
cstr += "      cout << \"writing \" << filename[w] << endl;\n"
cstr += "      TFile * f = TFile::Open(filename[w].c_str(),\"RECREATE\");\n"
for _def in plotDef:
    if "underflowbin" in _def.var1 and _def.var1["underflowbin"]:
        print "wtf"
        cstr+= "      histarr_{0}[w]->SetBinContent(1,histarr_{0}[w]->GetBinContent(0)+histarr_{0}[w]->GetBinContent(1));\n".format(_def.name)
        cstr+= "      histarr_{0}[w]->SetBinContent(0,0);\n".format(_def.name) 
    cstr += "      histarr_{0}[w]->Write();\n".format(_def.name) 
cstr += "      f->Close();\n"
cstr += "   }\n"

# close the Loop function
cstr += "}"

# write the C file
FILE = open("MyClass.C","w")
FILE.write(cstr)
FILE.close()

rt.gROOT.ProcessLine(".L MyClass.C+")
c = rt.MyClass()
c.Loop()


# write root macro
#macrostr ="""
#void MyMacro()
#{
#   gROOT->ProcessLine(".L MyClass.C+");
#   MyClass c;
#   c.Loop();
#}"""
#FILE = open("MyMacro.C","w")
#FILE.write(macrostr)
#FILE.close()
#"""

#os.system("root -l -b -q MyMacro.C")

