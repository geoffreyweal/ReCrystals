"""
remove_molecule_instruction.py, Geoffrey Weal, 31/5/24

This method is designed to remove molecules based on instruction.
"""
from copy import deepcopy
from ReCrystals.ReCrystals.repair_crystals_methods.Utilities.get_original_to_modified_atom_indices_for_mol     import get_original_to_modified_atom_indices_for_mol
from ReCrystals.ReCrystals.repair_crystals_methods.Modification_Methods.change_added_or_modified_tags_of_atoms import change_added_or_modified_tags_of_atoms

def change_added_or_modified_tags_instruction(instruction, molecules, molecule_graphs):
	"""
	This method is designed to change the added_or_modified_tag of atoms in the molecule. 

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

	# Second, input the data for "atoms" to change added_or_modified_tags of, and the associated updated_added_or_modified_tags list.
	if isinstance(instruction['atoms'],dict):

		# 2.1: If instruction['atoms'] is a dict:
		#      * The keys are the indices of the atoms to change the added_or_modified_tag of.
		#      * The values are the added_or_modified_tags that you want to change the atoms to. 

		# 2.1.1: Initialise the list to hold the atom indices to change added_or_modified_tags of.
		atoms_to_change_added_or_modified_tags_of  = []

		# 2.1.2: Initialise the list of the added_or_modified_tags to change the atoms to.
		updated_added_or_modified_tags = []

		# 2.1.3: For each atom index and the added_or_modified_tag to change the atom to:
		for original_atom_to_change_added_or_modified_tags_of, new_added_or_modified_tag in sorted(instruction['atoms'].items(),key=lambda x:x[0]):

			# 2.1.3.1: Add original_atom_to_add_hydrogens_to to atoms_to_add_hydrogens_to.
			atoms_to_change_added_or_modified_tags_of.append(original_atom_to_change_added_or_modified_tags_of)

			# 2.1.3.2: Add the updated added_or_modified_tag for each atom in atoms_to_change_added_or_modified_tags_of to the updated_added_or_modified_tags list. 
			updated_added_or_modified_tags.append(new_added_or_modified_tag)

	else:

		# 2.2: If instruction['atoms'] is a not a dict:
		#      * atoms_to_change_added_or_modified_tags_of: the "atoms" that you want to change the added_or_modified_tags of
		#      * The added_or_modified_tags you want to change the atoms in iatoms_to_change_added_or_modified_tags_of to

		# 2.2.1: Get the atom in the molecule to change the added_or_modified_tags of.
		atoms_to_change_added_or_modified_tags_of = deepcopy(instruction['atoms'])

		# 2.2.2: Get the position to move the atom to
		updated_added_or_modified_tags = deepcopy(instruction['updated_added_or_modified_tags'])

	# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - 
	# Part II: Make sure that the variable above have been updated so they are ready for the "change_added_or_modified_tags_of_atoms" method.

	# Third, remove any solvent tags in the molecule name. 
	if isinstance(molecule_name, str):
		molecule_name = int(molecule_name.replace('S',''))

	# Fourth, if atoms_to_change_added_or_modified_tags_of is an interger, convert it into a list 
	if isinstance(atoms_to_change_added_or_modified_tags_of, int):
		atoms_to_change_added_or_modified_tags_of = [atoms_to_change_added_or_modified_tags_of]

	# Fifth, obtain the original_to_modified_atom_indices_for_mol dictionary for molecules[molecule_name]
	original_to_modified_atom_indices_for_mol = get_original_to_modified_atom_indices_for_mol(molecules[molecule_name])

	# Sixth, update the atoms to change added_or_modified_tag list.
	atoms_to_change_added_or_modified_tags_of = [original_to_modified_atom_indices_for_mol[atom_to_change_added_or_modified_tags_of] for atom_to_change_added_or_modified_tags_of in atoms_to_change_added_or_modified_tags_of]

	# Seventh, if updated_added_or_modified_tags is an integer, convert it into a list of same size as atoms_to_change_added_or_modified_tags_of
	if isinstance(updated_added_or_modified_tags, bool):
		updated_added_or_modified_tags = [updated_added_or_modified_tags]*len(atoms_to_change_added_or_modified_tags_of)

	# Eighth, check that the length of atoms_to_change_added_or_modified_tags_of is the same as the length of updated_added_or_modified_tags
	if not len(atoms_to_change_added_or_modified_tags_of) == len(updated_added_or_modified_tags):
		to_string  = 'Error: The length of the lists recording "atoms_to_change_added_or_modified_tags_of" and "updated_added_or_modified_tags" are not the same\n'
		to_string += f'number of "atoms_to_change_added_or_modified_tags_of" to add hydrogens to: {len(atoms_to_change_added_or_modified_tags_of)}\n'
		to_string += f'number of "updated_added_or_modified_tags": {len(updated_added_or_modified_tags)}\n'
		to_string += f'"atoms_to_change_added_or_modified_tags_of" list: {atoms_to_change_added_or_modified_tags_of}\n'
		to_string += f'"updated_added_or_modified_tags" list: {updated_added_or_modified_tags}\n'
		to_string += 'Check this.'
		raise Exception(to_string)

	# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - 
	# PART III: Run the "change_added_or_modified_tags_of_atoms" method.

	# Ninth, move atom in molecule.
	change_added_or_modified_tags_of_atoms(molecule_name, atoms_to_change_added_or_modified_tags_of, updated_added_or_modified_tags, molecules, molecule_graphs)

	# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - 