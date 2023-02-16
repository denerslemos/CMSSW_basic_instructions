#! /cvmfs/sft.cern.ch/lcg/views/LCG_101swan/x86_64-centos7-gcc10-opt/bin/python3

from __future__ import print_function
from hepdata_lib import Submission
from hepdata_lib import Variable
from hepdata_lib import Table
from hepdata_lib import Uncertainty
from hepdata_lib import RootFileReader
import numpy as np

###Prepare submission to have all information

submission = Submission()
submission.read_abstract("abstract.txt")
##NEED TO ADD IN THE FUTURE
#submission.add_link("arXiv", "https://arxiv.org/abs/XXXX.XXXXX")
#submission.add_link("Webpage with all figures and tables", "http://cms-results.web.cern.ch/cms-results/public-results/publications/HIN-20-003/")
#submission.add_record_id(XXXXXXX, "inspire")

#Read file with TGraphs
reader_fig = RootFileReader("output_graphs.root")

#Read figures (Top panel)
#TGraphs with statistical uncertainties 
graphs_figtop_statunc = ["Figure1_jetshape_pp_inclusive",
                         "Figure1_jetshape_pp_bjet",
                         "Figure1a_jetshape_PbPb_3090_inclusive",
                         "Figure1a_jetshape_PbPb_3090_bjet",
                         "Figure1b_jetshape_PbPb_1030_inclusive",
                         "Figure1b_jetshape_PbPb_1030_bjet",
                         "Figure1c_jetshape_PbPb_010_inclusive",
                         "Figure1c_jetshape_PbPb_010_bjet"]
#TGraphs with systematical uncertainties
graphs_figtop_systunc = ["Figure1_jetshape_pp_inclusive_syst",
                         "Figure1_jetshape_pp_bjet_syst",
                         "Figure1a_jetshape_PbPb_3090_inclusive_syst",
                         "Figure1a_jetshape_PbPb_3090_bjet_syst",
                         "Figure1b_jetshape_PbPb_1030_inclusive_syst",
                         "Figure1b_jetshape_PbPb_1030_bjet_syst",
                         "Figure1c_jetshape_PbPb_010_inclusive_syst",
                         "Figure1c_jetshape_PbPb_010_bjet_syst"]


####Common Labels
description_cent = ["30-90%","10-30%","0-10%"]
xaxises_fig = ["$\Delta r$"] #x-axis label (as a vector for future usage)
labels_fig = ["Figure 1a","Figure 1b","Figure 1c","Figure 1d","Figure 1e","Figure 1f","Figure 1g","Figure 1h","Figure 1i","Figure 1j","Figure 1k","Figure 1l"]
descriptions_fig = ["Jet shapes, $\rho(\Delta r)$, for inclusive and b jets as function of $\Delta r$ from pp and PbPb collisions at $\sqrt{s_{\mathrm{NN}}} = 5.02$ TeV.",
                    "Jet shape ratios (\rho(\Delta r)_{\mathrm{PbPb}}/\rho(\Delta r)_{\mathrm{pp}}) for inclusive and b jets as function of $\Delta r$ at $\sqrt{s_{\mathrm{NN}}} = 5.02$ TeV.",
                    "Transverse momentum profile difference, (P(\Delta r)_{\mathrm{PbPb}}-P(\Delta r)_{\mathrm{pp}}), for inclusive and b jets as function of $\Delta r$ at $\sqrt{s_{\mathrm{NN}}} = 5.02$ TeV.",
                    "Jet shape ratios (\rho(\Delta r)_{\mathrm{b}}/\rho(\Delta r)_{\mathrm{incl.}}) as function of $\Delta r$ from pp and PbPb collisions at $\sqrt{s_{\mathrm{NN}}} = 5.02$ TeV."]

#yaxises_fig = ["$\rho(\Delta r) - pp $","$\rho(\Delta r)_{\mathrm{PbPb}}/#rho(\Delta r)_{\mathrm{pp}}$","$P(\Delta r)_{\mathrm{PbPb}} - P(\Delta r)_{\mathrm{pp}}$","#rho(\Delta r)_{\mathrm{b}}/#rho(\Delta r)_{\mathrm{incl.}}$"]

#start plots
#Upper panel
yaxises_fig_top = ["$\rho(\Delta r) - pp - inclusive jets$","$\rho(\Delta r) - pp - b jets$","$\rho(\Delta r) - PbPb - inclusive jets$","$\rho(\Delta r) - PbPb - b jets$"]
locations_figtop = ["Data from Figure 1 (upper left panel) - blue filled circles for b jets in PbPb collisions, blue open circles for b jets in pp collisions, red filled circles for inclusive jets in PbPb collisions, red open circles for incluse jets in pp collisions.", 
                    "Data from Figure 1 (upper middle panel) - blue filled circles for b jets in PbPb collisions, blue open circles for b jets in pp collisions, red filled circles for inclusive jets in PbPb collisions, red open circles for incluse jets in pp collisions.",
                    "Data from Figure 1 (upper right panel) - blue filled circles for b jets in PbPb collisions, blue open circles for b jets in pp collisions, red filled circles for inclusive jets in PbPb collisions, red open circles for incluse jets in pp collisions."]


#Start table/plots

#call TGraphs
data_fig_1_statunc = reader_fig.read_graph(graphs_figtop_statunc[0])
data_fig_1_systunc = reader_fig.read_graph(graphs_figtop_systunc[0])

#Define x-axis (commom for all plots)
x_fig_1 = Variable(xaxises_fig[0], is_independent=True, is_binned=False, units="")
x_fig_1.digits = 5
x_fig_1.values = data_fig_1_statunc["x"]
# to add uncertaintities we need to do is_independent=Fase
#uncx_fig_1_stat = Uncertainty("stat", is_symmetric=True)
#uncx_fig_1_stat.values = data_fig_1_statunc["dx"]
#x_fig_1.add_uncertainty(uncx_fig_1_stat)

#Figure 1 - upper left panel

#pp

table_1 = Table(labels_fig[0])
table_1.description = descriptions_fig[0]
table_1.location = locations_figtop[0]

#Add y-axis values (incluse pp plot --> commom for all plots in top panel)
y_fig_1_pp_incl_upleft = Variable(yaxises_fig_top[0], is_independent=False, is_binned=False, units="")
y_fig_1_pp_incl_upleft.digits = 5
y_fig_1_pp_incl_upleft.values = data_fig_1_statunc["y"]
y_fig_1_pp_incl_upleft.add_qualifier("Centrality range",description_cent[0])
y_fig_1_pp_incl_upleft.add_qualifier("anti-kt Jets ($R = 0.4$): ","$|\eta| < 1.6$; $p_{T} > 120~GeV$")
y_fig_1_pp_incl_upleft.add_qualifier("Tracks: ","$|\eta| < 2.4$; $p_{T} > 1~GeV$")
y_fig_1_pp_incl_upleft.add_qualifier("SQRT(S)/NUCLEON","$5020.0~GeV$")
unc_fig_1_pp_incl_upleft_stat = Uncertainty("stat", is_symmetric=True)
unc_fig_1_pp_incl_upleft_stat.values = data_fig_1_statunc["dy"]
unc_fig_1_pp_incl_upleft_syst = Uncertainty("sys", is_symmetric=True)
unc_fig_1_pp_incl_upleft_syst.values = data_fig_1_systunc["dy"]
y_fig_1_pp_incl_upleft.add_uncertainty(unc_fig_1_pp_incl_upleft_stat)
y_fig_1_pp_incl_upleft.add_uncertainty(unc_fig_1_pp_incl_upleft_syst)

#Add y-axis values (incluse pp plot --> commom for all plots in top panel)
data_fig_1_statunc = reader_fig.read_graph(graphs_figtop_statunc[1])
data_fig_1_systunc = reader_fig.read_graph(graphs_figtop_systunc[1])

y_fig_1_pp_bjet_upleft = Variable(yaxises_fig_top[1], is_independent=False, is_binned=False, units="")
y_fig_1_pp_bjet_upleft.digits = 5
y_fig_1_pp_bjet_upleft.values = data_fig_1_statunc["y"]
y_fig_1_pp_bjet_upleft.add_qualifier("RE","Pb Pb --> Jets + X")
y_fig_1_pp_bjet_upleft.add_qualifier("Centrality range",description_cent[0])
y_fig_1_pp_bjet_upleft.add_qualifier("anti-kt Jets ($R = 0.4$): ","$|\eta| < 1.6$; $p_{T} > 120~GeV$")
y_fig_1_pp_bjet_upleft.add_qualifier("Tracks: ","$|\eta| < 2.4$; $p_{T} > 1~GeV$")
y_fig_1_pp_bjet_upleft.add_qualifier("SQRT(S)/NUCLEON","$5020.0~GeV$")
unc_fig_1_pp_bjet_upleft_stat = Uncertainty("stat", is_symmetric=True)
unc_fig_1_pp_bjet_upleft_stat.values = data_fig_1_statunc["dy"]
unc_fig_1_pp_bjet_upleft_syst = Uncertainty("sys", is_symmetric=True)
unc_fig_1_pp_bjet_upleft_syst.values = data_fig_1_systunc["dy"]
y_fig_1_pp_bjet_upleft.add_uncertainty(unc_fig_1_pp_bjet_upleft_stat)
y_fig_1_pp_bjet_upleft.add_uncertainty(unc_fig_1_pp_bjet_upleft_syst)

