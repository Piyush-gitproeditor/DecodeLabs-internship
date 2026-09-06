import pandas as pd
# LOAD DATASET

df = pd.read_excel("PCBuilder_Recommendation_Dataset.xlsx")

# SEPARATE COMPONENTS

cpus = df[df["Type"] == "CPU"]
gpus = df[df["Type"] == "GPU"]
motherboards = df[df["Type"] == "Motherboard"]
ram = df[df["Type"] == "RAM"]
storage = df[df["Type"] == "Storage"]
psus = df[df["Type"] == "PSU"]
cases = df[df["Type"] == "Case"]
coolers = df[df["Type"] == "CPU Cooler"]

# USER INPUT

print("\n                                ")
print("      WELCOME TO PC BUILD RECOMMENDER       ")
print("                                 \n")

budget = float(input("Enter your budget ($): "))

print("\nWhat is your primary use?")
print("1. Gaming")
print("2. Programming")
print("3. Video Editing")
print("4. AI / ML")

use_choice = int(input("Enter choice (1-4): "))

use_options = {
    1: "Gaming",
    2: "Programming",
    3: "Video Editing",
    4: "AI / ML"
}

primary_use = use_options.get(use_choice, "Invalid Choice")

print("\nChoose your target resolution:")
print("1. 1080p")
print("2. 1440p")
print("3. 4K")

resolution_choice = int(input("Enter choice (1-3): "))

resolution_options = {
    1: "1080p",
    2: "1440p",
    3: "4K"
}

resolution = resolution_options.get(resolution_choice, "Invalid Choice")

ram_required = int(input("\nRequired RAM (GB): "))

print("\nStorage unit:")
print("1. GB")
print("2. TB")

storage_unit_choice = int(input("Enter choice (1-2): "))

if storage_unit_choice == 1:
    storage_required_gb = float(input("Required storage (GB): "))

elif storage_unit_choice == 2:
    storage_required_tb = float(input("Required storage (TB): "))
    storage_required_gb = storage_required_tb * 1000

else:
    print("Invalid choice!")
    storage_required_gb = 0


# CREATE USER PROFILE

preferences = {
    "budget": budget,
    "primary_use": primary_use,
    "resolution": resolution,
    "ram_required": ram_required,
    "storage_required_gb": storage_required_gb
}
suitable_ram = ram[
    ram["Capacity_or_VRAM_GB"] >= ram_required
]

print("\nSuitable RAM:")
print(suitable_ram[["Brand", "Model", "Capacity_or_VRAM_GB", "Price_USD"]])


suitable_storage = storage[
    storage["Capacity_or_VRAM_GB"] >= storage_required_gb
]

print("\nSuitable Storage:")
print(suitable_storage[
    ["Brand", "Model", "Capacity_or_VRAM_GB", "Price_USD"]
])

# CPU candidates
suitable_cpus = cpus.copy()

# GPU candidates
suitable_gpus = gpus.copy()

print("\nSuitable CPUs:")
print(suitable_cpus[
    ["Brand", "Model", "Price_USD", "Benchmark_Score_0_100"]
])

print("\nSuitable GPUs:")
print(suitable_gpus[
    ["Brand", "Model", "Price_USD", "Benchmark_Score_0_100"]
])

# DISPLAY USER PROFILE

print("\n                               ")
print("        YOUR REQUIREMENTS        ")
print("                                  \n")

print(f"Budget: ${preferences['budget']:,.0f}")
print(f"Primary Use: {preferences['primary_use']}")
print(f"Resolution: {preferences['resolution']}")
print(f"RAM Required: {preferences['ram_required']} GB")
if storage_unit_choice == 1:
    print(f"Storage Required: {storage_required_gb:.0f} GB")
else:
    print(f"Storage Required: {storage_required_gb / 1000:g} TB")