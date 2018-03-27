import os

########### All

massGrid = {'VBFhWWlnuqq': [125, 200, 250, 300, 350, 400, 450, 500, 550,600, 650, 700, 750, 800, 900, 1000, 1500, 2000, 2500, 3000]
            }


##################
#  400 <batch> Exited
##################
#massGrid = {'VBFhWWlnuqq': [125, 200, 250, 300, 350, 450, 500, 550,600, 650, 700, 750, 800, 900, 1000, 1500, 2000, 2500, 3000]
#            }

#massGrid = {'VBFhWWlnuqq': [400]
#            }

#####################################################
# Gridpack production with multiple processors
#####################################################

######################################
# Step1: Compiling the POWHEG source
######################################
#for mass in massGrid['VBFhWWlnuqq']:
#    print mass
#    if mass < 300 :
#        cmd = 'python ./run_pwg.py -p 0 -i production/2017/13TeV/Higgs/VBF_H_WW_NNPDF31_13TeV/VBF_H_WW_NNPDF31_13TeV_M'+str(mass)+'.input -g ../JHUGen/cards/decay/WWlnuqq_withtaus.input -m VBF_H -f vbfhWWlnuqq'+str(mass)
#    else :
#        cmd = 'python ./run_pwg.py -p 0 -i production/2017/13TeV/Higgs/VBF_H_WW_NNPDF31_13TeV/VBF_H_WW_NNPDF31_13TeV_M'+str(mass)+'.input -g ../JHUGen/cards/decay/WWlnuqq_withtaus_reweightdecay_CPS.input -m VBF_H -f vbfhWWlnuqq'+str(mass)
#
#    print cmd
#    os.system(cmd)
#
###############################################################
# Step2: Producting grids with 3 separate internal stages
################################################################
###########
# step 1-1  p1 x1,2,3,4,5 8nh
###########
#for mass in massGrid['VBFhWWlnuqq']:
#    print mass
#    if mass < 300 :
#        cmd = 'python ./run_pwg.py -p 1 -x 5 -i production/2017/13TeV/Higgs/VBF_H_WW_NNPDF31_13TeV/VBF_H_WW_NNPDF31_13TeV_M'+str(mass)+'.input -g ../JHUGen/cards/decay/WWlnuqq_withtaus.input -m VBF_H -f vbfhWWlnuqq'+str(mass) +' -q 8nh -j 10'
#    else :
#        cmd = 'python ./run_pwg.py -p 1 -x 5 -i production/2017/13TeV/Higgs/VBF_H_WW_NNPDF31_13TeV/VBF_H_WW_NNPDF31_13TeV_M'+str(mass)+'.input -g ../JHUGen/cards/decay/WWlnuqq_withtaus_reweightdecay_CPS.input -m VBF_H -f vbfhWWlnuqq'+str(mass) + ' -q 8nh -j 10'
#
#    print cmd
#    os.system(cmd)
#
###########
# step 2 (2nd), 3 (8nh)
###########
#for mass in massGrid['VBFhWWlnuqq']:
#    print mass
#    if mass < 300 :
#        cmd = 'python ./run_pwg.py -p 3 -i production/2017/13TeV/Higgs/VBF_H_WW_NNPDF31_13TeV/VBF_H_WW_NNPDF31_13TeV_M'+str(mass)+'.input -g ../JHUGen/cards/decay/WWlnuqq_withtaus.input -m VBF_H -f vbfhWWlnuqq'+str(mass) +' -q 2nd -j 10'
#    else :
#        cmd = 'python ./run_pwg.py -p 3 -i production/2017/13TeV/Higgs/VBF_H_WW_NNPDF31_13TeV/VBF_H_WW_NNPDF31_13TeV_M'+str(mass)+'.input -g ../JHUGen/cards/decay/WWlnuqq_withtaus_reweightdecay_CPS.input -m VBF_H -f vbfhWWlnuqq'+str(mass) + ' -q 2nd -j 10'
#
#    print cmd
#    os.system(cmd)
#
####################################################
# Step 3: Create the POWHEG gridpack tarball
####################################################
#for mass in massGrid['VBFhWWlnuqq']:
#    print mass
#    if mass < 300 :
#        cmd = 'python ./run_pwg.py -p 9 -i production/2017/13TeV/Higgs/VBF_H_WW_NNPDF31_13TeV/VBF_H_WW_NNPDF31_13TeV_M'+str(mass)+'.input -g ../JHUGen/cards/decay/WWlnuqq_withtaus.input -m VBF_H -f vbfhWWlnuqq'+str(mass) +' -k 1'
#    else :
#        cmd = 'python ./run_pwg.py -p 9 -i production/2017/13TeV/Higgs/VBF_H_WW_NNPDF31_13TeV/VBF_H_WW_NNPDF31_13TeV_M'+str(mass)+'.input -g ../JHUGen/cards/decay/WWlnuqq_withtaus_reweightdecay_CPS.input -m VBF_H -f vbfhWWlnuqq'+str(mass) + ' -k 1'
#
#    print cmd
#    os.system(cmd)
#########################
# one go
#########################
#for mass in massGrid['VBFhWWlnuqq']:
#    print mass
#    if mass < 300 :
#        cmd = 'python ./run_pwg.py -p f -i production/2017/13TeV/Higgs/VBF_H_WW_NNPDF31_13TeV/VBF_H_WW_NNPDF31_13TeV_M'+str(mass)+'.input -g ../JHUGen/cards/decay/WWlnuqq_withtaus.input -m VBF_H -f vbfhWWlnuqq'+str(mass)+' -q 1nd -n 1000'
#    else :
#        cmd = 'python ./run_pwg.py -p f -i production/2017/13TeV/Higgs/VBF_H_WW_NNPDF31_13TeV/VBF_H_WW_NNPDF31_13TeV_M'+str(mass)+'.input -g ../JHUGen/cards/decay/WWlnuqq_withtaus_reweightdecay_CPS.input -m VBF_H -f vbfhWWlnuqq'+str(mass)+' -q 1nd -n 1000'
#
#    print cmd
#    os.system(cmd)
#


