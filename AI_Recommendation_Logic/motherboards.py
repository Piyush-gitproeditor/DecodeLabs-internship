import pandas as pd
from pathlib import Path

dataset_path = Path(__file__).resolve().parent / "PCBuilder_Recommendation_Dataset.xlsx"
df = pd.read_excel(dataset_path)
motherboards = df[df["Type"] == "Motherboard"]

# print("\nMOTHERBOARD DATA")
# print("--------------------------------")
#
# print(motherboards[
#     [
#         "Brand",
#         "Model",
#         "Price_USD",
#         "Chipset_or_Subtype",
#         "CPU_Socket",
#         "RAM_Type",
#         "Form_Factor_or_Interface",
#         "M2_Slots"
#     ]
# ])
def find_motherboards_for_cpu(cpu, motherboards):

    compatible_motherboards = motherboards[
        motherboards["CPU_Socket"] == cpu["CPU_Socket"]
    ]

    return compatible_motherboards
