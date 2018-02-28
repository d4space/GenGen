import os

doCmd=1

massGrid = {'gghWW2l2n': [700, 800, 900, 1000, 1500, 2000, 2500, 3000],
        'gghWWlnuqq': [125, 200, 250, 300, 350, 400, 500, 550, 600, 650, 700,
            800, 900,1500, 2000, 2500, 3000]}


massGrid['vbfhWWlnuqq']= [125, 200, 250, 300, 350, 400, 450, 500, 550,600, 650, 700, 750, 800, 900, 1000, 1500, 2000, 2500, 3000]


key='vbfhWWlnuqq'


targetDir = key+ 'TopFiles'


for mass in massGrid[key]:
    print mass
    f_btlgrid = key+str(mass)+'/'+'pwg-btlgrid.top'
    tg_btlgrid = key+str(mass)+'_'+'pwg_btlgrid.top'
    if not os.path.isfile(f_btlgrid):
        print "file not exists: ",f_btlgrid
        exit()
    cmd = 'cp'+' '+f_btlgrid+' '+targetDir+'/'+tg_btlgrid
    print cmd
    if doCmd == 1:
        os.system(cmd)

    f_rmngrid = key+str(mass)+'/'+'pwg-rmngrid.top'
    tg_rmngrid = key+str(mass)+'_'+'pwg_rmngrid.top'
    if not os.path.isfile(f_rmngrid):
        print "file not exists: ",f_rmngrid
        exit()
    cmd = 'cp'+' '+f_rmngrid+' '+targetDir+'/'+tg_rmngrid
    print cmd
    if doCmd == 1:
        os.system(cmd)

    f_borngrid = key+str(mass)+'/'+'pwgborngrid.top'
    tg_borngrid = key+str(mass)+'_'+'pwgborngrid.top'
    if not os.path.isfile(f_borngrid):
        print "file not exists: ",f_borngrid
        exit()
    cmd = 'cp'+' '+f_borngrid+' '+targetDir+'/'+tg_borngrid
    print cmd
    if doCmd == 1:
        os.system(cmd)

    f_histnorms = key+str(mass)+'/'+'pwghistnorms.top'
    tg_histnorms = key+str(mass)+'_'+'pwghistnorms.top'
    if not os.path.isfile(f_histnorms):
        print "file not exists: ",f_histnorms
        exit()
    cmd = 'cp'+' '+f_histnorms+' '+targetDir+'/'+tg_histnorms
    print cmd
    if doCmd == 1:
        os.system(cmd)


