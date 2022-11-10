# coding: utf-8

"""
Selectors to set ak columns for gen particles of hh2bbww
"""
import numpy as np
from columnflow.util import maybe_import
from columnflow.columnar_util import set_ak_column  # , Route, EMPTY_FLOAT
from columnflow.selection import Selector, selector

ak = maybe_import("awkward")

coffea = maybe_import("coffea")
maybe_import("coffea.nanoevents.methods.nanoaod")

@selector(
    uses={
        "gen_hbw_decay",
        "nJet", "Jet.*", #"Jet.genJetIdx",
        "nGenJet", "GenJet.*",
        "nFatJet", "FatJet.*",
        "nGenJetAK8", "GenJetAK8.*",
    },
    produces={
        "cutflow.h1_pt", "cutflow.h1_eta", "cutflow.h1_phi", "cutflow.h1_mass",
        "cutflow.h2_pt", "cutflow.h2_eta", "cutflow.h2_phi", "cutflow.h2_mass",
        "cutflow.b1_pt", "cutflow.b1_eta", "cutflow.b1_phi", "cutflow.b1_mass",
        "cutflow.b2_pt", "cutflow.b2_eta", "cutflow.b2_phi", "cutflow.b2_mass",
        "cutflow.wlep_pt", "cutflow.wlep_eta", "cutflow.wlep_phi", "cutflow.wlep_mass",
        "cutflow.whad_pt", "cutflow.whad_eta", "cutflow.whad_phi", "cutflow.whad_mass",
        "cutflow.l_pt", "cutflow.l_eta", "cutflow.l_phi", "cutflow.l_mass",
        "cutflow.nu_pt", "cutflow.nu_eta", "cutflow.nu_phi", "cutflow.nu_mass",
        "cutflow.q1_pt", "cutflow.q1_eta", "cutflow.q1_phi", "cutflow.q1_mass",
        "cutflow.q2_pt", "cutflow.q2_eta", "cutflow.q2_phi", "cutflow.q2_mass",
        "cutflow.sec1_pt", "cutflow.sec1_eta", "cutflow.sec1_phi", "cutflow.sec1_mass",
        "cutflow.sec2_pt", "cutflow.sec2_eta", "cutflow.sec2_phi", "cutflow.sec2_mass",
        #"cutflow.DeltaR_bb","cutflow.DeltaR_WW","cutflow.DeltaR_qq", "cutflow.DeltaR_jetb1", "cutflow.DeltaR_jetb2",
        #"cutflow.b1_and_b2_in_fatjet",
        "cutflow.DeltaRbb", "cutflow.DeltaRWW", "cutflow.DeltaRqq", "cutflow.DeltaRjb1", "cutflow.DeltaRjb2",
        "cutflow.b1_and_b2_in_fatjet_coffea", "cutflow.b1_and_b2_in_genjetak8_coffea",
        "cutflow.DeltaR_genjetb1", "cutflow.DeltaR_genjetb2",

        "cutflow.leadingJet_partonFlavour", "cutflow.NleadingJet_partonFlavour",
        "cutflow.NNleadingJet_partonFlavour", "cutflow.NNNleadingJet_partonFlavour",
        "cutflow.leadingJet_hadronFlavour", "cutflow.NleadingJet_hadronFlavour",
        "cutflow.NNleadingJet_hadronFlavour", "cutflow.NNNleadingJet_hadronFlavour",

        "cutflow.leadingGenJet_partonFlavour", "cutflow.NleadingGenJet_partonFlavour",
        "cutflow.NNleadingGenJet_partonFlavour", "cutflow.NNNleadingGenJet_partonFlavour",
        "cutflow.leadingGenJet_hadronFlavour", "cutflow.NleadingGenJet_hadronFlavour",
        "cutflow.NNleadingGenJet_hadronFlavour", "cutflow.NNNleadingGenJet_hadronFlavour",

        "cutflow.leadingFatJet_partonFlavour", "cutflow.NleadingFatJet_partonFlavour",
        "cutflow.NNleadingFatJet_partonFlavour", "cutflow.NNNleadingFatJet_partonFlavour",
        "cutflow.leadingFatJet_hadronFlavour", "cutflow.NleadingFatJet_hadronFlavour",
        "cutflow.NNleadingFatJet_hadronFlavour", "cutflow.NNNleadingFatJet_hadronFlavour",

        "cutflow.leadingGenJetAK8_partonFlavour", "cutflow.NleadingGenJetAK8_partonFlavour",
        "cutflow.NNleadingGenJetAK8_partonFlavour", "cutflow.NNNleadingGenJetAK8_partonFlavour",
        "cutflow.leadingGenJetAK8_hadronFlavour", "cutflow.NleadingGenJetAK8_hadronFlavour",
        "cutflow.NNleadingGenJetAK8_hadronFlavour", "cutflow.NNNleadingGenJetAK8_hadronFlavour",
    },
    # set(f"cutflow.{gp}_{var}"
    #     for gp in ["h1", "h2", "b1", "b2", "wlep", "whad", "l", "nu", "q1", "q2", "sec1", "sec2"]
    #     for var in ["pt", "eta", "phi", "mass"]),

)
def gen_hbw_decay_features(self: Selector, events: ak.Array, **kwargs) -> ak.Array:
    for var in ["pt", "eta", "phi", "mass"]:
         for gp in ["h1", "h2", "b1", "b2", "wlep", "whad", "l", "nu", "q1", "q2", "sec1", "sec2"]:
        #for gp in ["h1"]:
            events = set_ak_column(events, f"cutflow.{gp}_{var}", events.gen_hbw_decay[gp][var])
    #from IPython import embed; embed()
    #valid_fatjet_idxs = ak.mask(events.FatJet.genJetAK8Idx, events.FatJet.genJetAK8Idx >= 0)
    #padded_fatjets = ak.pad_none(events.FatJet, ak.max(valid_fatjet_idxs) + 1)

    #DeltaR_bb = np.sqrt(np.square(events.gen_hbw_decay["b1"]["eta"]-events.gen_hbw_decay["b2"]["eta"]) + np.square(events.gen_hbw_decay["b1"]["phi"]-events.gen_hbw_decay["b2"]["phi"]))
    #DeltaR_WW = np.sqrt(np.square(events.gen_hbw_decay["wlep"]["eta"]-events.gen_hbw_decay["whad"]["eta"]) + np.square(events.gen_hbw_decay["wlep"]["phi"]-events.gen_hbw_decay["whad"]["phi"]))
    #DeltaR_qq = np.sqrt(np.square(events.gen_hbw_decay["q1"]["eta"]-events.gen_hbw_decay["q2"]["eta"]) + np.square(events.gen_hbw_decay["q1"]["phi"]-events.gen_hbw_decay["q2"]["phi"]))
    #DeltaR_jetb1 = np.sqrt(np.square(events.gen_hbw_decay["b1"]["eta"]-padded_fatjets.eta[:,0]) + np.square(events.gen_hbw_decay["b1"]["phi"]-padded_fatjets.phi[:,0]))
    #DeltaR_jetb2 = np.sqrt(np.square(events.gen_hbw_decay["b2"]["eta"]-padded_fatjets.eta[:,0]) + np.square(events.gen_hbw_decay["b2"]["phi"]-padded_fatjets.phi[:,0]))

    #b1_in_fatjet_mask = DeltaR_jetb1 <= 0.8
    #b2_in_fatjet_mask = DeltaR_jetb2 <= 0.8
    #b1_and_b2_in_fatjet_mask = b1_in_fatjet_mask & b2_in_fatjet_mask
    #x_for_b1_and_b2_in_fatjet = ak.Array(np.ones(len(b1_and_b2_in_fatjet_mask)))
    #y_for_b1_and_b2_in_fatjet = ak.Array(np.zeros(len(b1_and_b2_in_fatjet_mask)))
    #b1_and_b2_in_fatjet = ak.where(b1_and_b2_in_fatjet_mask, x_for_b1_and_b2_in_fatjet, y_for_b1_and_b2_in_fatjet)

    #from IPython import embed; embed()

    events = ak.Array(events, behavior=coffea.nanoevents.methods.nanoaod.behavior)
    events["FatJet"] = ak.with_name(events.FatJet, "PtEtaPhiMLorentzVector")
    for gp in ["h1", "h2", "b1", "b2", "wlep", "whad", "l", "nu", "q1", "q2", "sec1", "sec2"]:
        events["gen_hbw_decay", gp] = ak.with_name(events.gen_hbw_decay[gp], "PtEtaPhiMLorentzVector")

    DeltaRbb = events.gen_hbw_decay["b1"].delta_r(events.gen_hbw_decay["b2"])
    DeltaRWW = events.gen_hbw_decay["wlep"].delta_r(events.gen_hbw_decay["whad"])
    DeltaRqq = events.gen_hbw_decay["q1"].delta_r(events.gen_hbw_decay["q2"])
    padded_fatjets = ak.pad_none(events.FatJet, 1)
    padded_gen_fatjets = ak.pad_none(events.GenJetAK8, 1)
    DeltaRjb1 = padded_fatjets[:,0].delta_r(events.gen_hbw_decay["b1"])
    DeltaRjb2 = padded_fatjets[:,0].delta_r(events.gen_hbw_decay["b2"])
    DeltaR_genjetb1 = padded_gen_fatjets[:,0].delta_r(events.gen_hbw_decay["b1"])
    DeltaR_genjetb2 = padded_gen_fatjets[:,0].delta_r(events.gen_hbw_decay["b2"])

    b1_in_fatjet_mask_coffea = DeltaRjb1 <= 0.8
    b2_in_fatjet_mask_coffea = DeltaRjb2 <= 0.8
    b1_and_b2_in_fatjet_mask_coffea = b1_in_fatjet_mask_coffea & b2_in_fatjet_mask_coffea
    x_for_b1_and_b2_in_fatjet_coffea = ak.Array(np.ones(len(b1_and_b2_in_fatjet_mask_coffea)))
    y_for_b1_and_b2_in_fatjet_coffea = ak.Array(np.zeros(len(b1_and_b2_in_fatjet_mask_coffea)))
    b1_and_b2_in_fatjet_coffea = ak.where(b1_and_b2_in_fatjet_mask_coffea, x_for_b1_and_b2_in_fatjet_coffea, y_for_b1_and_b2_in_fatjet_coffea)

    b1_in_genjetak8_mask_coffea = DeltaR_genjetb1 <= 0.8
    b2_in_genjetak8_mask_coffea = DeltaR_genjetb2 <= 0.8
    b1_and_b2_in_genjetak8_mask_coffea = b1_in_genjetak8_mask_coffea & b2_in_genjetak8_mask_coffea
    x_for_b1_and_b2_in_genjetak8_coffea = ak.Array(np.ones(len(b1_and_b2_in_genjetak8_mask_coffea)))
    y_for_b1_and_b2_in_genjetak8_coffea = ak.Array(np.zeros(len(b1_and_b2_in_genjetak8_mask_coffea)))
    b1_and_b2_in_genjetak8_coffea = ak.where(b1_and_b2_in_genjetak8_mask_coffea, x_for_b1_and_b2_in_genjetak8_coffea, y_for_b1_and_b2_in_genjetak8_coffea)

    #events = set_ak_column(events, "cutflow.DeltaR_bb", DeltaR_bb)
    #events = set_ak_column(events, "cutflow.DeltaR_WW", DeltaR_WW)
    #events = set_ak_column(events, "cutflow.DeltaR_qq", DeltaR_qq)
    #events = set_ak_column(events, "cutflow.DeltaR_jetb1", DeltaR_jetb1)
    #events = set_ak_column(events, "cutflow.DeltaR_jetb2", DeltaR_jetb2)
    #events = set_ak_column(events, "cutflow.b1_and_b2_in_fatjet", b1_and_b2_in_fatjet)
    events = set_ak_column(events, "cutflow.DeltaRbb", DeltaRbb)
    events = set_ak_column(events, "cutflow.DeltaRWW", DeltaRWW)
    events = set_ak_column(events, "cutflow.DeltaRqq", DeltaRqq)
    events = set_ak_column(events, "cutflow.DeltaRjb1", DeltaRjb1)
    events = set_ak_column(events, "cutflow.DeltaR_genjetb1", DeltaR_genjetb1)
    events = set_ak_column(events, "cutflow.DeltaRjb2", DeltaRjb2)
    events = set_ak_column(events, "cutflow.DeltaR_genjetb2", DeltaR_genjetb2)
    events = set_ak_column(events, "cutflow.b1_and_b2_in_fatjet_coffea", b1_and_b2_in_fatjet_coffea)
    events = set_ak_column(events, "cutflow.b1_and_b2_in_genjetak8_coffea", b1_and_b2_in_genjetak8_coffea)

    # mask negative gen jet indices (= no gen match)
    valid_gen_jet_idxs = ak.mask(events.Jet.genJetIdx, events.Jet.genJetIdx >= 0)
    # pad list of gen jets to prevent index error on match lookup
    padded_gen_jets = ak.pad_none(events.GenJet, ak.max(valid_gen_jet_idxs) + 1)
    # gen jets that match the reconstructed jets
    matched_gen_jets = padded_gen_jets[valid_gen_jet_idxs]
    matched_gen_jets = ak.pad_none(matched_gen_jets, 4)
    #from IPython import embed; embed()
    for var in ["partonFlavour","hadronFlavour"]:
        for index, jet in enumerate(["leadingJet", "NleadingJet", "NNleadingJet", "NNNleadingJet"]):
            events = set_ak_column(events, f"cutflow.{jet}_{var}", matched_gen_jets[f"{var}"][:,index])

    padded_genjets = ak.pad_none(events.GenJet, 4)

    for var in ["partonFlavour","hadronFlavour"]:
        for index, genjet in enumerate(["leadingGenJet", "NleadingGenJet", "NNleadingGenJet", "NNNleadingGenJet"]):
            events = set_ak_column(events, f"cutflow.{genjet}_{var}", padded_genjets[var][:, index])

    padded_genjetsak8 = ak.pad_none(events.GenJetAK8, 4)

    for var in ["partonFlavour","hadronFlavour"]:
        for index, genjetak8 in enumerate(["leadingGenJetAK8", "NleadingGenJetAK8", "NNleadingGenJetAK8", "NNNleadingGenJetAK8"]):
            events = set_ak_column(events, f"cutflow.{genjetak8}_{var}", padded_genjetsak8[var][:, index])

    valid_gen_fatjet_idxs = ak.mask(events.FatJet.genJetAK8Idx, events.FatJet.genJetAK8Idx >= 0)
    # pad list of gen fatjets to prevent index error on match lookup
    padded_gen_fatjets = ak.pad_none(events.GenJetAK8, ak.max(valid_gen_fatjet_idxs) + 1)
    # gen jets that match the reconstructed fatjets
    matched_gen_fatjets = padded_gen_fatjets[valid_gen_fatjet_idxs]
    #from IPython import embed; embed()
    matched_gen_fatjets = ak.pad_none(matched_gen_fatjets, 4)

    for var in ["partonFlavour","hadronFlavour"]:
        for index, FatJet in enumerate(["leadingFatJet", "NleadingFatJet", "NNleadingFatJet", "NNNleadingFatJet"]):
            events = set_ak_column(events, f"cutflow.{FatJet}_{var}", matched_gen_fatjets[f"{var}"][:,index])


    return events
