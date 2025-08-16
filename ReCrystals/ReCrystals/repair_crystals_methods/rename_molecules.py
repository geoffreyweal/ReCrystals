"""
renumber_molecules.py, Geoffrey Weal, 2/4/24

This method is designed to rename the molecules in a crystal.
"""

def rename_molecules(original_molecules, original_molecule_graphs, original_SolventsList):
	"""
	This method is designed to rename the molecules in a crystal.

	This is commonly used to update the molecules in a crystal if one has been deleted. 

	Parameters
	----------
	original_molecules : dict. of ase.Atoms
		These are the molecules in the crystal (Only the structurally unique molecules due to the symmetry of the crystal).
	original_molecule_graphs : dict. of networkx.Graphs
		These are the graphs associated with each molecule in the molecules dictionary. 
	original_SolventsList : list
		This list contains all the molecules in the molecules dictionary that are solvents. 

	Returns
	-------
	renamed_molecules : dict. of ase.Atoms
		These are the molecules in the crystal with updated names
	renamed_molecule_graphs : dict. of networkx.Graphs
		These are the graphs associated with each molecule in the molecules dictionary with updated names.
	renamed_SolventsList : list
		This list contains all the molecules in the molecules dictionary that are solvents, with updated names. 
	"""

	# First, initialise new dictionaries and lists for recording the molecules with new names
	renamed_molecules = {}
	renamed_molecule_graphs = {}
	renamed_SolventsList = []

	# Second, for each molecule in the molecules dictionary.
	for new_name, old_name in enumerate(sorted(original_molecules.keys()), start=1):

		# 2.1: Rename the molecule
		renamed_molecules[new_name] = original_molecules[old_name]

		# 2.2: Rename the associated graph for this molecule
		renamed_molecule_graphs[new_name] = original_molecule_graphs[old_name]

		# 2.3: If original_molecule_graphs[old_name] is a solvent, make sure this is updated in renamed_SolventsList
		if old_name in original_SolventsList:
			renamed_SolventsList.append(new_name)

	# Third, return renamed_molecules, renamed_molecule_graphs, and renamed_SolventsList
	return renamed_molecules, renamed_molecule_graphs, renamed_SolventsList