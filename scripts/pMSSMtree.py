#!/usr/bin/env python

# BASICS:
# this script reads in a bunch of tables in txt format and converts them into a tree
# each table should contain a column ID,
# each unique ID will correspond to an entry in the tree


import sys,ConfigParser,tempfile,sets
import ROOT as rt
from mytools import slurptable

# command line options
path_cfg = sys.argv[1]
path_ofile = sys.argv[2] 

############################################
# read in the tables
############################################

class Section:
    def __init__(self):
        self.name = ""
        self.files = ""
        self.data_ci = []
        self.data = []
        self.branchNameBase = ""
        self.columnNames = []
        self.skipID = []

print 'path_cfg', path_cfg
FILE = open(path_cfg)
str_cfg = FILE.read() 
FILE.close()
exec(str_cfg)
sections = []
for entry in treeCfg:
    _cfg = entry[1]
    section = Section()
    # name
    section.name = entry[0]
    # read data
    section.files = _cfg["files"]
    section.data_ci,section.data = slurptable(filenames=section.files,dictMode=True)
    print "read data '{0}' from files '{1}', # of columns: '{2}'".format(section.name,section.files,len(section.data_ci))
    # branch name base
    if "base" in _cfg:
        section.branchNameBase = _cfg["base"]
    else:
        section.branchNameBase = section.name
    if len(section.branchNameBase) > 0:
        section.branchNameBase += "_"
    # columns to read into the tree
    section.columnNames = sorted(section.data_ci.keys())
    if "skip_col" in _cfg:
        skipColumns = _cfg["skip_col"].split(",")
        for c in reversed(range(0,len(section.columnNames))):
            if section.columnNames[c] in skipColumns:
                del section.columnNames[c]
    # ids to be skipped
    if "skip_ID" in _cfg:
        section.skipID.extend(_cfg["skip_ID"])
    sections.append(section)

############################################
# define c++ struct to interface the tree
############################################

struct_str  = "struct MyEntry{\n"
struct_str += "   int ID;\n"
struct_str += "   bool all_OK;\n" 
for section in sections:
    struct_str += "   // " + section.name + "\n"
    struct_str += "   bool " + section.name + "_OK;\n"
    for name in section.columnNames:
        struct_str += "   double " + section.branchNameBase + name + ";\n"
# a reset function
struct_str += "void reset(){\n"
struct_str += "   ID=-1;\n"
struct_str += "   all_OK=false;\n"
for section in sections:
    struct_str += "   // " + section.name + "\n" 
    for name in section.columnNames:
        struct_str += "   " + section.name + "_OK = false;\n"
        struct_str += "   " + section.branchNameBase + name + " = -9.99999999e+9;\n"
        
struct_str += "}\n"
struct_str += "};\n"

# write for check:
FILE = open("pMSSMtree_struct.C","w")
FILE.write(struct_str)
FILE.close()

# write struct to temporary file
TEMPFILE = tempfile.NamedTemporaryFile()
TEMPFILE.write(struct_str)
TEMPFILE.flush()
# load it into root
tempfileName = TEMPFILE.name
rt.gROOT.ProcessLine(".L " + tempfileName);
# create an instance
myEntry = rt.MyEntry();


############################################
# define python function to fill struct
############################################

func_str  = "def fillMyEntry(myEntry,ID,sections):\n"
func_str += "   myEntry.ID = ID\n"
func_str += "   myEntry.all_OK = True\n"
for s in range(0,len(sections)):
    func_str += "   # " + sections[s].name + "\n"
    func_str += "   myEntry." + sections[s].name + "_OK = True\n"
    func_str += "   if ID in sections[{0}].data:\n".format(s)
    func_str += "      _data = sections[{0}].data[ID]\n".format(s)
    for name in sections[s].columnNames:
        if name == "pointName":
            continue
        func_str += "      myEntry.{0} = _data[sections[{1}].data_ci[\"{2}\"]]\n".format(sections[s].branchNameBase + name,s,name)
    func_str += "   else:\n"
    func_str += "      myEntry.{0}_OK = False\n".format(sections[s].name)
    func_str += "      myEntry.all_OK = False\n"
    func_str += "      print \"WARNING: no ID \" + str(ID) + \" in table {0}\"\n".format(sections[s].name)
    func_str += "   if ID in sections[{0}].skipID:\n".format(s)
    func_str += "      myEntry.{0}_OK = False\n".format(sections[s].name)
    func_str += "      myEntry.all_OK = False\n"

# write for check
FILE = open("pMSSMtree_func.py","w")
FILE.write(func_str)
FILE.close()
# load into python
exec(func_str)

############################################
# define tree
############################################

tfile = rt.TFile.Open(path_ofile,"RECREATE")
tree  = rt.TTree("pMSSM","pMSSM")
tree.Branch("ID",rt.AddressOf(myEntry,"ID"),"ID/I")
tree.Branch("all_OK",rt.AddressOf(myEntry,"all_OK"),"all_OK/O")
for section in sections:
    varName = section.name + "_OK"
    tree.Branch(varName,rt.AddressOf(myEntry,varName),varName + "/O")
    for name in section.columnNames:
        if name == "pointName":
            continue
        varName = section.branchNameBase + name
        tree.Branch(varName,rt.AddressOf(myEntry,varName),varName + "/D")

############################################
# fill the tree
############################################
# create exaustive list of IDs
ID = sets.Set()
for section in sections:
    _ID = sets.Set(section.data.keys())
    ID = _ID|ID
ID = sorted(list(ID))

for _ID in ID:
    
    # TODO: RESET THE ENTRY:
    myEntry.reset()
    # fill struct
    try:
        _ID = int(_ID)
    except: 
        print ID
        print 'problem _ID', _ID
        exit(0)
    fillMyEntry(myEntry,_ID,sections)   # myEntry passed by ref?"
    tree.Fill()

############################################
# BYE BYE!
############################################
tree.Write()
print 'just created', tfile.GetName()
tfile.Close()







