# CMSSW Basic Instructions

This repository was created for students that are starting to learning CMS SoftWare (CMSSW) tools. 

## Setup your LXPLUS area

Once you have a CERN account you can access the lxplus machines using SSH as:

```
ssh username@lxplus.cern.ch
```
enter your password and you will be logged.

The first step do be done (just once) is the github setup. This page explains easily how to do that: https://kbroman.org/github_tutorial/pages/first_time.html

Other important step is your grid certificate. To install at LXPLUS you must download the certificate from CERN website and install at LXPLUS.  The step-by-step can be found here: https://uscms.org/uscms_at_work/computing/getstarted/get_grid_cert.shtml . This step is important to submit CRAB jobs. To check your certificate (and you will do that many times) use:
```
voms-proxy-init -rfc -voms cms
```

### Advices
Add the following lines in your ~/.bashrc

CRAB setup (CRAB is a useful tool to spread jobs around the CMS grid architecture)
```
source /cvmfs/cms.cern.ch/crab3/crab.sh
```
More about CRAB can be found here: https://twiki.cern.ch/twiki/bin/view/CMSPublic/SWGuideCrab

Useful for HTCondor jobs (HTCondor is used to spread jobs in the CERN clusters)
See examples how to submit here: https://indico.cern.ch/event/366578/sessions/73138/attachments/728847/1000050/LHC_.pdf
```
alias condstat='condor_status -schedd' 

alias bigbird08='export _condor_SCHEDD_HOST="bigbird08.cern.ch" export _condor_CREDD_HOST="bigbird08.cern.ch"'
alias bigbird09='export _condor_SCHEDD_HOST="bigbird09.cern.ch" export _condor_CREDD_HOST="bigbird09.cern.ch"'
alias bigbird10='export _condor_SCHEDD_HOST="bigbird10.cern.ch" export _condor_CREDD_HOST="bigbird10.cern.ch"'
alias bigbird11='export _condor_SCHEDD_HOST="bigbird11.cern.ch" export _condor_CREDD_HOST="bigbird11.cern.ch"'
alias bigbird12='export _condor_SCHEDD_HOST="bigbird12.cern.ch" export _condor_CREDD_HOST="bigbird12.cern.ch"'
alias bigbird13='export _condor_SCHEDD_HOST="bigbird13.cern.ch" export _condor_CREDD_HOST="bigbird13.cern.ch"'
alias bigbird14='export _condor_SCHEDD_HOST="bigbird14.cern.ch" export _condor_CREDD_HOST="bigbird14.cern.ch"'
alias bigbird15='export _condor_SCHEDD_HOST="bigbird15.cern.ch" export _condor_CREDD_HOST="bigbird15.cern.ch"'
alias bigbird16='export _condor_SCHEDD_HOST="bigbird16.cern.ch" export _condor_CREDD_HOST="bigbird16.cern.ch"'
alias bigbird17='export _condor_SCHEDD_HOST="bigbird17.cern.ch" export _condor_CREDD_HOST="bigbird17.cern.ch"'
alias bigbird18='export _condor_SCHEDD_HOST="bigbird18.cern.ch" export _condor_CREDD_HOST="bigbird18.cern.ch"'
alias bigbird19='export _condor_SCHEDD_HOST="bigbird19.cern.ch" export _condor_CREDD_HOST="bigbird19.cern.ch"'
alias bigbird20='export _condor_SCHEDD_HOST="bigbird20.cern.ch" export _condor_CREDD_HOST="bigbird20.cern.ch"'
alias bigbird21='export _condor_SCHEDD_HOST="bigbird21.cern.ch" export _condor_CREDD_HOST="bigbird21.cern.ch"'
alias bigbird22='export _condor_SCHEDD_HOST="bigbird22.cern.ch" export _condor_CREDD_HOST="bigbird22.cern.ch"'
alias bigbird23='export _condor_SCHEDD_HOST="bigbird23.cern.ch" export _condor_CREDD_HOST="bigbird23.cern.ch"'
```
condstat will return the machine usage: number of jobs running, idle or hold.
the other commands you can use to change between machines based on the usage (there are others than bigbird, however this are the ones with more processing power).

Once this steps are followed we can now move to understand a bit CMSSW.

## CMSSW related stuff

CMSSW contain many codes writen in python and C++ (it is also possible to use python only). 
You can see in more details here http://cms-sw.github.io

