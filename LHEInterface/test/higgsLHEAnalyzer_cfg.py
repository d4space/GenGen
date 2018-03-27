import FWCore.ParameterSet.Config as cms

process = cms.Process("higgsLHE")

process.load("FWCore.MessageService.MessageLogger_cfi")

process.maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )

process.source = cms.Source("PoolSource",
    # replace 'myfile.root' with the source file you want to use
    fileNames = cms.untracked.vstring('file:MCDBtoEDM_ggh_0L1_WW2l2n_M125_jhu710.root')
    #fileNames = cms.untracked.vstring(
    #    'file:myfile.root'
    #)
)

process.TFileService = cms.Service("TFileService",
    fileName = cms.string("ggh_0L1_WW2l2n_LHEAnal.root"),
    #closeFileFast = cms.untracked.bool(True)
    )

process.hAna = cms.EDAnalyzer('higgsLHEAnalyzer',
    src = cms.InputTag("source")
)


process.p = cms.Path(process.hAna)
