import pandas as pd
import numpy as np

# ---------- 1. Final Parameter Names (Updated Units) ----------

PARAM_NAMES = [
    "k_translation_collagen",          # 1/h
    "k_inhibition_collagen_by_miR378", # 1/h
    "k_uptake_exosomes",               # 1/h
    "k_exo_deg",                       # 1/h
    "k_mRNA_deg_collagen",             # 1/h
    "k_protein_deg_collagen",          # 1/h
    "k_miR_deg",                       # 1/h
    "k_miR_release",                   # 1/h

    "k_miRISC_formation",              # 1/(nM*h)
    "k_miRISC_dissociation_r",         # 1/h

    "k_mRNA_miRISC_binding_r",         # 1/h
    "k_mRNA_miRISC_binding_f",         # 1/(nM*h)

    "k_AGO2_synth",                    # nM/h
    "k_AGO2_deg",                      # 1/h

    "k_deadenylase_synth",             # nM/h
    "k_deadenylase_deg",               # 1/h

    "k_TGFB1_signal",                  # nM/h

    "k_SMAD_nuclear_translocation_f",  # 1/h
    "k_SMAD_nuclear_translocation_r",  # 1/h
    "k_SMAD_deactivation",             # 1/h

    "k_SMAD_activation",               # 1/h
    "k_TGFB1_activation",              # 1/h
    "k_TGFB1_degradation",             # 1/h

    "k_transcript"                     # 1/h
]

# ---------- 2. Final Parameter Values (Updated) ----------

PARAM_VALUES = [
    0.531419,
    0.0162442,
    1.16194,
    0.841679,
    0.0433217,
    0.000386801,
    0.025993,
    0.205185,

    1.5,        # UPDATED
    0.03,

    0.3,
    2.0,        # UPDATED

    0.249,
    0.03,

    0.498,
    0.03,

    0.332,

    1.38629,
    0.7,
    0.8,

    3.85358,
    0.203075,
    0.214546,

    0.10259
]

# ---------- 3. Build and Save Population CSV ----------

df = pd.DataFrame({
    "parameter_name": PARAM_NAMES,
    "value": PARAM_VALUES
})

df.to_csv("saem_param_population.csv", index=False)
print("Saved updated saem_param_population.csv")
