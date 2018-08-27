from netpyne import specs,sim
import pickle, json
try:
        from __main__ import cfg
except:
        from cfg import cfg

netParams = specs.NetParams()
netParams.popParams['CSTR_pop'] = {'cellType': 'CSTR','numCells':1, 'cellModel': 'HH'}

cellRule = {'conds': {'popLabel': 'CSTR_pop'}, 'secs': {}}
soma = {'geom':{}, 'mechs':{}}
soma['geom'] = {'diam': 44.3, 'L': 23.9, 'Ra':123.0}
soma['mechs']['hh'] = {'gnabar': 0.13, 'gkbar': 0.036, 'gl': 0.003, 'el': -65}

dend = {'geom': {}, 'topol': {}, 'mechs': {}}
dend['geom'] = {'diam': 1.1, 'L':229.4, 'Ra': 150.0}
dend['topol'] = {'parentSec': 'soma', 'parentX': 1.0, 'childX': 0}
dend['mechs']['pas'] = {'g': 0.0000357, 'e': -70}

cellRule['secs'] = {'soma':soma, 'dend': dend}
netParams.cellParams['CSTRrule'] = cellRule

netParams.synMechParams['AMPA'] = {'mod': 'Exp2Syn', 'tau1': cfg.synMechTau1, 'tau2': 1.0, 'e': 0}

netParams.addConnParams('CSTR_pop->CSTR_pop',{'preConds': {'popLabel': 'CSTR_pop'}, 'postConds': {'postLabel': 'CSTR_pop'}, 'delay':5, 'sec':'dend', 'loc':cfg.connLoc, 'synMech':'exc'})

netParams.stimSourceParams['Input_1'] = {'type': 'NetStim', 'rate': 10, 'noise': 0.5, 'start': 1}

netParams.stimTargetParams['Input_1->CSTR_pop'] = {'source': 'Input_1', 'sec':'soma', 'loc':0.5, 'conds': {'popLabel': 'CSTR_pop'}}

simConfig = specs.SimConfig()
simConfig.duration = 70
simConfig.dt = 0.025
simConfig.verbose = False
simConfig.recordTraces = {'V_soma': {'sec':'soma', 'loc':0.5, 'var':'v'}}
simConfig.seeds = {'conn':1, 'stim':1, 'loc':1}
simConfig.createNEURONObj = 1
simConfig.recordStim = True
simConfig.recordStep = 0.5
simConfig.filename = 'CSTR_output'
simConfig.savePickle = True
simConfig.analysis['plotRaster'] = {'saveFig': True}
simConfig.analysis['plotTraces'] = {'include': [0]}
simConfig.analysis['plot2Dnet'] = True

sim.createSimulateAnalyze(netParams, simConfig)
import pylab; pylab.show()
