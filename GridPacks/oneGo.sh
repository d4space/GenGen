# Definition of the input parameters:
# (1) -p grid production stage [f]  (one go)
# (2) -i intput card name [powheg.input]
# (3) -m process name (process defined in POWHEG)
# (4) -f working folder [my_ggH]
# (5) -q batch queue name (run locally if not specified)
# (6) -n the number of events to run


###################
# 2l2nu
###################
#python ./run_pwg.py -p f -i production/2017/13TeV/Higgs/gg_H_WW_quark-mass-effects_NNPDF31_13TeV/gg_H_WW_quark-mass-effects_NNPDF31_13TeV_M700.input -g ../JHUGen/cards/decay/WW2l2nu_withtaus_reweightdecay_CPS.input -m gg_H_quark-mass-effects -f gghWW2l2n700 -q 8nh -n 1000
#python ./run_pwg.py -p f -i production/2017/13TeV/Higgs/gg_H_WW_quark-mass-effects_NNPDF31_13TeV/gg_H_WW_quark-mass-effects_NNPDF31_13TeV_M800.input -g ../JHUGen/cards/decay/WW2l2nu_withtaus_reweightdecay_CPS.input -m gg_H_quark-mass-effects -f gghWW2l2n800 -q 8nh -n 1000
#python ./run_pwg.py -p f -i production/2017/13TeV/Higgs/gg_H_WW_quark-mass-effects_NNPDF31_13TeV/gg_H_WW_quark-mass-effects_NNPDF31_13TeV_M900.input -g ../JHUGen/cards/decay/WW2l2nu_withtaus_reweightdecay_CPS.input -m gg_H_quark-mass-effects -f gghWW2l2n900 -q 8nh -n 1000
#python ./run_pwg.py -p f -i production/2017/13TeV/Higgs/gg_H_WW_quark-mass-effects_NNPDF31_13TeV/gg_H_WW_quark-mass-effects_NNPDF31_13TeV_M1000.input -g ../JHUGen/cards/decay/WW2l2nu_withtaus_reweightdecay_CPS.input -m gg_H_quark-mass-effects -f gghWW2l2n1000 -q 8nh -n 1000
#python ./run_pwg.py -p f -i production/2017/13TeV/Higgs/gg_H_WW_quark-mass-effects_NNPDF31_13TeV/gg_H_WW_quark-mass-effects_NNPDF31_13TeV_M1500.input -g ../JHUGen/cards/decay/WW2l2nu_withtaus_reweightdecay_CPS.input -m gg_H_quark-mass-effects -f gghWW2l2n1500 -q 8nh -n 1000
#python ./run_pwg.py -p f -i production/2017/13TeV/Higgs/gg_H_WW_quark-mass-effects_NNPDF31_13TeV/gg_H_WW_quark-mass-effects_NNPDF31_13TeV_M2000.input -g ../JHUGen/cards/decay/WW2l2nu_withtaus_reweightdecay_CPS.input -m gg_H_quark-mass-effects -f gghWW2l2n2000 -q 8nh -n 1000
#python ./run_pwg.py -p f -i production/2017/13TeV/Higgs/gg_H_WW_quark-mass-effects_NNPDF31_13TeV/gg_H_WW_quark-mass-effects_NNPDF31_13TeV_M2500.input -g ../JHUGen/cards/decay/WW2l2nu_withtaus_reweightdecay_CPS.input -m gg_H_quark-mass-effects -f gghWW2l2n2500 -q 8nh -n 1000
#python ./run_pwg.py -p f -i production/2017/13TeV/Higgs/gg_H_WW_quark-mass-effects_NNPDF31_13TeV/gg_H_WW_quark-mass-effects_NNPDF31_13TeV_M3000.input -g ../JHUGen/cards/decay/WW2l2nu_withtaus_reweightdecay_CPS.input -m gg_H_quark-mass-effects -f gghWW2l2n3000 -q 8nh -n 1000
#
######################
# lnuqq
######################
#python ./run_pwg.py -p f -i production/2017/13TeV/Higgs/gg_H_WW_quark-mass-effects_NNPDF31_13TeV/gg_H_WW_quark-mass-effects_NNPDF31_13TeV_M125.input -g ../JHUGen/cards/decay/WWlnuqq_withtaus.input  -m gg_H_quark-mass-effects -f gghWWlnuqq125 -q 8nh -n 1000
#python ./run_pwg.py -p f -i production/2017/13TeV/Higgs/gg_H_WW_quark-mass-effects_NNPDF31_13TeV/gg_H_WW_quark-mass-effects_NNPDF31_13TeV_M200.input -g ../JHUGen/cards/decay/WWlnuqq_withtaus.input  -m gg_H_quark-mass-effects -f gghWWlnuqq200 -q 8nh -n 1000
#python ./run_pwg.py -p f -i production/2017/13TeV/Higgs/gg_H_WW_quark-mass-effects_NNPDF31_13TeV/gg_H_WW_quark-mass-effects_NNPDF31_13TeV_M250.input -g ../JHUGen/cards/decay/WWlnuqq_withtaus.input  -m gg_H_quark-mass-effects -f gghWWlnuqq250 -q 8nh -n 1000
#python ./run_pwg.py -p f -i production/2017/13TeV/Higgs/gg_H_WW_quark-mass-effects_NNPDF31_13TeV/gg_H_WW_quark-mass-effects_NNPDF31_13TeV_M300.input -g ../JHUGen/cards/decay/WWlnuqq_withtaus_reweightdecay_CPS.input  -m gg_H_quark-mass-effects -f gghWWlnuqq300 -q 8nh -n 1000
#python ./run_pwg.py -p f -i production/2017/13TeV/Higgs/gg_H_WW_quark-mass-effects_NNPDF31_13TeV/gg_H_WW_quark-mass-effects_NNPDF31_13TeV_M350.input -g ../JHUGen/cards/decay/WWlnuqq_withtaus_reweightdecay_CPS.input  -m gg_H_quark-mass-effects -f gghWWlnuqq350 -q 8nh -n 1000
#python ./run_pwg.py -p f -i production/2017/13TeV/Higgs/gg_H_WW_quark-mass-effects_NNPDF31_13TeV/gg_H_WW_quark-mass-effects_NNPDF31_13TeV_M400.input -g ../JHUGen/cards/decay/WWlnuqq_withtaus_reweightdecay_CPS.input  -m gg_H_quark-mass-effects -f gghWWlnuqq400 -q 8nh -n 1000
#python ./run_pwg.py -p f -i production/2017/13TeV/Higgs/gg_H_WW_quark-mass-effects_NNPDF31_13TeV/gg_H_WW_quark-mass-effects_NNPDF31_13TeV_M500.input -g ../JHUGen/cards/decay/WWlnuqq_withtaus_reweightdecay_CPS.input  -m gg_H_quark-mass-effects -f gghWWlnuqq500 -q 8nh -n 1000
#python ./run_pwg.py -p f -i production/2017/13TeV/Higgs/gg_H_WW_quark-mass-effects_NNPDF31_13TeV/gg_H_WW_quark-mass-effects_NNPDF31_13TeV_M550.input -g ../JHUGen/cards/decay/WWlnuqq_withtaus_reweightdecay_CPS.input  -m gg_H_quark-mass-effects -f gghWWlnuqq550 -q 8nh -n 1000
#python ./run_pwg.py -p f -i production/2017/13TeV/Higgs/gg_H_WW_quark-mass-effects_NNPDF31_13TeV/gg_H_WW_quark-mass-effects_NNPDF31_13TeV_M600.input -g ../JHUGen/cards/decay/WWlnuqq_withtaus_reweightdecay_CPS.input  -m gg_H_quark-mass-effects -f gghWWlnuqq600 -q 8nh -n 1000
#python ./run_pwg.py -p f -i production/2017/13TeV/Higgs/gg_H_WW_quark-mass-effects_NNPDF31_13TeV/gg_H_WW_quark-mass-effects_NNPDF31_13TeV_M650.input -g ../JHUGen/cards/decay/WWlnuqq_withtaus_reweightdecay_CPS.input  -m gg_H_quark-mass-effects -f gghWWlnuqq650 -q 8nh -n 1000
#python ./run_pwg.py -p f -i production/2017/13TeV/Higgs/gg_H_WW_quark-mass-effects_NNPDF31_13TeV/gg_H_WW_quark-mass-effects_NNPDF31_13TeV_M700.input -g ../JHUGen/cards/decay/WWlnuqq_withtaus_reweightdecay_CPS.input  -m gg_H_quark-mass-effects -f gghWWlnuqq700 -q 8nh -n 1000
#python ./run_pwg.py -p f -i production/2017/13TeV/Higgs/gg_H_WW_quark-mass-effects_NNPDF31_13TeV/gg_H_WW_quark-mass-effects_NNPDF31_13TeV_M800.input -g ../JHUGen/cards/decay/WWlnuqq_withtaus_reweightdecay_CPS.input  -m gg_H_quark-mass-effects -f gghWWlnuqq800 -q 8nh -n 1000
#python ./run_pwg.py -p f -i production/2017/13TeV/Higgs/gg_H_WW_quark-mass-effects_NNPDF31_13TeV/gg_H_WW_quark-mass-effects_NNPDF31_13TeV_M900.input -g ../JHUGen/cards/decay/WWlnuqq_withtaus_reweightdecay_CPS.input  -m gg_H_quark-mass-effects -f gghWWlnuqq900 -q 8nh -n 1000
#python ./run_pwg.py -p f -i production/2017/13TeV/Higgs/gg_H_WW_quark-mass-effects_NNPDF31_13TeV/gg_H_WW_quark-mass-effects_NNPDF31_13TeV_M1500.input -g ../JHUGen/cards/decay/WWlnuqq_withtaus_reweightdecay_CPS.input  -m gg_H_quark-mass-effects -f gghWWlnuqq1500 -q 8nh -n 1000
#python ./run_pwg.py -p f -i production/2017/13TeV/Higgs/gg_H_WW_quark-mass-effects_NNPDF31_13TeV/gg_H_WW_quark-mass-effects_NNPDF31_13TeV_M2000.input -g ../JHUGen/cards/decay/WWlnuqq_withtaus_reweightdecay_CPS.input  -m gg_H_quark-mass-effects -f gghWWlnuqq2000 -q 8nh -n 1000
#python ./run_pwg.py -p f -i production/2017/13TeV/Higgs/gg_H_WW_quark-mass-effects_NNPDF31_13TeV/gg_H_WW_quark-mass-effects_NNPDF31_13TeV_M2500.input -g ../JHUGen/cards/decay/WWlnuqq_withtaus_reweightdecay_CPS.input  -m gg_H_quark-mass-effects -f gghWWlnuqq2500 -q 8nh -n 1000
#python ./run_pwg.py -p f -i production/2017/13TeV/Higgs/gg_H_WW_quark-mass-effects_NNPDF31_13TeV/gg_H_WW_quark-mass-effects_NNPDF31_13TeV_M3000.input -g ../JHUGen/cards/decay/WWlnuqq_withtaus_reweightdecay_CPS.input  -m gg_H_quark-mass-effects -f gghWWlnuqq3000 -q 8nh -n 1000
#



