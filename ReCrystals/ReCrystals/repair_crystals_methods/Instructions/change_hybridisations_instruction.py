"""
remove_molecule_instruction.py, Geoffrey Weal, 5/4/24

This method is designed to remove molecules based on instruction.
"""
from copy import deepcopy
from ReCrystals.ReCrystals.repair_crystals_methods.Utilities.get_original_to_modified_atom_indices_for_mol import get_original_to_modified_atom_indices_for_mol
from ReCrystals.ReCrystals.repair_crystals_methods.Modification_Methods.change_hybridisations_of_atoms     import change_hybridisations_of_atoms

def change_hybridisations_instruction(instruction, molecules, molecule_graphs):
	"""
	This method is designed to change the hybridisation of atoms in the molecule. 

	Parameters
	----------
	instruction : dict. 
		This is the instruction you would like to perform upon the molecules in the crystal.
	molecules : dict. of ase.Atoms
		These are the molecules in the crystal (Only the structurally unique molecules due to the symmetry of the crystal).
	molecule_graphs : dict. of networkx.Graphs
		These are the graphs associated with each molecule in the molecules dictionary. 
	"""

	# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - 
	# PART I: Import input variables from the instruction dictionary.

	# First, get the molecule to move an atom in.
	molecule_name = deepcopy(instruction['molecule'])

	# Second, input the data for "atoms" to change hybridisations of, and the associated updated_hybridisations list.
	if isinstance(instruction['atoms'],dict):

		# 2.1: If instruction['atoms'] is a dict:
		#      * The keys are the indices of the atoms to change the hybridisation of.
		#      * The values are the hybridisations that you want to change the atoms to. 

		# 2.1.1: Initialise the list to hold the atom indices to change hybridisations of.
		atoms_to_change_hybridisations_of  = []

		# 2.1.2: Initialise the list of the hybridisations to change the atoms to.
		updated_hybridisations = []

		# 2.1.3: For each atom index and the hybridisation to change the atom to:
		for original_atom_to_change_hybridisations_of, new_hybridisation in sorted(instruction['atoms'].items(),key=lambda x:x[0]):

			# 2.1.3.1: Add original_atom_to_add_hydrogens_to to atoms_to_add_hydrogens_to.
			atoms_to_change_hybridisations_of.append(original_atom_to_change_hybridisations_of)

			# 2.1.3.2: Add the updated hybridisation for each atom in atoms_to_change_hybridisations_of to the updated_hybridisations list. 
			updated_hybridisations.append(new_hybridisation)

	else:

		# 2.2: If instruction['atoms'] is a not a dict:
		#      * atoms_to_change_hybridisations_of: the "atoms" that you want to change the hybridisations of
		#      * The hybridisations you want to change the atoms in iatoms_to_change_hybridisations_of to

		# 2.2.1: Get the atom in the molecule to change the hybridisations of.
		atoms_to_change_hybridisations_of = deepcopy(instruction['atoms'])

		# 2.2.2: Get the position to move the atom to
		updated_hybridisations = deepcopy(instruction['updated_hybridisations'])

	# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - 
	# Part II: Make sure that the variable above have been updated so they are ready for the "change_hybridisations_of_atoms" method.

	# Third, remove any solvent tags in the molecule name. 
	if isinstance(molecule_name, str):
		molecule_name = int(molecule_name.replace('S',''))

	# Fourth, if atoms_to_change_hybridisations_of is an interger, convert it into a list 
	if isinstance(atoms_to_change_hybridisations_of, int):
		atoms_to_change_hybridisations_of = [atoms_to_change_hybridisations_of]

	# Fifth, obtain the original_to_modified_atom_indices_for_mol dictionary for molecules[molecule_name]
	original_to_modified_atom_indices_for_mol = get_original_to_modified_atom_indices_for_mol(molecules[molecule_name])

	# Sixth, update the atoms to change hybridisation list.
	atoms_to_change_hybridisations_of = [original_to_modified_atom_indices_for_mol[atom_to_change_hybridisations_of] for atom_to_change_hybridisations_of in atoms_to_change_hybridisations_of]

	# Seventh, if updated_hybridisations is an integer, convert it into a list of same size as atoms_to_change_hybridisations_of
	if isinstance(updated_hybridisations, str):
		updated_hybridisations = [updated_hybridisations]*len(atoms_to_change_hybridisations_of)

	# Eighth, check that the length of atoms_to_change_hybridisations_of is the same as the length of updated_hybridisations
	if not len(atoms_to_change_hybridisations_of) == len(updated_hybridisations):
		to_string  = 'Error: The length of the lists recording "atoms_to_change_hybridisations_of" and "updated_hybridisations" are not the same\n'
		to_string += f'number of "atoms_to_change_hybridisations_of" to add hydrogens to: {len(atoms_to_change_hybridisations_of)}\n'
		to_string += f'number of "updated_hybridisations": {len(updated_hybridisations)}\n'
		to_string += f'"atoms_to_change_hybridisations_of" list: {atoms_to_change_hybridisations_of}\n'
		to_string += f'"updated_hybridisations" list: {updated_hybridisations}\n'
		to_string += 'Check this.'
		raise Exception(to_string)

	# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - 
	# PART III: Run the "change_hybridisations_of_atoms" method.

	# Ninth, move atom in molecule.
	change_hybridisations_of_atoms(molecule_name, atoms_to_change_hybridisations_of, updated_hybridisations, molecules, molecule_graphs)

	# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - 