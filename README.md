# Repo for maintaining Run-2 pMSSM results

## Setup

```
cmsrel CMSSW_10_0_5
cd CMSSW_10_0_5/src/
cmsenv
git clone https://github.com/UhhCmsAnalysis/Run2pMSSM
cd Run2pMSSM
mkdir odata
mkdir odata/pMSSMtree
mkdir odata/hist_sel
mkdir odata/hist_fs
mkdir odata/hist_Z
mkdir odata/distributions_Z
mkdir odata/survprob_sel
mkdir odata/distributions_2D_sel
```

how to add a result

1. add a folder SUSYYNNN to idata [this has already been done for a few analyses

2. add files to to SUSYYNNN:

a) cme.txt

b) {counts.txt, data_bg.txt, lumi.txt} OR maxllhd.txt

3. add SUSYYNNN to bashsequences/calcLlhd.sh, and run, and run:

```
bash bashsequences/calcLlhd.sh
```

4. add SUSYYNNN to calcZ.sh, edit combineZ.py, and run calcZ.sh
```
bash bashsequences/calcZ.sh
```

create a pMSSM tree:
```
python scripts/pMSSMtree.py "scripts/pMSSMtree.cfg.py" odata/pMSSMtree/pMSSMtree.root
```

create histograms in root files; best to break open fillHist_sel.sh and run things individually, but you can also just do:
```
source scripts/fillHist_sel.sh
```

ok, time to make nice canvases and stuff

```
      python scripts/drawZ.py
      python scripts/drawZ2D.py
      python scripts/draw1D.py odata/hist_sel scripts/draw1D_combinations_cfg.py odata/distributions_1D_sel/
      python scripts/drawSurvProb.py odata/hist_sel scripts/draw1D_combinations_sp_cfg.py odata/survprob_sel
      python scripts/draw2D.py odata/hist_sel/ odata/distributions_2D_sel
```


