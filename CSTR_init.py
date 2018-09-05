from netpyne import sim

simConfig, netParams = sim.readCmdLineArgs(simConfigDefault='CSTR_cfg.py', netParamsDefault='CSTR_netParams.py')

sim.createSimulateAnalyze(netParams=netParams, simConfig=simConfig)



import pylab; pylab.show()
