import pandas as pd

# 1) Load 10-study table
df = pd.read_csv("per_study_params_for_saem.csv")

# 2) Compute median across studies
param_medians = df.drop(columns=["study_id"]).median()

# 3) Convert to vertical format
vertical = param_medians.reset_index()
vertical.columns = ["parameter_name", "value"]

# 4) Pretty-print
print("\n" + "="*60)
print("  FINAL PARAMETER ESTIMATES (VERTICAL TABLE)")
print("="*60 + "\n")
print(vertical.to_string(index=False))

# 5) Save
output_file = "single_param_estimates_vertical.csv"
vertical.to_csv(output_file, index=False)
print(f"\nSaved vertical table to: {output_file}\n")
