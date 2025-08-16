"""
remove_atoms_from_molecule.py, Geoffrey Weal, 2/4/24

This method is designed to remove atoms for a molecule in the crystal.
"""
from networkx import relabel_nodes

def remove_atoms_from_molecule(molecule_to_remove_atoms_from, atoms_to_remove, remove_attached_hydrogens, molecules, molecule_graphs, add_edges_after_removing_atoms=[], create_new_molecules=False):
	"""
	This method is designed to remove molecules from the dictionaries associated with a crystal.

	Parameters
	----------
	molecule_to_remove_atoms_from : int.
		This is the molecules to remove atoms from.
	atoms_to_remove : list of int. 
		These are the indices of the atoms to remove from the molecule given by molecule_to_remove_atoms_from.
	remove_attached_hydrogens : bool.
		This boolean indicates if you want to remove hydrogens that are attached to atoms you are removing. 
	molecules : dict. of ase.Atoms
		These are the molecules in the crystal (Only the structurally unique molecules due to the symmetry of the crystal).
	molecule_graphs : dict. of networkx.Graphs
		These are the graphs associated with each molecule in the molecules dictionary. 
	add_edges_after_removing_atoms : list of tuple (int, int)
		These are the new edges to add just in case removing atoms causes fragmentation in the graph, but where there obviously still should have a bond. 
	create_new_molecules : bool.
		This boolean indicates if you are happy that a molecule can be separated into multiple molecules by deleting atoms from a molecule. 
	"""

	# First, get the molecule we will be removing atoms from.
	molecule       = molecules[molecule_to_remove_atoms_from]

	# Second, get the graph of the molecule we will be removing atoms from.
	molecule_graph = molecule_graphs[molecule_to_remove_atoms_from]

	# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
	# Third, check that the graph of the molecule is fully connected before proceeding
	if not create_new_molecules:
		start_of_to_string  = f'Error: Molecule {molecule_to_remove_atoms_from} has an graph that is not fully connected.\n'
		start_of_to_string += 'Atom indices in fragments:\n'
		check_if_molecule_if_fully_connected(molecule, molecule_graph, start_of_to_string)

	# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
	# Fourth, add attached hydrogens to the atoms_to_remove list.
	if remove_attached_hydrogens:

		# 4.1: For each atom in atoms_to_remove
		for atom_index_to_remove in tuple(atoms_to_remove):

			# 4.2: Inspect the neighbouring atoms attached to each atom_index_to_remove
			for neighbouring_atom_index in molecule_graph[atom_index_to_remove].keys():

				# 4.3: If the neighbouring atom is a hydrogen (and is not already in atoms_to_remove)
				if (molecule[neighbouring_atom_index].symbol in ['H', 'D', 'T']) and (neighbouring_atom_index not in atoms_to_remove):

					# 4.4: Check that neighbouring_atom_index is not already in atoms_to_remove, other it may have already been added to this list by the user, so move on
					if neighbouring_atom_index in atoms_to_remove:
						continue

					# 4.5: Add the hydrogen to the atoms_to_remove list for removing.
					atoms_to_remove.append(neighbouring_atom_index)

	# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -

	# Fifth, make sure that atoms_to_remove has been sorted from highest to lowest value.
	atoms_to_remove.sort(reverse=True)

	# Sixth, map the old index names to the new index names:
	mapping = {}; new_atom_index = 0
	for old_atom_index in range(len(molecules[molecule_to_remove_atoms_from])):

		# 6.1: If the atom index is in atoms_to_remove, we do not want to include it in the mapping.
		if old_atom_index in atoms_to_remove:
			continue

		# 6.2: If you have got here, map old_atom_index --> new_atom_index
		mapping[old_atom_index] = new_atom_index

		# 6.3: Increment new_atom_index
		new_atom_index += 1

	# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -

	# Seventh, for each molecule to remove:
	for atom_to_remove in sorted(atoms_to_remove, reverse=True):
		del molecule[atom_to_remove]

	# Eighth, remove the atoms from atoms_to_remove from the molecule graph for molecule_to_remove_atoms_from
	molecule_graph.remove_nodes_from(atoms_to_remove)

	# Ninth, update the node names in molecule_graphs[molecule_to_remove_atoms_from]
	molecule_graphs[molecule_to_remove_atoms_from] = relabel_nodes(molecule_graph, mapping=mapping)

	# Tenth, get updated molecule_graph from molecule_graphs[molecule_to_remove_atoms_from]
	molecule_graph = molecule_graphs[molecule_to_remove_atoms_from]

	# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
	# Eleventh, if there are edges in add_edges_after_removing_atoms, add them to the graph
	if len(add_edges_after_removing_atoms) > 0:

		# 11.1: For each edge in add_edges_after_removing_atoms:
		for index, (u_atom_index, v_atom_index, bond_info) in enumerate(add_edges_after_removing_atoms):

			# 11.1.1: Get the edge with updated atom indices.
			edge_with_updated_indices = (mapping[u_atom_index], mapping[v_atom_index], bond_info)

			# 11.1.2: Update entry in add_edges_after_removing_atoms
			add_edges_after_removing_atoms[index] = edge_with_updated_indices

		# 11.2: Add edges to molecule_graph
		molecule_graph.add_edges_from([edge_with_updated_indices])

	# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
	# Twelfth, it is possible that you have made multiple molecules/components by removing certain atoms.
	#          There are two options for proceeding:
	#          1. If create_new_molecules is True, move on, we will deal with this later.
	#          2. If create_new_molecules is False, make sure that the molecule has not been split into multiple components. 
	if not create_new_molecules:
		start_of_to_string  = f'Error: The molecule seems to have split into fragments after removing atoms from molecule {molecule_to_remove_atoms_from}\n'
		start_of_to_string += 'Updated atom indices in fragments:\n'
		check_if_molecule_if_fully_connected(molecule, molecule_graph, start_of_to_string)

# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - 

from networkx import connected_components
from ase.visualize import view
def check_if_molecule_if_fully_connected(molecule, molecule_graph, start_of_to_string):
	"""
	This method is designed to determine if the molecule is fully connected. 

	Parameters
	----------
	molecule : ase.Atoms
		This is the molecule of interest
	molecule_graph : networkx.Graph
		This is the graph representation of the molecule. 
	start_of_to_string : str
		This is the start of the error message to give
	"""

	# First, obtain the atom indices of the components of connected graphs, after having removing atoms from the original molecule. 
	connected_graphs = list(connected_components(molecule_graph))

	# Second, make sure that there is only one connected graph.
	if len(connected_graphs) > 1:

		# 2.1: Write the full error message.
		to_string  = start_of_to_string
		for connected_graph in connected_graphs:
			to_string += f'{sorted(connected_graph)}\n'
		to_string += 'Check this.\n'
		
		# 2.2: Print the error message and show the molecule. 
		view(molecule)
		print(to_string)
		import pdb; pdb.set_trace()
		raise Exception(to_string)

# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - 