#Upper left panel: Jet shapes for 30-90% 
data_fig_1_statunc = reader_fig.read_graph(graphs_figtop_statunc[2])
data_fig_1_systunc = reader_fig.read_graph(graphs_figtop_systunc[2])

y_fig_1_PbPb3090_incl_upleft = Variable(yaxises_fig_top[2], is_independent=False, is_binned=False, units="")
y_fig_1_PbPb3090_incl_upleft.digits = 5
y_fig_1_PbPb3090_incl_upleft.values = data_fig_1_statunc["y"]
y_fig_1_PbPb3090_incl_upleft.add_qualifier("Centrality range",description_cent[0])
y_fig_1_PbPb3090_incl_upleft.add_qualifier("anti-kt Jets ($R = 0.4$): ","$|\eta| < 1.6$; $p_{T} > 120~GeV$")
y_fig_1_PbPb3090_incl_upleft.add_qualifier("Tracks: ","$|\eta| < 2.4$; $p_{T} > 1~GeV$")
y_fig_1_PbPb3090_incl_upleft.add_qualifier("SQRT(S)/NUCLEON","$5020.0~GeV$")
unc_fig_1_PbPb3090_incl_upleft_stat = Uncertainty("stat", is_symmetric=True)
unc_fig_1_PbPb3090_incl_upleft_stat.values = data_fig_1_statunc["dy"]
unc_fig_1_PbPb3090_incl_upleft_syst = Uncertainty("sys", is_symmetric=True)
unc_fig_1_PbPb3090_incl_upleft_syst.values = data_fig_1_systunc["dy"]
y_fig_1_PbPb3090_incl_upleft.add_uncertainty(unc_fig_1_PbPb3090_incl_upleft_stat)
y_fig_1_PbPb3090_incl_upleft.add_uncertainty(unc_fig_1_PbPb3090_incl_upleft_syst)

#Add y-axis values (incluse pp plot --> commom for all plots in top panel)
data_fig_1_statunc = reader_fig.read_graph(graphs_figtop_statunc[3])
data_fig_1_systunc = reader_fig.read_graph(graphs_figtop_systunc[3])

y_fig_1_PbPb3090_bjet_upleft = Variable(yaxises_fig_top[3], is_independent=False, is_binned=False, units="")
y_fig_1_PbPb3090_bjet_upleft.digits = 5
y_fig_1_PbPb3090_bjet_upleft.values = data_fig_1_statunc["y"]
y_fig_1_PbPb3090_bjet_upleft.add_qualifier("Centrality range",description_cent[0])
y_fig_1_PbPb3090_bjet_upleft.add_qualifier("anti-kt Jets ($R = 0.4$): ","$|\eta| < 1.6$; $p_{T} > 120~GeV$")
y_fig_1_PbPb3090_bjet_upleft.add_qualifier("Tracks: ","$|\eta| < 2.4$; $p_{T} > 1~GeV$")
y_fig_1_PbPb3090_bjet_upleft.add_qualifier("SQRT(S)/NUCLEON","$5020.0~GeV$")
unc_fig_1_PbPb3090_bjet_upleft_stat = Uncertainty("stat", is_symmetric=True)
unc_fig_1_PbPb3090_bjet_upleft_stat.values = data_fig_1_statunc["dy"]
unc_fig_1_PbPb3090_bjet_upleft_syst = Uncertainty("sys", is_symmetric=True)
unc_fig_1_PbPb3090_bjet_upleft_syst.values = data_fig_1_systunc["dy"]
y_fig_1_PbPb3090_bjet_upleft.add_uncertainty(unc_fig_1_PbPb3090_bjet_upleft_stat)
y_fig_1_PbPb3090_bjet_upleft.add_uncertainty(unc_fig_1_PbPb3090_bjet_upleft_syst)

#make the tables

table_1.add_variable(x_fig_1)
table_1.add_variable(y_fig_1_pp_incl_upleft)
table_1.add_variable(y_fig_1_pp_bjet_upleft)
table_1.add_variable(y_fig_1_PbPb3090_incl_upleft)
table_1.add_variable(y_fig_1_PbPb3090_bjet_upleft)


#Figure 1 - upper middle panel


#pp

table_2 = Table(labels_fig[1])
table_2.description = descriptions_fig[0]
table_2.location = locations_figtop[1]

#call TGraphs
data_fig_1_statunc = reader_fig.read_graph(graphs_figtop_statunc[0])
data_fig_1_systunc = reader_fig.read_graph(graphs_figtop_systunc[0])


#Add y-axis values (incluse pp plot --> commom for all plots in top panel)
y_fig_1_pp_incl_upmidd = Variable(yaxises_fig_top[0], is_independent=False, is_binned=False, units="")
y_fig_1_pp_incl_upmidd.digits = 5
y_fig_1_pp_incl_upmidd.values = data_fig_1_statunc["y"]
y_fig_1_pp_incl_upmidd.add_qualifier("Centrality range",description_cent[1])
y_fig_1_pp_incl_upmidd.add_qualifier("anti-kt Jets ($R = 0.4$): ","$|\eta| < 1.6$; $p_{T} > 120~GeV$")
y_fig_1_pp_incl_upmidd.add_qualifier("Tracks: ","$|\eta| < 2.4$; $p_{T} > 1~GeV$")
y_fig_1_pp_incl_upmidd.add_qualifier("SQRT(S)/NUCLEON","$5020.0~GeV$")
unc_fig_1_pp_incl_upmidd_stat = Uncertainty("stat", is_symmetric=True)
unc_fig_1_pp_incl_upmidd_stat.values = data_fig_1_statunc["dy"]
unc_fig_1_pp_incl_upmidd_syst = Uncertainty("sys", is_symmetric=True)
unc_fig_1_pp_incl_upmidd_syst.values = data_fig_1_systunc["dy"]
y_fig_1_pp_incl_upmidd.add_uncertainty(unc_fig_1_pp_incl_upmidd_stat)
y_fig_1_pp_incl_upmidd.add_uncertainty(unc_fig_1_pp_incl_upmidd_syst)

#Add y-axis values (incluse pp plot --> commom for all plots in top panel)
data_fig_1_statunc = reader_fig.read_graph(graphs_figtop_statunc[1])
data_fig_1_systunc = reader_fig.read_graph(graphs_figtop_systunc[1])

y_fig_1_pp_bjet_upmidd = Variable(yaxises_fig_top[1], is_independent=False, is_binned=False, units="")
y_fig_1_pp_bjet_upmidd.digits = 5
y_fig_1_pp_bjet_upmidd.values = data_fig_1_statunc["y"]
y_fig_1_pp_bjet_upmidd.add_qualifier("RE","Pb Pb --> Jets + X")
y_fig_1_pp_bjet_upmidd.add_qualifier("Centrality range",description_cent[1])
y_fig_1_pp_bjet_upmidd.add_qualifier("anti-kt Jets ($R = 0.4$): ","$|\eta| < 1.6$; $p_{T} > 120~GeV$")
y_fig_1_pp_bjet_upmidd.add_qualifier("Tracks: ","$|\eta| < 2.4$; $p_{T} > 1~GeV$")
y_fig_1_pp_bjet_upmidd.add_qualifier("SQRT(S)/NUCLEON","$5020.0~GeV$")
unc_fig_1_pp_bjet_upmidd_stat = Uncertainty("stat", is_symmetric=True)
unc_fig_1_pp_bjet_upmidd_stat.values = data_fig_1_statunc["dy"]
unc_fig_1_pp_bjet_upmidd_syst = Uncertainty("sys", is_symmetric=True)
unc_fig_1_pp_bjet_upmidd_syst.values = data_fig_1_systunc["dy"]
y_fig_1_pp_bjet_upmidd.add_uncertainty(unc_fig_1_pp_bjet_upmidd_stat)
y_fig_1_pp_bjet_upmidd.add_uncertainty(unc_fig_1_pp_bjet_upmidd_syst)

#Upper left panel: Jet shapes for 30-90% 
data_fig_1_statunc = reader_fig.read_graph(graphs_figtop_statunc[4])
data_fig_1_systunc = reader_fig.read_graph(graphs_figtop_systunc[4])

