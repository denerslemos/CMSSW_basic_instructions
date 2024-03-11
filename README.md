<img src="https://github.com/denerslemos/CMSSW_basic_instructions/blob/main/CMSlogo_color_nolabel_1024_May2014.png"  width="20%" height="20%">

# CMS Survival Guide 

This repository was created for people starting to learn about CMS tools. 
1. [Setup your LXPLUS area](#setup)
    1. [Some advices](#advices)
2. [Introduction to CMSSW and tools](#introduction)
    1. [CMS Data Format](#dataformat)
    2. [CMSSW](#cmssw)
    3. [CRAB3](#crab3)
    4. [rucio](#rucio)
    5. [XROOTD](#xrootd)
    6. [HIN Forest Framework](#forest)
3. [CMS Talk and CMS Pub Talk](#cmstalk)
4. [CADI Instructions](#cadi)
5. [TDR](#tdr)
    1. [Diff](#diff)

## Setup your LXPLUS area <a name="setup"></a>

Once you have a CERN account you can access the lxplus machines using SSH as:

```
ssh username@lxplus.cern.ch
```
enter your password and you will be logged.

The first step do be done (just once) is the github setup (important for code maintenance and sharing). This page explains easily how to do that: https://kbroman.org/github_tutorial/pages/first_time.html

Similarly as shown in the website, you can add a key in gitlab (important to write analysis notes and papers) following:
https://docs.gitlab.com/ee/user/ssh.html


Other important step is your grid certificate. To install at LXPLUS you must download the certificate from CERN website and install at LXPLUS.  The step-by-step can be found here: https://uscms.org/uscms_at_work/computing/getstarted/get_grid_cert.shtml . This step is important to submit jobs in grid (CRAB or HTCondor) using files located in another Tier's. To check your certificate (and you will do that many times) use:

```
voms-proxy-init -rfc -voms cms
```

Note that the AFS space in LXPLUS is limited. You can request up to 10 GB here: https://resources.web.cern.ch/resources/Manage/AFS/Settings.aspx . In addition you can create an eos space at https://cernbox.cern.ch (/eos/user/first_letter_username/username) with 1 TB.

### Some advices <a name="advices"></a>

Add the following lines in your ~/.bashrc (optional, you can also type that everytime you log in) 

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
alias bigbird24='export _condor_SCHEDD_HOST="bigbird24.cern.ch" export _condor_CREDD_HOST="bigbird24.cern.ch"'
alias bigbird25='export _condor_SCHEDD_HOST="bigbird25.cern.ch" export _condor_CREDD_HOST="bigbird25.cern.ch"'
alias bigbird26='export _condor_SCHEDD_HOST="bigbird26.cern.ch" export _condor_CREDD_HOST="bigbird26.cern.ch"'
alias bigbird27='export _condor_SCHEDD_HOST="bigbird27.cern.ch" export _condor_CREDD_HOST="bigbird27.cern.ch"'
alias bigbird28='export _condor_SCHEDD_HOST="bigbird28.cern.ch" export _condor_CREDD_HOST="bigbird28.cern.ch"'
```
condstat will return the machine usage: number of jobs running, idle or hold.
the other commands you can use to change between clusters based on the usage (there are others than bigbird, however this are the ones with more processing power).

Once this steps are followed we can now move to understand a bit CMSSW.

## Introduction to CMSSW and tools <a name="introduction"></a>

CMSSW contain many codes writen in python and C++ (it is also possible to use python only). 
You can see in more details here http://cms-sw.github.io

In most of the cases the python files are configuration that calls C++ codes. The CMSSW C++ codes are usually divided in (there is another but is never used):
  - EDAnalyzer: read only -> useful to access data and created root TTrees or histograms
    - https://twiki.cern.ch/twiki/bin/view/CMSPublic/WorkBookWriteFrameworkModule
  - EDProducer: it produces an edm file with informations about the event (see next section)
    - https://twiki.cern.ch/twiki/bin/view/CMSPublic/SWGuideEDProducer
  - EDFilter: used to remove events that are no important for the analysis (example: pileup for heavy ions)
    - https://twiki.cern.ch/twiki/bin/view/CMSPublic/SWGuideEDFilterAnalysis
    
We usually use the EDAnalyzer. One example that uses many EDAnalyzer's is the Heavy Ion Forest Framework that can be found:
  - https://twiki.cern.ch/twiki/bin/viewauth/CMS/HiForestSetup
  - https://github.com/CmsHI/cmssw
  
Other important topic is the CMSSW version. It depents when you collect the data, or process the MC. For example, for pPb at 2016 we use CMSSW_8_0_28, while in 2018 PbPb data we use CMSSW_10_3_1. Because it is direct related with the detector reconstruction and design. The architecture of linux and C++ version are also important, in that case you can ask me (for example for pPb we use: ```export SCRAM_ARCH=slc7_amd64_gcc530```) or check in the Forest twiki above. In most of the cases we can do the analysis using the Forest, see this Forest introduction github page and this twiki. 

### CMS data format <a name="dataformat"></a>

After the trigger selection (L1T+HLT), the online reconstruction is done and the events selected are stored in a format called RAW data, saved at the computational infrastructure used by CMS. The RAW data contain all the information coming from the detector with a size of ∼1 MB per event. To allow the physicists/users (also called analyzers) to perform analysis, an offline reconstruction is performed over the RAW files by using CMSSW, producing a new data format called RECO (∼ 3MB/ev), where the physical objects (tracks, jets, ...) are available. The final data format used by the CMS Heavy Ion Group is the analysis object data (AOD), which is a subset of RECO (just removing some objects) and has the information needed for all the analysis with a reduced size (∼0.5MB/ev). Starting in 2022 the CMS Heavy Ion group will use miniAOD, which is a reduced (~1/10) size version of AOD  (in pp collisions they also have a so-called nanoAOD). See: https://twiki.cern.ch/twiki/bin/view/CMSPublic/WorkBookDataFormats and https://twiki.cern.ch/twiki/bin/view/CMSPublic/WorkBookChapter2 .

All of this formats are EDM (Event Data Model) format. To see the objects inside of the .root files you just need to use:
```
edmDumpEventContent file.root > list.txt
```
the file "list.txt" will contain the objects and in which format they are stored. See more about EDM and examples: https://twiki.cern.ch/twiki/bin/view/CMSPublic/WorkBookCMSSWFramework
https://twiki.cern.ch/twiki/bin/view/CMSPublic/WorkBookEdmInfoOnDataFile

The CMS data and MC can be fouded at the CMSDAS website: https://cmsweb.cern.ch/das/

To analyze this data we use CMSSW as shown in the next topic.

### CMSSW  <a name="cmssw"></a>
Setup CMSSW
```
cmsrel CMSSW_X_Y_Z
cd $CMSSW_BASE/src
cmsenv
```
cmsrel download an specific version of CMSSW (remember of linux architecture) 

To run a code locally you just need to run the python configuration file by using 
```
cmsRun conf_file.py
```
example: https://twiki.cern.ch/twiki/bin/view/CMSPublic/WorkBookWriteFrameworkModule

See information how to write your own code in the https://twiki.cern.ch/twiki/bin/view/CMSPublic/WorkBookWriteFrameworkModule

### CRAB3  <a name="crab3"></a>
For CRAB, we will access files that are not locally, for that you need a certificate:
```
voms-proxy-init -rfc -voms cms
```
The CRAB has it's own python configuration file that call the default python configuration file you use at cmsRun. In the crab configuration files included, the jobs are submitted using a python command (do not forget voms command)
```
crab submit crabfile.py
```
- Observation: in the crab configuration file you will include the path of the dataset at CMSDAS and this will overwrite the input dataset file in the local configuration file.

To check status of your jobs, you can just use ```crab status -d workArea/requestName/```, where workArea and requestName are folders generated automatically based on the name included in your crab configuration file. 

In addition, the status of the jobs can be checked in the GRAFANA interface (https://monit-grafana.cern.ch). The account is automatic created (takes 10 min) once you log in with your CERN account. 

To download the files you can use (be carefull if your files has large size)
```
crab getoutput workArea/requestName/
```
details here: https://twiki.cern.ch/twiki/bin/view/CMSPublic/SWGuideCrab

### rucio  <a name="rucio"></a>
If a dataset that you want to use is in TAPE only (which means it was deleted from Tier's HD's), you can use rucio to save it temporarily in your T2*. 
In that case you first need to call rucio libraries and certificate (you can also add the first two lines in the .bashrc)
```
source /cvmfs/cms.cern.ch/cmsset_default.sh
source /cvmfs/cms.cern.ch/rucio/setup-py3.sh
voms-proxy-init -rfc -voms cms
```
To add a dataset in the queue for TAPE to DISK tranfer you must use:
```
rucio add-rule --ask-approval cms:CSMSDAS_PATH 1 T2_MY_SITE --lifetime 2592000 (for 1 month for example)
```
where CSMSDAS_PATH is the path dataset from DAS, T2_MY_SITE is the T2 site that you can access and lifetime is the time that this sample will be available.
To check the status of the request, do:
```
rucio list-rules --account username
```
it will return something like:
```
ID          ACCOUNT    SCOPE:NAME       STATE[OK/REPL/STUCK]    RSE_EXPRESSION     COPIES    EXPIRES (UTC)        CREATED (UTC)
RULE_ID     usename   cms:/CMSDAS_PATH  REPLICATING[63/30/0]     T2_MY_SITE          1     YYYY-MM-DD HH:MM:SS  YYYY-MM-DD HH:MM:SS
```
if you use the example above (1 month) you will see the EXPIRES is 1 month ahead of CREATED.
To delete a rule, you can use:
```
rucio delete-rule RULE_ID
```

### XROOTD  <a name="xrootd"></a>
To access any files in different Tier's we ca use XROOTD, in that case you may use your certificate:
```
voms-proxy-init -rfc -voms cms
```
Files are copied to your local machine using xrdcp, example
```
xrdcp -d 1 -f root://cmsxrootd.fnal.gov//store/user/ahingraj/Dijet_pThat-15_pPb-Bst_8p16_Pythia8/HeavyIon_Forest_pPb_8p16TeV_pgoing_PYTHIA8_Unembedded_pthat15_out/220808_162221/0000/HiForestAOD_9.root . &> out.txt &
```

To access or find files and create a list of files you can use xrdfs, example:
```
xrdfs root://cmsxrootd.fnal.gov ls /store/user/ahingraj/Dijet_pThat-15_pPb-Bst_8p16_Pythia8/HeavyIon_Forest_pPb_8p16TeV_pgoing_PYTHIA8_Unembedded_pthat15_out/220808_162221/0000/ &> listofforestfiles.txt &
```

Look, the ```&``` symbol will allow your code to run on background (not showing in the screen, to check the if the job is running use the command ```jobs```.

### HIN Forest Framework  <a name="forest"></a>

As mentioned, the HIN Forest framework is composed by a bunch of EDAnalyzer's that runs different algorithms in order to produce one output file with different objects like jets, electrons and photons, tracks, muons, and so on. This has been used along the years in different analysis for all the colliding systems at CMS. The setup for HI Forest can be found in this twiki: https://twiki.cern.ch/twiki/bin/viewauth/CMS/HiForestSetup and the code in this github: https://github.com/CmsHI/cmssw . A tutorial for HI Forest (by Jussi) can be founded here: https://twiki.cern.ch/twiki/bin/view/CMS/HiForestTutorial . There you can find more information about the Forest code and details about each algorithm used for 2018 PbPb data. The structure of the forest code is similar for pp, pPb, XeXe and PbPb. In addition to this nice twiki, I have added some slides for 2016 pPb data with the output structure, see slides here: https://github.com/denerslemos/CMSSW_basic_instructions/blob/main/HIForest.pdf . You can download the file in the [XROOTD](#xrootd) section and play with it. Those objects are analysis related, and skims can be made depending on your need (see e.g. https://github.com/denerslemos/pPbskims). 

## CMS Talk and CMS Pub Talk <a name="cmstalk"></a>

Recently the CMS collaboration started to comunicate using CMS Talk (https://cms-talk.web.cern.ch) (for general: detectors, meetings, jobs, ...) and  CMS Pub Talk (https://cms-pub-talk.web.cern.ch/) (for analysis related updates) which is similar to a forum where people can interact. I made a set of slides with the some intructions that can be found here: https://github.com/denerslemos/CMSSW_basic_instructions/blob/main/cmstalk.pdf . Also, CMS uses Twiki's (https://twiki.org/cgi-bin/view/TWiki/TWikiUsersGuide) and Indico (https://indico.nucleares.unam.mx/ihelp/pdf/IndicoUserGuide.pdf) pages for meetings and presentations. In addition, Mattermost is a chat used for different groups in CMS to quick contact. To use it you just need to go to http://mattermost.web.cern.ch and log in with your CERN account. For additional information of invitation links, text/email me.

## CADI Intructions <a name="cadi"></a>

To publish a papers in CMS you will need to use the CMS Analysis Database Interface (CADI): https://cms.cern.ch/iCMS/analysisadmin/cadilines (called CADI lines). There you can find information for any analysis. Usually to open a CADI for you analysis you need to have a Analysis Note (AN) in a good shape (at least results and systematics) and approval for you PInG convener.

To create an AN, go to https://cms.cern.ch/iCMS/jsp/iCMS.jsp?mode=single&block=publications website and than select ```New note``` (or new thesis if you are using for thesis. NOTE that you will use My Pending are to update your AN (in that case only pdf file is needed). Once selected you will see a Publish note page, fill it with important information (usually Document Type is Analysis Note, our work group is ``` HIN - Heavy Ion Physics ``` and Document Category/Keyword is ``` Physics ```) and you can upload a dummy pdf file. Once done you need to ask someone to create a gitlab repository for this AN to edit the pdf/latex (see intructions here: https://twiki.cern.ch/twiki/bin/view/CMS/Internal/TdrProcessing). 

Once you AN is in a good shape you can ask the HIN conveners for CADI line and once you have HIN-XX-YYY you will create a gitlab folder and this must be done in the same way as the AN. The CADI lines will include all the information from the analysis including AN link, twiki page, CMS Pub Talk, pre-approval and approval talks and so on. However, in the CADI you will not upload the pdf, for that you must update the Physics Analysis Summary (PAS) or paper via CADI lines tool. In that case, you will ```switch to EDIT mode``` and go to PAS/PAPER actions and pull directly from gitlab (remember to have last version of .tex there with no compiling errors. The instructions to edit the .tex are in the section bellow.

In addition we have to add our results at HEPData (https://www.hepdata.net) before publication. There are some instructions here: 
https://agenda.infn.it/event/25088/contributions/127174/attachments/77898/100501/smueller_PrecisionSM2020_2.pdf
https://alice-publications.web.cern.ch/sites/default/files/documents/HOWTO_new_HEPData_authors_0.pdf

An example for HIN-20-003 (https://www.hepdata.net/record/ins2165920) can be found here: https://github.com/denerslemos/CMSSW_basic_instructions/blob/main/script_HEPDATA_HIN20003.py

## TDR <a name="tdr"></a>

In the CMS we use the TDR (see https://twiki.cern.ch/twiki/bin/view/CMS/Internal/TdrProcessing) to write the documentation of analysis or detector performance and so on. Here I write some intructions that I think it can help (assuming you are working at LXPLUS, but should also work at Linux or Mac OS).

Before go to command line instructions, you can edit you files directly in the gitlab in https://gitlab.cern.ch/tdr/papers/HIN-XX-YYY but you will not be able to compile. There is also a possibility to connect with Overleaf that looks interesting, but I have never tried. I will let the link for that here:
- https://twiki.cern.ch/twiki/bin/view/CMS/Internal/TdrOverleaf

Let us move to the terminal commands. For LXPLUS or CENTOS Linux users (not valid for all Linux or MAC, in that case, skip this step), you can use the recent version of git using
```
scl enable rh-git29 bash # this allows you to access a recent version of git. It will place you in a bash shell.
```

Next, download the folder using (assuming that you already setup the gitlab key as mentioned in the beginning of this intructions, if not go back to. ```Setup your LXPLUS area``` and do it)
```
git clone --recursive ssh://git@gitlab.cern.ch:7999/tdr/papers/HIN-XX-YYY.git
```

this example is for paper, check the one you have permission to write. The ```--recursive``` is important to download all the TDR tools. Than

```
ls
cd HIN-XX-YYY
```
inside of the folder you will see a file ```HIN-XX-YYY.tex``` that is the main file. In case of analysis note we usually add source files because it is a big document. However in the case of papers, everything must be in this ```HIN-XX-YYY.tex``` and figures in the same ```HIN-XX-YYY``` folder. This is mandatory in CMS and important to make diff versions (explained later).

Once you are on the folder you can compile and make the pdf using:
```
mkdir -p output
./utils/tdr --temp_dir="./output" --style=[paper|pas|an|note] b  # the local document with the name of the directory is the default build target
```
the pdf and log files will be save at HIN-XX-YYY/output folder.

Once you start to edit your files (.tex, sources, figures, ...) you can upload by:
```
git pull                            # always do a git pull before push to not overlap work from another people
git status                          # shows all changes to be done
git diff                            # shows all differences between 2 versions: before updates and after updates
git add .                           # add all files modified in current directory. "." means all, but you can select individual changes from status
git commit -m "add my new stuff"    # to stage your changes
git push                            # to send them back to the repo
```
once done you will update the gitlab folder. All this command should work in LXPLUS as well as in MAC or LINUX systems (never tried in Windows).

### Diff <a name="diff"></a>
As mentioned before, to make a diff (see twiki: https://twiki.cern.ch/twiki/bin/view/Main/TdrDiffInstr#For_GITLAB), all the files must be in the same folder (figures, .tex, .bib) and all the text in the main .tex. If this conditions are satisfied, you can make a diff by downloading the most recent version of the text (only tested at LXPLUS):
```
scl enable rh-git29 bash 
git clone --recursive ssh://git@gitlab.cern.ch:7999/tdr/papers/HIN-XX-YYY.git
cd HIN-XX-YYY
mkdir -p output
```
than follow this steps:

- edit: ```utils/general/cms-tdr.cls``` under the ```"\usepackage{ptdr-definitions}"```, put in the following two lines: 
```
\RequirePackage[normalem]{ulem} %DIF PREAMBLE
\RequirePackage{color}
```
- execute the command:
```
PATH=/cvmfs/cms.cern.ch/external/tex/texlive/2017/bin/x86_64-linux/:$PATH
```

- Find out the version you want to use as reference via ```git log HIN-XX-YYY.tex```
  - for example you want to compare the current version with version b174241c04ff018b67e600b4d3acde00816c3c0b
    - b174241c04ff018b67e600b4d3acde00816c3c0b is the commit number 
    - can also be found at gitlab (https://gitlab.cern.ch/tdr/papers/HIN-XX-YYY/-/commits/master/)
    
- Run: ```latexdiff-vc -r b174241c04ff018b67e600b4d3acde00816c3c0b --append-context2cmd="abstract" HIN-XX-YYY.tex```
  - this will create a texft file: HIN-XX-YYY-diffb174241c04ff018b67e600b4d3acde00816c3c0b.tex (HIN-XX-XXX.tex-referenceVersion.tex)
  
- manually add the following line into this newly created tex file (HIN-XX-YYY-diffb174241c04ff018b67e600b4d3acde00816c3c0b.tex):
```
\definecolor{RED}{rgb}{1,0,0}\definecolor{BLUE}{rgb}{0,0,1} %DIF PREAMBLE
\providecommand{\DIFadd}[1]{{\protect\color{blue}\uwave{#1}}} %DIF PREAMBLE
\providecommand{\DIFdel}[1]{{\protect\color{red}\sout{#1}}} %DIF PREAMBLE
%DIF SAFE PREAMBLE %DIF PREAMBLE
\providecommand{\DIFaddbegin}{} %DIF PREAMBLE
\providecommand{\DIFaddend}{} %DIF PREAMBLE
\providecommand{\DIFdelbegin}{} %DIF PREAMBLE
\providecommand{\DIFdelend}{} %DIF PREAMBLE
%DIF FLOATSAFE PREAMBLE %DIF PREAMBLE
\providecommand{\DIFaddFL}[1]{\DIFadd{#1}} %DIF PREAMBLE
\providecommand{\DIFdelFL}[1]{\DIFdel{#1}} %DIF PREAMBLE
\providecommand{\DIFaddbeginFL}{} %DIF PREAMBLE
\providecommand{\DIFaddendFL}{} %DIF PREAMBLE
\providecommand{\DIFdelbeginFL}{} %DIF PREAMBLE
\providecommand{\DIFdelendFL}{} %DIF PREAMBLE
```
- Compile again, to create the colorful diff: ```./utils/tdr --temp_dir="./output" b HIN-XX-YYY-diffb174241c04ff018b67e600b4d3acde00816c3c0b.tex```
  - The diff file will be created on output folder, but look carefully in the spit-out on the screed to see the location of the pdf file. 
