#!/usr/bin/env python

legendTitle = {
    "preCMS" : "Prior from non-DCS data",
    "preCMS_123mh128" : "Prior from non-DCS data, 123 GeV < m_{h} < 128 GeV",
    # monojet
    "EXO11059" : "Monojet, 7 TeV, 5 fb^{-1}",
    "EXO12048" : "Monojet EXO, 8 TeV, 20 fb^{-1}",
    "SUS13009" : "Monojet SUS, 8 TeV, 20 fb^{-1}",
    "EXO12048_SUS13009" : "Monojet, 8 TeV",
    "EXO11059_EXO12048_SUS13009" : "Monojet, all",
    # SUS12003
    "SUS12003_1BL": "H_{T} + E_{T}^{miss} + b-jets, 1BL, 7 TeV, 4.98 fb^{-1}",
    "SUS12003_1BT": "H_{T} + E_{T}^{miss} + b-jets, 1BT, 7 TeV, 4.98 fb^{-1}",
    "SUS12003_2BL": "H_{T} + E_{T}^{miss} + b-jets, 2BL, 7 TeV, 4.98 fb^{-1}",
    "SUS12003_2BT": "H_{T} + E_{T}^{miss} + b-jets, 2BT, 7 TeV, 4.98 fb^{-1}",
    "SUS12003_3BL": "H_{T} + E_{T}^{miss} + b-jets, 3BL, 7 TeV, 4.98 fb^{-1}",
    "SUS12003"    : "H_{T} + E_{T}^{miss} + b-jets, 7 TeV, 4.98 fb^{-1}",
    # SUS12006
    "SUS12006_ss" : "EW prod. #tilde{#chi}^{#pm} #tilde{#chi}^{0} #tilde{l} (ss), 7 TeV, 4.98 fb^{-1}",
    "SUS12006_3l" : "EW prod. #tilde{#chi}^{#pm} #tilde{#chi}^{0} #tilde{l} (3l), 7 TeV, 4.98 fb^{-1}",
    "SUS12006_os2j" : "EW prod. #tilde{#chi}^{#pm} #tilde{#chi}^{0} #tilde{l} (os2j), 7 TeV, 4.98 fb^{-1}",
    "SUS12006" : "EW prod. #tilde{#chi}^{#pm} #tilde{#chi}^{0} #tilde{l}, 7 TeV, 4.98 fb^{-1}",
    # SUS12011
    "SUS12011":"H_{T} + H_{T}^{miss}, 7 TeV, 4.98 fb^{-1}",
    # SUS12024
    "SUS12024":"H_{T} + E_{T}^{miss} + b-jets, 8 TeV, 19.4 fb^{-1}",
    # SUS13006
    "SUS13006_ss":"EW prod. #tilde{#chi}^{#pm} #tilde{#chi}^{0} #tilde{l} (ss), 8 TeV, 19.5 fb^{-1}",
    "SUS13006_3l":"EW prod. #tilde{#chi}^{#pm} #tilde{#chi}^{0} #tilde{l} (3l), 8 TeV, 19.5 fb^{-1}",
    "SUS13006_3lOSSF0":"EW prod. #tilde{#chi}^{#pm} #tilde{#chi}^{0} #tilde{l} (3l, 0 ossf), 8 TeV, 19.5 fb^{-1}",
    "SUS13006_3lOSSF1":"EW prod. #tilde{#chi}^{#pm} #tilde{#chi}^{0} #tilde{l} (3l, #geq 1 ossf), 8 TeV, 19.5 fb^{-1}",
    "SUS13006_OSSF1tau":"EW prod. #tilde{#chi}^{#pm} #tilde{#chi}^{0} #tilde{l} (3l, ossf + tau), 8 TeV, 19.5 fb^{-1}",
    "SUS13006_SStau":"EW prod. #tilde{#chi}^{#pm} #tilde{#chi}^{0} #tilde{l} (3l, ss + tau), 8 TeV, 19.5 fb^{-1}",
    "SUS13006_4l":"EW prod. #tilde{#chi}^{#pm} #tilde{#chi}^{0} #tilde{l} (4l), 8 TeV, 19.5 fb^{-1}",
    "SUS13006":"EW prod. #tilde{#chi}^{#pm} #tilde{#chi}^{0} #tilde{l}, 8 TeV, 19.5 fb^{-1}",
    # SUS13012
    "SUS13012":"H_{T} + H_{T}^{miss}, 8 TeV, 19.5 fb^{-1}",
    # SUS13013
    "SUS13013_inc":"LS ll, 8 TeV, 19.5 fb^{-1}",
    # SUS13015
    "SUS13015":"Hadr. 3^{rd} gen., 8 TeV, 19.4 fb^{-1}",
    # SUS13019
    "SUS13019":"M_{T2}, 8 TeV, 19.5 fb^{-1}",
    # SUS14014
    "SUS14014":"OS ll, 8 TeV, 19.4 fb^{-1}",
    # SUS12003 + SUS12024
    "SUS12003_1BL_SUS12024": "H_{T} + E_{T}^{miss} + b-jets, 7(1BL) and 8 TeV",
    "SUS12003_1BT_SUS12024": "H_{T} + E_{T}^{miss} + b-jets, 7(1BT) and 8 TeV",
    "SUS12003_2BL_SUS12024": "H_{T} + E_{T}^{miss} + b-jets, 7(2BL) and 8 TeV",
    "SUS12003_2BT_SUS12024": "H_{T} + E_{T}^{miss} + b-jets, 7(2BT) and 8 TeV",
    "SUS12003_3BL_SUS12024": "H_{T} + E_{T}^{miss} + b-jets, 7(3BL) and 8 TeV",
    "SUS12003_SUS12024": "H_{T} + E_{T}^{miss} + b-jets, 7 + 8 TeV",
    # SUS12006 + SUS13006
    "SUS12006_SUS13006": "EW prod. #tilde{#chi}^{#pm} #tilde{#chi}^{0} #tilde{l}, 7 + 8 TeV",
    # SUS12011 + SUS13012
    "SUS12011_SUS13012" : "H_{T} + H_{T}^{miss}, 7 + 8 TeV",
    # 7 TeV combined
    "combined7TeV":"Combined, 7 TeV",
    "combined7TeV_mj":"Combined, 7 TeV",
    # 8 TeV combined
    "combined8TeV":"Combined, 8 TeV",
    "combined8TeV_mj":"Combined, 8 TeV",
    # 7 + 8 TeV combinations
    "combined7and8TeV":"Combined, 7 + 8 TeV",
    "combined7and8TeV_mj":"Combined, 7 + 8 TeV",
    "combined7and8TeV_123mh128":"Combined, 7 + 8 TeV, 123 GeV < m_{h} < 128 GeV",
    "SUS16033":"H_{T} + H_{T}^{miss}, n(b) 13 TeV, 35.9 fb^{-1}",
    "combined7and8and13TeV":"somewhat lossy combo I believe",
    "SUS12024_SUS12011_SUS13012_SUS16033":"Combined 7+8+13 TeV, H_{T} + H_{T}^{miss}, n(b)",
    }

legendTitleFrame = {
    "preCMS_lhd":"p^{{non-DCS}}(#theta) {0}",
    "preCMS_123mh128_lhd":"p^{{non-DCS}}(#theta | 123 < m_{{h}} < 128 ) {0}",
    "preCMS_simple":"{0}",
    "lhd": "p(#theta|D^{{CMS}}) {0}",
    "zlhd": "p(#theta|Z > -1.64) {0}",
    "zlhd": "p(#theta|Z > -1.64) {0}",
    "zlhd_123mh128": "p(#theta|Z > -1.64,123 < m_{{h}} < 128) {0}",
    "excl": "{0}, excl.",
    "surv": "{0}, surv.",
    "invZlhd" : "p(#theta|Z > -1.64,123 < m_{{h}} < 128) {0}",
}

