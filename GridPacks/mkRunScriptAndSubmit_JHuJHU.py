import os

ZH = {'0PM':        ['anomalouscouplings/ZH_NNPDF31_13TeV/SM.input','WWany_filter2l.input'],
      '0M':         ['anomalouscouplings/ZH_NNPDF31_13TeV/a3.input','anomalouscouplings/WWany_filter2l_a3.input'],
      '0Mf05ph0':   ['anomalouscouplings/ZH_NNPDF31_13TeV/a3mix.input','anomalouscouplings/WWany_filter2l_a3mixforZH.input'],
      '0PH':        ['anomalouscouplings/ZH_NNPDF31_13TeV/a2.input','anomalouscouplings/WWany_filter2l_a2.input'],
      '0PHf05ph0':  ['anomalouscouplings/ZH_NNPDF31_13TeV/a2mix.input','anomalouscouplings/WWany_filter2l_a2mixforZH.input'],
      '0L1':        ['anomalouscouplings/ZH_NNPDF31_13TeV/L1.input','anomalouscouplings/WWany_filter2l_L1.input'],
      '0L1f05ph0':  ['anomalouscouplings/ZH_NNPDF31_13TeV/L1mix.input','anomalouscouplings/WWany_filter2l_L1mixforZH.input'],
      '0L1Zgf05ph0':['anomalouscouplings/ZH_NNPDF31_13TeV/L1Zgmix.input','WWany_filter2l.input'],
    }
prodCardBase='cards/2017/13TeV/'
decayCardBase='cards/decay/'
for key in ZH:
  print "For coupling "+key
  prodCard = prodCardBase+ZH[key][0]
  decayCard = decayCardBase+ZH[key][1]
  name = 'ZHiggs'+key+'ToWW_2L_M-125_13TeV-JHU710'
  fileName='mkJHuJHU_ZhWW_2L_'+key+'.sh'
  f=open(fileName,"w")
  f.write("cd /afs/cern.ch/user/s/salee/WorkSpace/private/PowhegV2/CMSSW936ptch2/src/\n")
  f.write("eval `scramv1 runtime -sh`\n")
  f.write("cd /afs/cern.ch/user/s/salee/WorkSpace/private/PowhegV2/CMSSW936ptch2/src/genproductions/bin/JHUGen\n")
  f.write("./install.py --card "+prodCard+" --decay-card "+decayCard+" --name "+name+"\n")
  f.close()
  cmd = "chmod u+x "+fileName
  os.system(cmd)
  subCmd='bsub -q 1nd '+fileName
  os.system(subCmd)
