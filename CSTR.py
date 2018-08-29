from netpyne import specs,sim

netParams = specs.NetParams()

cellParamLabels = ['IT_full_BS1578'] 
loadCellParams = cellParamLabels
saveCellParams = False 

for ruleLabel in loadCellParams:
	netParams.loadCellParamsRule(label=ruleLabel, fileName='Documents/GitHub/netpyne/examples/M1detailed/cells/'+ruleLabel+'_cellParams.pkl')

#if 'PT5B_full' not in loadCellParams:
    #cellRule = netParams.importCellParams(label='CSTR_full',conds={'cellType': 'IT', 'cellModel': 'HH'},
                                      #fileName='cells/IT_full_BS1578_cellParams.pkl', cellName='ITcell')
cellRule = netParams.cellParams['IT_full_BS1578']
for secName,sec in cellRule['secs'].iteritems(): sec['vinit'] = -94.6
cellRule['secLists']['perisom'] = ['soma']
cellRule['secLists']['perisom'].extend([sec for sec in cellRule.secs if 'dend' in sec])  # soma+basal  
cellRule['secLists']['alldend'] = [sec for sec in cellRule.secs if ('dend' in sec or 'apic' in sec)] # basal+apical
cellRule['secLists']['apicdend'] = [sec for sec in cellRule.secs if ('apic' in sec)] # basal+apical
cellRule['secLists']['spiny'] = [sec for sec in cellRule['secLists']['alldend'] if sec not in ['apic_0', 'apic_1']]



netParams.popParams['CSTR_pop'] = {'cellType': 'CSTR','numCells':1, 'cellModel': 'HH'}

#cellRule = {'conds': {'popLabel': 'CSTR_pop'}, 'secs': {}}
#soma = {'geom':{}, 'mechs':{}}
#soma['geom'] = {'diam': 44.3, 'L': 23.9, 'Ra':123.0}
#soma['mechs']['hh'] = {'gnabar': 0.13, 'gkbar': 0.036, 'gl': 0.003, 'el': -65}

#dend = {'geom': {}, 'topol': {}, 'mechs': {}}
#dend['geom'] = {'diam': 1.1, 'L':229.4, 'Ra': 150.0}
#dend['topol'] = {'parentSec': 'soma', 'parentX': 1.0, 'childX': 0}
#dend['mechs']['pas'] = {'g': 0.0000357, 'e': -70}

#cellRule['secs'] = {'soma':soma, 'dend': dend}
#netParams.cellParams['CSTRrule'] = cellRule

netParams.synMechParams['AMPA'] = {'mod': 'Exp2Syn', 'tau1': 0.1, 'tau2': 1.0, 'e': 0}
netParams.synMechParams['NMDA'] = {'mod': 'MyExp2SynNMDABB', 'tau1NMDA':15,'tau2NMDA': 150, 'e': 0}

netParams.stimSourceParams['Input_1'] = {'type': 'NetStim', 'rate': 10, 'noise': 0.5, 'start': 1}
netParams.stimSourceParams['Input_2'] = {'type': 'IClamp', 'delay': 3, 'dur': 10, 'amp': 30}

netParams.stimTargetParams['Input_1->CSTR_pop'] = {'source': 'Input_1', 'sec':'soma', 'loc':0.5, 'conds': {'popLabel': 'CSTR_pop'}}
netParams.stimTargetParams['Input_2->CSTR_pop'] = {'source': 'Input_2', 'sec':'dend', 'loc':1.0, 'delay': 0, 'conds':{'popLabel': 'CSTR_pop'}}

simConfig = specs.SimConfig()
simConfig.duration = 70
simConfig.dt = 0.025
simConfig.verbose = False
simConfig.recordTraces = {'V_Dend': {'sec':'dend', 'loc':0.5, 'var':'v'}}
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
