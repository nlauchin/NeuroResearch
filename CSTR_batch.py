from netpyne import specs
from netpyne.batch import Batch
 
def batchCSTR():

    params = specs.ODict()

    # Add params
    from CSTR_cfg import cfg
    from CSTR_netParams import netParams

    secs = netParams.cellParams['ITrule']['secs'].keys()
    

    params['stimSec'] = secs
    params[('recordTraces', 'V_dend', 'sec')] = secs
    params['stimWeight'] = [0.2, 0.4]
    
    groupedParams = ['stimSec', ('recordTraces', 'V_dend', 'sec')]
    
    b = Batch(params=params, netParamsFile = 'CSTR_netParams.py', cfgFile = 'CSTR_cfg.py', groupedParams = groupedParams)
    
    b.batchLabel = 'secStims'
    b.saveFolder = 'CSTR_data'
    b.method = 'grid'
    b.runCfg = {'type': 'mpi_bulletin', 'script': 'CSTR_init.py', 'skip': True}
    b.run()

if __name__ == '__main__':
    batchCSTR()

