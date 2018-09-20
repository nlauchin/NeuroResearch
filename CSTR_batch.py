from netpyne import specs
from netpyne.batch import Batch
 
def batchCSTR():

    params = specs.ODict()

    # Add params
    from CSTR_cfg import cfg
    from CSTR_netParams import netParams

    secs = netParams.cellParams['ITrule']['secs'].keys()
    
    params['stimSec'] = secs
    
    b = Batch(params=params, netParamsFile = 'CSTR_netParams.py', cfgFile = 'CSTR_cfg.py')
    
    b.batchLabel = 'secStims'
    b.saveFolder = 'CSTR_data'
    b.method = 'grid'
    b.runCfg = {'type': 'mpi_bulletin', 'script': 'CSTR_init.py', 'skip': True}
    b.run()

if __name__ == '__main__':
    batchCSTR()

