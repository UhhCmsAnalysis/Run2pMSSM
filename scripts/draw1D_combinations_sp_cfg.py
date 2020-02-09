from draw1D_combinations_cfg import *
combination = combined

import copy


del combination[1][0] # no line for preCMS

# the 7+8 TeV line
combination[1][4][1]["showStatUncert"] = False
combination[1][4][1]["pb_fillcolor"] = 17
combination[1][4][1]["pb_fillstyle"] = 1001
for i in range(0,len(combination[1])):
    combination[1][i][1]["denom"] = "preCMS"
# add the higss line
combination[1].append(copy.deepcopy(combination[1][4]))
combination[1][-1][0] = combination[1][4][0] + "_higgs"
combination[1][-1][1]["linecolor"] = 10
combination[1][-1][1]["drawstyle"] = "P0"
combination[1][-1][1]["linewidth"] = 1
combination[1][-1][1]["showStatUncert"] = False
combination[1][-1][1]["denom"] = "preCMS_higgs"
combination[1][-1][1]["markerstyle"] = 33
combination[1][-1][1]["markercolor"] = rt.kOrange + 7
combination[1][-1][1]["legendoption"] += "p"
combination[1][-1][1]["legendtitle"] += ", Higgs data"

lc = combination[1][3][1]["linecolor"]
lineLayout = {
    "050":{"linestyle":2,"linewidth":2,"linetitle":"#mu=0.5","linecolor":lc},
    "100":{"linestyle":1,"linewidth":4,"linetitle":"#mu=1.0","linecolor":lc},
    "150":{"linestyle":3,"linewidth":2,"linetitle":"#mu=1.5","linecolor":lc}
}


combinations = [combination]

for entry in combinations[0][1]:
    print entry

"""



combination[1][0][1]["legendtitle"] = legendTitle[combination[1][1][0].replace("_surv_100","")]
combination[1][1][1]["legendtitle"] = legendTitle[combination[1][4][0].replace("_surv_100","")]
#combination[1][3][1]["legendtitle"] = legendTitle[combination[1][3][1].replace("_surv_100","")]
combination[1][3][1]["legendoption"] = "lf"
combination[1][0][1].update(lineLayout)


#lc = combination[1][7][1]["linecolor"]

for i in range(0,len(combination[1])):
    combination[1][i][1]["denom"] = "preCMS"



print combination
sys.exit()
"""
