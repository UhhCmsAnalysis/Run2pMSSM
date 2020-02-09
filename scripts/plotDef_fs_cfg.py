# read variables from variables.cfg.py
from variables_cfg import varCfg

# create plot cfg
plotCfg = []

# 1D plots for all defined variabels
keys = [
    # met
    "fs_met",
    "fs_frac_met35",
    "fs_A_met35",
    "fs_frac_met80",
    "fs_A_met80",
    "fs_frac_met200",
    "fs_A_met200",
    "fs_frac_met300",
    "fs_A_met300",
    "fs_frac_met450",
    "fs_A_met450",
    "fs_frac_met600",
    "fs_A_met600",
    # ht
    "fs_ht",
    "fs_frac_ht80",
    "fs_A_ht80",
    "fs_frac_ht300",
    "fs_A_ht300",
    "fs_frac_ht500",
    "fs_A_ht500",
    "fs_frac_ht800",
    "fs_A_ht800",
    "fs_frac_ht1000",
    "fs_A_ht1000",
    "fs_frac_ht1250",
    "fs_A_ht1250",
    "fs_frac_ht1500",
    "fs_A_ht1500",
    # jets
    "fs_njet",
    "fs_ptjet1",
    # jet1
    "fs_frac_jet1pt30",
    "fs_A_jet1pt30",
    "fs_frac_jet1pt50",
    "fs_A_jet1pt50",
    "fs_frac_jet1pt80",
    "fs_A_jet1pt80",
    "fs_frac_jet1pt100",
    "fs_A_jet1pt100",
    "fs_frac_jet1pt200",
    "fs_A_jet1pt200",
    #"fs_frac_jet1pt400",
    #"fs_A_jet1pt400",
    "fs_frac_jet1pt500",
    "fs_A_jet1pt500",
    # jet2
    #"fs_frac_jet2pt30",
    #"fs_A_jet2pt30",
    "fs_frac_jet2pt50",
    "fs_A_jet2pt50",
    "fs_frac_jet2pt80",
    "fs_A_jet2pt80",
    "fs_frac_jet2pt100",
    "fs_A_jet2pt100",
    "fs_frac_jet2pt200",
    "fs_A_jet2pt200",
    "fs_frac_jet2pt400",
    "fs_A_jet2pt400",
    "fs_frac_jet2pt500",
    "fs_A_jet2pt500",
    # multi-jet
    "fs_frac_jet4pt50", #
    "fs_A_jet4pt50", #
    "fs_frac_jet6pt50", #
    "fs_A_jet6pt50", #
    "fs_frac_jet8pt50", #
    "fs_A_jet8pt50", #
    # bjets
    "fs_nbjet",
    "fs_ptbjet1",
    "fs_frac_bjet1pt30", #
    "fs_frac_bjet1pt50", #
    "fs_frac_bjet1pt80", #
    "fs_frac_bjet1pt100", #
    "fs_frac_bjet1pt200", #
    "fs_frac_bjet1pt400", #
    "fs_frac_bjet1pt500", #
    #"fs_frac_bjet2pt30", #
    "fs_frac_bjet2pt50", #
    "fs_frac_bjet2pt80", #
    "fs_frac_bjet2pt100", #
    "fs_frac_bjet2pt200", #
    "fs_frac_bjet2pt400", #
    "fs_frac_bjet2pt500", #
"fs_A_bjet1pt30", #
    "fs_A_bjet1pt50", #
    "fs_A_bjet1pt80", #
    "fs_A_bjet1pt100", #
    "fs_A_bjet1pt200", #
    "fs_A_bjet1pt400", #
    "fs_A_bjet1pt500", #
    #"fs_A_bjet2pt30", #
    "fs_A_bjet2pt50", #
    "fs_A_bjet2pt80", #
    "fs_A_bjet2pt100", #
    "fs_A_bjet2pt200", #
    "fs_A_bjet2pt400", #
    "fs_A_bjet2pt500", #
    # phtons
    "fs_npho",
    "fs_ptpho1",
    "fs_frac_pho1pt10",
    "fs_A_pho1pt10",
    "fs_frac_pho1pt25",
    "fs_A_pho1pt25",
    "fs_frac_pho1pt50",
    "fs_A_pho1pt50",
    "fs_frac_pho2pt10",
    "fs_A_pho2pt10",
    "fs_frac_pho2pt25",
    "fs_A_pho2pt25",
    "fs_frac_pho2pt50",
    "fs_A_pho2pt50",
    # leptons
    "fs_nlep",
    "fs_ptlep1",
    #
    "fs_frac_lep1pt5",
    "fs_A_lep1pt5",
    "fs_frac_lep1pt10",
    "fs_A_lep1pt10",
    "fs_frac_lep1pt25",
    "fs_A_lep1pt25",
    #
    "fs_frac_lep2pt5",
    "fs_A_lep2pt5",
    "fs_frac_lep2pt10",
    "fs_A_lep2pt10",
    "fs_frac_lep2pt25",
    "fs_A_lep2pt25",
    #
    "fs_frac_lep3pt5",
    "fs_A_lep3pt5",
    "fs_frac_lep3pt10",
    "fs_A_lep3pt10",
    "fs_frac_lep3pt25",
    "fs_A_lep3pt25",
    #
    "fs_pdgidSusy",
    # dphi stuff
    "fs_frac_dphijet1mht",
    "fs_A_dphijet1mht",
    "fs_dphijet1mht"
    ]

# 1D plot cfg
for key in keys:
    plotCfg.append([varCfg[key]])