python ./run_pwg.py -p f -i production/2017/13TeV/Higgs/HJJ_WW_NNPDF31_13TeV/HJJ_WW_NNPDF31_13TeV_M125.input -g ../JHUGen/cards/decay/WW2l2nu_withtaus.input -m HJJ -f ggHJJWW2l2n125_1 -q 2nw -n 1

python ./run_pwg.py -p f -i production/2017/13TeV/Higgs/HJJ_WW_NNPDF31_13TeV/HJJ_WW_NNPDF31_13TeV_M125.input -g ../JHUGen/cards/decay/WW2l2nu_withtaus.input -m HJJ -f ggHJJWW2l2n125_10 -q 2nw -n 10

python ./run_pwg.py -p f -i production/2017/13TeV/Higgs/HJJ_WW_NNPDF31_13TeV/HJJ_WW_NNPDF31_13TeV_M125.input -g ../JHUGen/cards/decay/WW2l2nu_withtaus.input -m HJJ -f ggHJJWW2l2n125_100 -q 2nw -n 100

python ./run_pwg.py -p f -i production/2017/13TeV/Higgs/HJJ_WW_NNPDF31_13TeV/HJJ_WW_NNPDF31_13TeV_M125.input -g ../JHUGen/cards/decay/WW2l2nu_withtaus.input -m HJJ -f ggHJJWW2l2n125_500 -q 2nw -n 500

python ./run_pwg.py -p f -i production/2017/13TeV/Higgs/HJJ_WW_NNPDF31_13TeV/HJJ_WW_NNPDF31_13TeV_M125.input -g ../JHUGen/cards/decay/WW2l2nu_withtaus.input -m HJJ -f ggHJJWW2l2n125_1000 -q 2nw -n 1000
