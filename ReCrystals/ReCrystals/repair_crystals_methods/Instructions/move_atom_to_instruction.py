"""
move_atom_to_instruction.py, Geoffrey Weal, 5/4/24

This method is designed to move the atoms in a molecule.
"""
from copy import deepcopy
from ReCrystals.ReCrystals.repair_crystals_methods.Utilities.get_original_to_modified_atom_indices_for_mol import get_original_to_modified_atom_indices_for_mol
from ReCrystals.ReCrystals.repair_crystals_methods.Modification_Methods.move_atom_in_molecule_to           import move_atom_in_molecule_to

def move_atom_to_instruction(instruction, molecules):
	"""
	This method is designed to move the atoms in a molecule.

	Parameters
	----------
	instruction : dict. 
		This is the instruction you would like to perform upon the molecules in the crystal.
	molecules : dict. of ase.Atoms
		These are the molecules in the crystal (Only the structurally unique molecules due to the symmetry of the crystal).
	"""

	# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - 
	# PART I: Import input variables from the instruction dictionary.

	# First, get the molecule to move an atom in.
	molecule_name = deepcopy(instruction['molecule'])

	# Second, initialise the list to hold the atom in the molecule to move.
	atoms_to_move = []

	# Third, initialise the list to hold the positions to move the atom to
	positions_to_move_atom_to = []

	# Fourth, for each entry in the instruction['atoms'] dictionary:
	for original_atom_to_move, updated_position in sorted(instruction['atoms'].items(),key=lambda x:x[0]):

		# 4.1: Add the atom to move to atoms_to_move
		atoms_to_move.append(original_atom_to_move)

		# 4.2: Add updated_position to  positions_to_move_atom_to
		positions_to_move_atom_to.append(updated_position)

	# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - 
	# Part II: Make sure that the variable above have been updated so they are ready for the "move_atom_in_molecule_to" method.

	# Fifth, remove any solvent tags in the molecule name. 
	if isinstance(molecule_name, str):
		molecule_name = int(molecule_name.replace('S',''))

	# Sixth, obtain the original_to_modified_atom_indices_for_mol dictionary for molecules[molecule_name]
	original_to_modified_atom_indices_for_mol = get_original_to_modified_atom_indices_for_mol(molecules[molecule_name])

	# Seventh, update the atom indices in atoms_to_move based on original_to_modified_atom_indices
	#          * This is required because atoms may have been removed in a previous instruction.
	#          * original_to_modified_atom_indices indices how the indices of atoms have changed due to previous atom removal commands. 
	atoms_to_move = [original_to_modified_atom_indices_for_mol[original_atom_to_move] for original_atom_to_move in atoms_to_move]

	# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - 
	# PART III: Run the "move_atom_in_molecule_to" method.

	# Seventh, move atom in molecule.
	move_atom_in_molecule_to(molecule_name, atoms_to_move, positions_to_move_atom_to, molecules)

	# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - 