y_fig_1_PbPb1030_incl_upmidd = Variable(yaxises_fig_top[2], is_independent=False, is_binned=False, units="")
y_fig_1_PbPb1030_incl_upmidd.digits = 5
y_fig_1_PbPb1030_incl_upmidd.values = data_fig_1_statunc["y"]
y_fig_1_PbPb1030_incl_upmidd.add_qualifier("Centrality range",description_cent[1])
y_fig_1_PbPb1030_incl_upmidd.add_qualifier("anti-kt Jets ($R = 0.4$): ","$|\eta| < 1.6$; $p_{T} > 120~GeV$")
y_fig_1_PbPb1030_incl_upmidd.add_qualifier("Tracks: ","$|\eta| < 2.4$; $p_{T} > 1~GeV$")
y_fig_1_PbPb1030_incl_upmidd.add_qualifier("SQRT(S)/NUCLEON","$5020.0~GeV$")
unc_fig_1_PbPb1030_incl_upmidd_stat = Uncertainty("stat", is_symmetric=True)
unc_fig_1_PbPb1030_incl_upmidd_stat.values = data_fig_1_statunc["dy"]
unc_fig_1_PbPb1030_incl_upmidd_syst = Uncertainty("sys", is_symmetric=True)
unc_fig_1_PbPb1030_incl_upmidd_syst.values = data_fig_1_systunc["dy"]
y_fig_1_PbPb1030_incl_upmidd.add_uncertainty(unc_fig_1_PbPb1030_incl_upmidd_stat)
y_fig_1_PbPb1030_incl_upmidd.add_uncertainty(unc_fig_1_PbPb1030_incl_upmidd_syst)

#Add y-axis values (incluse pp plot --> commom for all plots in top panel)
data_fig_1_statunc = reader_fig.read_graph(graphs_figtop_statunc[5])
data_fig_1_systunc = reader_fig.read_graph(graphs_figtop_systunc[5])

y_fig_1_PbPb1030_bjet_upmidd = Variable(yaxises_fig_top[3], is_independent=False, is_binned=False, units="")
y_fig_1_PbPb1030_bjet_upmidd.digits = 5
y_fig_1_PbPb1030_bjet_upmidd.values = data_fig_1_statunc["y"]
y_fig_1_PbPb1030_bjet_upmidd.add_qualifier("Centrality range",description_cent[1])
y_fig_1_PbPb1030_bjet_upmidd.add_qualifier("anti-kt Jets ($R = 0.4$): ","$|\eta| < 1.6$; $p_{T} > 120~GeV$")
y_fig_1_PbPb1030_bjet_upmidd.add_qualifier("Tracks: ","$|\eta| < 2.4$; $p_{T} > 1~GeV$")
y_fig_1_PbPb1030_bjet_upmidd.add_qualifier("SQRT(S)/NUCLEON","$5020.0~GeV$")
unc_fig_1_PbPb1030_bjet_upmidd_stat = Uncertainty("stat", is_symmetric=True)
unc_fig_1_PbPb1030_bjet_upmidd_stat.values = data_fig_1_statunc["dy"]
unc_fig_1_PbPb1030_bjet_upmidd_syst = Uncertainty("sys", is_symmetric=True)
unc_fig_1_PbPb1030_bjet_upmidd_syst.values = data_fig_1_systunc["dy"]
y_fig_1_PbPb1030_bjet_upmidd.add_uncertainty(unc_fig_1_PbPb1030_bjet_upmidd_stat)
y_fig_1_PbPb1030_bjet_upmidd.add_uncertainty(unc_fig_1_PbPb1030_bjet_upmidd_syst)

#make the tables

table_2.add_variable(x_fig_1)
table_2.add_variable(y_fig_1_pp_incl_upmidd)
table_2.add_variable(y_fig_1_pp_bjet_upmidd)
table_2.add_variable(y_fig_1_PbPb1030_incl_upmidd)
table_2.add_variable(y_fig_1_PbPb1030_bjet_upmidd)


#Figure 1 - upper right panel

#pp

table_3 = Table(labels_fig[2])
table_3.description = descriptions_fig[0]
table_3.location = locations_figtop[2]

#call TGraphs
data_fig_1_statunc = reader_fig.read_graph(graphs_figtop_statunc[0])
data_fig_1_systunc = reader_fig.read_graph(graphs_figtop_systunc[0])


#Add y-axis values (incluse pp plot --> commom for all plots in top panel)
y_fig_1_pp_incl_uprigh = Variable(yaxises_fig_top[0], is_independent=False, is_binned=False, units="")
y_fig_1_pp_incl_uprigh.digits = 5
y_fig_1_pp_incl_uprigh.values = data_fig_1_statunc["y"]
y_fig_1_pp_incl_uprigh.add_qualifier("Centrality range",description_cent[2])
y_fig_1_pp_incl_uprigh.add_qualifier("anti-kt Jets ($R = 0.4$): ","$|\eta| < 1.6$; $p_{T} > 120~GeV$")
y_fig_1_pp_incl_uprigh.add_qualifier("Tracks: ","$|\eta| < 2.4$; $p_{T} > 1~GeV$")
y_fig_1_pp_incl_uprigh.add_qualifier("SQRT(S)/NUCLEON","$5020.0~GeV$")
unc_fig_1_pp_incl_uprigh_stat = Uncertainty("stat", is_symmetric=True)
unc_fig_1_pp_incl_uprigh_stat.values = data_fig_1_statunc["dy"]
unc_fig_1_pp_incl_uprigh_syst = Uncertainty("sys", is_symmetric=True)
unc_fig_1_pp_incl_uprigh_syst.values = data_fig_1_systunc["dy"]
y_fig_1_pp_incl_uprigh.add_uncertainty(unc_fig_1_pp_incl_uprigh_stat)
y_fig_1_pp_incl_uprigh.add_uncertainty(unc_fig_1_pp_incl_uprigh_syst)

#Add y-axis values (incluse pp plot --> commom for all plots in top panel)
data_fig_1_statunc = reader_fig.read_graph(graphs_figtop_statunc[1])
data_fig_1_systunc = reader_fig.read_graph(graphs_figtop_systunc[1])

y_fig_1_pp_bjet_uprigh = Variable(yaxises_fig_top[1], is_independent=False, is_binned=False, units="")
y_fig_1_pp_bjet_uprigh.digits = 5
y_fig_1_pp_bjet_uprigh.values = data_fig_1_statunc["y"]
y_fig_1_pp_bjet_uprigh.add_qualifier("RE","Pb Pb --> Jets + X")
y_fig_1_pp_bjet_uprigh.add_qualifier("Centrality range",description_cent[2])
y_fig_1_pp_bjet_uprigh.add_qualifier("anti-kt Jets ($R = 0.4$): ","$|\eta| < 1.6$; $p_{T} > 120~GeV$")
y_fig_1_pp_bjet_uprigh.add_qualifier("Tracks: ","$|\eta| < 2.4$; $p_{T} > 1~GeV$")
y_fig_1_pp_bjet_uprigh.add_qualifier("SQRT(S)/NUCLEON","$5020.0~GeV$")
unc_fig_1_pp_bjet_uprigh_stat = Uncertainty("stat", is_symmetric=True)
unc_fig_1_pp_bjet_uprigh_stat.values = data_fig_1_statunc["dy"]
unc_fig_1_pp_bjet_uprigh_syst = Uncertainty("sys", is_symmetric=True)
unc_fig_1_pp_bjet_uprigh_syst.values = data_fig_1_systunc["dy"]
y_fig_1_pp_bjet_uprigh.add_uncertainty(unc_fig_1_pp_bjet_uprigh_stat)
y_fig_1_pp_bjet_uprigh.add_uncertainty(unc_fig_1_pp_bjet_uprigh_syst)

#Upper left panel: Jet shapes for 30-90% 
data_fig_1_statunc = reader_fig.read_graph(graphs_figtop_statunc[6])
data_fig_1_systunc = reader_fig.read_graph(graphs_figtop_systunc[6])

y_fig_1_PbPb010_incl_uprigh = Variable(yaxises_fig_top[2], is_independent=False, is_binned=False, units="")
y_fig_1_PbPb010_incl_uprigh.digits = 5
y_fig_1_PbPb010_incl_uprigh.values = data_fig_1_statunc["y"]
y_fig_1_PbPb010_incl_uprigh.add_qualifier("Centrality range",description_cent[2])
y_fig_1_PbPb010_incl_uprigh.add_qualifier("anti-kt Jets ($R = 0.4$): ","$|\eta| < 1.6$; $p_{T} > 120~GeV$")
y_fig_1_PbPb010_incl_uprigh.add_qualifier("Tracks: ","$|\eta| < 2.4$; $p_{T} > 1~GeV$")
y_fig_1_PbPb010_incl_uprigh.add_qualifier("SQRT(S)/NUCLEON","$5020.0~GeV$")
unc_fig_1_PbPb010_incl_uprigh_stat = Uncertainty("stat", is_symmetric=True)
unc_fig_1_PbPb010_incl_uprigh_stat.values = data_fig_1_statunc["dy"]
unc_fig_1_PbPb010_incl_uprigh_syst = Uncertainty("sys", is_symmetric=True)
unc_fig_1_PbPb010_incl_uprigh_syst.values = data_fig_1_systunc["dy"]
y_fig_1_PbPb010_incl_uprigh.add_uncertainty(unc_fig_1_PbPb010_incl_uprigh_stat)
y_fig_1_PbPb010_incl_uprigh.add_uncertainty(unc_fig_1_PbPb010_incl_uprigh_syst)

#Add y-axis values (incluse pp plot --> commom for all plots in top panel)
data_fig_1_statunc = reader_fig.read_graph(graphs_figtop_statunc[7])
data_fig_1_systunc = reader_fig.read_graph(graphs_figtop_systunc[7])

