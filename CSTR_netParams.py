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

# Current clamp inout
#netParams.stimSourceParams['Input_3'] = {'type': 'IClamp', 'delay': 0, 'dur': 50, 'amp': 0.5}
#netParams.stimTargetParams['Input_3->IT'] = {'source': 'Input_3', 'sec':'soma_0', 'loc':0.5, 'conds': {'pop': 'ITpop'}}

# Netstim input
netParams.stimSourceParams['Input_1'] = {'type': 'NetStim', 'rate': 10, 'noise': 0.0, 'start': 100}
netParams.stimTargetParams['Input_1->IT'] = {'source': 'Input_1', 'sec': 'soma_0', 'loc': 0.5, 'weight': 0.2, 
														'delay': 0, 'synMech': 'AMPA', 'conds': {'popLabel': 'ITpop'}}


# add secs to record
secs = netParams.cellParams['ITrule']['secs'].keys()
cfg.recordTraces = {'V_'+sec: {'sec':sec, 'loc': 0.5, 'var':'v'} for sec in secs }
