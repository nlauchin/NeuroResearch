from netpyne import specs
from netpyne.batch import Batch


def batchCSTR():
    params = specs.ODict()
    
    params['synMechTau1'] = [0.3, 0.5, 0.7]
    params['connLoc'] = [2.0, 3.0, 4.0]
    
    b = Batch(params=params, cfgFile='cfg.py', netParamsFile='netParams.py')

    b.batchLabel = 'tauLoc'
    b.saveFolder = 'CSTR_data'
    b.method = 'grid'
    b.runCfg = {'type': 'mpi', 'script': 'init.py', 'skip': True}

    b.run()

if __name__ == '__main__':
    batchCSTR()
