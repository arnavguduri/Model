import pandas as pd
import numpy as np

# ---------------- 1. Parameter Names (Final) ----------------

PARAM_NAMES = [
    "k_translation_collagen",
    "k_inhibition_collagen_by_miR378",
    "k_uptake_exosomes",
    "k_exo_deg",
    "k_mRNA_deg_collagen",
    "k_protein_deg_collagen",
    "k_miR_deg",
    "k_miR_release",

    "k_miRISC_formation",
    "k_miRISC_dissociation_r",

    "k_mRNA_miRISC_binding_r",
    "k_mRNA_miRISC_binding_f",

    "k_AGO2_synth",
    "k_AGO2_deg",

    "k_deadenylase_synth",
    "k_deadenylase_deg",

    "k_TGFB1_signal",

    "k_SMAD_nuclear_translocation_f",
    "k_SMAD_nuclear_translocation_r",
    "k_SMAD_deactivation",

    "k_SMAD_activation",
    "k_TGFB1_activation",
    "k_TGFB1_degradation",

    "k_transcript"
]

# ---------------- 2. Updated Central Values ----------------

CENTER_VALUES = np.array([
    0.531419,
    0.0162442,
    1.16194,
    0.841679,
    0.0433217,
    0.000386801,
    0.025993,
    0.205185,

    1.5,       # UPDATED
    0.03,

    0.3,
    2.0,       # UPDATED

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
])

# Variability for generating synthetic per-study values
VARIABILITY = 0.15

num_studies = 10
data = {}

for i in range(num_studies):
    study_id = f"S{i+1}"
    sample = CENTER_VALUES * np.exp(np.random.normal(0, VARIABILITY, size=len(CENTER_VALUES)))
    data[study_id] = sample

df = pd.DataFrame(data, index=PARAM_NAMES).T
df.insert(0, "study_id", df.index)

df.to_csv("per_study_params_for_saem.csv", index=False)
print("Saved updated per_study_params_for_saem.csv")
