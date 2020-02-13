########
# 7 TeV
########

#multi-count is probably the most realistic thing we can expect from analyzers
#example: python scripts/calcLlhdMultiCount.py idata/SUS12011/counts.sezen.txt idata/SUS12011/data_bg.txt idata/SUS12011/llhd.txt

########
# 8 TeV
########

#max llhd is probably the nicest result we can have:
#example: python scripts/calcLlhdMaxLlhd.py idata/SUS12024/maxllhd.txt idata/SUS12024/llhd.txt
#python scripts/calcLlhdMultiCount.py idata/SUS13012/counts.txt idata/SUS13012/data_bg.txt idata/SUS13012/llhd.txt

########
# 13 TeV
########

#example: python scripts/calcLlhdMultiCount.py idata/SUS16033/counts.txt idata/SUS16033/data_bg.txt idata/SUS16033/llhd.txt
python scripts/calcLlhdMultiCount.py idata/SUSRa2bMockup/counts.txt idata/SUSRa2bMockup/data_bg.txt idata/SUSRa2bMockup/llhd.txt

########
# 7+8+13
########
#this just multiplies the likelihoods for each pMSSM point
#example: python scripts/combineLlhd.py "idata/SUS12024/llhd.txt,idata/SUS12011/llhd.txt,idata/SUS13012/llhd.txt,idata/SUS16033/llhd.txt" "idata/SUS12024_SUS12011_SUS13012_SUS16033/llhd.txt"