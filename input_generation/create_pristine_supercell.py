import sys
from ase import io
from ase.io import read, write
from ase.build.supercells import make_supercell

# Check if the correct number of arguments is provided
if len(sys.argv) != 2:
    print("Usage: python create_pristine_supercell.py name_of_file")
    sys.exit(1)

# Read the filename from command-line arguments
file_name = sys.argv[1]

# Define the supercell size (NxNxN)
N = 2
M = [[N, 0, 0], [0, N, 0], [0, 0, N]]

try:
    # Read the structure from the specified file
    structure = io.read(file_name)
except Exception as e:
    print(f"Error reading file {file_name}: {e}")
    sys.exit(1)

# Create the supercell
sc = make_supercell(structure, M)

# Write the supercell to a new POSCAR file
write('POSCAR_supercell', sc, sort=True, direct=False)

print(f"Supercell created and saved as POSCAR_supercell from {file_name}")

