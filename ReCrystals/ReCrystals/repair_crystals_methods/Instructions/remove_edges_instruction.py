"""
remove_edges_instruction.py, Geoffrey Weal, 11/4/24

This method is designed to remove edges between atoms in a molecule that you want to remove. 
"""
from copy import deepcopy
from ReCrystals.ReCrystals.repair_crystals_methods.Utilities.get_original_to_modified_atom_indices_for_mol import get_original_to_modified_atom_indices_for_mol
from ReCrystals.ReCrystals.repair_crystals_methods.Modification_Methods.remove_edges_to_molecule_graph     import remove_edges_to_molecule_graph

def remove_edges_instruction(instruction, molecules, molecule_graphs):
	"""
	This method is designed to remove edges between atoms in a molecule that you want to remove. 

	Parameters
	----------
	instruction : dict. 
		This is the instruction you would like to perform upon the molecules in the crystal.
	molecules : dict. of ase.Atoms
		These are the molecules in the crystal (Only the structurally unique molecules due to the symmetry of the crystal).
	molecule_graphs : dict. of networkx.Graphs
		These are the graphs associated with each molecule in the molecules dictionary.
	"""

	raise Exception('need to try this method out')

	# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - 
	# PART I: Import input variables from the instruction dictionary.

	# First, get the molecule to move an atom in.
	molecule_name = deepcopy(instruction['molecule'])

	# Second, record all the information about the edges to remove to the molecule
	edges_to_remove = instruction['edges']

	# Third, obtain the molecule whose graph that you want to modify
	molecule = molecules[molecule_name]

	# Fourth, obtain the graph that you want to modify
	molecule_graph = molecule_graphs[molecule_name]

	# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - 
	# Part II: Make sure that the variable above have been updated so they are ready for the "remove_edges_to_molecule_graph" method.

	# Fifth, remove any solvent tags in the molecule name. 
	if isinstance(molecule_name, str):
		molecule_name = int(molecule_name.replace('S',''))

	# Sixth, check that the input for "edges" is either a list or a tuple.
	if not (isinstance(edges_to_remove,list) or isinstance(edges_to_remove,tuple)):
		to_string  = 'Error: the input for "edges" is not a list or a tuple.\n'
		to_string += f"instruction['edges'] = {instruction['edges']}\n"
		to_string += f"Full Instruction = {instruction}\n"
		to_string += 'Check this.'
		raise Exception(to_string)

	# Seventh, convert the edges object to a list
	edges_to_remove = list(edges_to_remove)

	# Eighth, obtain the number of atoms in the molecule.
	no_of_mols = len(molecule)

	# Ninth, obtain the original_to_modified_atom_indices_for_mol dictionary for molecules[molecule_name]
	original_to_modified_atom_indices_for_mol = get_original_to_modified_atom_indices_for_mol(molecules[molecule_name])

	# Tenth, make sure that the inputs in the list are ok 
	for index, edge_input in enumerate(edges_to_remove):

		# 10.1: Make sure that edge_input is a list of tuple
		if not (isinstance(edge_input,list) or isinstance(edge_input,tuple)):
			to_string  = f'Error: the input for "edges[{index}]" is not a list or a tuple.\n'
			to_string += f"instruction['edges'][{index}] = {edges[index]}\n"
			to_string += f"Full Instruction = {instruction}\n"
			to_string += 'Check this.'
			raise Exception(to_string)

		# 10.2: Make sure that edge_input is only a size of 2
		if not len(edge_input) == 2:
			to_string  = f'Error: the number of values in the "edges[{index}]" tuple/list is not 2.\n'
			to_string += f"len(instruction['edges'][{index}]) = {len(edges[index])}\n"
			to_string += f"instruction['edges'][{index}] = {edges[index]}\n"
			to_string += f"Full Instruction = {instruction}\n"
			to_string += 'Check this.'
			raise Exception(to_string)

		# 10.3: Convert edge_input to a list.
		edge_input = list(edge_input)

		# 10.4: Check that the first two inputs are consistent
		for ii in range(2):

			# 10.4.1: Check that the input is an integer
			if not isinstance(edge_input[ii],int):
				to_string  = 'Error: One of the atom indices to describe the edge is not an integer.\n'
				to_string += f'Problematic atom index input: {edge_input[ii]}\n'
				to_string += f'Edge input with problem: {edge_input}\n'
				to_string += f'Full Instruction: {instruction}\n'
				to_string += 'Check this.'
				raise Exception(to_string)

			# 10.4.2: Check that the input for the atom index is less than 0, it is negative, which does not make sense for an atom index.
			if edge_input[ii] < 0:
				to_string  = 'Error: One of the atom indices is a negative value.\n'
				to_string += f'Problematic atom index input: {edge_input[ii]}\n'
				to_string += f'Edge input with problem: {edge_input}\n'
				to_string += f'Full Instruction: {instruction}\n'
				to_string += 'Check this.'
				raise Exception(to_string)

			# 10.4.3: Check that the input for the atom index is between 0 and no_of_mols-1
			if not (0 <= edge_input[ii] < no_of_mols):
				to_string  = 'Error: One of the atom indices is not consistent with the number of atoms in the molecule\n'
				to_string += f'All atom indices should be between 0 and {no_of_mols-1} (no. of atoms in molecule: {no_of_mols})'
				to_string += f'Problematic atom index input: {edge_input[ii]}\n'
				to_string += f'Edge input with problem: {edge_input}\n'
				to_string += f'Full Instruction: {instruction}\n'
				to_string += 'Check this.'
				from ase.visualize import view
				view(molecule)
				raise Exception(to_string)

			# 10.4.4: Get the original atom index.
			original_atom_index = edge_input[ii]

			# 10.4.5: Convert the atom index for the bond edge from its original index to the modified index. 
			update_atom_index = original_to_modified_atom_indices_for_mol[original_atom_index]

			# 10.4.6: Update the atom index in edge_input
			edge_input[ii] = update_atom_index

	# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - 
	# PART III: Run the "remove_edges_to_molecule_graph" method.

	# Eleventh, remove the edge information to the molecule graph (for the associated molecule). 
	remove_edges_to_molecule_graph(molecule_name, edges_to_remove, molecule_graphs)

	# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - 

