from CRABClient.UserUtilities import config, getUsernameFromSiteDB
config = config()

config.General.requestName = 'stealth_stop_350_singlino_SYY_DIGI_V3'
config.General.workArea = 'crab_projects'
config.General.transferOutputs = True
config.General.transferLogs = True

config.JobType.pluginName = 'Analysis'
config.JobType.psetName = 'step1_DIGI_SYY.py'
config.JobType.numCores = 1
config.JobType.maxMemoryMB = 3900

config.Data.inputDataset = '/stealth_stop_350_singlino_SYY_GENSIM/soha-stealth_stop_350_singlino_SYY_RAWSIMoutput-3e0ede18a629c4819212ba3ff63fe107/USER'
config.Data.inputDBS = 'phys03'
config.Data.splitting = 'FileBased'
config.Data.unitsPerJob = 1
config.Data.outLFNDirBase = '/store/user/soha/stealth'
config.Data.publication = True
config.Data.outputDatasetTag = 'stealth_stop_350_singlino_SYY_DIGI_V3'

config.Site.storageSite = 'T3_US_FNALLPC'
config.Data.ignoreLocality = True
config.Site.whitelist = ["T2_US_UCSD","T2_US_Wisconsin","T2_US_Nebraska","T2_US_Caltech","T2_US_MIT"]