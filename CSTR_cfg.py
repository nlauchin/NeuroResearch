from netpyne import specs

cfg = specs.SimConfig()

cfg.recordTracesLoc = 0.1

cfg.duration = 0.5*1e3
cfg.dt = 0.05
cfg.seeds = {'conn': 1, 'stim': 2, 'loc': 1}
cfg.verbose = 0
cfg.hParams = {'celsius': 34, 'v_init': -94.6}

cfg.recordStims = False
cfg.recordTraces = {'V_dend': {'sec':'dend', 'loc':cfg.recordTracesLoc, 'var':'v'}}
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

cfg.analysis['plotTraces'] = {'include': [('IT_full_BS1578',00)], 'saveFig': True, 'showFig': False}
cfg.addNetStim = 1

cfg.NetStim1 = {'numStims': 1,'pop': ['IT_L5B'], 'cellRule': 'CSTR_pop', 'secList': 'dend_16', 'allSegs': True, \
 						'synMech': ['AMPA', 'NMDA'] , 'start': 300, 'interval': 1000/20.0, 'noise': 0.25, 'number': 1, 'loc': 0.5, 'weight': 0.01, 'delay': 0}
cfg.printPopAvgRates = True
