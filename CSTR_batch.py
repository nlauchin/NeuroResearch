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

#secs = []
#locs = []
#pops=['IT_full_BS1578']
#weights = [0.1]

#def weightNormE(pops=['IT_full_BS1578'],
                #segs = None, allSegs = True, rule = 'IT_full', weights= [0.1]):
    # Add params
    #from cfg import cfg
    #from M1_detailed import netParams
    #excludeSegs = ['axon']
    #if not segs:
        #for secName,sec in netParams.cellParams[rule]['secs'].iteritems():
            #if secName not in excludeSegs:
                #if allSegs:
                    #nseg = sec['geom']['nseg']
                    #for iseg in range(nseg):
                        #secs.append(secName)
                        #locs.append((iseg+1)*(1.0/(nseg+1)))
                #else:
                    #secs.append(secName)
                    #locs.append(0.5)



#weightNormE(pops= pops,
                #segs = None, allSegs = True, rule = 'IT_full', weights=weights)

#params = specs.ODict()
#params[('NetStim1', 'pop')] = pops
#params[('NetStim1', 'secList')] = secs
#params[('NetStim1', 'loc')] = locs
#params[('NetStim1', 'weight')] = weights
#groupedParams = [('NetStim1', 'secList'), ('NetStim1', 'loc')]

if __name__ == '__main__':
    batchCSTR()