y_fig_1_PbPb010_bjet_uprigh = Variable(yaxises_fig_top[3], is_independent=False, is_binned=False, units="")
y_fig_1_PbPb010_bjet_uprigh.digits = 5
y_fig_1_PbPb010_bjet_uprigh.values = data_fig_1_statunc["y"]
y_fig_1_PbPb010_bjet_uprigh.add_qualifier("Centrality range",description_cent[2])
y_fig_1_PbPb010_bjet_uprigh.add_qualifier("anti-kt Jets ($R = 0.4$): ","$|\eta| < 1.6$; $p_{T} > 120~GeV$")
y_fig_1_PbPb010_bjet_uprigh.add_qualifier("Tracks: ","$|\eta| < 2.4$; $p_{T} > 1~GeV$")
y_fig_1_PbPb010_bjet_uprigh.add_qualifier("SQRT(S)/NUCLEON","$5020.0~GeV$")
unc_fig_1_PbPb010_bjet_uprigh_stat = Uncertainty("stat", is_symmetric=True)
unc_fig_1_PbPb010_bjet_uprigh_stat.values = data_fig_1_statunc["dy"]
unc_fig_1_PbPb010_bjet_uprigh_syst = Uncertainty("sys", is_symmetric=True)
unc_fig_1_PbPb010_bjet_uprigh_syst.values = data_fig_1_systunc["dy"]
y_fig_1_PbPb010_bjet_uprigh.add_uncertainty(unc_fig_1_PbPb010_bjet_uprigh_stat)
y_fig_1_PbPb010_bjet_uprigh.add_uncertainty(unc_fig_1_PbPb010_bjet_uprigh_syst)

#make the tables

table_3.add_variable(x_fig_1)
table_3.add_variable(y_fig_1_pp_incl_uprigh)
table_3.add_variable(y_fig_1_pp_bjet_uprigh)
table_3.add_variable(y_fig_1_PbPb010_incl_uprigh)
table_3.add_variable(y_fig_1_PbPb010_bjet_uprigh)

#Read figures (top-middle panel)
#TGraphs with statistical uncertainties 
graphs_figtopmid_statunc = ["Figure1a_ratio_jetshape_PbPb_to_pp_3090_inclusive",
                         "Figure1a_ratio_jetshape_PbPb_to_pp_3090_bjet",
                         "Figure1a_ratio_jetshape_PbPb_to_pp_1030_inclusive",
                         "Figure1a_ratio_jetshape_PbPb_to_pp_1030_bjet",
                         "Figure1a_ratio_jetshape_PbPb_to_pp_010_inclusive",
                         "Figure1a_ratio_jetshape_PbPb_to_pp_010_bjet"]
#TGraphs with systematical uncertainties
graphs_figtopmid_systunc = ["Figure1a_ratio_jetshape_PbPb_to_pp_3090_inclusive_syst",
                         "Figure1a_ratio_jetshape_PbPb_to_pp_3090_bjet_syst",
                         "Figure1a_ratio_jetshape_PbPb_to_pp_1030_inclusive_syst",
                         "Figure1a_ratio_jetshape_PbPb_to_pp_1030_bjet_syst",
                         "Figure1a_ratio_jetshape_PbPb_to_pp_010_inclusive_syst",
                         "Figure1a_ratio_jetshape_PbPb_to_pp_010_bjet_syst"]

#Figure 1 - upper-middle left panel
#Upper panel
yaxises_fig_topmid = ["$\rho(\Delta r)_{\mathrm{PbPb}}/$\rho(\Delta r)_{\mathrm{pp}} - inclusive jets$","$\rho(\Delta r)_{\mathrm{PbPb}}/$\rho(\Delta r)_{\mathrm{pp}} - b jets$"]
locations_figtopmid = ["Data from Figure 1 (upper-middle left panel) - blue filled circles for b jets (PbPb/pp), red open squares for incluse jets (PbPb/pp).", 
                       "Data from Figure 1 (upper-middle middle panel) - blue filled circles for b jets (PbPb/pp), red open squares for incluse jets (PbPb/pp).",
                       "Data from Figure 1 (upper-middle right panel) - blue filled circles for b jets (PbPb/pp), red open squares for incluse jets (PbPb/pp)."]


table_4 = Table(labels_fig[3])
table_4.description = descriptions_fig[1]
table_4.location = locations_figtopmid[0]

#Upper left panel: Jet shapes for 30-90% 
data_fig_1a_statunc = reader_fig.read_graph(graphs_figtopmid_statunc[0])
data_fig_1a_systunc = reader_fig.read_graph(graphs_figtopmid_systunc[0])

y_fig_1_PbPb3090_incl_upmidleft = Variable(yaxises_fig_topmid[0], is_independent=False, is_binned=False, units="")
y_fig_1_PbPb3090_incl_upmidleft.digits = 5
y_fig_1_PbPb3090_incl_upmidleft.values = data_fig_1a_statunc["y"]
y_fig_1_PbPb3090_incl_upmidleft.add_qualifier("Centrality range",description_cent[0])
y_fig_1_PbPb3090_incl_upmidleft.add_qualifier("anti-kt Jets ($R = 0.4$): ","$|\eta| < 1.6$; $p_{T} > 120~GeV$")
y_fig_1_PbPb3090_incl_upmidleft.add_qualifier("Tracks: ","$|\eta| < 2.4$; $p_{T} > 1~GeV$")
y_fig_1_PbPb3090_incl_upmidleft.add_qualifier("SQRT(S)/NUCLEON","$5020.0~GeV$")
unc_fig_1_PbPb3090_incl_upmidleft_stat = Uncertainty("stat", is_symmetric=True)
unc_fig_1_PbPb3090_incl_upmidleft_stat.values = data_fig_1a_statunc["dy"]
unc_fig_1_PbPb3090_incl_upmidleft_syst = Uncertainty("sys", is_symmetric=True)
unc_fig_1_PbPb3090_incl_upmidleft_syst.values = data_fig_1a_systunc["dy"]
y_fig_1_PbPb3090_incl_upmidleft.add_uncertainty(unc_fig_1_PbPb3090_incl_upmidleft_stat)
y_fig_1_PbPb3090_incl_upmidleft.add_uncertainty(unc_fig_1_PbPb3090_incl_upmidleft_syst)

data_fig_1a_statunc = reader_fig.read_graph(graphs_figtopmid_statunc[1])
data_fig_1a_systunc = reader_fig.read_graph(graphs_figtopmid_systunc[1])

y_fig_1_PbPb3090_bjet_upmidleft = Variable(yaxises_fig_topmid[1], is_independent=False, is_binned=False, units="")
y_fig_1_PbPb3090_bjet_upmidleft.digits = 5
y_fig_1_PbPb3090_bjet_upmidleft.values = data_fig_1a_statunc["y"]
y_fig_1_PbPb3090_bjet_upmidleft.add_qualifier("Centrality range",description_cent[0])
y_fig_1_PbPb3090_bjet_upmidleft.add_qualifier("anti-kt Jets ($R = 0.4$): ","$|\eta| < 1.6$; $p_{T} > 120~GeV$")
y_fig_1_PbPb3090_bjet_upmidleft.add_qualifier("Tracks: ","$|\eta| < 2.4$; $p_{T} > 1~GeV$")
y_fig_1_PbPb3090_bjet_upmidleft.add_qualifier("SQRT(S)/NUCLEON","$5020.0~GeV$")
unc_fig_1_PbPb3090_bjet_upmidleft_stat = Uncertainty("stat", is_symmetric=True)
unc_fig_1_PbPb3090_bjet_upmidleft_stat.values = data_fig_1a_statunc["dy"]
unc_fig_1_PbPb3090_bjet_upmidleft_syst = Uncertainty("sys", is_symmetric=True)
unc_fig_1_PbPb3090_bjet_upmidleft_syst.values = data_fig_1a_systunc["dy"]
y_fig_1_PbPb3090_bjet_upmidleft.add_uncertainty(unc_fig_1_PbPb3090_bjet_upmidleft_stat)
y_fig_1_PbPb3090_bjet_upmidleft.add_uncertainty(unc_fig_1_PbPb3090_bjet_upmidleft_syst)

table_4.add_variable(x_fig_1)
table_4.add_variable(y_fig_1_PbPb3090_incl_upmidleft)
table_4.add_variable(y_fig_1_PbPb3090_bjet_upmidleft)

#Upper-middle left panel: Jet shapes for 10-30% 

table_5 = Table(labels_fig[4])
table_5.description = descriptions_fig[1]
table_5.location = locations_figtopmid[1]

data_fig_1a_statunc = reader_fig.read_graph(graphs_figtopmid_statunc[2])
data_fig_1a_systunc = reader_fig.read_graph(graphs_figtopmid_systunc[2])

