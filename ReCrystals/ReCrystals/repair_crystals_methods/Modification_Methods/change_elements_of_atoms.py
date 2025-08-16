"""
change_elements_of_atoms.py, Geoffrey Weal, 2/4/24

This method is designed to change the elements of the atoms in the molecule
"""

def change_elements_of_atoms(molecule_name, atoms_to_change_elements_of, updated_elements, molecules, molecule_graphs):
	"""
	This method is designed to remove molecules from the dictionaries associated with a crystal.

	Parameters
	----------
	molecule_name : int
		This is the name of the molecule to change the elements of.
	atoms_to_change_elements_of : list of int
		These are the indices of the atoms in the molecule that you want to change the element of.
	updated_elements : list of str.
		These are the elements that you want to change the atoms in atoms_to_change_elements_of to. 
	molecules : dict. of ase.Atoms
		These are the molecules in the crystal (Only the structurally unique molecules due to the symmetry of the crystal).
	molecule_graphs : dict. of networkx.Graphs
		These are the graphs associated with each molecule in the molecules dictionary.
	"""

	# First, get the molecule we want to focus on from the molecules dictionary. 
	molecule = molecules[molecule_name]

	# Second, get the graph associated with molecule we want to add hydrogens to.
	molecule_graph = molecule_graphs[molecule_name]

	# Third, for each molecule to to change the element of:
	for atom_index, element in zip(atoms_to_change_elements_of, updated_elements):

		# 3.1: Change the element of the atom in molecule
		molecule[atom_index].symbol = element

		# 3.2: Change the element of the atom in molecule_graph
		if 'E' in molecule_graph.nodes[atom_index]:
			molecule_graph.nodes[atom_index]['E'] = element
		if 'element' in molecule_graph.nodes[atom_index]:
			warning.warn('Warning: Found element in node')
			raise Exception('Error: Element found in graph. This is old, should be E')
			molecule_graph.nodes[atom_index]['E'] = element
			del molecule_graph.nodes[atom_index]['element']