from netpyne import specs

cfg = specs.SimConfig()


# simulation config
cfg.duration = 0.5*1e3
cfg.dt = 0.05
cfg.seeds = {'conn': 1, 'stim': 2, 'loc': 1}
cfg.verbose = 0
cfg.hParams = {'celsius': 34, 'v_init': -94.6}

cfg.recordStims = False

cfg.recordStep = 0.1

cfg.simLabel = 'CSTRcell'
cfg.saveFolder = 'data'
cfg.savePickle = False
cfg.saveJson = True 
cfg.saveMat = False
cfg.saveDataInclude = ['simData', 'simConfig', 'netParams']
cfg.gatherOnlySimData = False

cfg.saveCellSecs = True
cfg.saveCellConns = True

cfg.synWeightFractionEE = [1.0, 0.1] 
cfg.synWeightFractionEI = [1.0, 0.1] 
cfg.synWeightFractionSOME = [1.0, 7.5] 

cfg.analysis['plotTraces'] = {'include': [('ITpop',0)], 'oneFigPer': 'trace', 'saveFig': True, 'showFig': False}

cfg.printPopAvgRates = True


# # parameters for batch
# cfg.stimSec = 'soma_0'
# cfg.stimWeight = 0.2
