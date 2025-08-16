"""
change_hybridisation_of_atoms.py, Geoffrey Weal, 2/4/24

This method is designed to change the hybridisation of the atoms in the molecule.
"""

def change_hybridisations_of_atoms(molecule_name, atoms_to_change_hybridisations_of, list_of_hybridisations, molecules, molecule_graphs):
	"""
	This method is designed to change the hybridisation of the atoms in the molecule.

	Parameters
	----------
	molecule_name : int
		This is the name of the molecule to change the elements of.
	atoms_to_change_hybridisations_of : list of int
		These are the indices of the atoms in the molecule that you want to change the hybridisations of.
	list_of_hybridisations : list of str.
		These are the hybridisations of the atoms you want to change. 
	molecules : dict. of ase.Atoms
		These are the molecules in the crystal (Only the structurally unique molecules due to the symmetry of the crystal).
	molecule_graphs : dict. of networkx.Graphs
		These are the graphs associated with each molecule in the molecules dictionary.
	"""

	# First, get the graph associated with molecule we want to change the hybridisation of
	molecule_graph = molecule_graphs[molecule_name]

	# Second, for each molecule to change the hybridisation of atoms of:
	for atom_index, hybridisation in zip(atoms_to_change_hybridisations_of, list_of_hybridisations):

		# 2.1: Change the hybridisation of the atom in molecule_graph
		molecule_graph.nodes[atom_index]['hybridisation'] = hybridisation