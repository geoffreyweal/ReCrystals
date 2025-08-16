"""
remove_molecule.py, Geoffrey Weal, 2/4/24

This method is designed to remove molecules from the dictionaries associated with a crystal
"""

def remove_molecules(molecules_to_remove, molecules, molecule_graphs, SolventsList):
	"""
	This method is designed to remove molecules from the dictionaries associated with a crystal.

	Parameters
	----------
	molecules_to_remove : list of int. 
		These are the molecules to remove from the crystal. 
	molecules : dict. of ase.Atoms
		These are the molecules in the crystal (Only the structurally unique molecules due to the symmetry of the crystal).
	molecule_graphs : dict. of networkx.Graphs
		These are the graphs associated with each molecule in the molecules dictionary. 
	SolventsList : list
		This list contains all the molecules in the molecules dictionary that are solvents. 
	"""

	# First, for each molecule to remove:
	for molecule_name_to_remove in molecules_to_remove:

		# Second, remove molecule_name_to_remove from molecules
		del molecules[molecule_name_to_remove]

		# Third, remove molecule_name_to_remove from molecule_graphs
		del molecule_graphs[molecule_name_to_remove]

		# Fourth, if molecule_name_to_remove is a solvent, remove it from SolventsList
		if molecule_name_to_remove in SolventsList:
			SolventsList.remove(molecule_name_to_remove)