y_fig_1_PbPb1030_incl_upmidleft = Variable(yaxises_fig_topmid[0], is_independent=False, is_binned=False, units="")
y_fig_1_PbPb1030_incl_upmidleft.digits = 5
y_fig_1_PbPb1030_incl_upmidleft.values = data_fig_1a_statunc["y"]
y_fig_1_PbPb1030_incl_upmidleft.add_qualifier("Centrality range",description_cent[1])
y_fig_1_PbPb1030_incl_upmidleft.add_qualifier("anti-kt Jets ($R = 0.4$): ","$|\eta| < 1.6$; $p_{T} > 120~GeV$")
y_fig_1_PbPb1030_incl_upmidleft.add_qualifier("Tracks: ","$|\eta| < 2.4$; $p_{T} > 1~GeV$")
y_fig_1_PbPb1030_incl_upmidleft.add_qualifier("SQRT(S)/NUCLEON","$5020.0~GeV$")
unc_fig_1_PbPb1030_incl_upmidleft_stat = Uncertainty("stat", is_symmetric=True)
unc_fig_1_PbPb1030_incl_upmidleft_stat.values = data_fig_1a_statunc["dy"]
unc_fig_1_PbPb1030_incl_upmidleft_syst = Uncertainty("sys", is_symmetric=True)
unc_fig_1_PbPb1030_incl_upmidleft_syst.values = data_fig_1a_systunc["dy"]
y_fig_1_PbPb1030_incl_upmidleft.add_uncertainty(unc_fig_1_PbPb1030_incl_upmidleft_stat)
y_fig_1_PbPb1030_incl_upmidleft.add_uncertainty(unc_fig_1_PbPb1030_incl_upmidleft_syst)

data_fig_1a_statunc = reader_fig.read_graph(graphs_figtopmid_statunc[3])
data_fig_1a_systunc = reader_fig.read_graph(graphs_figtopmid_systunc[3])

y_fig_1_PbPb1030_bjet_upmidleft = Variable(yaxises_fig_topmid[1], is_independent=False, is_binned=False, units="")
y_fig_1_PbPb1030_bjet_upmidleft.digits = 5
y_fig_1_PbPb1030_bjet_upmidleft.values = data_fig_1a_statunc["y"]
y_fig_1_PbPb1030_bjet_upmidleft.add_qualifier("Centrality range",description_cent[1])
y_fig_1_PbPb1030_bjet_upmidleft.add_qualifier("anti-kt Jets ($R = 0.4$): ","$|\eta| < 1.6$; $p_{T} > 120~GeV$")
y_fig_1_PbPb1030_bjet_upmidleft.add_qualifier("Tracks: ","$|\eta| < 2.4$; $p_{T} > 1~GeV$")
y_fig_1_PbPb1030_bjet_upmidleft.add_qualifier("SQRT(S)/NUCLEON","$5020.0~GeV$")
unc_fig_1_PbPb1030_bjet_upmidleft_stat = Uncertainty("stat", is_symmetric=True)
unc_fig_1_PbPb1030_bjet_upmidleft_stat.values = data_fig_1a_statunc["dy"]
unc_fig_1_PbPb1030_bjet_upmidleft_syst = Uncertainty("sys", is_symmetric=True)
unc_fig_1_PbPb1030_bjet_upmidleft_syst.values = data_fig_1a_systunc["dy"]
y_fig_1_PbPb1030_bjet_upmidleft.add_uncertainty(unc_fig_1_PbPb1030_bjet_upmidleft_stat)
y_fig_1_PbPb1030_bjet_upmidleft.add_uncertainty(unc_fig_1_PbPb1030_bjet_upmidleft_syst)

table_5.add_variable(x_fig_1)
table_5.add_variable(y_fig_1_PbPb1030_incl_upmidleft)
table_5.add_variable(y_fig_1_PbPb1030_bjet_upmidleft)


#Upper-middle left panel: Jet shapes for 0-10% 

table_6 = Table(labels_fig[5])
table_6.description = descriptions_fig[1]
table_6.location = locations_figtopmid[2]

data_fig_1a_statunc = reader_fig.read_graph(graphs_figtopmid_statunc[4])
data_fig_1a_systunc = reader_fig.read_graph(graphs_figtopmid_systunc[4])

y_fig_1_PbPb010_incl_upmidleft = Variable(yaxises_fig_topmid[0], is_independent=False, is_binned=False, units="")
y_fig_1_PbPb010_incl_upmidleft.digits = 5
y_fig_1_PbPb010_incl_upmidleft.values = data_fig_1a_statunc["y"]
y_fig_1_PbPb010_incl_upmidleft.add_qualifier("Centrality range",description_cent[2])
y_fig_1_PbPb010_incl_upmidleft.add_qualifier("anti-kt Jets ($R = 0.4$): ","$|\eta| < 1.6$; $p_{T} > 120~GeV$")
y_fig_1_PbPb010_incl_upmidleft.add_qualifier("Tracks: ","$|\eta| < 2.4$; $p_{T} > 1~GeV$")
y_fig_1_PbPb010_incl_upmidleft.add_qualifier("SQRT(S)/NUCLEON","$5020.0~GeV$")
unc_fig_1_PbPb010_incl_upmidleft_stat = Uncertainty("stat", is_symmetric=True)
unc_fig_1_PbPb010_incl_upmidleft_stat.values = data_fig_1a_statunc["dy"]
unc_fig_1_PbPb010_incl_upmidleft_syst = Uncertainty("sys", is_symmetric=True)
unc_fig_1_PbPb010_incl_upmidleft_syst.values = data_fig_1a_systunc["dy"]
y_fig_1_PbPb010_incl_upmidleft.add_uncertainty(unc_fig_1_PbPb010_incl_upmidleft_stat)
y_fig_1_PbPb010_incl_upmidleft.add_uncertainty(unc_fig_1_PbPb010_incl_upmidleft_syst)

data_fig_1a_statunc = reader_fig.read_graph(graphs_figtopmid_statunc[5])
data_fig_1a_systunc = reader_fig.read_graph(graphs_figtopmid_systunc[5])

y_fig_1_PbPb010_bjet_upmidleft = Variable(yaxises_fig_topmid[1], is_independent=False, is_binned=False, units="")
y_fig_1_PbPb010_bjet_upmidleft.digits = 5
y_fig_1_PbPb010_bjet_upmidleft.values = data_fig_1a_statunc["y"]
y_fig_1_PbPb010_bjet_upmidleft.add_qualifier("Centrality range",description_cent[2])
y_fig_1_PbPb010_bjet_upmidleft.add_qualifier("anti-kt Jets ($R = 0.4$): ","$|\eta| < 1.6$; $p_{T} > 120~GeV$")
y_fig_1_PbPb010_bjet_upmidleft.add_qualifier("Tracks: ","$|\eta| < 2.4$; $p_{T} > 1~GeV$")
y_fig_1_PbPb010_bjet_upmidleft.add_qualifier("SQRT(S)/NUCLEON","$5020.0~GeV$")
unc_fig_1_PbPb010_bjet_upmidleft_stat = Uncertainty("stat", is_symmetric=True)
unc_fig_1_PbPb010_bjet_upmidleft_stat.values = data_fig_1a_statunc["dy"]
unc_fig_1_PbPb010_bjet_upmidleft_syst = Uncertainty("sys", is_symmetric=True)
unc_fig_1_PbPb010_bjet_upmidleft_syst.values = data_fig_1a_systunc["dy"]
y_fig_1_PbPb010_bjet_upmidleft.add_uncertainty(unc_fig_1_PbPb010_bjet_upmidleft_stat)
y_fig_1_PbPb010_bjet_upmidleft.add_uncertainty(unc_fig_1_PbPb010_bjet_upmidleft_syst)

table_6.add_variable(x_fig_1)
table_6.add_variable(y_fig_1_PbPb010_incl_upmidleft)
table_6.add_variable(y_fig_1_PbPb010_bjet_upmidleft)

#Read figures (middle-bottom panel)
#TGraphs with statistical uncertainties 
graphs_figbotmidd_statunc = ["Figure1a_difference_P_PbPb_to_pp_3090_inclusive",
                         "Figure1a_difference_P_PbPb_to_pp_3090_bjet",
                         "Figure1a_difference_P_PbPb_to_pp_1030_inclusive",
                         "Figure1a_difference_P_PbPb_to_pp_1030_bjet",
                         "Figure1a_difference_P_PbPb_to_pp_010_inclusive",
                         "Figure1a_difference_P_PbPb_to_pp_010_bjet"]
#TGraphs with systematical uncertainties
graphs_figbotmidd_systunc = ["Figure1a_difference_P_PbPb_to_pp_3090_inclusive_syst",
                         "Figure1a_difference_P_PbPb_to_pp_3090_bjet_syst",
                         "Figure1a_difference_P_PbPb_to_pp_1030_inclusive_syst",
                         "Figure1a_difference_P_PbPb_to_pp_1030_bjet_syst",
                         "Figure1a_difference_P_PbPb_to_pp_010_inclusive_syst",
                         "Figure1a_difference_P_PbPb_to_pp_010_bjet_syst"]

yaxises_fig_botmiddd = ["$P(\Delta r)_{\mathrm{PbPb}} - $P(\Delta r)_{\mathrm{pp}} - inclusive jets$","$P(\Delta r)_{\mathrm{PbPb}} - $P(\Delta r)_{\mathrm{pp}} - b jets$"]
locations_figbotmiddd = ["Data from Figure 1 (middle-bottom left panel) - blue filled circles for b jets (PbPb-pp), red open squares for incluse jets (PbPb-pp).", 
                       "Data from Figure 1 (middle-bottom middle panel) - blue filled circles for b jets (PbPb-pp), red open squares for incluse jets (PbPb-pp).",
                       "Data from Figure 1 (middle-bottom right panel) - blue filled circles for b jets (PbPb-pp), red open squares for incluse jets (PbPb-pp)."]


