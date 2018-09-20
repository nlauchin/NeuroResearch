from netpyne import specs

cfg = specs.SimConfig()

# simulation configuration
cfg.duration = 0.5*1e3
cfg.dt = 0.05
cfg.seeds = {'conn': 1, 'stim': 1, 'loc': 1}
cfg.verbose = 0
cfg.hParams = {'celsius': 34, 'v_init': -94.6}

cfg.recordStims = False
cfg.recordTraces = {'V_soma': {'sec':'soma', 'loc':0.5, 'var':'v'}}
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

cfg.analysis['plotTraces'] = {'include': [('PT5B',00)], 'saveFig': True, 'showFig': False}

# parameters for batch
stimSec = 'soma_0'