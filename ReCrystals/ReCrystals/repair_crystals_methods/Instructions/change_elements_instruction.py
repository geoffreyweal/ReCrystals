"""
remove_molecule_instruction.py, Geoffrey Weal, 5/4/24

This method is designed to change the element of atoms in the molecule. 
"""
from copy import deepcopy
from ReCrystals.ReCrystals.repair_crystals_methods.Utilities.get_original_to_modified_atom_indices_for_mol import get_original_to_modified_atom_indices_for_mol
from ReCrystals.ReCrystals.repair_crystals_methods.Modification_Methods.change_elements_of_atoms           import change_elements_of_atoms

def change_elements_instruction(instruction, molecules, molecule_graphs):
	"""
	This method is designed to change the element of atoms in the molecule. 

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

	# Second, input the data for "atoms" to change elements of, and the associated updated_elements list.
	if isinstance(instruction['atoms'],dict):

		# 2.1: If instruction['atoms'] is a dict:
		#      * The keys are the indices of the atoms to change the element of.
		#      * The values are the elements that you want to change the atoms to. 

		# 2.1.1: Initialise the list to hold the atom indices to change elements of.
		atoms_to_change_elements_of  = []

		# 2.1.2: Initialise the list of the elements to change the atoms to.
		updated_elements = []

		# 2.1.3: For each atom index and the element to change the atom to:
		for original_atom_to_change_elements_of, new_element in sorted(instruction['atoms'].items(),key=lambda x:x[0]):

			# 2.1.3.1: Add original_atom_to_add_hydrogens_to to atoms_to_add_hydrogens_to.
			atoms_to_change_elements_of.append(original_atom_to_change_elements_of)

			# 2.1.3.2: Add the updated element for each atom in atoms_to_change_elements_of to the updated_elements list. 
			updated_elements.append(new_element)

	else:

		# 2.2: If instruction['atoms'] is a not a dict:
		#      * atoms_to_change_elements_of: the "atoms" that you want to change the elements of
		#      * The elements you want to change the atoms in iatoms_to_change_elements_of to

		# 2.2.1: Get the atom in the molecule to change the elements of.
		atoms_to_change_elements_of = deepcopy(instruction['atoms'])

		# 2.2.2: Get the position to move the atom to
		updated_elements = deepcopy(instruction['updated_elements'])

	# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - 
	# Part II: Make sure that the variable above have been updated so they are ready for the "change_elements_of_atoms" method.

	# Third, remove any solvent tags in the molecule name. 
	if isinstance(molecule_name, str):
		molecule_name = int(molecule_name.replace('S',''))

	# Fourth, if atoms_to_change_elements_of is an integer, convert it into a list 
	if isinstance(atoms_to_change_elements_of, int):
		atoms_to_change_elements_of = [atoms_to_change_elements_of]

	# Fifth, obtain the original_to_modified_atom_indices_for_mol dictionary for molecules[molecule_name]
	original_to_modified_atom_indices_for_mol = get_original_to_modified_atom_indices_for_mol(molecules[molecule_name])

	# Sixth, update the atom indices in atoms_to_add_hydrogens_to based on original_to_modified_atom_indices
	#         * This is required because atoms may have been removed in a previous instruction.
	#         * original_to_modified_atom_indices indices how the indices of atoms have changed due to previous atom removal commands. 
	atoms_to_change_elements_of = [original_to_modified_atom_indices_for_mol[original_atom_to_change_elements_of] for original_atom_to_change_elements_of in atoms_to_change_elements_of]

	# Seventh, if updated_elements is an integer, convert it into a list of same size as atoms_to_change_elements_of
	if isinstance(updated_elements, str):
		updated_elements = [updated_elements]*len(atoms_to_change_elements_of)

	# Eighth, check that the length of atoms_to_change_elements_of is the same as the length of updated_elements
	if not len(atoms_to_change_elements_of) == len(updated_elements):
		to_string  = 'Error: The length of the lists recording "atoms_to_change_elements_of" and "updated_elements" are not the same\n'
		to_string += f'number of "atoms_to_change_elements_of" to add hydrogens to: {len(atoms_to_change_elements_of)}\n'
		to_string += f'number of "updated_elements": {len(updated_elements)}\n'
		to_string += f'"atoms_to_change_elements_of" list: {atoms_to_change_elements_of}\n'
		to_string += f'"updated_elements" list: {updated_elements}\n'
		to_string += 'Check this.'
		raise Exception(to_string)

	# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - 
	# PART III: Run the "change_elements_of_atoms" method.

	# Ninth, move atom in molecule.
	change_elements_of_atoms(molecule_name, atoms_to_change_elements_of, updated_elements, molecules, molecule_graphs)

	# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - 












