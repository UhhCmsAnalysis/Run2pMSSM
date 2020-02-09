# read variables from variables.cfg.py
from variables_cfg import varCfg

# create plot cfg
plotCfg = []

# 1D plots for all defined variabels
keys = [
    # basic colored
    "mg_rebin","muL_rebin","muR_rebin","mb1_rebin","mt1_rebin","mLCSP_rebin",
    # basic ewk
    "mz1_rebin","mz1_rebin3","meL_rebin","meR_rebin","min_meLmeR_rebin","mtau1_rebin","mLNDw_rebin",
    # more ewk
    "mz2_rebin","mw1_rebin","mz3_rebin","mz4_rebin","mw2_rebin","mtau2_rebin",
    # more colored
    "mdL_rebin","mdR_rebin","mb2_rebin","mt2_rebin",
    # higgs
    "mh_rebin","mA_pole_rebin","mHh_rebin","mHc_rebin",
    # more
    "xsect_8TeV",
    "log10_xsect_8TeV_rebin",
    "At",
    "mu",
    "tanb",
    "tanb_rebin",
    "M_SUSY",
    "log10_hSUSY",
    "hSUSY_zoom",
    "log10_hSUSY_zoom",
    # dark matter
    "log10_omgh2_rebin",
    "log10_sigSD_rebin",
    "log10_sigSI_rebin",
    ]
    
# 1D plot cfg
for key in keys:
    plotCfg.append([varCfg[key]])

# 2D X vs LSP plot cfg
for key in keys:
    if key == "mz1_rebin":
        continue
    plotCfg.append([varCfg[key],varCfg["mz1_rebin"]])

# 2D X vs LSP plot cfg
for key in keys:
    plotCfg.append([varCfg[key],varCfg["mz1_rebin2"]])
