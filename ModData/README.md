# ModData Update Instructions: Expanded Wildlife Pack Units

To update the database with new or changed units from the Expanded Wildlife Pack mod, follow these steps:

## 1. Replace the Units.po File
- Copy the latest `Expanded Wildlife Pack - Units.po` file from the mod into the `ModData` directory, replacing the existing file.

## 2. Run the Python Script
- Open a terminal in the project root directory.
- Run the following command to extract and update the unit data:
  
  ```
  python ModData/extract_unit_names.py
  ```
- This will:
  - Parse the `.po` file and update `Expanded Wildlife Pack - Unit Names.json`.
  - Filter the main unit database and create `ModdedUnits.json` with only the enabled units from the pack.

## 3. Add Unit Preview Images
- For each new or updated unit, add a preview image in `.avif` format.
- Place the image in the appropriate directory (e.g., `PreviewsAvif/`).
- The file name must be all lower case, with spaces replaced by underscores (`_`).
- The format is:
  
  ```
  unit_name.avif
  ```
  For example: `bald_eagle.avif`, `great_eagle.avif`, etc.

---

**Note:**
- Make sure the unit name in the `.avif` file matches exactly (all lower case, spaces as underscores) the name in the database.
- If you disable a unit, remove or archive its preview image as needed.

If you have any issues, check the script output for errors or review the unit names in `Expanded Wildlife Pack - Unit Names.json`.
