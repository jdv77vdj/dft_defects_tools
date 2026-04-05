import sys
from ase import io
from ase.io import read, write

# Check if the correct number of arguments is provided
if len(sys.argv) != 3:
    print("Usage: python create_defective_supercell.py name_of_file atom_index_to_remove")
    sys.exit(1)

# Read the filename and atom index from command-line arguments
file_name = sys.argv[1]
atom_index = int(sys.argv[2])

try:
    # Load the supercell structure from the specified file
    structure = io.read(file_name)
except Exception as e:
    print(f"Error reading file {file_name}: {e}")
    sys.exit(1)

# Ensure the atom index is valid
if atom_index < 0 or atom_index >= len(structure):
    print(f"Error: Invalid atom index {atom_index}. The structure contains {len(structure)} atoms.")
    sys.exit(1)

# Remove the atom at the specified index (index is 0-based)
structure.pop(atom_index)

# Write the modified supercell to a new POSCAR file without sorting
output_filename = f"defective_supercell_{atom_index}.poscar"
write(output_filename, structure, sort=False, direct=False)

print(f"Defective supercell created by removing atom {atom_index} and saved as {output_filename}")

