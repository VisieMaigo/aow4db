import json
import re

input_file = "ModData/Expanded Wildlife Pack - Units.po"
output_file = "ModData/Expanded Wildlife Pack - Unit Names.json"
units_json_file = "Data/Units.json"
modded_units_output = "ModData/ModdedUnits.json"

disabled_units = {"Young Panther"}  # Add more unit names to this set as needed

unit_names = {}

# Step 1: Extract unit names from the .po file and write to output_file
with open(input_file, encoding="utf-8") as f:
    lines = f.readlines()
    for line in lines:
        match = re.match(r'^msgstr\s+"(.+\^n)"', line)
        if match:
            name = match.group(1)
            clean_name = name[:-2] if name.endswith('^n') else name
            unit_names[clean_name] = False if clean_name in disabled_units else True

with open(output_file, "w", encoding="utf-8") as f:
    json.dump(unit_names, f, ensure_ascii=False, indent=2)

# Step 2: Extract data for enabled units from Data/Units.json and write to ModData/ModdedUnits.json
with open(units_json_file, encoding="utf-8") as f:
    all_units = json.load(f)

# Load the enabled unit names from the just-written output_file
with open(output_file, encoding="utf-8") as f:
    enabled_units = json.load(f)

# Create a list of units whose name is present and set to True in enabled_units
modded_units = [unit for unit in all_units if unit.get("name") in enabled_units and enabled_units[unit["name"]]]

with open(modded_units_output, "w", encoding="utf-8") as f:
    json.dump(modded_units, f, ensure_ascii=False, indent=2)