cmd = 'python ./run_pwg.py -p f -i production/2017/13TeV/Higgs/gg_H_WW_quark-mass-effects_NNPDF31_13TeV/gg_H_WW_quark-mass-effects_NNPDF31_13TeV_M125.input -g ../JHUGen/cards/decay/WW2l2nu_withtaus.input -m gg_H_quark-mass-effects -f ggh_0PM_WW2l2n_M125_jhu710 -q 1nd -n 1000'
print cmd
os.system(cmd)

cmd = 'python ./run_pwg.py -p f -i production/2017/13TeV/Higgs/gg_H_WW_quark-mass-effects_NNPDF31_13TeV/gg_H_WW_quark-mass-effects_NNPDF31_13TeV_M125.input -g ../JHUGen/cards/decay/anomalouscouplings/WW2l2nu_withtaus_a3.input -m gg_H_quark-mass-effects -f ggh_0M_WW2l2n_M125_jhu710 -q 1nd -n 1000'
print cmd
os.system(cmd)

cmd = 'python ./run_pwg.py -p f -i production/2017/13TeV/Higgs/gg_H_WW_quark-mass-effects_NNPDF31_13TeV/gg_H_WW_quark-mass-effects_NNPDF31_13TeV_M125.input -g ../JHUGen/cards/decay/anomalouscouplings/WW2l2nu_withtaus_a3mix.input -m gg_H_quark-mass-effects -f ggh_0Mf05ph0_WW2l2n_M125_jhu710 -q 1nd -n 1000'
print cmd
os.system(cmd)


cmd = 'python ./run_pwg.py -p f -i production/2017/13TeV/Higgs/gg_H_WW_quark-mass-effects_NNPDF31_13TeV/gg_H_WW_quark-mass-effects_NNPDF31_13TeV_M125.input -g ../JHUGen/cards/decay/anomalouscouplings/WW2l2nu_withtaus_a2.input -m gg_H_quark-mass-effects -f ggh_0PH_WW2l2n_M125_jhu710 -q 1nd -n 1000'
print cmd
os.system(cmd)


cmd = 'python ./run_pwg.py -p f -i production/2017/13TeV/Higgs/gg_H_WW_quark-mass-effects_NNPDF31_13TeV/gg_H_WW_quark-mass-effects_NNPDF31_13TeV_M125.input -g ../JHUGen/cards/decay/anomalouscouplings/WW2l2nu_withtaus_a2mix.input -m gg_H_quark-mass-effects -f ggh_0PHf05ph0_WW2l2n_M125_jhu710 -q 1nd -n 1000'
print cmd
os.system(cmd)


cmd = 'python ./run_pwg.py -p f -i production/2017/13TeV/Higgs/gg_H_WW_quark-mass-effects_NNPDF31_13TeV/gg_H_WW_quark-mass-effects_NNPDF31_13TeV_M125.input -g ../JHUGen/cards/decay/anomalouscouplings/WW2l2nu_withtaus_L1.input -m gg_H_quark-mass-effects -f ggh_0L1_WW2l2n_M125_jhu710 -q 1nd -n 1000'
print cmd
os.system(cmd)


cmd = 'python ./run_pwg.py -p f -i production/2017/13TeV/Higgs/gg_H_WW_quark-mass-effects_NNPDF31_13TeV/gg_H_WW_quark-mass-effects_NNPDF31_13TeV_M125.input -g ../JHUGen/cards/decay/anomalouscouplings/WW2l2nu_withtaus_L1mix.input -m gg_H_quark-mass-effects -f ggh_0L1f05ph0_WW2l2n_M125_jhu710 -q 1nd -n 1000'
print cmd
os.system(cmd)


