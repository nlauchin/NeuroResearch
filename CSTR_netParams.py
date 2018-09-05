from netpyne import specs,sim
import pickle, json

try:
        from __main__ import cfg
except:
        from cfg import cfg
        
from netpyne import specs,sim

netParams = specs.NetParams()
netParams.popParams['IT_full_BS1578'] = {'cellType': 'CSTR','numCells':1, 'cellModel': 'HH'}

cellParamLabels = ['IT_full_BS1578'] 
loadCellParams = cellParamLabels
saveCellParams = False 

for ruleLabel in loadCellParams:
	netParams.loadCellParamsRule(label=ruleLabel, fileName='Documents/GitHub/netpyne/examples/M1detailed/cells/'+ruleLabel+'_cellParams.pkl')
	
cellRule = {'conds': {'popLabel': 'IT_full_BS1578'}, 'secs': {}}
#soma = {'geom':{}, 'mechs':{}}
#soma['geom'] = {'diam': 44.3, 'L': 23.9, 'Ra':123.0}
#soma['mechs']['hh'] = {'gnabar': 0.13, 'gkbar': 0.036, 'gl': 0.003, 'el': -65}

#dend = {'geom': {}, 'topol': {}, 'mechs': {}}
#dend['geom'] = {'diam': 1.1, 'L':229.4, 'Ra': 150.0}
#dend['topol'] = {'parentSec': 'soma', 'parentX': 1.0, 'childX': 0}
#dend['mechs']['pas'] = {'g': 0.0000357, 'e': -70}

#cellRule['secs'] = {'soma':soma, 'dend': dend}
netParams.cellParams['ITrule'] = cellRule

netParams.synMechParams['AMPA'] = {'mod': 'Exp2Syn', 'tau1': 0.1, 'tau2': 1.0, 'e': 0}

#netParams.addConnParams('CSTR_pop->CSTR_pop',{'preConds': {'popLabel': 'CSTR_pop'}, 'postConds': {'postLabel': 'CSTR_pop'}, 'delay':5, 'sec':'dend', 'loc':0.1, 'synMech':'exc'})

netParams.stimSourceParams['Input_1'] = {'type': 'NetStim', 'rate': 10, 'noise': 0.5, 'start': 1}
netParams.stimSourceParams['Input_3'] = {'type': 'IClamp', 'delay': 3, 'dur': 10, 'amp': 50}
netParams.stimTargetParams['Input_1->IT_full_BS1578'] = {'source': 'Input_1', 'sec':'soma', 'loc':0.5, 'conds': {'popLabel': 'IT_full_BS1578'}}
netParams.stimTargetParams['Input_3->IT_full_BS1578'] = {'source': 'Input_3', 'sec':'soma', 'loc':1.0, 'weight': 1, 'delay': 0, 'synMech': 'exc', 'conds':{'popLabel': 'IT_full_BS1578'}