table_7 = Table(labels_fig[6])
table_7.description = descriptions_fig[2]
table_7.location = locations_figbotmiddd[0]

#Upper left panel: Jet shapes for 30-90% 
data_fig_1b_statunc = reader_fig.read_graph(graphs_figbotmidd_statunc[0])
data_fig_1b_systunc = reader_fig.read_graph(graphs_figbotmidd_systunc[0])

y_fig_1_PbPb3090_incl_botmidleft = Variable(yaxises_fig_topmid[0], is_independent=False, is_binned=False, units="")
y_fig_1_PbPb3090_incl_botmidleft.digits = 5
y_fig_1_PbPb3090_incl_botmidleft.values = data_fig_1b_statunc["y"]
y_fig_1_PbPb3090_incl_botmidleft.add_qualifier("Centrality range",description_cent[0])
y_fig_1_PbPb3090_incl_botmidleft.add_qualifier("anti-kt Jets ($R = 0.4$): ","$|\eta| < 1.6$; $p_{T} > 120~GeV$")
y_fig_1_PbPb3090_incl_botmidleft.add_qualifier("Tracks: ","$|\eta| < 2.4$; $1 < p_{T} < 4~GeV$")
y_fig_1_PbPb3090_incl_botmidleft.add_qualifier("SQRT(S)/NUCLEON","$5020.0~GeV$")
unc_fig_1_PbPb3090_incl_botmidleft_stat = Uncertainty("stat", is_symmetric=True)
unc_fig_1_PbPb3090_incl_botmidleft_stat.values = data_fig_1b_statunc["dy"]
unc_fig_1_PbPb3090_incl_botmidleft_syst = Uncertainty("sys", is_symmetric=True)
unc_fig_1_PbPb3090_incl_botmidleft_syst.values = data_fig_1b_systunc["dy"]
y_fig_1_PbPb3090_incl_botmidleft.add_uncertainty(unc_fig_1_PbPb3090_incl_botmidleft_stat)
y_fig_1_PbPb3090_incl_botmidleft.add_uncertainty(unc_fig_1_PbPb3090_incl_botmidleft_syst)

data_fig_1b_statunc = reader_fig.read_graph(graphs_figbotmidd_statunc[1])
data_fig_1b_systunc = reader_fig.read_graph(graphs_figbotmidd_systunc[1])

y_fig_1_PbPb3090_bjet_botmidleft = Variable(yaxises_fig_topmid[1], is_independent=False, is_binned=False, units="")
y_fig_1_PbPb3090_bjet_botmidleft.digits = 5
y_fig_1_PbPb3090_bjet_botmidleft.values = data_fig_1b_statunc["y"]
y_fig_1_PbPb3090_bjet_botmidleft.add_qualifier("Centrality range",description_cent[0])
y_fig_1_PbPb3090_bjet_botmidleft.add_qualifier("anti-kt Jets ($R = 0.4$): ","$|\eta| < 1.6$; $p_{T} > 120~GeV$")
y_fig_1_PbPb3090_bjet_botmidleft.add_qualifier("Tracks: ","$|\eta| < 2.4$; $1 < p_{T} < 4~GeV$")
y_fig_1_PbPb3090_bjet_botmidleft.add_qualifier("SQRT(S)/NUCLEON","$5020.0~GeV$")
unc_fig_1_PbPb3090_bjet_botmidleft_stat = Uncertainty("stat", is_symmetric=True)
unc_fig_1_PbPb3090_bjet_botmidleft_stat.values = data_fig_1b_statunc["dy"]
unc_fig_1_PbPb3090_bjet_botmidleft_syst = Uncertainty("sys", is_symmetric=True)
unc_fig_1_PbPb3090_bjet_botmidleft_syst.values = data_fig_1b_systunc["dy"]
y_fig_1_PbPb3090_bjet_botmidleft.add_uncertainty(unc_fig_1_PbPb3090_bjet_botmidleft_stat)
y_fig_1_PbPb3090_bjet_botmidleft.add_uncertainty(unc_fig_1_PbPb3090_bjet_botmidleft_syst)

table_7.add_variable(x_fig_1)
table_7.add_variable(y_fig_1_PbPb3090_incl_botmidleft)
table_7.add_variable(y_fig_1_PbPb3090_bjet_botmidleft)

#Upper-middle left panel: Jet shapes for 10-30% 

table_8 = Table(labels_fig[7])
table_8.description = descriptions_fig[2]
table_8.location = locations_figbotmiddd[1]

data_fig_1b_statunc = reader_fig.read_graph(graphs_figbotmidd_statunc[2])
data_fig_1b_systunc = reader_fig.read_graph(graphs_figbotmidd_systunc[2])

y_fig_1_PbPb1030_incl_botmidleft = Variable(yaxises_fig_topmid[0], is_independent=False, is_binned=False, units="")
y_fig_1_PbPb1030_incl_botmidleft.digits = 5
y_fig_1_PbPb1030_incl_botmidleft.values = data_fig_1b_statunc["y"]
y_fig_1_PbPb1030_incl_botmidleft.add_qualifier("Centrality range",description_cent[1])
y_fig_1_PbPb1030_incl_botmidleft.add_qualifier("anti-kt Jets ($R = 0.4$): ","$|\eta| < 1.6$; $p_{T} > 120~GeV$")
y_fig_1_PbPb1030_incl_botmidleft.add_qualifier("Tracks: ","$|\eta| < 2.4$; $1 < p_{T} < 4~GeV$")
y_fig_1_PbPb1030_incl_botmidleft.add_qualifier("SQRT(S)/NUCLEON","$5020.0~GeV$")
unc_fig_1_PbPb1030_incl_botmidleft_stat = Uncertainty("stat", is_symmetric=True)
unc_fig_1_PbPb1030_incl_botmidleft_stat.values = data_fig_1b_statunc["dy"]
unc_fig_1_PbPb1030_incl_botmidleft_syst = Uncertainty("sys", is_symmetric=True)
unc_fig_1_PbPb1030_incl_botmidleft_syst.values = data_fig_1b_systunc["dy"]
y_fig_1_PbPb1030_incl_botmidleft.add_uncertainty(unc_fig_1_PbPb1030_incl_botmidleft_stat)
y_fig_1_PbPb1030_incl_botmidleft.add_uncertainty(unc_fig_1_PbPb1030_incl_botmidleft_syst)

data_fig_1b_statunc = reader_fig.read_graph(graphs_figbotmidd_statunc[3])
data_fig_1b_systunc = reader_fig.read_graph(graphs_figbotmidd_systunc[3])

y_fig_1_PbPb1030_bjet_botmidleft = Variable(yaxises_fig_topmid[1], is_independent=False, is_binned=False, units="")
y_fig_1_PbPb1030_bjet_botmidleft.digits = 5
y_fig_1_PbPb1030_bjet_botmidleft.values = data_fig_1b_statunc["y"]
y_fig_1_PbPb1030_bjet_botmidleft.add_qualifier("Centrality range",description_cent[1])
y_fig_1_PbPb1030_bjet_botmidleft.add_qualifier("anti-kt Jets ($R = 0.4$): ","$|\eta| < 1.6$; $p_{T} > 120~GeV$")
y_fig_1_PbPb1030_bjet_botmidleft.add_qualifier("Tracks: ","$|\eta| < 2.4$; $1 < p_{T} < 4~GeV$")
y_fig_1_PbPb1030_bjet_botmidleft.add_qualifier("SQRT(S)/NUCLEON","$5020.0~GeV$")
unc_fig_1_PbPb1030_bjet_botmidleft_stat = Uncertainty("stat", is_symmetric=True)
unc_fig_1_PbPb1030_bjet_botmidleft_stat.values = data_fig_1b_statunc["dy"]
unc_fig_1_PbPb1030_bjet_botmidleft_syst = Uncertainty("sys", is_symmetric=True)
unc_fig_1_PbPb1030_bjet_botmidleft_syst.values = data_fig_1b_systunc["dy"]
y_fig_1_PbPb1030_bjet_botmidleft.add_uncertainty(unc_fig_1_PbPb1030_bjet_botmidleft_stat)
y_fig_1_PbPb1030_bjet_botmidleft.add_uncertainty(unc_fig_1_PbPb1030_bjet_botmidleft_syst)

table_8.add_variable(x_fig_1)
table_8.add_variable(y_fig_1_PbPb1030_incl_botmidleft)
table_8.add_variable(y_fig_1_PbPb1030_bjet_botmidleft)


#Upper-middle left panel: Jet shapes for 0-10% 

table_9 = Table(labels_fig[8])
table_9.description = descriptions_fig[2]
table_9.location = locations_figbotmiddd[2]

