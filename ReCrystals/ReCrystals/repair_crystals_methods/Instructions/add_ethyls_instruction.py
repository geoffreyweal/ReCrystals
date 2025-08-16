"""
add_ethyls_instruction.py, Geoffrey Weal, 15/4/24

This method is designed to add ethyl groups to atoms in the molecule. 
"""
from copy import deepcopy
from ReCrystals.ReCrystals.repair_crystals_methods.Utilities.get_original_to_modified_atom_indices_for_mol import get_original_to_modified_atom_indices_for_mol
from ReCrystals.ReCrystals.repair_crystals_methods.Modification_Methods.add_ethyls_to_atoms_in_molecule_to import add_ethyls_to_atoms_in_molecule_to

def add_ethyls_instruction(instruction, identifier, molecules, molecule_graphs, symmetry_operations, cell, crystal, crystal_graph):
	"""
	This method is designed to add ethyl groups to atoms in the molecule. 

	Parameters
	----------
	instruction : dict. 
		This is the instruction you would like to perform upon the molecules in the crystal.
	identifier : str.
		This is the name of the crystal. 
	molecules : dict. of ase.Atoms
		These are the molecules in the crystal (Only the structurally unique molecules due to the symmetry of the crystal).
	molecule_graphs : dict. of networkx.Graphs
		These are the graphs associated with each molecule in the molecules dictionary. 
	symmetry_operations : list of (3x3 numpy.array, 3x1 numpy.array)
		These are all the transformation matrices that describe the crystal synmetries. The positions of molecules in the crystal can be multipled by these matrices. 
	cell : 3x3 numpy.array or ase.Cell
		This is the dimensions of the unit cell for the crystal.
	crystal : ase.Atoms
		This is the ase Atoms object of the crystal of interest we are wanting to repair. 
	crystal_graph : networkx.graph
		This is the graph of the associated graph.

	Returns
	-------
		Return the indices of hydrogen atoms you would like to be allow to freely rotate about the attached atom in molecule given by molecule_name
	"""

	# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - 
	# PART I: Import input variables from the instruction dictionary.

	# First, get the molecule to move an atom in.
	molecule_name = deepcopy(instruction['molecule'])

	# Second, input the data for "atoms" to add ethyl groups to and number_of_ethyls_to_add
	if isinstance(instruction['atoms'],dict):

		# 2.1: If instruction['atoms'] is a dict:
		#      * The keys are the indices of the atoms to add ethyl groups to
		#      * The values are the number of ethyl groups to add to the atom. 

		# 2.1.1: Initialise the list to hold the atom indices to add ethyl groups to
		atoms_to_add_ethyls_to  = []

		# 2.1.2: Initialise the list to record the number of ethyl groups to add to the atoms of interest
		number_of_ethyls_to_add = []

		# 2.1.3: For each atom index and the number of ethyl groups you want to attach.
		for original_atom_to_add_ethyl_groups_to, no_of_ethyl_groups in sorted(instruction['atoms'].items(),key=lambda x:x[0]):

			# 2.1.3.1: Add original_atom_to_add_ethyl_groups_to to atoms_to_add_ethyls_to.
			atoms_to_add_ethyls_to.append(original_atom_to_add_ethyl_groups_to)

			# 2.1.3.2: Add no_ethyl_groups to number_of_ethyls_to_add.
			number_of_ethyls_to_add.append(no_of_ethyl_groups)

	else:

		# 2.2: If instruction['atoms'] is a not a dict:
		#      * atoms_to_add_ethyls_to: the "atoms" to add ethyl groups to are given in by instruction['atoms']
		#      * number_of_ethyls_to_add: is given by instruction['number_of_ethyls_to_add']

		# 2.2.1: Get the atom in the molecule to move.
		atoms_to_add_ethyls_to = deepcopy(instruction['atoms'])

		# 2.2.2: Get the position to move the atom to
		number_of_ethyls_to_add = instruction['number_of_ethyls_to_add']

	# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - 
	# Part II: Make sure that the variable above have been updated so they are ready for the "add_ethyls_to_atoms_in_molecule_to" method.

	# Third, remove any solvent tags in the molecule name. 
	if isinstance(molecule_name, str):
		molecule_name = int(molecule_name.replace('S',''))

	# Fourth, if atoms_to_add_ethyls_to is an integer, convert it into a list.
	if isinstance(atoms_to_add_ethyls_to, int):
		atoms_to_add_ethyls_to = [atoms_to_add_ethyls_to]

	# Fifth, obtain the original_to_modified_atom_indices_for_mol dictionary for molecules[molecule_name]
	original_to_modified_atom_indices_for_mol = get_original_to_modified_atom_indices_for_mol(molecules[molecule_name])

	# Sixth, update the atom indices in atoms_to_add_ethyls_to based on original_to_modified_atom_indices
	#        * This is required because atoms may have been removed in a previous instruction.
	#        * original_to_modified_atom_indices indices how the indices of atoms have changed due to previous atom removal commands. 
	atoms_to_add_ethyls_to = [original_to_modified_atom_indices_for_mol[original_atom_to_add_ethyl_groups_to] for original_atom_to_add_ethyl_groups_to in atoms_to_add_ethyls_to]

	# Seventh, if number_of_ethyls_to_add is an integer, convert it into a list of same size as atoms_to_add_ethyls_to
	if isinstance(number_of_ethyls_to_add, int):
		number_of_ethyls_to_add = [number_of_ethyls_to_add]*len(atoms_to_add_ethyls_to)

	# Eighth, check that the length of atoms_to_add_ethyls_to is the same as the length of number_of_ethyls_to_add
	if not len(atoms_to_add_ethyls_to) == len(number_of_ethyls_to_add):
		to_string  = 'Error: The length of the lists recording "atoms" and "number_of_ethyls_to_add" are not the same\n'
		to_string += f'number of "atoms" to add ethyl groups to: {len(atoms)}\n'
		to_string += f'number of "number_of_ethyls_to_add": {len(number_of_ethyls_to_add)}\n'
		to_string += f'"atoms" list: {atoms_to_add_ethyls_to}\n'
		to_string += f'"number_of_ethyls_to_add" list: {number_of_ethyls_to_add}\n'
		to_string += 'Check this.'
		raise Exception(to_string)

	# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - 
	# PART III: Run the "add_ethyls_to_atoms_in_molecule_to" method.

	# Ninth, move atom in molecule.
	hydrogens_to_add_to_atoms = add_ethyls_to_atoms_in_molecule_to(molecule_name, atoms_to_add_ethyls_to, number_of_ethyls_to_add, identifier, molecules, molecule_graphs, symmetry_operations, cell, crystal, crystal_graph)

	# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - 

	# Tenth, return the indices of the hydrogens that have been added to the molecule when the ethyls were added to the system.
	return hydrogens_to_add_to_atoms

	# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - 

