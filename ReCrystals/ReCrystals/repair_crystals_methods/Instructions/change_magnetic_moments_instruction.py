"""
remove_molecule_instruction.py, Geoffrey Weal, 5/4/24

This method is designed to remove molecules based on instruction.
"""
from copy import deepcopy
from ReCrystals.ReCrystals.repair_crystals_methods.Utilities.get_original_to_modified_atom_indices_for_mol import get_original_to_modified_atom_indices_for_mol
from ReCrystals.ReCrystals.repair_crystals_methods.Modification_Methods.change_magnetic_moments_of_atoms   import change_magnetic_moments_of_atoms

def change_magnetic_moments_instruction(instruction, molecules):
	"""
	This method is designed to change the magnetic_moment of atoms in the molecule. 

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

	# Second, input the data for "atoms" to change magnetic_moments of, and the associated updated_magnetic_moments list.
	if isinstance(instruction['atoms'],dict):

		# 2.1: If instruction['atoms'] is a dict:
		#      * The keys are the indices of the atoms to change the magnetic_moment of.
		#      * The values are the magnetic_moments that you want to change the atoms to. 

		# 2.1.1: Initialise the list to hold the atom indices to change magnetic_moments of.
		atoms_to_change_magnetic_moments_of  = []

		# 2.1.2: Initialise the list of the magnetic_moments to change the atoms to.
		updated_magnetic_moments = []

		# 2.1.3: For each atom index and the magnetic_moment to change the atom to:
		for original_atom_to_change_magnetic_moments_of, new_magnetic_moment in sorted(instruction['atoms'].items(),key=lambda x:x[0]):

			# 2.1.3.1: Add original_atom_to_add_hydrogens_to to atoms_to_change_magnetic_moments_of.
			atoms_to_change_magnetic_moments_of.append(original_atom_to_change_magnetic_moments_of)

			# 2.1.3.2: Add the updated magnetic_moment for each atom in atoms_to_change_magnetic_moments_of to the updated_magnetic_moments list. 
			updated_magnetic_moments.append(new_magnetic_moment)

	else:

		# 2.2: If instruction['atoms'] is a not a dict:
		#      * atoms_to_change_magnetic_moments_of: the "atoms" that you want to change the magnetic_moments of
		#      * The magnetic_moments you want to change the atoms in iatoms_to_change_magnetic_moments_of to

		# 2.2.1: Get the atom in the molecule to change the magnetic_moments of.
		atoms_to_change_magnetic_moments_of = deepcopy(instruction['atoms'])

		# 2.2.2: Get the position to move the atom to
		updated_magnetic_moments = deepcopy(instruction['updated_magnetic_moments'])

	# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - 
	# Part II: Make sure that the variable above have been updated so they are ready for the "change_magnetic_moments_of_atoms" method.

	# Third, remove any solvent tags in the molecule name. 
	if isinstance(molecule_name, str):
		molecule_name = int(molecule_name.replace('S',''))

	# Fourth, if atoms_to_change_magnetic_moments_of is an interger, convert it into a list 
	if isinstance(atoms_to_change_magnetic_moments_of, int):
		atoms_to_change_magnetic_moments_of = [atoms_to_change_magnetic_moments_of]

	# Fifth, obtain the original_to_modified_atom_indices_for_mol dictionary for molecules[molecule_name]
	original_to_modified_atom_indices_for_mol = get_original_to_modified_atom_indices_for_mol(molecules[molecule_name])

	# Sixth, update the atom indices in atoms_to_change_magnetic_moments_of based on original_to_modified_atom_indices
	#         * This is required because atoms may have been removed in a previous instruction.
	#         * original_to_modified_atom_indices indices how the indices of atoms have changed due to previous atom removal commands. 
	atoms_to_change_magnetic_moments_of = [original_to_modified_atom_indices_for_mol[atom_to_change_elements_of] for atom_to_change_elements_of in atoms_to_change_magnetic_moments_of]

	# Seventh, if updated_magnetic_moments is an integer, convert it into a list of same size as atoms_to_change_hybridisation_of
	if isinstance(updated_magnetic_moments, int):
		updated_magnetic_moments = [updated_magnetic_moments]*len(atoms_to_change_magnetic_moments_of)

	# Eighth, check that the length of updated_magnetic_moments is the same as the length of updated_magnetic_moments
	if not len(atoms_to_change_magnetic_moments_of) == len(updated_magnetic_moments):
		to_string  = 'Error: The length of the lists recording "updated_magnetic_moments" and "updated_magnetic_moments" are not the same\n'
		to_string += f'number of "updated_magnetic_moments" to add hydrogens to: {len(updated_magnetic_moments)}\n'
		to_string += f'number of "updated_magnetic_moments": {len(updated_magnetic_moments)}\n'
		to_string += f'"updated_magnetic_moments" list: {updated_magnetic_moments}\n'
		to_string += f'"updated_magnetic_moments" list: {updated_magnetic_moments}\n'
		to_string += 'Check this.'
		raise Exception(to_string)

	# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - 
	# PART III: Run the "change_magnetic_moments_of_atoms" method.

	# Ninth, move atom in molecule.
	change_magnetic_moments_of_atoms(molecule_name, atoms_to_change_magnetic_moments_of, updated_magnetic_moments, molecules)

	# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - 