data_fig_1b_statunc = reader_fig.read_graph(graphs_figbotmidd_statunc[4])
data_fig_1b_systunc = reader_fig.read_graph(graphs_figbotmidd_systunc[4])

y_fig_1_PbPb010_incl_botmidleft = Variable(yaxises_fig_topmid[0], is_independent=False, is_binned=False, units="")
y_fig_1_PbPb010_incl_botmidleft.digits = 5
y_fig_1_PbPb010_incl_botmidleft.values = data_fig_1b_statunc["y"]
y_fig_1_PbPb010_incl_botmidleft.add_qualifier("Centrality range",description_cent[2])
y_fig_1_PbPb010_incl_botmidleft.add_qualifier("anti-kt Jets ($R = 0.4$): ","$|\eta| < 1.6$; $p_{T} > 120~GeV$")
y_fig_1_PbPb010_incl_botmidleft.add_qualifier("Tracks: ","$|\eta| < 2.4$; $1 < p_{T} < 4~GeV$")
y_fig_1_PbPb010_incl_botmidleft.add_qualifier("SQRT(S)/NUCLEON","$5020.0~GeV$")
unc_fig_1_PbPb010_incl_botmidleft_stat = Uncertainty("stat", is_symmetric=True)
unc_fig_1_PbPb010_incl_botmidleft_stat.values = data_fig_1b_statunc["dy"]
unc_fig_1_PbPb010_incl_botmidleft_syst = Uncertainty("sys", is_symmetric=True)
unc_fig_1_PbPb010_incl_botmidleft_syst.values = data_fig_1b_systunc["dy"]
y_fig_1_PbPb010_incl_botmidleft.add_uncertainty(unc_fig_1_PbPb010_incl_botmidleft_stat)
y_fig_1_PbPb010_incl_botmidleft.add_uncertainty(unc_fig_1_PbPb010_incl_botmidleft_syst)

data_fig_1b_statunc = reader_fig.read_graph(graphs_figbotmidd_statunc[5])
data_fig_1b_systunc = reader_fig.read_graph(graphs_figbotmidd_systunc[5])

y_fig_1_PbPb010_bjet_botmidleft = Variable(yaxises_fig_topmid[1], is_independent=False, is_binned=False, units="")
y_fig_1_PbPb010_bjet_botmidleft.digits = 5
y_fig_1_PbPb010_bjet_botmidleft.values = data_fig_1b_statunc["y"]
y_fig_1_PbPb010_bjet_botmidleft.add_qualifier("Centrality range",description_cent[2])
y_fig_1_PbPb010_bjet_botmidleft.add_qualifier("anti-kt Jets ($R = 0.4$): ","$|\eta| < 1.6$; $p_{T} > 120~GeV$")
y_fig_1_PbPb010_bjet_botmidleft.add_qualifier("Tracks: ","$|\eta| < 2.4$; $1 < p_{T} < 4~GeV$")
y_fig_1_PbPb010_bjet_botmidleft.add_qualifier("SQRT(S)/NUCLEON","$5020.0~GeV$")
unc_fig_1_PbPb010_bjet_botmidleft_stat = Uncertainty("stat", is_symmetric=True)
unc_fig_1_PbPb010_bjet_botmidleft_stat.values = data_fig_1b_statunc["dy"]
unc_fig_1_PbPb010_bjet_botmidleft_syst = Uncertainty("sys", is_symmetric=True)
unc_fig_1_PbPb010_bjet_botmidleft_syst.values = data_fig_1b_systunc["dy"]
y_fig_1_PbPb010_bjet_botmidleft.add_uncertainty(unc_fig_1_PbPb010_bjet_botmidleft_stat)
y_fig_1_PbPb010_bjet_botmidleft.add_uncertainty(unc_fig_1_PbPb010_bjet_botmidleft_syst)

table_9.add_variable(x_fig_1)
table_9.add_variable(y_fig_1_PbPb010_incl_botmidleft)
table_9.add_variable(y_fig_1_PbPb010_bjet_botmidleft)

#Read figures (bottom panel)
#TGraphs with statistical uncertainties 
graphs_figbotmid_statunc = ["Figure1_ratio_jetshape_b_to_inclusive_pp",
                         "Figure1_ratio_jetshape_b_to_inclusive_3090_PbPb",
                         "Figure1_ratio_jetshape_b_to_inclusive_1030_PbPb",
                         "Figure1_ratio_jetshape_b_to_inclusive_010_PbPb",
                         "Figure1a_difference_P_PbPb_to_pp_010_inclusive",
                         "Figure1a_difference_P_PbPb_to_pp_010_bjet"]
#TGraphs with systematical uncertainties
graphs_figbotmid_systunc = ["Figure1_ratio_jetshape_b_to_inclusive_pp_syst",
                         "Figure1_ratio_jetshape_b_to_inclusive_3090_PbPb_syst",
                         "Figure1_ratio_jetshape_b_to_inclusive_1030_PbPb_syst",
                         "Figure1_ratio_jetshape_b_to_inclusive_010_PbPb_syst"]

yaxises_fig_botmid = ["$\rho(\Delta r)_{\mathrm{b}}/$\rho(\Delta r)_{\mathrm{incl.}} - \mathrm{pp}$","$\rho(\Delta r)_{\mathrm{b}}/$\rho(\Delta r)_{\mathrm{incl.}} - \mathrm{PbPb}$"]
locations_figbotmid = ["Data from Figure 1 (bottom left panel) - green filled circles for PbPb, grey open squares for pp.", 
                       "Data from Figure 1 (bottom middle panel) - green filled circles for PbPb, grey open squares for pp",
                       "Data from Figure 1 (bottom right panel) - green filled circles for PbPb, grey open squares for pp"]



table_10 = Table(labels_fig[9])
table_10.description = descriptions_fig[3]
table_10.location = locations_figbotmid[0]

#bottom left panel
#Jet shapes for 30-90% 
data_fig_1c_statunc = reader_fig.read_graph(graphs_figbotmid_statunc[1])
data_fig_1c_systunc = reader_fig.read_graph(graphs_figbotmid_systunc[1])

y_fig_1_PbPb3090_PbPb_bottom = Variable(yaxises_fig_botmid[1], is_independent=False, is_binned=False, units="")
y_fig_1_PbPb3090_PbPb_bottom.digits = 5
y_fig_1_PbPb3090_PbPb_bottom.values = data_fig_1c_statunc["y"]
y_fig_1_PbPb3090_PbPb_bottom.add_qualifier("Centrality range",description_cent[0])
y_fig_1_PbPb3090_PbPb_bottom.add_qualifier("anti-kt Jets ($R = 0.4$): ","$|\eta| < 1.6$; $p_{T} > 120~GeV$")
y_fig_1_PbPb3090_PbPb_bottom.add_qualifier("Tracks: ","$|\eta| < 2.4$; $p_{T} > 1~GeV$")
y_fig_1_PbPb3090_PbPb_bottom.add_qualifier("SQRT(S)/NUCLEON","$5020.0~GeV$")
unc_fig_1_PbPb3090_PbPb_bottom_stat = Uncertainty("stat", is_symmetric=True)
unc_fig_1_PbPb3090_PbPb_bottom_stat.values = data_fig_1c_statunc["dy"]
unc_fig_1_PbPb3090_PbPb_bottom_syst = Uncertainty("sys", is_symmetric=True)
unc_fig_1_PbPb3090_PbPb_bottom_syst.values = data_fig_1c_systunc["dy"]
y_fig_1_PbPb3090_PbPb_bottom.add_uncertainty(unc_fig_1_PbPb3090_PbPb_bottom_stat)
y_fig_1_PbPb3090_PbPb_bottom.add_uncertainty(unc_fig_1_PbPb3090_PbPb_bottom_syst)

data_fig_1c_statunc = reader_fig.read_graph(graphs_figbotmid_statunc[0])
data_fig_1c_systunc = reader_fig.read_graph(graphs_figbotmid_systunc[0])

y_fig_1_PbPb3090_pp_bottom = Variable(yaxises_fig_botmid[0], is_independent=False, is_binned=False, units="")
y_fig_1_PbPb3090_pp_bottom.digits = 5
y_fig_1_PbPb3090_pp_bottom.values = data_fig_1c_statunc["y"]
y_fig_1_PbPb3090_pp_bottom.add_qualifier("Centrality range",description_cent[0])
y_fig_1_PbPb3090_pp_bottom.add_qualifier("anti-kt Jets ($R = 0.4$): ","$|\eta| < 1.6$; $p_{T} > 120~GeV$")
y_fig_1_PbPb3090_pp_bottom.add_qualifier("Tracks: ","$|\eta| < 2.4$; $p_{T} > 1~GeV$")
y_fig_1_PbPb3090_pp_bottom.add_qualifier("SQRT(S)/NUCLEON","$5020.0~GeV$")
unc_fig_1_PbPb3090_pp_bottom_stat = Uncertainty("stat", is_symmetric=True)
unc_fig_1_PbPb3090_pp_bottom_stat.values = data_fig_1c_statunc["dy"]
unc_fig_1_PbPb3090_pp_bottom_syst = Uncertainty("sys", is_symmetric=True)
unc_fig_1_PbPb3090_pp_bottom_syst.values = data_fig_1c_systunc["dy"]
y_fig_1_PbPb3090_pp_bottom.add_uncertainty(unc_fig_1_PbPb3090_pp_bottom_stat)
y_fig_1_PbPb3090_pp_bottom.add_uncertainty(unc_fig_1_PbPb3090_pp_bottom_syst)