In most of the cases the python files are configuration that calls C++ codes. The CMSSW C++ codes are usually divided in (there is another but is never used):
  - EDAnalyzer: read only -> useful to access data and created root TTrees or histograms
    - see https://twiki.cern.ch/twiki/bin/view/CMSPublic/WorkBookWriteFrameworkModule
  - EDProducer: it produces an edm file with informations about the event (see next section)
    - https://twiki.cern.ch/twiki/bin/view/CMSPublic/SWGuideEDProducer
  - EDFilter: used to remove events that are no important for the analysis (example: pileup for heavy ions)
    - https://twiki.cern.ch/twiki/bin/view/CMSPublic/SWGuideEDFilterAnalysis
    
We usually use the EDAnalyzer. One example that uses many EDAnalyzer's is the Heavy Ion Forest Framework that can be found:
  - https://twiki.cern.ch/twiki/bin/viewauth/CMS/HiForestSetup
  - https://github.com/CmsHI/cmssw
  
Other important topic is the CMSSW version. It depents when you collect the data, or process the MC. For example, for pPb at 2016 we use CMSSW_8_0_28, while in 2018 Pbpb data we use CMSSW_10_3_1. Because it is direct related with the detector reconstruction and design.

## CMS data format

After the trigger selection (L1T+HLT), the online reconstruction is done and the events selected are stored in a format called RAW data, saved at the computational infrastructure used by CMS. The RAW data contain all  the information coming from the detector with a size of ∼1 MB per event. To allow the physicists/users (also called analyzers) to perform analysis, an offline reconstruction is performed over the RAW files by using CMSSW, producing a new data format called RECO (∼ 3 MB/ev), where the physical objects (tracks, jets, ...) are available. The final data format used by the CMS Heavy Ion Group is the analysis object data (AOD), which is a subset of RECO (just removing some objects) and has the information needed for all the analysis with a reduced size (∼ 0.5MB/ev). Starting in 2022 the CMS Heavy Ion group will use miniAOD, which is a reduced (~1/10) size version of AOD  (in pp collisions they also have a so-called nanoAOD). See: https://twiki.cern.ch/twiki/bin/view/CMSPublic/WorkBookDataFormats and https://twiki.cern.ch/twiki/bin/view/CMSPublic/WorkBookChapter2 .

All of this formats are EDM (Event Data Model) format. To see the objects inside of the .root files you just need to use:
```
edmDumpEventContent file.root > list.txt
```
the file "list.txt" will contain the objects and in which format they are stored. See more about EDM and examples: https://twiki.cern.ch/twiki/bin/view/CMSPublic/WorkBookCMSSWFramework
https://twiki.cern.ch/twiki/bin/view/CMSPublic/WorkBookEdmInfoOnDataFile

The CMS data and MC can be fouded at the CMSDAS website: https://cmsweb.cern.ch/das/

### Useful CMSSW commands
To run a code locally you just need to run the python configuration file by using 
```
cmsRun conf_file.py
```
example: https://twiki.cern.ch/twiki/bin/view/CMSPublic/WorkBookWriteFrameworkModule

### Useful CRAB3 commands
For CRAB, we will access files that are not locally, for that you need a certificate:
```
voms-proxy-init -rfc -voms cms
```
The CRAB has it's own python  configuration file that call the default python configuration file you use at cmsRun. In the crab configuration files included, the jobs are submitted using a python command (do not forget voms command)
```
python crabfile.py
```
observation: in the crab configuration file you will include the path of the dataset at CMSDAS and this will overwrite the input dataset file in the local configuration file.

To check status of your jobs, you can just use ```crab status -d workArea/requestName/```, where workArea and requestName are folders generated automatically based on the name included in your crab configuration file. Example: 
```
crab status -d workArea/requestName/
```

To download the files you can use (be carefull if your files has large size)
```
crab getoutput workArea/requestName/
```

### Useful xrootd commands

Files are copied to your local machine using xrdcp, example
```
xrdcp -d 1 -f root://cmsxrootd.fnal.gov//store/user/ddesouza/PAEGJet1/HiForest_pPb_8TeV_p-going_JetSamples_out/211211_161432/0000/HiForestAOD_1.root . &> out.txt &
```

To access files and create a list of files you can use xrdfs, example:
```
xrdfs root://cmsxrootd.fnal.gov ls /store/user/ddesouza/PAEGJet1/HiForest_pPb_8TeV_p-going_JetSamples_out/211211_161432/0000/ &> listofforestfiles.txt &
```
