from netpyne import specs
from netpyne.batch import Batch
 
def createBatch(params):
    b = Batch(netParamsFile='CSTR_netParams.py', groupedParams=groupedParams)
    for k,v in params.iteritems():
        b.params.append({'label': k, 'values': v})
    return b

def batchCSTR():
    params = specs.ODict()
    
    params['recordTracesLoc'] = [0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1]
    
    b = Batch(params=params, cfgFile='CSTR_cfg.py', netParamsFile='CSTR_netParams.py')

    b.batchLabel = 'TracesLoc'
    b.saveFolder = 'CSTR_data'
    b.method = 'grid'
    b.runCfg = {'type': 'mpi', 'script': 'CSTR_init.py', 'skip': True}

    b.run()

    initCfg = {}
    initCfg['duration'] = 1.0*1e3
    initCfg[('analysis','plotTraces','timeRange')] = [0, 1000]
    initCfg['weightNorm'] = False
    initCfg['stimSubConn'] = False
    initCfg[('NetStim1', 'synMech')] = ['AMPA','NMDA']
    initCfg[('NetStim1','synMechWeightFactor')] = [0.5,0.5]
    initCfg[('NetStim1', 'start')] = 300
    initCfg[('NetStim1', 'interval')] = 1000/20.0
    initCfg[('NetStim1', 'noise')] = 0.25
    initCfg[('NetStim1', 'number')] = 1
    initCfg[('NetStim1', 'delay')] = 0
    #initCfg[('GroupNetStimW1', 'pop')] = 'None'
    initCfg['addIClamp'] = 0
    
if __name__ == '__main__':
    batchCSTR()
