"""
get_original_to_modified_atom_indices_for_mol.py, Geoffrey Weal, 6/4/24

This method is designed to obtain the original_to_modified_atom_indices_for_mol dictionary. 
"""

def get_original_to_modified_atom_indices_for_mol(molecule):
	"""
	This method is designed to obtain the original_to_modified_atom_indices_for_mol dictionary. 

	This dictionary is designed to determine how to convert the original index of an atom in a molecule to what it is now currently after modifications performed by the ReCrystals program.

	Parameters
	----------
	molecule : ase.Atoms
		This is the molecule to obtain the original_to_modified_atom_indices for

	Returns
	-------
	original_to_modified_atom_indices_for_mol : dict.
		This is the dictionary that allows the user to convert the original index for an atom in the molecule to the current index the atoms are now after modifications performed by the ReCrystals program.
	"""

	# First, initialise the original_to_modified_atom_indices_for_mol dictionary 
	original_to_modified_atom_indices_for_mol = {}

	# Second, for each atom in the molecule:
	for current_atom_index, original_atom_index in enumerate(molecule.get_array('original_indices')):

		# 2.1: If original_atom_index is None, move on.
		if original_atom_index == -1:
			continue

		# 2.2: Make sure that original_atom_index has not already been added to original_to_modified_atom_indices_for_mol
		if original_atom_index in original_to_modified_atom_indices_for_mol.keys():
			to_string  = 'Error: original_atom_index is already in original_to_modified_atom_indices_for_mol\n'
			to_string += 'There may be a programming error\n'
			to_string += f'original_atom_index = {original_atom_index}\n'
			to_string += f'original_to_modified_atom_indices_for_mol.keys() = {original_to_modified_atom_indices_for_mol.keys()}\n'
			to_string += f'original_to_modified_atom_indices_for_mol = {original_to_modified_atom_indices_for_mol}\n'
			to_string += 'Check this'
			raise Exception(to_string)

		# 2.3: Add original_atom_index to original_to_modified_atom_indices_for_mol
		original_to_modified_atom_indices_for_mol[original_atom_index] = current_atom_index

	# Third, return original_to_modified_atom_indices_for_mol
	return original_to_modified_atom_indices_for_mol