table_10.add_variable(x_fig_1)
table_10.add_variable(y_fig_1_PbPb3090_pp_bottom)
table_10.add_variable(y_fig_1_PbPb3090_PbPb_bottom)


table_11 = Table(labels_fig[10])
table_11.description = descriptions_fig[3]
table_11.location = locations_figbotmid[1]

#bottom middle panel
#Jet shapes for 10-30% 

data_fig_1c_statunc = reader_fig.read_graph(graphs_figbotmid_statunc[2])
data_fig_1c_systunc = reader_fig.read_graph(graphs_figbotmid_systunc[2])

y_fig_1_PbPb1030_PbPb_bottom = Variable(yaxises_fig_botmid[1], is_independent=False, is_binned=False, units="")
y_fig_1_PbPb1030_PbPb_bottom.digits = 5
y_fig_1_PbPb1030_PbPb_bottom.values = data_fig_1c_statunc["y"]
y_fig_1_PbPb1030_PbPb_bottom.add_qualifier("Centrality range",description_cent[1])
y_fig_1_PbPb1030_PbPb_bottom.add_qualifier("anti-kt Jets ($R = 0.4$): ","$|\eta| < 1.6$; $p_{T} > 120~GeV$")
y_fig_1_PbPb1030_PbPb_bottom.add_qualifier("Tracks: ","$|\eta| < 2.4$; $p_{T} > 1~GeV$")
y_fig_1_PbPb1030_PbPb_bottom.add_qualifier("SQRT(S)/NUCLEON","$5020.0~GeV$")
unc_fig_1_PbPb1030_PbPb_bottom_stat = Uncertainty("stat", is_symmetric=True)
unc_fig_1_PbPb1030_PbPb_bottom_stat.values = data_fig_1c_statunc["dy"]
unc_fig_1_PbPb1030_PbPb_bottom_syst = Uncertainty("sys", is_symmetric=True)
unc_fig_1_PbPb1030_PbPb_bottom_syst.values = data_fig_1c_systunc["dy"]
y_fig_1_PbPb1030_PbPb_bottom.add_uncertainty(unc_fig_1_PbPb1030_PbPb_bottom_stat)
y_fig_1_PbPb1030_PbPb_bottom.add_uncertainty(unc_fig_1_PbPb1030_PbPb_bottom_syst)

data_fig_1c_statunc = reader_fig.read_graph(graphs_figtopmid_statunc[0])
data_fig_1c_systunc = reader_fig.read_graph(graphs_figtopmid_systunc[0])

y_fig_1_PbPb1030_pp_bottom = Variable(yaxises_fig_botmid[0], is_independent=False, is_binned=False, units="")
y_fig_1_PbPb1030_pp_bottom.digits = 5
y_fig_1_PbPb1030_pp_bottom.values = data_fig_1c_statunc["y"]
y_fig_1_PbPb1030_pp_bottom.add_qualifier("Centrality range",description_cent[1])
y_fig_1_PbPb1030_pp_bottom.add_qualifier("anti-kt Jets ($R = 0.4$): ","$|\eta| < 1.6$; $p_{T} > 120~GeV$")
y_fig_1_PbPb1030_pp_bottom.add_qualifier("Tracks: ","$|\eta| < 2.4$; $p_{T} > 1~GeV$")
y_fig_1_PbPb1030_pp_bottom.add_qualifier("SQRT(S)/NUCLEON","$5020.0~GeV$")
unc_fig_1_PbPb1030_pp_bottom_stat = Uncertainty("stat", is_symmetric=True)
unc_fig_1_PbPb1030_pp_bottom_stat.values = data_fig_1c_statunc["dy"]
unc_fig_1_PbPb1030_pp_bottom_syst = Uncertainty("sys", is_symmetric=True)
unc_fig_1_PbPb1030_pp_bottom_syst.values = data_fig_1c_systunc["dy"]
y_fig_1_PbPb1030_pp_bottom.add_uncertainty(unc_fig_1_PbPb1030_pp_bottom_stat)
y_fig_1_PbPb1030_pp_bottom.add_uncertainty(unc_fig_1_PbPb1030_pp_bottom_syst)

table_11.add_variable(x_fig_1)
table_11.add_variable(y_fig_1_PbPb1030_pp_bottom)
table_11.add_variable(y_fig_1_PbPb1030_PbPb_bottom)


table_12 = Table(labels_fig[11])
table_12.description = descriptions_fig[3]
table_12.location = locations_figbotmid[2]

#bottom right panel
#Jet shapes for 0-10% 

data_fig_1c_statunc = reader_fig.read_graph(graphs_figtopmid_statunc[3])
data_fig_1c_systunc = reader_fig.read_graph(graphs_figtopmid_systunc[3])

y_fig_1_PbPb010_PbPb_bottom = Variable(yaxises_fig_botmid[1], is_independent=False, is_binned=False, units="")
y_fig_1_PbPb010_PbPb_bottom.digits = 5
y_fig_1_PbPb010_PbPb_bottom.values = data_fig_1c_statunc["y"]
y_fig_1_PbPb010_PbPb_bottom.add_qualifier("Centrality range",description_cent[2])
y_fig_1_PbPb010_PbPb_bottom.add_qualifier("anti-kt Jets ($R = 0.4$): ","$|\eta| < 1.6$; $p_{T} > 120~GeV$")
y_fig_1_PbPb010_PbPb_bottom.add_qualifier("Tracks: ","$|\eta| < 2.4$; $p_{T} > 1~GeV$")
y_fig_1_PbPb010_PbPb_bottom.add_qualifier("SQRT(S)/NUCLEON","$5020.0~GeV$")
unc_fig_1_PbPb010_PbPb_bottom_stat = Uncertainty("stat", is_symmetric=True)
unc_fig_1_PbPb010_PbPb_bottom_stat.values = data_fig_1c_statunc["dy"]
unc_fig_1_PbPb010_PbPb_bottom_syst = Uncertainty("sys", is_symmetric=True)
unc_fig_1_PbPb010_PbPb_bottom_syst.values = data_fig_1c_systunc["dy"]
y_fig_1_PbPb010_PbPb_bottom.add_uncertainty(unc_fig_1_PbPb010_PbPb_bottom_stat)
y_fig_1_PbPb010_PbPb_bottom.add_uncertainty(unc_fig_1_PbPb010_PbPb_bottom_syst)

data_fig_1c_statunc = reader_fig.read_graph(graphs_figtopmid_statunc[0])
data_fig_1c_systunc = reader_fig.read_graph(graphs_figtopmid_systunc[0])

y_fig_1_PbPb010_pp_bottom = Variable(yaxises_fig_botmid[0], is_independent=False, is_binned=False, units="")
y_fig_1_PbPb010_pp_bottom.digits = 5
y_fig_1_PbPb010_pp_bottom.values = data_fig_1c_statunc["y"]
y_fig_1_PbPb010_pp_bottom.add_qualifier("Centrality range",description_cent[2])
y_fig_1_PbPb010_pp_bottom.add_qualifier("anti-kt Jets ($R = 0.4$): ","$|\eta| < 1.6$; $p_{T} > 120~GeV$")
y_fig_1_PbPb010_pp_bottom.add_qualifier("Tracks: ","$|\eta| < 2.4$; $p_{T} > 1~GeV$")
y_fig_1_PbPb010_pp_bottom.add_qualifier("SQRT(S)/NUCLEON","$5020.0~GeV$")
unc_fig_1_PbPb010_pp_bottom_stat = Uncertainty("stat", is_symmetric=True)
unc_fig_1_PbPb010_pp_bottom_stat.values = data_fig_1c_statunc["dy"]
unc_fig_1_PbPb010_pp_bottom_syst = Uncertainty("sys", is_symmetric=True)
unc_fig_1_PbPb010_pp_bottom_syst.values = data_fig_1c_systunc["dy"]
y_fig_1_PbPb010_pp_bottom.add_uncertainty(unc_fig_1_PbPb010_pp_bottom_stat)
y_fig_1_PbPb010_pp_bottom.add_uncertainty(unc_fig_1_PbPb010_pp_bottom_syst)

table_12.add_variable(x_fig_1)
table_12.add_variable(y_fig_1_PbPb010_pp_bottom)
table_12.add_variable(y_fig_1_PbPb010_PbPb_bottom)


#make the submission file

submission.add_table(table_1)
submission.add_table(table_2)
submission.add_table(table_3)
submission.add_table(table_4)
submission.add_table(table_5)
submission.add_table(table_6)
submission.add_table(table_7)
submission.add_table(table_8)
submission.add_table(table_9)
submission.add_table(table_10)
submission.add_table(table_11)
submission.add_table(table_12)

#Make figures and tables for hepdata
for itable in submission.tables:
  itable.keywords["cmenergies"] = [50200]
outdir = "hin20003_output"
submission.create_files(outdir)

