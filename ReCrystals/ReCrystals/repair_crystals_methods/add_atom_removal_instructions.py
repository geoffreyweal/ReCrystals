"""
add_atom_removal_instructions.py, Geoffrey Weal, 6/4/24

This method is designed to take any instructions that also include a removal component to it and split it into two instructions, a removal section and the original instruction
"""
from copy import deepcopy

def add_atom_removal_instructions(original_instructions, molecules, molecule_graphs):
	"""
	This method is designed to take any instructions that also include a removal component to it and split it into two instructions, a removal section and the original instruction

	Parameters
	----------
	original_instructions : list
		This is the original set of instructions

	Returns
	-------
	instructions : list
		This is the instructions, where any atom removal instructions attached to other instructions have been split off and added as their own instruction. 
	"""

	# First, initialise a list that will include all instructions, including split instructions for adding atom removal methods
	instructions = []

	# Second, for each instruction in original_instructions
	for instruction in original_instructions:

		# 2.1: If you are adding hydrogens and the "remove_existing_hydrogens" tag is True, split the removal instruction as its own instruction.  
		if (instruction['action'] == 'add_hydrogens') and ('remove_existing_hydrogens' in instruction) and (instruction['remove_existing_hydrogens'] == True):

			# 2.1.1: Obtain the removal instruction for removing all the existing neighbouring hydrogen attached to the atoms you want to add new hydrogens to.
			instruction_remove_hydrogens = get_existing_hydrogen_indices_for_add_hydrogens_method(instruction, molecules, molecule_graphs)

			# 2.1.2: Add instruction_remove_hydrogens to instructions
			instructions.append(instruction_remove_hydrogens)

		# 2.2: Add the original instruction to instructions
		instructions.append(instruction)

	# Third, return instructions
	return instructions

# ======================================================================================================================================================

def get_existing_hydrogen_indices_for_add_hydrogens_method(instruction, molecules, molecule_graphs):
	"""
	This method is designed to obtain the neighbouring hydrogens that are currently bound to atom you want to add new hydrogens to.

	Parameters
	----------
	instruction : dict.
		This is the add hydrogens instruction.
	molecules : dict. of ase.Atoms
		This is the molecule you want to add hydrogens to.
	molecule_graphs : dict. of networkx.Graph
		This is the associated graph for the molecules object. 
	"""

	# First, get the molecule to move an atom in.
	molecule_name = deepcopy(instruction['molecule'])

	# Second, obtain the indices of the atoms you want to add hydrogens to.
	if isinstance(instruction['atoms'],dict):
		atoms_to_add_hydrogens_to = sorted(instruction['atoms'].keys())
	else:
		atoms_to_add_hydrogens_to = deepcopy(instruction['atoms'])

	# Third, obtain the atom indices of the atoms you want to add hydrogens to.
	existing_hydrogens_to_remove = obtain_atom_indices_hydrogens_to_remove(atoms_to_add_hydrogens_to, molecules[molecule_name], molecule_graphs[molecule_name])

	# Fourth, create the instruction for removing the 
	instruction_remove_hydrogens = {'action': 'remove_atoms', 'molecule': molecule_name, 'atoms': existing_hydrogens_to_remove, 'remove_attached_hydrogens': False, 'add_edges_after_removing_atoms': []}

	# Fifth, remove instruction_remove_hydrogens
	return instruction_remove_hydrogens

def obtain_atom_indices_hydrogens_to_remove(atoms_to_add_hydrogens_to, molecule, molecule_graph):
	"""
	This method is designed to obtain all the atom indices of hydrogens bound to current atoms that you want to add other hydrogens to.

	Parameters
	----------
	atoms_to_add_hydrogens_to : list
		These are the atoms that you want to add hydrogens to.
	molecule : ase.Atoms
		This is the molecule you want to add hydrogens to.
	molecule_graph : networkx.Graph
		This is the associated graph for the molecules object. 

	Returns
	-------
	existing_hydrogens_to_remove : list
		These are the indices of hydrogens to remove before adding other hydrogens. 
	"""

	# First, iniitalise the list to add hydrogen indices to that you want to remove initially. 
	existing_hydrogens_to_remove = []

	# Second, for each atom in atoms_to_add_hydrogens_to:
	for atom_index in atoms_to_add_hydrogens_to:

		# 2.1: Look at all the atoms that are bonded to atom_index
		for neighbouring_hydrogen_index in molecule_graph[atom_index].keys():

			# 2.2: If the neighbouring atom is not a hydrogen, move on
			if not molecule[neighbouring_hydrogen_index].symbol in ['H', 'D', 'T']:
				continue

			# 2.3: Check that neighbouring_hydrogen_index is not already in existing_hydrogens_to_remove
			if neighbouring_hydrogen_index in existing_hydrogens_to_remove:
				raise Exception('huh?')

			# 2.4: Add neighbouring_hydrogen_index to existing_hydrogens_to_remove
			existing_hydrogens_to_remove.append(neighbouring_hydrogen_index)

	# Third, return existing_hydrogens_to_remove
	return existing_hydrogens_to_remove

# ======================================================================================================================================================




