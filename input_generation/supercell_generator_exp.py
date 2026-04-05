import os
from ase.io import read, write
from ase.build.supercells import make_supercell

# Define the list of metals you want to process
metals = ["Ni", "Pd", "Pt", "Cu", "Ag", "Au", "Al"]

# Supercell transformation matrix (2x2x2)
N = 2
M = [[N, 0, 0], [0, N, 0], [0, 0, N]]

# Loop through each metal
for metal in metals:
    bulk_poscar = f"POSCAR_bulk_exp_{metal}"

    # Check if the input POSCAR exists
    if not os.path.exists(bulk_poscar):
        print(f"File {bulk_poscar} not found. Skipping...")
        continue

    try:
        # Load the bulk structure
        structure = read(bulk_poscar)
    except Exception as e:
        print(f"Error reading {bulk_poscar}: {e}")
        continue

    # --- Step 1: Create pristine supercell ---
    supercell = make_supercell(structure, M)
    pristine_filename = f"POSCAR_supercell_pristine_{metal}"
    write(pristine_filename, supercell, sort=False, direct=True, vasp5=True)
    print(f"[{metal}] Pristine supercell saved as {pristine_filename}")

    # --- Step 2: Create defective supercell (remove atom at index 2) ---
    defective_supercell = supercell.copy()
    atom_index_to_remove = 28
    if atom_index_to_remove >= len(defective_supercell):
        print(f"[{metal}] Skipping defect: atom index {atom_index_to_remove} out of bounds (only {len(defective_supercell)} atoms).")
        continue

    defective_supercell.pop(atom_index_to_remove)
    defective_filename = f"POSCAR_supercell_defective_{metal}_rm{atom_index_to_remove}"
    write(defective_filename, defective_supercell, sort=False, direct=True, vasp5=True)
    print(f"[{metal}] Defective supercell saved as {defective_filename}")

