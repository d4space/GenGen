import os

doCmd=1

massGrid = {'gghWW2l2n': [700, 800, 900, 1000, 1500, 2000, 2500, 3000],
        'gghWWlnuqq': [125, 200, 250, 300, 350, 400, 500, 550, 600, 650, 700,
            800, 900,1500, 2000, 2500, 3000]}

massGrid['vbfhWWlnuqq']= [125, 200, 250, 300, 350, 400, 450, 500, 550,600, 650, 700, 750, 800, 900, 1000, 1500, 2000, 2500, 3000]

key='vbfhWWlnuqq'
targetDir = key+'TopFiles'

for mass in massGrid[key]:
    print mass
    for topFiles in ['pwg_btlgrid.top','pwg_rmngrid.top','pwgborngrid.top','pwghistnorms.top']:
        a_topFile = targetDir+'/'+key+str(mass)+'_'+topFiles
        if not os.path.isfile(a_topFile):
            print "file not exists: ",a_topFile
            exit()
        cmd = './td'+' '+a_topFile
        print cmd
        if doCmd == 1:
            os.system(cmd)


