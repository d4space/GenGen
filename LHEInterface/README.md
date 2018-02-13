# LHE Interface 



## Purpose
```
Making histograms from LHE file.
Packages are originated from CMSSW/GeneratorInterface/LHEInterface
```

## Procedure
```
* . runCmsDriver.sh ; to make a script (MCDBtoEDM\_NONE.py) which turen lhe to EDM roottuple
* cmsRun MCDBtoEDM\_NONE.py ; to turn lhe file to EDM roottuple
* cmsRun higgsLHEAnalyzer\_cfg.py ; to analyze LHE EDM roottuple for higgs boson
```

