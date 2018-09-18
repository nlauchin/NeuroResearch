from netpyne import specs
from netpyne.batch import Batch
 
def batchCSTR():

    params = specs.ODict()
    
    params['recordTracesLoc'] = [0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1]
    
    b = Batch(params=params, netParamsFile = 'CSTR_netParams.py', cfgFile = 'CSTR_cfg.py')
    
    b.batchLabel = 'traceLoc'
    b.saveFolder = 'CSTR_data'
    b.method = 'grid'
    b.runCfg = {'type': 'mpi', 'script': 'CSTR_init.py', 'skip': True}
    b.run()

if __name__ == '__main__':
    batchCSTR()

