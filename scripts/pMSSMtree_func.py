def fillMyEntry(myEntry,ID,sections):
   myEntry.ID = ID
   myEntry.all_OK = True
   # params
   myEntry.params_OK = True
   if ID in sections[0].data:
      _data = sections[0].data[ID]
      myEntry.Ab = _data[sections[0].data_ci["Ab"]]
      myEntry.Al = _data[sections[0].data_ci["Al"]]
      myEntry.At = _data[sections[0].data_ci["At"]]
      myEntry.M1 = _data[sections[0].data_ci["M1"]]
      myEntry.M2 = _data[sections[0].data_ci["M2"]]
      myEntry.M3 = _data[sections[0].data_ci["M3"]]
      myEntry.Md1 = _data[sections[0].data_ci["Md1"]]
      myEntry.Md3 = _data[sections[0].data_ci["Md3"]]
      myEntry.Ml1 = _data[sections[0].data_ci["Ml1"]]
      myEntry.Ml3 = _data[sections[0].data_ci["Ml3"]]
      myEntry.Mq1 = _data[sections[0].data_ci["Mq1"]]
      myEntry.Mq3 = _data[sections[0].data_ci["Mq3"]]
      myEntry.Mr1 = _data[sections[0].data_ci["Mr1"]]
      myEntry.Mr3 = _data[sections[0].data_ci["Mr3"]]
      myEntry.Mu1 = _data[sections[0].data_ci["Mu1"]]
      myEntry.Mu3 = _data[sections[0].data_ci["Mu3"]]
      myEntry.alpha_em = _data[sections[0].data_ci["alpha_em"]]
      myEntry.alpha_s = _data[sections[0].data_ci["alpha_s"]]
      myEntry.mA_pole = _data[sections[0].data_ci["mA_pole"]]
      myEntry.mHc = _data[sections[0].data_ci["mHc"]]
      myEntry.mHh = _data[sections[0].data_ci["mHh"]]
      myEntry.mb1 = _data[sections[0].data_ci["mb1"]]
      myEntry.mb2 = _data[sections[0].data_ci["mb2"]]
      myEntry.mbmb = _data[sections[0].data_ci["mbmb"]]
      myEntry.mdL = _data[sections[0].data_ci["mdL"]]
      myEntry.mdR = _data[sections[0].data_ci["mdR"]]
      myEntry.meL = _data[sections[0].data_ci["meL"]]
      myEntry.meR = _data[sections[0].data_ci["meR"]]
      myEntry.mg = _data[sections[0].data_ci["mg"]]
      myEntry.mh = _data[sections[0].data_ci["mh"]]
      myEntry.mneute = _data[sections[0].data_ci["mneute"]]
      myEntry.mneuttau = _data[sections[0].data_ci["mneuttau"]]
      myEntry.mt = _data[sections[0].data_ci["mt"]]
      myEntry.mt1 = _data[sections[0].data_ci["mt1"]]
      myEntry.mt2 = _data[sections[0].data_ci["mt2"]]
      myEntry.mtau1 = _data[sections[0].data_ci["mtau1"]]
      myEntry.mtau2 = _data[sections[0].data_ci["mtau2"]]
      myEntry.mu = _data[sections[0].data_ci["mu"]]
      myEntry.muL = _data[sections[0].data_ci["muL"]]
      myEntry.muR = _data[sections[0].data_ci["muR"]]
      myEntry.mw1 = _data[sections[0].data_ci["mw1"]]
      myEntry.mw2 = _data[sections[0].data_ci["mw2"]]
      myEntry.mz1 = _data[sections[0].data_ci["mz1"]]
      myEntry.mz2 = _data[sections[0].data_ci["mz2"]]
      myEntry.mz3 = _data[sections[0].data_ci["mz3"]]
      myEntry.mz4 = _data[sections[0].data_ci["mz4"]]
      myEntry.tanb = _data[sections[0].data_ci["tanb"]]
   else:
      myEntry.params_OK = False
      myEntry.all_OK = False
      print "WARNING: no ID " + str(ID) + " in table params"
   if ID in sections[0].skipID:
      myEntry.params_OK = False
      myEntry.all_OK = False
   # moreparams
   myEntry.moreparams_OK = True
   if ID in sections[1].data:
      _data = sections[1].data[ID]
      myEntry.BDtaunu = _data[sections[1].data_ci["BDtaunu"]]
      myEntry.BDtaunu_BDenu = _data[sections[1].data_ci["BDtaunu_BDenu"]]
      myEntry.Bsmumu = _data[sections[1].data_ci["Bsmumu"]]
      myEntry.Btaunu = _data[sections[1].data_ci["Btaunu"]]
      myEntry.CXT1imag = _data[sections[1].data_ci["CXT1imag"]]
      myEntry.CXT1real = _data[sections[1].data_ci["CXT1real"]]
      myEntry.Dmunu = _data[sections[1].data_ci["Dmunu"]]
      myEntry.Dsmunu = _data[sections[1].data_ci["Dsmunu"]]
      myEntry.Dstaunu = _data[sections[1].data_ci["Dstaunu"]]
      myEntry.GLTT11 = _data[sections[1].data_ci["GLTT11"]]
      myEntry.GLVV = _data[sections[1].data_ci["GLVV"]]
      myEntry.H0AA = _data[sections[1].data_ci["H0AA"]]
      myEntry.H0SUSY = _data[sections[1].data_ci["H0SUSY"]]
      myEntry.H0WW = _data[sections[1].data_ci["H0WW"]]
      myEntry.H0WmHpm = _data[sections[1].data_ci["H0WmHpm"]]
      myEntry.H0WpHpm = _data[sections[1].data_ci["H0WpHpm"]]
      myEntry.H0ZA = _data[sections[1].data_ci["H0ZA"]]
      myEntry.H0ZZ = _data[sections[1].data_ci["H0ZZ"]]
      myEntry.H0ZhA = _data[sections[1].data_ci["H0ZhA"]]
      myEntry.H0b1b1 = _data[sections[1].data_ci["H0b1b1"]]
      myEntry.H0b1b2 = _data[sections[1].data_ci["H0b1b2"]]
      myEntry.H0b2b1 = _data[sections[1].data_ci["H0b2b1"]]
      myEntry.H0b2b2 = _data[sections[1].data_ci["H0b2b2"]]
      myEntry.H0bb = _data[sections[1].data_ci["H0bb"]]
      myEntry.H0cc = _data[sections[1].data_ci["H0cc"]]
      myEntry.H0gg = _data[sections[1].data_ci["H0gg"]]
      myEntry.H0h = _data[sections[1].data_ci["H0h"]]
      myEntry.H0hAhA = _data[sections[1].data_ci["H0hAhA"]]
      myEntry.H0hh = _data[sections[1].data_ci["H0hh"]]
      myEntry.H0l1l1 = _data[sections[1].data_ci["H0l1l1"]]
      myEntry.H0l1l2 = _data[sections[1].data_ci["H0l1l2"]]
      myEntry.H0l2l1 = _data[sections[1].data_ci["H0l2l1"]]
      myEntry.H0l2l2 = _data[sections[1].data_ci["H0l2l2"]]
      myEntry.H0ll = _data[sections[1].data_ci["H0ll"]]
      myEntry.H0mm = _data[sections[1].data_ci["H0mm"]]
      myEntry.H0sbsb = _data[sections[1].data_ci["H0sbsb"]]
      myEntry.H0slsl = _data[sections[1].data_ci["H0slsl"]]
      myEntry.H0ss = _data[sections[1].data_ci["H0ss"]]
      myEntry.H0stst = _data[sections[1].data_ci["H0stst"]]
      myEntry.H0t1t1 = _data[sections[1].data_ci["H0t1t1"]]
      myEntry.H0t1t2 = _data[sections[1].data_ci["H0t1t2"]]
      myEntry.H0t2t1 = _data[sections[1].data_ci["H0t2t1"]]
      myEntry.H0t2t2 = _data[sections[1].data_ci["H0t2t2"]]
      myEntry.H0tt = _data[sections[1].data_ci["H0tt"]]
      myEntry.H0width = _data[sections[1].data_ci["H0width"]]
      myEntry.H0z1z1 = _data[sections[1].data_ci["H0z1z1"]]
      myEntry.HpmSUSY = _data[sections[1].data_ci["HpmSUSY"]]
      myEntry.HpmWh = _data[sections[1].data_ci["HpmWh"]]
      myEntry.HpmWhA = _data[sections[1].data_ci["HpmWhA"]]
      myEntry.Hpmcb = _data[sections[1].data_ci["Hpmcb"]]
      myEntry.Hpmcs = _data[sections[1].data_ci["Hpmcs"]]
      myEntry.Hpmh = _data[sections[1].data_ci["Hpmh"]]
      myEntry.Hpmmnm = _data[sections[1].data_ci["Hpmmnm"]]
      myEntry.Hpmtb = _data[sections[1].data_ci["Hpmtb"]]
      myEntry.Hpmtnt = _data[sections[1].data_ci["Hpmtnt"]]
      myEntry.Hpmub = _data[sections[1].data_ci["Hpmub"]]
      myEntry.Hpmus = _data[sections[1].data_ci["Hpmus"]]
      myEntry.Hpmwidth = _data[sections[1].data_ci["Hpmwidth"]]
      myEntry.Kmunu_pimunu = _data[sections[1].data_ci["Kmunu_pimunu"]]
      myEntry.MH3 = _data[sections[1].data_ci["MH3"]]
      myEntry.R = _data[sections[1].data_ci["R"]]
      myEntry.RBtaunu = _data[sections[1].data_ci["RBtaunu"]]
      myEntry.RVBFH0AA = _data[sections[1].data_ci["RVBFH0AA"]]
      myEntry.RVBFH0WW = _data[sections[1].data_ci["RVBFH0WW"]]
      myEntry.RVBFH0ZZ = _data[sections[1].data_ci["RVBFH0ZZ"]]
      myEntry.RVBFH0bb = _data[sections[1].data_ci["RVBFH0bb"]]
      myEntry.RVBFH0ll = _data[sections[1].data_ci["RVBFH0ll"]]
      myEntry.RVBFhAA = _data[sections[1].data_ci["RVBFhAA"]]
      myEntry.RVBFhAAA = _data[sections[1].data_ci["RVBFhAAA"]]
      myEntry.RVBFhAWW = _data[sections[1].data_ci["RVBFhAWW"]]
      myEntry.RVBFhAZZ = _data[sections[1].data_ci["RVBFhAZZ"]]
      myEntry.RVBFhAbb = _data[sections[1].data_ci["RVBFhAbb"]]
      myEntry.RVBFhAll = _data[sections[1].data_ci["RVBFhAll"]]
      myEntry.RVBFhZZ = _data[sections[1].data_ci["RVBFhZZ"]]
      myEntry.RVBFhbb = _data[sections[1].data_ci["RVBFhbb"]]
      myEntry.RVBFhll = _data[sections[1].data_ci["RVBFhll"]]
      myEntry.RggH0AA = _data[sections[1].data_ci["RggH0AA"]]
      myEntry.RggH0WW = _data[sections[1].data_ci["RggH0WW"]]
      myEntry.RggH0ZZ = _data[sections[1].data_ci["RggH0ZZ"]]
      myEntry.RggH0bb = _data[sections[1].data_ci["RggH0bb"]]
      myEntry.RggH0ll = _data[sections[1].data_ci["RggH0ll"]]
      myEntry.RgghAA = _data[sections[1].data_ci["RgghAA"]]
      myEntry.RgghAAA = _data[sections[1].data_ci["RgghAAA"]]
      myEntry.RgghAWW = _data[sections[1].data_ci["RgghAWW"]]
      myEntry.RgghAZZ = _data[sections[1].data_ci["RgghAZZ"]]
      myEntry.RgghAbb = _data[sections[1].data_ci["RgghAbb"]]
      myEntry.RgghAll = _data[sections[1].data_ci["RgghAll"]]
      myEntry.RgghZZ = _data[sections[1].data_ci["RgghZZ"]]
      myEntry.Rgghbb = _data[sections[1].data_ci["Rgghbb"]]
      myEntry.Rgghll = _data[sections[1].data_ci["Rgghll"]]
      myEntry.Rmu23 = _data[sections[1].data_ci["Rmu23"]]
      myEntry.XFAC = _data[sections[1].data_ci["XFAC"]]
      myEntry.XFACNOSTOP = _data[sections[1].data_ci["XFACNOSTOP"]]
      myEntry.XFACNOSUSY = _data[sections[1].data_ci["XFACNOSUSY"]]
      myEntry.XFACT1 = _data[sections[1].data_ci["XFACT1"]]
      myEntry.bsgamma = _data[sections[1].data_ci["bsgamma"]]
      myEntry.chainno = _data[sections[1].data_ci["chainno"]]
      myEntry.costhetastop = _data[sections[1].data_ci["costhetastop"]]
      myEntry.ctau = _data[sections[1].data_ci["ctau"]]
      myEntry.delta0 = _data[sections[1].data_ci["delta0"]]
      myEntry.drho = _data[sections[1].data_ci["drho"]]
      myEntry.freq = _data[sections[1].data_ci["freq"]]
      myEntry.hAA = _data[sections[1].data_ci["hAA"]]
      myEntry.hAAA = _data[sections[1].data_ci["hAAA"]]
      myEntry.hASUSY = _data[sections[1].data_ci["hASUSY"]]
      myEntry.hAWW = _data[sections[1].data_ci["hAWW"]]
      myEntry.hAZA = _data[sections[1].data_ci["hAZA"]]
      myEntry.hAZZ = _data[sections[1].data_ci["hAZZ"]]
      myEntry.hAZh = _data[sections[1].data_ci["hAZh"]]
      myEntry.hAb1b1 = _data[sections[1].data_ci["hAb1b1"]]
      myEntry.hAb1b2 = _data[sections[1].data_ci["hAb1b2"]]
      myEntry.hAb2b1 = _data[sections[1].data_ci["hAb2b1"]]
      myEntry.hAb2b2 = _data[sections[1].data_ci["hAb2b2"]]
      myEntry.hAbb = _data[sections[1].data_ci["hAbb"]]
      myEntry.hAcc = _data[sections[1].data_ci["hAcc"]]
      myEntry.hAgg = _data[sections[1].data_ci["hAgg"]]
      myEntry.hAh = _data[sections[1].data_ci["hAh"]]
      myEntry.hAl1l1 = _data[sections[1].data_ci["hAl1l1"]]
      myEntry.hAl1l2 = _data[sections[1].data_ci["hAl1l2"]]
      myEntry.hAl2l1 = _data[sections[1].data_ci["hAl2l1"]]
      myEntry.hAl2l2 = _data[sections[1].data_ci["hAl2l2"]]
      myEntry.hAll = _data[sections[1].data_ci["hAll"]]
      myEntry.hAmm = _data[sections[1].data_ci["hAmm"]]
      myEntry.hAsbsb = _data[sections[1].data_ci["hAsbsb"]]
      myEntry.hAslsl = _data[sections[1].data_ci["hAslsl"]]
      myEntry.hAss = _data[sections[1].data_ci["hAss"]]
      myEntry.hAstst = _data[sections[1].data_ci["hAstst"]]
      myEntry.hAt1t1 = _data[sections[1].data_ci["hAt1t1"]]
      myEntry.hAt1t2 = _data[sections[1].data_ci["hAt1t2"]]
      myEntry.hAt2t1 = _data[sections[1].data_ci["hAt2t1"]]
      myEntry.hAt2t2 = _data[sections[1].data_ci["hAt2t2"]]
      myEntry.hAtt = _data[sections[1].data_ci["hAtt"]]
      myEntry.hAwidth = _data[sections[1].data_ci["hAwidth"]]
      myEntry.hAz1z1 = _data[sections[1].data_ci["hAz1z1"]]
      myEntry.hSUSY = _data[sections[1].data_ci["hSUSY"]]
      myEntry.hWW = _data[sections[1].data_ci["hWW"]]
      myEntry.hZA = _data[sections[1].data_ci["hZA"]]
      myEntry.hZZ = _data[sections[1].data_ci["hZZ"]]
      myEntry.hbb = _data[sections[1].data_ci["hbb"]]
      myEntry.hcc = _data[sections[1].data_ci["hcc"]]
      myEntry.hgg = _data[sections[1].data_ci["hgg"]]
      myEntry.hll = _data[sections[1].data_ci["hll"]]
      myEntry.hmm = _data[sections[1].data_ci["hmm"]]
      myEntry.hss = _data[sections[1].data_ci["hss"]]
      myEntry.hwidth = _data[sections[1].data_ci["hwidth"]]
      myEntry.hz1z1 = _data[sections[1].data_ci["hz1z1"]]
      myEntry.ichn = _data[sections[1].data_ci["ichn"]]
      myEntry.itr = _data[sections[1].data_ci["itr"]]
      myEntry.lh = _data[sections[1].data_ci["lh"]]
      myEntry.lhratio_bsg = _data[sections[1].data_ci["lhratio_bsg"]]
      myEntry.lhratio_bsmm = _data[sections[1].data_ci["lhratio_bsmm"]]
      myEntry.lhratio_butn = _data[sections[1].data_ci["lhratio_butn"]]
      myEntry.lhratio_mbmb = _data[sections[1].data_ci["lhratio_mbmb"]]
      myEntry.lhratio_mt = _data[sections[1].data_ci["lhratio_mt"]]
      myEntry.lhratio_preCMS = _data[sections[1].data_ci["lhratio_preCMS"]]
      myEntry.mW = _data[sections[1].data_ci["mW"]]
      myEntry.mlim = _data[sections[1].data_ci["mlim"]]
      myEntry.muon_gm2 = _data[sections[1].data_ci["muon_gm2"]]
      myEntry.omg = _data[sections[1].data_ci["omg"]]
      myEntry.sigSD = _data[sections[1].data_ci["sigSD"]]
      myEntry.sigSI = _data[sections[1].data_ci["sigSI"]]
      myEntry.sinthetastop = _data[sections[1].data_ci["sinthetastop"]]
      myEntry.tb = _data[sections[1].data_ci["tb"]]
      myEntry.u = _data[sections[1].data_ci["u"]]
      myEntry.w1width = _data[sections[1].data_ci["w1width"]]
      myEntry.z1lsp = _data[sections[1].data_ci["z1lsp"]]
      myEntry.zn11 = _data[sections[1].data_ci["zn11"]]
      myEntry.zn12 = _data[sections[1].data_ci["zn12"]]
      myEntry.zn13 = _data[sections[1].data_ci["zn13"]]
      myEntry.zn14 = _data[sections[1].data_ci["zn14"]]
   else:
      myEntry.moreparams_OK = False
      myEntry.all_OK = False
      print "WARNING: no ID " + str(ID) + " in table moreparams"
   if ID in sections[1].skipID:
      myEntry.moreparams_OK = False
      myEntry.all_OK = False
   # fs
   myEntry.fs_OK = True
   if ID in sections[2].data:
      _data = sections[2].data[ID]
      myEntry.fs_dphijet1mht = _data[sections[2].data_ci["dphijet1mht"]]
      myEntry.fs_frac_bjet1pt100 = _data[sections[2].data_ci["frac_bjet1pt100"]]
      myEntry.fs_frac_bjet1pt200 = _data[sections[2].data_ci["frac_bjet1pt200"]]
      myEntry.fs_frac_bjet1pt30 = _data[sections[2].data_ci["frac_bjet1pt30"]]
      myEntry.fs_frac_bjet1pt400 = _data[sections[2].data_ci["frac_bjet1pt400"]]
      myEntry.fs_frac_bjet1pt50 = _data[sections[2].data_ci["frac_bjet1pt50"]]
      myEntry.fs_frac_bjet1pt500 = _data[sections[2].data_ci["frac_bjet1pt500"]]
      myEntry.fs_frac_bjet1pt80 = _data[sections[2].data_ci["frac_bjet1pt80"]]
      myEntry.fs_frac_bjet2pt100 = _data[sections[2].data_ci["frac_bjet2pt100"]]
      myEntry.fs_frac_bjet2pt200 = _data[sections[2].data_ci["frac_bjet2pt200"]]
      myEntry.fs_frac_bjet2pt30 = _data[sections[2].data_ci["frac_bjet2pt30"]]
      myEntry.fs_frac_bjet2pt400 = _data[sections[2].data_ci["frac_bjet2pt400"]]
      myEntry.fs_frac_bjet2pt50 = _data[sections[2].data_ci["frac_bjet2pt50"]]
      myEntry.fs_frac_bjet2pt500 = _data[sections[2].data_ci["frac_bjet2pt500"]]
      myEntry.fs_frac_bjet2pt80 = _data[sections[2].data_ci["frac_bjet2pt80"]]
      myEntry.fs_frac_dphijet1mht = _data[sections[2].data_ci["frac_dphijet1mht"]]
      myEntry.fs_frac_ht1000 = _data[sections[2].data_ci["frac_ht1000"]]
      myEntry.fs_frac_ht1250 = _data[sections[2].data_ci["frac_ht1250"]]
      myEntry.fs_frac_ht1500 = _data[sections[2].data_ci["frac_ht1500"]]
      myEntry.fs_frac_ht300 = _data[sections[2].data_ci["frac_ht300"]]
      myEntry.fs_frac_ht500 = _data[sections[2].data_ci["frac_ht500"]]
      myEntry.fs_frac_ht80 = _data[sections[2].data_ci["frac_ht80"]]
      myEntry.fs_frac_ht800 = _data[sections[2].data_ci["frac_ht800"]]
      myEntry.fs_frac_jet1pt100 = _data[sections[2].data_ci["frac_jet1pt100"]]
      myEntry.fs_frac_jet1pt200 = _data[sections[2].data_ci["frac_jet1pt200"]]
      myEntry.fs_frac_jet1pt30 = _data[sections[2].data_ci["frac_jet1pt30"]]
      myEntry.fs_frac_jet1pt50 = _data[sections[2].data_ci["frac_jet1pt50"]]
      myEntry.fs_frac_jet1pt500 = _data[sections[2].data_ci["frac_jet1pt500"]]
      myEntry.fs_frac_jet1pt80 = _data[sections[2].data_ci["frac_jet1pt80"]]
      myEntry.fs_frac_jet2pt100 = _data[sections[2].data_ci["frac_jet2pt100"]]
      myEntry.fs_frac_jet2pt200 = _data[sections[2].data_ci["frac_jet2pt200"]]
      myEntry.fs_frac_jet2pt30 = _data[sections[2].data_ci["frac_jet2pt30"]]
      myEntry.fs_frac_jet2pt400 = _data[sections[2].data_ci["frac_jet2pt400"]]
      myEntry.fs_frac_jet2pt50 = _data[sections[2].data_ci["frac_jet2pt50"]]
      myEntry.fs_frac_jet2pt500 = _data[sections[2].data_ci["frac_jet2pt500"]]
      myEntry.fs_frac_jet2pt80 = _data[sections[2].data_ci["frac_jet2pt80"]]
      myEntry.fs_frac_jet4pt50 = _data[sections[2].data_ci["frac_jet4pt50"]]
      myEntry.fs_frac_jet6pt50 = _data[sections[2].data_ci["frac_jet6pt50"]]
      myEntry.fs_frac_jet8pt50 = _data[sections[2].data_ci["frac_jet8pt50"]]
      myEntry.fs_frac_lep1pt10 = _data[sections[2].data_ci["frac_lep1pt10"]]
      myEntry.fs_frac_lep1pt25 = _data[sections[2].data_ci["frac_lep1pt25"]]
      myEntry.fs_frac_lep1pt5 = _data[sections[2].data_ci["frac_lep1pt5"]]
      myEntry.fs_frac_lep2pt10 = _data[sections[2].data_ci["frac_lep2pt10"]]
      myEntry.fs_frac_lep2pt25 = _data[sections[2].data_ci["frac_lep2pt25"]]
      myEntry.fs_frac_lep2pt5 = _data[sections[2].data_ci["frac_lep2pt5"]]
      myEntry.fs_frac_lep3pt10 = _data[sections[2].data_ci["frac_lep3pt10"]]
      myEntry.fs_frac_lep3pt25 = _data[sections[2].data_ci["frac_lep3pt25"]]
      myEntry.fs_frac_lep3pt5 = _data[sections[2].data_ci["frac_lep3pt5"]]
      myEntry.fs_frac_met200 = _data[sections[2].data_ci["frac_met200"]]
      myEntry.fs_frac_met300 = _data[sections[2].data_ci["frac_met300"]]
      myEntry.fs_frac_met35 = _data[sections[2].data_ci["frac_met35"]]
      myEntry.fs_frac_met450 = _data[sections[2].data_ci["frac_met450"]]
      myEntry.fs_frac_met600 = _data[sections[2].data_ci["frac_met600"]]
      myEntry.fs_frac_met80 = _data[sections[2].data_ci["frac_met80"]]
      myEntry.fs_frac_pho1pt10 = _data[sections[2].data_ci["frac_pho1pt10"]]
      myEntry.fs_frac_pho1pt25 = _data[sections[2].data_ci["frac_pho1pt25"]]
      myEntry.fs_frac_pho1pt50 = _data[sections[2].data_ci["frac_pho1pt50"]]
      myEntry.fs_frac_pho2pt10 = _data[sections[2].data_ci["frac_pho2pt10"]]
      myEntry.fs_frac_pho2pt25 = _data[sections[2].data_ci["frac_pho2pt25"]]
      myEntry.fs_frac_pho2pt50 = _data[sections[2].data_ci["frac_pho2pt50"]]
      myEntry.fs_ht = _data[sections[2].data_ci["ht"]]
      myEntry.fs_met = _data[sections[2].data_ci["met"]]
      myEntry.fs_nbjet = _data[sections[2].data_ci["nbjet"]]
      myEntry.fs_njet = _data[sections[2].data_ci["njet"]]
      myEntry.fs_nlep = _data[sections[2].data_ci["nlep"]]
      myEntry.fs_npho = _data[sections[2].data_ci["npho"]]
      myEntry.fs_pdgidSusy = _data[sections[2].data_ci["pdgidSusy"]]
      myEntry.fs_ptbjet1 = _data[sections[2].data_ci["ptbjet1"]]
      myEntry.fs_ptjet1 = _data[sections[2].data_ci["ptjet1"]]
      myEntry.fs_ptlep1 = _data[sections[2].data_ci["ptlep1"]]
      myEntry.fs_ptpho1 = _data[sections[2].data_ci["ptpho1"]]
   else:
      myEntry.fs_OK = False
      myEntry.all_OK = False
      print "WARNING: no ID " + str(ID) + " in table fs"
   if ID in sections[2].skipID:
      myEntry.fs_OK = False
      myEntry.all_OK = False
   # lilith
   myEntry.lilith_OK = True
   if ID in sections[3].data:
      _data = sections[3].data[ID]
      myEntry.lilith_llhd = _data[sections[3].data_ci["llhd"]]
   else:
      myEntry.lilith_OK = False
      myEntry.all_OK = False
      print "WARNING: no ID " + str(ID) + " in table lilith"
   if ID in sections[3].skipID:
      myEntry.lilith_OK = False
      myEntry.all_OK = False
   # xsect8
   myEntry.xsect8_OK = True
   if ID in sections[4].data:
      _data = sections[4].data[ID]
      myEntry.xsect_8TeV_pb = _data[sections[4].data_ci["xsect_8TeV_pb"]]
   else:
      myEntry.xsect8_OK = False
      myEntry.all_OK = False
      print "WARNING: no ID " + str(ID) + " in table xsect8"
   if ID in sections[4].skipID:
      myEntry.xsect8_OK = False
      myEntry.all_OK = False
   # xsect7
   myEntry.xsect7_OK = True
   if ID in sections[5].data:
      _data = sections[5].data[ID]
      myEntry.xsect_7TeV_pb = _data[sections[5].data_ci["xsect_7TeV_pb"]]
   else:
      myEntry.xsect7_OK = False
      myEntry.all_OK = False
      print "WARNING: no ID " + str(ID) + " in table xsect7"
   if ID in sections[5].skipID:
      myEntry.xsect7_OK = False
      myEntry.all_OK = False
   # SUS12011_llhd
   myEntry.SUS12011_llhd_OK = True
   if ID in sections[6].data:
      _data = sections[6].data[ID]
      myEntry.SUS12011_N_TOT = _data[sections[6].data_ci["N_TOT"]]
      myEntry.SUS12011_llhd_000 = _data[sections[6].data_ci["llhd_000"]]
      myEntry.SUS12011_llhd_050 = _data[sections[6].data_ci["llhd_050"]]
      myEntry.SUS12011_llhd_100 = _data[sections[6].data_ci["llhd_100"]]
      myEntry.SUS12011_llhd_150 = _data[sections[6].data_ci["llhd_150"]]
   else:
      myEntry.SUS12011_llhd_OK = False
      myEntry.all_OK = False
      print "WARNING: no ID " + str(ID) + " in table SUS12011_llhd"
   if ID in sections[6].skipID:
      myEntry.SUS12011_llhd_OK = False
      myEntry.all_OK = False
   # SUS13012_llhd
   myEntry.SUS13012_llhd_OK = True
   if ID in sections[7].data:
      _data = sections[7].data[ID]
      myEntry.SUS13012_N_TOT = _data[sections[7].data_ci["N_TOT"]]
      myEntry.SUS13012_llhd_000 = _data[sections[7].data_ci["llhd_000"]]
      myEntry.SUS13012_llhd_050 = _data[sections[7].data_ci["llhd_050"]]
      myEntry.SUS13012_llhd_100 = _data[sections[7].data_ci["llhd_100"]]
      myEntry.SUS13012_llhd_150 = _data[sections[7].data_ci["llhd_150"]]
   else:
      myEntry.SUS13012_llhd_OK = False
      myEntry.all_OK = False
      print "WARNING: no ID " + str(ID) + " in table SUS13012_llhd"
   if ID in sections[7].skipID:
      myEntry.SUS13012_llhd_OK = False
      myEntry.all_OK = False
   # SUS16033_llhd
   myEntry.SUS16033_llhd_OK = True
   if ID in sections[8].data:
      _data = sections[8].data[ID]
      myEntry.SUS16033_N_TOT = _data[sections[8].data_ci["N_TOT"]]
      myEntry.SUS16033_llhd_000 = _data[sections[8].data_ci["llhd_000"]]
      myEntry.SUS16033_llhd_050 = _data[sections[8].data_ci["llhd_050"]]
      myEntry.SUS16033_llhd_100 = _data[sections[8].data_ci["llhd_100"]]
      myEntry.SUS16033_llhd_150 = _data[sections[8].data_ci["llhd_150"]]
   else:
      myEntry.SUS16033_llhd_OK = False
      myEntry.all_OK = False
      print "WARNING: no ID " + str(ID) + " in table SUS16033_llhd"
   if ID in sections[8].skipID:
      myEntry.SUS16033_llhd_OK = False
      myEntry.all_OK = False
   # SUS12024_SUS12011_SUS13012_SUS16033_llhd
   myEntry.SUS12024_SUS12011_SUS13012_SUS16033_llhd_OK = True
   if ID in sections[9].data:
      _data = sections[9].data[ID]
      myEntry.SUS12024_SUS12011_SUS13012_SUS16033_llhd_000 = _data[sections[9].data_ci["llhd_000"]]
      myEntry.SUS12024_SUS12011_SUS13012_SUS16033_llhd_050 = _data[sections[9].data_ci["llhd_050"]]
      myEntry.SUS12024_SUS12011_SUS13012_SUS16033_llhd_100 = _data[sections[9].data_ci["llhd_100"]]
      myEntry.SUS12024_SUS12011_SUS13012_SUS16033_llhd_150 = _data[sections[9].data_ci["llhd_150"]]
   else:
      myEntry.SUS12024_SUS12011_SUS13012_SUS16033_llhd_OK = False
      myEntry.all_OK = False
      print "WARNING: no ID " + str(ID) + " in table SUS12024_SUS12011_SUS13012_SUS16033_llhd"
   if ID in sections[9].skipID:
      myEntry.SUS12024_SUS12011_SUS13012_SUS16033_llhd_OK = False
      myEntry.all_OK = False
   # SUS12011_Z
   myEntry.SUS12011_Z_OK = True
   if ID in sections[10].data:
      _data = sections[10].data[ID]
      myEntry.SUS12011_Z_050 = _data[sections[10].data_ci["Z_050"]]
      myEntry.SUS12011_Z_100 = _data[sections[10].data_ci["Z_100"]]
      myEntry.SUS12011_Z_150 = _data[sections[10].data_ci["Z_150"]]
   else:
      myEntry.SUS12011_Z_OK = False
      myEntry.all_OK = False
      print "WARNING: no ID " + str(ID) + " in table SUS12011_Z"
   if ID in sections[10].skipID:
      myEntry.SUS12011_Z_OK = False
      myEntry.all_OK = False
   # SUS13012_Z
   myEntry.SUS13012_Z_OK = True
   if ID in sections[11].data:
      _data = sections[11].data[ID]
      myEntry.SUS13012_Z_050 = _data[sections[11].data_ci["Z_050"]]
      myEntry.SUS13012_Z_100 = _data[sections[11].data_ci["Z_100"]]
      myEntry.SUS13012_Z_150 = _data[sections[11].data_ci["Z_150"]]
   else:
      myEntry.SUS13012_Z_OK = False
      myEntry.all_OK = False
      print "WARNING: no ID " + str(ID) + " in table SUS13012_Z"
   if ID in sections[11].skipID:
      myEntry.SUS13012_Z_OK = False
      myEntry.all_OK = False
   # SUS16033_Z
   myEntry.SUS16033_Z_OK = True
   if ID in sections[12].data:
      _data = sections[12].data[ID]
      myEntry.SUS16033_Z_050 = _data[sections[12].data_ci["Z_050"]]
      myEntry.SUS16033_Z_100 = _data[sections[12].data_ci["Z_100"]]
      myEntry.SUS16033_Z_150 = _data[sections[12].data_ci["Z_150"]]
   else:
      myEntry.SUS16033_Z_OK = False
      myEntry.all_OK = False
      print "WARNING: no ID " + str(ID) + " in table SUS16033_Z"
   if ID in sections[12].skipID:
      myEntry.SUS16033_Z_OK = False
      myEntry.all_OK = False
   # SUS12024_SUS12011_SUS13012_SUS16033_Z
   myEntry.SUS12024_SUS12011_SUS13012_SUS16033_Z_OK = True
   if ID in sections[13].data:
      _data = sections[13].data[ID]
      myEntry.SUS12024_SUS12011_SUS13012_SUS16033_Z_050 = _data[sections[13].data_ci["Z_050"]]
      myEntry.SUS12024_SUS12011_SUS13012_SUS16033_Z_100 = _data[sections[13].data_ci["Z_100"]]
      myEntry.SUS12024_SUS12011_SUS13012_SUS16033_Z_150 = _data[sections[13].data_ci["Z_150"]]
   else:
      myEntry.SUS12024_SUS12011_SUS13012_SUS16033_Z_OK = False
      myEntry.all_OK = False
      print "WARNING: no ID " + str(ID) + " in table SUS12024_SUS12011_SUS13012_SUS16033_Z"
   if ID in sections[13].skipID:
      myEntry.SUS12024_SUS12011_SUS13012_SUS16033_Z_OK = False
      myEntry.all_OK = False
   # lossycombined7and8and13TeV_Z
   myEntry.lossycombined7and8and13TeV_Z_OK = True
   if ID in sections[14].data:
      _data = sections[14].data[ID]
      myEntry.lossycombined7and8and13TeV_Z_050 = _data[sections[14].data_ci["Z_050"]]
      myEntry.lossycombined7and8and13TeV_Z_100 = _data[sections[14].data_ci["Z_100"]]
      myEntry.lossycombined7and8and13TeV_Z_150 = _data[sections[14].data_ci["Z_150"]]
   else:
      myEntry.lossycombined7and8and13TeV_Z_OK = False
      myEntry.all_OK = False
      print "WARNING: no ID " + str(ID) + " in table lossycombined7and8and13TeV_Z"
   if ID in sections[14].skipID:
      myEntry.lossycombined7and8and13TeV_Z_OK = False
      myEntry.all_OK = False
