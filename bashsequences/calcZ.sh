
##################
# 7 TeV
################## 

./scripts/calcZ.py idata/SUS12011/llhd.txt

##################
# 8 TeV
##################

./scripts/calcZ.py idata/SUS12024/llhd.txt

./scripts/calcZ.py idata/SUS13012/llhd.txt

# zbest combinations

###./combineZ.py

##################
# 13 TeV
##################

./scripts/calcZ.py idata/SUS16033/llhd.txt

##################
# 8 + 13 TeV
##################

./scripts/calcZ.py idata/SUS12024_SUS12011_SUS13012_SUS16033/llhd.txt

python scripts/combineZ.py