from netpyne import sim

simConfig, netParams = sim.readCmdLineArgs(simConfigDefault='CSTR_cfg.py', netParamsDefault='CSTR_netParams.py')

sim.createSimulateAnalyze(netParams=netParams, simConfig=simConfig)


sim.initialize(
    simConfig=cfg, 
    netParams=netParams)  # create network object and set cfg and net params
sim.net.createPops()                  # instantiate network populations
sim.net.createCells()                 # instantiate network cells based on defined populations
sim.net.connectCells()                # create connections between cells based on params
sim.setupRecording()              # setup variables to record for each cell (spikes, V traces, etc)
sim.runSim()                      # run parallel Neuron simulation  
sim.gatherData()                  # gather spiking data and cell info from each node
sim.saveData()                    # save params, cell info and sim output to file (pickle,mat,txt,etc)
sim.analysis.plotData()               # plot spike raster

import pylab; pylab.show()
                                                                                                                                                                                                                                                                                                                                                                    
