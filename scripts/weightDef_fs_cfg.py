from weightDef_sel_cfg import weightCfg as weightCfgFull

weightCfg = []
for k in range(len(weightCfgFull)):
    key = weightCfgFull[k][0]
    for _key in ["preCMS","combined7and8TeV","combined7TeV"]:
        if key.find(_key)==0:
            weightCfg.append(weightCfgFull[k])
            print key

weightCfg.append(["preCMS",["all_OK","lhratio_preCMS"]])
weightCfg.append(["combined7and8and13TeV",["all_OK","lhratio_preCMS*(SUS12024_SUS12011_SUS13012_SUS16033_Z_100 >= -1.64)"]])
weightCfg.append(["preCMS_pb001",["all_OK","lhratio_preCMS*(xsect_8TeV_pb > 0.001)"]])
weightCfg.append(["combined7and8TeV_pb001",["all_OK","lhratio_preCMS*(SUS12024_SUS12011_SUS13012_SUS16033_Z_100 >= -1.64)*(xsect_8TeV_pb > 0.001)"]])
weightCfg.append(["preCMS_pb01",["all_OK","lhratio_preCMS*(xsect_8TeV_pb > 0.01)"]])
weightCfg.append(["combined7and8and13TeV_pb01",["all_OK","lhratio_preCMS*(SUS12024_SUS12011_SUS13012_SUS16033_Z_100 >= -1.64)*(xsect_8TeV_pb > 0.01)"]])
weightCfg.append(["preCMS_pb1",["all_OK","lhratio_preCMS*(xsect_8TeV_pb > 0.1)"]])
weightCfg.append(["combined7and8and13TeV_pb1",["all_OK","lhratio_preCMS*(SUS12024_SUS12011_SUS13012_SUS16033_Z_100 >= -1.64)*(xsect_8TeV_pb > 0.1)"]])

