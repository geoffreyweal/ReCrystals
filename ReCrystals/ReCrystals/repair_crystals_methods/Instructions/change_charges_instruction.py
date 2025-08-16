"""
remove_molecule_instruction.py, Geoffrey Weal, 5/4/24

This method is designed to remove molecules based on instruction.
"""
from copy import deepcopy
from ReCrystals.ReCrystals.repair_crystals_methods.Utilities.get_original_to_modified_atom_indices_for_mol import get_original_to_modified_atom_indices_for_mol
from ReCrystals.ReCrystals.repair_crystals_methods.Modification_Methods.change_charges_of_atoms            import change_charges_of_atoms

def change_charges_instruction(instruction, molecules):
	"""
	This method is designed to change the charge of atoms in the molecule. 

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

	# Second, input the data for "atoms" to change charges of, and the associated updated_charges list.
	if isinstance(instruction['atoms'],dict):

		# 2.1: If instruction['atoms'] is a dict:
		#      * The keys are the indices of the atoms to change the charge of.
		#      * The values are the charges that you want to change the atoms to. 

		# 2.1.1: Initialise the list to hold the atom indices to change charges of.
		atoms_to_change_charges_of  = []

		# 2.1.2: Initialise the list of the charges to change the atoms to.
		updated_charges = []

		# 2.1.3: For each atom index and the charge to change the atom to:
		for original_atom_to_change_charges_of, new_charge in sorted(instruction['atoms'].items(),key=lambda x:x[0]):

			# 2.1.3.1: Add original_atom_to_add_hydrogens_to to atoms_to_change_charges_of.
			atoms_to_change_charges_of.append(original_atom_to_change_charges_of)

			# 2.1.3.2: Add the updated charge for each atom in atoms_to_change_charges_of to the updated_charges list. 
			updated_charges.append(new_charge)

	else:

		# 2.2: If instruction['atoms'] is a not a dict:
		#      * atoms_to_change_charges_of: the "atoms" that you want to change the charges of
		#      * The charges you want to change the atoms in iatoms_to_change_charges_of to

		# 2.2.1: Get the atom in the molecule to change the charges of.
		atoms_to_change_charges_of = deepcopy(instruction['atoms'])

		# 2.2.2: Get the position to move the atom to
		updated_charges = deepcopy(instruction['updated_charges'])

	# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - 
	# Part II: Make sure that the variable above have been updated so they are ready for the "change_charges_of_atoms" method.

	# Third, remove any solvent tags in the molecule name. 
	if isinstance(molecule_name, str):
		molecule_name = int(molecule_name.replace('S',''))

	# Fourth, if atoms_to_change_charges_of is an interger, convert it into a list 
	if isinstance(atoms_to_change_charges_of, int):
		atoms_to_change_charges_of = [atoms_to_change_charges_of]

	# Fifth, obtain the original_to_modified_atom_indices_for_mol dictionary for molecules[molecule_name]
	original_to_modified_atom_indices_for_mol = get_original_to_modified_atom_indices_for_mol(molecules[molecule_name])

	# Sixth, update the atom indices in atoms_to_change_charges_of based on original_to_modified_atom_indices
	#         * This is required because atoms may have been removed in a previous instruction.
	#         * original_to_modified_atom_indices indices how the indices of atoms have changed due to previous atom removal commands. 
	atoms_to_change_charges_of = [original_to_modified_atom_indices_for_mol[atom_to_change_elements_of] for atom_to_change_elements_of in atoms_to_change_charges_of]

	# Seventh, if updated_charges is an integer, convert it into a list of same size as atoms_to_change_hybridisation_of
	if isinstance(updated_charges, int):
		updated_charges = [updated_charges]*len(atoms_to_change_charges_of)

	# Eighth, check that the length of updated_charges is the same as the length of updated_charges
	if not len(atoms_to_change_charges_of) == len(updated_charges):
		to_string  = 'Error: The length of the lists recording "updated_charges" and "updated_charges" are not the same\n'
		to_string += f'number of "updated_charges" to add hydrogens to: {len(updated_charges)}\n'
		to_string += f'number of "updated_charges": {len(updated_charges)}\n'
		to_string += f'"updated_charges" list: {updated_charges}\n'
		to_string += f'"updated_charges" list: {updated_charges}\n'
		to_string += 'Check this.'
		raise Exception(to_string)

	# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - 
	# PART III: Run the "change_charges_of_atoms" method.

	# Ninth, move atom in molecule.
	change_charges_of_atoms(molecule_name, atoms_to_change_charges_of, updated_charges, molecules)

	# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - 









