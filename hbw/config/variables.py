# coding: utf-8

"""
Definition of variables.
"""

import order as od

from columnflow.columnar_util import EMPTY_FLOAT


def add_variables(config: od.Config) -> None:
    """
    Adds all variables to a *config*.
    """
    config.add_variable(
        name="mc_weight",
        expression="mc_weight",
        binning=(200, -10, 10),
        x_title="MC weight",
    )

    # Event properties
    config.add_variable(
        name="n_jet",
        binning=(11, -0.5, 10.5),
        x_title="Number of jets",
    )
    config.add_variable(
        name="n_deepjet",
        binning=(11, -0.5, 10.5),
        x_title="Number of deepjets",
    )
    config.add_variable(
        name="n_electron",
        binning=(11, -0.5, 10.5),
        x_title="Number of electrons",
    )
    config.add_variable(
        name="n_muon",
        binning=(11, -0.5, 10.5),
        x_title="Number of muons",
    )
    config.add_variable(
        name="ht",
        binning=(40, 0, 1500),
        x_title="HT",
    )
    config.add_variable(
        name="ht_rebin",
        expression="ht",
        binning=[0, 80, 120, 160, 200, 240, 280, 320, 400, 500, 600, 800, 1200],
        unit="GeV",
        x_title="HT",
    )

    # Object properties

    # Jets (4 pt-leading jets)
    for i in range(4):
        config.add_variable(
            name=f"jet{i+1}_pt",
            expression=f"Jet.pt[:,{i}]",
            null_value=EMPTY_FLOAT,
            binning=(40, 0., 400.),
            unit="GeV",
            x_title=r"Jet %i $p_{T}$" % (i + 1),
        )
        config.add_variable(
            name=f"jet{i+1}_eta",
            expression=f"Jet.eta[:,{i}]",
            null_value=EMPTY_FLOAT,
            binning=(50, 0., 5),
            x_title=r"Jet %i $\eta$" % (i + 1),
        )
        config.add_variable(
            name=f"jet{i+1}_phi",
            expression=f"Jet.phi[:,{i}]",
            null_value=EMPTY_FLOAT,
            binning=(40, -3.2, 3.2),
            x_title=r"Jet %i $\phi$" % (i + 1),
        )
        config.add_variable(
            name=f"jet{i+1}_mass",
            expression=f"Jet.mass[:,{i}]",
            null_value=EMPTY_FLOAT,
            binning=(40, -3.2, 3.2),
            x_title=r"Jet %i mass" % (i + 1),
        )

    # Bjets (2 b-score leading jets)
    for i in range(2):
        config.add_variable(
            name=f"bjet{i+1}_pt",
            expression=f"Bjet.pt[:,{i}]",
            null_value=EMPTY_FLOAT,
            binning=(40, 0., 400.),
            unit="GeV",
            x_title=r"Bjet %i $p_{T}$" % (i + 1),
        )
        config.add_variable(
            name=f"bjet{i+1}_eta",
            expression=f"Bjet.eta[:,{i}]",
            null_value=EMPTY_FLOAT,
            binning=(50, 0., 5),
            x_title=r"Bjet %i $\eta$" % (i + 1),
        )
        config.add_variable(
            name=f"bjet{i+1}_phi",
            expression=f"Jet.phi[:,{i}]",
            null_value=EMPTY_FLOAT,
            binning=(40, -3.2, 3.2),
            x_title=r"Bjet %i $\phi$" % (i + 1),
        )
        config.add_variable(
            name=f"bjet{i+1}_mass",
            expression=f"Bjet.mass[:,{i}]",
            null_value=EMPTY_FLOAT,
            binning=(40, -3.2, 3.2),
            x_title=r"Bjet %i mass" % (i + 1),
        )

    # Leptons
    for obj in ["Electron", "Muon"]:
        config.add_variable(
            name=f"{obj.lower()}_pt",
            expression=f"{obj}.pt[:,0]",
            null_value=EMPTY_FLOAT,
            binning=(40, 0., 400.),
            unit="GeV",
            x_title=obj + r" $p_{T}$",
        )
        config.add_variable(
            name=f"{obj.lower()}_phi",
            expression=f"{obj}.phi[:,0]",
            null_value=EMPTY_FLOAT,
            binning=(40, -3.2, 3.2),
            x_title=obj + r" $\phi$",
        )
        config.add_variable(
            name=f"{obj.lower()}_eta",
            expression=f"{obj}.eta[:,0]",
            null_value=EMPTY_FLOAT,
            binning=(50, 0., 5),
            x_title=obj + r" $\eta$",
        )
        config.add_variable(
            name=f"{obj.lower()}_mass",
            expression=f"{obj}.mass[:,0]",
            null_value=EMPTY_FLOAT,
            binning=(40, -3.2, 3.2),
            x_title=obj + " mass",
        )

    # MET
    config.add_variable(
        name="met_pt",
        expression="MET.pt[:,0]",
        null_value=EMPTY_FLOAT,
        binning=(40, 0., 400.),
        unit="GeV",
        x_title=r"MET $p_{T}$",
    )
    config.add_variable(
        name="met_phi",
        expression="MET.phi[:,0]",
        null_value=EMPTY_FLOAT,
        binning=(40, -3.2, 3.2),
        x_title=r"MET $\phi$",
    )

    # bb features
    config.add_variable(
        name="m_bb",
        binning=(40, 0., 400.),
        unit="GeV",
        x_title=r"$m_{bb}$",
    )
    config.add_variable(
        name="deltaR_bb",
        binning=(40, 0, 5),
        x_title=r"$\Delta R(b,b)$",
    )
    # jj features
    config.add_variable(
        name="m_jj",
        binning=(40, 0., 400.),
        unit="GeV",
        x_title=r"$m_{jj}$",
    )
    config.add_variable(
        name="deltaR_jj",
        binning=(40, 0, 5),
        x_title=r"$\Delta R(j_{1},j_{2})$",
    )

    # Gen particles

    # cutflow variables
    config.add_variable(
        name="cf_jet1_pt",
        expression="cutflow.jet1_pt",
        binning=(40, 0., 400.),
        unit="GeV",
        x_title=r"Jet 1 $p_{T}$",
    )
    config.add_variable(
        name="cf_jet2_pt",
        expression="cutflow.jet2_pt",
        binning=(40, 0., 400.),
        unit="GeV",
        x_title=r"Jet 2$p_{T}$",
    )
    config.add_variable(
        name="cf_jet3_pt",
        expression="cutflow.jet3_pt",
        binning=(40, 0., 400.),
        unit="GeV",
        x_title=r"Jet 3 $p_{T}$",
    )
    config.add_variable(
        name="cf_jet4_pt",
        expression="cutflow.jet4_pt",
        binning=(40, 0., 400.),
        unit="GeV",
        x_title=r"Jet 4 $p_{T}$",
    )
    config.add_variable(
        name="cf_n_jet",
        expression="cutflow.n_jet",
        binning=(11, -0.5, 10.5),
        x_title=r"Number of jets",
    )
    config.add_variable(
        name="cf_n_electron",
        expression="cutflow.n_electron",
        binning=(11, -0.5, 10.5),
        x_title=r"Number of electrons",
    )
    config.add_variable(
        name="cf_n_muon",
        expression="cutflow.n_muon",
        binning=(11, -0.5, 10.5),
        x_title=r"Number of muons",
    )


    #for gp in ["h1"]:
    for gp in ["h1", "h2", "b1", "b2", "wlep", "whad", "l", "nu", "q1", "q2", "sec1", "sec2"]:
        config.add_variable(
            name=f"gen_{gp}_pt",
            expression=f"cutflow.{gp}_pt",
            binning=(40, 0., 400.),
            unit="GeV",
            x_title=r"$p_{T, %s}^{gen}$" % (gp),
        )
        config.add_variable(
            name=f"gen_{gp}_mass",
            expression=f"cutflow.{gp}_mass",
            binning=(130, 0., 130.),
            unit="GeV",
            x_title=r"$m_{%s}^{gen}$" % (gp),
        )
        config.add_variable(
            name=f"gen_{gp}_eta",
            expression=f"cutflow.{gp}_eta",
            binning=(12, -6., 6.),
            unit="GeV",
            x_title=r"$\eta_{%s}^{gen}$" % (gp),
        )
        config.add_variable(
            name=f"gen_{gp}_phi",
            expression=f"cutflow.{gp}_phi",
            binning=(8, -4, 4),
            unit="GeV",
            x_title=r"$\phi_{%s}^{gen}$" % (gp),
        )
    #config.add_variable(
    #    name=f"gen_DeltaR_bb",
    #    expression=f"cutflow.DeltaR_bb",
    #    binning=(70, 0., 7.),
    #    x_title=r"$\Delta R_{bb}^{gen}$",
    #)
    config.add_variable(
        name=f"gen_DeltaRbb",
        expression=f"cutflow.DeltaRbb",
        binning=(70, 0., 7.),
        x_title=r"$\Delta R_{bb}^{gen}$",
    )
    #config.add_variable(
    #    name=f"gen_DeltaR_WW",
    #    expression=f"cutflow.DeltaR_WW",
    #    binning=(70, 0., 7.),
    #    x_title=r"$\Delta R_{WW}^{gen}$",
    #)
    config.add_variable(
        name=f"gen_DeltaRWW",
        expression=f"cutflow.DeltaRWW",
        binning=(70, 0., 7.),
        x_title=r"$\Delta R_{WW}^{gen}$",
    )
    #config.add_variable(
    #    name=f"gen_DeltaR_qq",
    #    expression=f"cutflow.DeltaR_qq",
    #    binning=(70, 0., 7.),
    #    x_title=r"$\Delta R_{qq}^{gen}$",
    #)
    config.add_variable(
        name=f"gen_DeltaRqq",
        expression=f"cutflow.DeltaRqq",
        binning=(70, 0., 7.),
        x_title=r"$\Delta R_{qq}^{gen}$",
    )
    #config.add_variable(
    #    name=f"gen_DeltaR_jetb1",
    #    expression=f"cutflow.DeltaR_jetb1",
    #    binning=(70, 0., 7.),
    #    x_title=r"$\Delta R_{jetb1}^{gen}$",
    #)
    config.add_variable(
        name=f"reco_DeltaRjb1",
        expression=f"cutflow.DeltaRjb1",
        binning=(70, 0., 7.),
        x_title=r"$\Delta R_{jetb1}^{reco}$",
    )
    config.add_variable(
        name=f"gen_DeltaR_genjetb1",
        expression=f"cutflow.DeltaR_genjetb1",
        binning=(70, 0., 7.),
        x_title=r"$\Delta R_{jetb1}^{gen}$",
    )
    #config.add_variable(
    #    name=f"gen_DeltaR_jetb2",
    #    expression=f"cutflow.DeltaR_jetb2",
    #    binning=(70, 0., 7.),
    #    x_title=r"$\Delta R_{jetb2}^{gen}$",
    #)
    config.add_variable(
        name=f"reco_DeltaRjb2",
        expression=f"cutflow.DeltaRjb2",
        binning=(70, 0., 7.),
        x_title=r"$\Delta R_{jetb2}^{reco}$",
    )
    config.add_variable(
        name=f"gen_DeltaR_genjetb2",
        expression=f"cutflow.DeltaR_genjetb2",
        binning=(70, 0., 7.),
        x_title=r"$\Delta R_{jetb2}^{gen}$",
    )
    #config.add_variable(
    #    name=f"b1_and_b2_in_fatjet",
    #    expression=f"cutflow.b1_and_b2_in_fatjet",
    #    binning=(2, 0, 2),
    #    x_title=r"b1 and b2 in fatjet",
    #)
    config.add_variable(
        name=f"b1_and_b2_in_fatjet_coffea",
        expression=f"cutflow.b1_and_b2_in_fatjet_coffea",
        binning=(2, 0, 2),
        x_title=r"b1 and b2 in fatjet with coffea distance",
    )
    config.add_variable(
        name=f"b1_and_b2_in_genjetak8_coffea",
        expression=f"cutflow.b1_and_b2_in_genjetak8_coffea",
        binning=(2, 0, 2),
        x_title=r"b1 and b2 in GenJetAK8 with coffea distance",
    )
    config.add_variable(
        name=f"FatJet_particleNet_HbbvsQCD",
        expression=f"cutflow.FatJet_particleNet_HbbvsQCD",
        binning=(30, 0., 1.),
        x_title=r"FatJet particleNet HbbvsQCD",
    )
    for jet in ["leadingJet", "NleadingJet", "NNleadingJet", "NNNleadingJet"]:
        config.add_variable(
            name=f"matched_{jet}_partonFlavour",
            expression=f"cutflow.{jet}_partonFlavour",
            binning=(34, -10.5, 23.5),
            unit="PdgId",
            x_title=r"$partonFlavour_{%s}^{matched}$" % (jet),
        )
        config.add_variable(
            name=f"matched_{jet}_hadronFlavour",
            expression=f"cutflow.{jet}_hadronFlavour",
            binning=(34, -10.5, 23.5),
            unit="PdgId",
            x_title=r"$hadronFlavour_{%s}^{matched}$" % (jet),
        )
    for genjet in ["leadingGenJet", "NleadingGenJet", "NNleadingGenJet", "NNNleadingGenJet"]:
        config.add_variable(
            name=f"gen_{genjet}_partonFlavour",
            expression=f"cutflow.{genjet}_partonFlavour",
            binning=(34, -10.5, 23.5),
            unit="PdgId",
            x_title=r"$partonFlavour_{%s}^{GenJet}$" % (genjet),
        )
        config.add_variable(
            name=f"gen_{genjet}_hadronFlavour",
            expression=f"cutflow.{genjet}_hadronFlavour",
            binning=(34, -10.5, 23.5),
            unit="PdgId",
            x_title=r"$hadronFlavour_{%s}^{GenJet}$" % (genjet),
        )
    for FatJet in ["leadingFatJet", "NleadingFatJet", "NNleadingFatJet", "NNNleadingFatJet"]:
        config.add_variable(
            name=f"matched_{FatJet}_partonFlavour",
            expression=f"cutflow.{FatJet}_partonFlavour",
            binning=(34, -10.5, 23.5),
            unit="PdgId",
            x_title=r"$partonFlavour_{%s}^{matched}$" % (FatJet),
        )
        config.add_variable(
            name=f"matched_{FatJet}_hadronFlavour",
            expression=f"cutflow.{FatJet}_hadronFlavour",
            binning=(34, -10.5, 23.5),
            unit="PdgId",
            x_title=r"$hadronFlavour_{%s}^{matched}$" % (FatJet),
        )
    for genjetak8 in ["leadingGenJetAK8", "NleadingGenJetAK8", "NNleadingGenJetAK8", "NNNleadingGenJetAK8"]:
        config.add_variable(
            name=f"gen_{genjetak8}_partonFlavour",
            expression=f"cutflow.{genjetak8}_partonFlavour",
            binning=(34, -10.5, 23.5),
            unit="PdgId",
            x_title=r"$partonFlavour_{%s}^{GenJet}$" % (genjetak8),
        )
        config.add_variable(
            name=f"gen_{genjetak8}_hadronFlavour",
            expression=f"cutflow.{genjetak8}_hadronFlavour",
            binning=(34, -10.5, 23.5),
            unit="PdgId",
            x_title=r"$hadronFlavour_{%s}^{GenJet}$" % (genjetak8),
        )
