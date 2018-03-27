
cd /afs/cern.ch/user/s/salee/WorkSpace/private/PowhegV2/CMSSW936ptch2/src/
eval `scramv1 runtime -sh`
cd /afs/cern.ch/user/s/salee/WorkSpace/private/PowhegV2/CMSSW936ptch2/src/genproductions/bin/JHUGen
#eval `scramv1 runtime -csh`

#./install.py --card production_card --decay-card decay_card --name arbitrary_name_that_goes_in_the_tarball_filename
./install.py --card cards/2017/13TeV/anomalouscouplings/VBF_NNPDF31_13TeV/L1.input --decay-card cards/decay/anomalouscouplings/WW2l2nu_withtaus_L1.input --name VBFHiggs0L1ToWWTo2L2Nu_M-125_13TeV-JHU710
