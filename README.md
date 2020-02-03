# Repo for maintaining Run-2 pMSSM results

## Setup

```
cmsrel CMSSW_10_0_5
cd CMSSW_10_0_5/src/
cmsenv
git clone https://github.com/UhhCmsAnalysis/Run2pMSSM
cd Run2pMSSM
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

