from netpyne import specs,sim

try:
	from __main__ import cfg
except:
	from CSTR_cfg import cfg
        
netParams = specs.NetParams()
netParams.popParams['ITpop'] = {'cellType': 'IT','numCells':1, 'cellModel': 'HH'}

netParams.loadCellParamsRule(label='ITrule', fileName='IT_full_BS1578_cellParams.pkl')
netParams.cellParams['ITrule']['conds'] = {'pop': 'ITpop'}

netParams.synMechParams['AMPA'] = {'mod': 'Exp2Syn', 'tau1': 0.1, 'tau2': 1.0, 'e': 0}

netParams.stimSourceParams['Input_1'] = {'type': 'NetStim', 'rate': 10, 'noise': 0.5, 'start': 1}
netParams.stimSourceParams['Input_3'] = {'type': 'IClamp', 'delay': 3, 'dur': 10, 'amp': 50}
netParams.stimTargetParams['Input_1->IT_full_BS1578'] = {'source': 'Input_1', 'sec':'soma', 'loc':0.5, 'conds': {'pop': 'ITpop'}}
netParams.stimTargetParams['Input_3->IT_full_BS1578'] = {'source': 'Input_3', 'sec':'soma', 'loc':1.0, 'weight': 1, 'delay': 0, 'synMech': 'exc', 'conds': {'popLabel': 'ITpop'}}


