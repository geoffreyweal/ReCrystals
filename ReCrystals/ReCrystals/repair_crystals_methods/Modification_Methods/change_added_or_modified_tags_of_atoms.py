"""
change_added_or_modified_tag_of_atoms.py, Geoffrey Weal, 31/5/24

This method is designed to change the added_or_modified_tag of the atoms in the molecule.
"""

def change_added_or_modified_tags_of_atoms(molecule_name, atoms_to_change_added_or_modified_tags_of, list_of_added_or_modified_tags, molecules, molecule_graphs):
	"""
	This method is designed to change the added_or_modified_tag of the atoms in the molecule.

	Parameters
	----------
	molecule_name : int
		This is the name of the molecule to change the elements of.
	atoms_to_change_added_or_modified_tags_of : list of int
		These are the indices of the atoms in the molecule that you want to change the added_or_modified_tags of.
	list_of_added_or_modified_tags : list of str.
		These are the added_or_modified_tags of the atoms you want to change. 
	molecules : dict. of ase.Atoms
		These are the molecules in the crystal (Only the structurally unique molecules due to the symmetry of the crystal).
	molecule_graphs : dict. of networkx.Graphs
		These are the graphs associated with each molecule in the molecules dictionary.
	"""

	# First, get the graph associated with molecule we want to change the added_or_modified_tag of
	molecule_graph = molecule_graphs[molecule_name]

	# Second, for each molecule to change the added_or_modified_tag of atoms of:
	for atom_index, added_or_modified_tag in zip(atoms_to_change_added_or_modified_tags_of, list_of_added_or_modified_tags):

		# 2.1: Change the added_or_modified_tag of the atom in molecule_graph
		molecule_graph.nodes[atom_index]['added_or_modified'] = added_or_modified_tag