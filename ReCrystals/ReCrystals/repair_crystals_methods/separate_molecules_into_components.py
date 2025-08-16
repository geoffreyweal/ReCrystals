"""
separate_molecules_into_components.py, Geoffrey Weal, 10/4/24

This method is designed to split molecules into separate molecules (components) if removing one or more molecules causes multiple molecules to be made as a consequence. 

This method runs upon molecules and molecule_graphs inplace (i.e. modifies molecules and molecule_graphs themselves).
"""
from ase import Atoms
from networkx import connected_components, relabel_nodes

def separate_molecules_into_components(molecules, molecule_graphs):
	"""
	This method is designed to split molecules into separate molecules (components) if removing one or more molecules causes multiple molecules to be made as a consequence. 

	This method runs upon molecules and molecule_graphs inplace (i.e. modifies molecules and molecule_graphs themselves).

	Parameters
	----------
	molecules : dict. of ase.Atoms
		These are the molecules in the crystal (Only the structurally unique molecules due to the symmetry of the crystal).
	molecule_graphs : dict. of networkx.Graphs
		These are the graphs associated with each molecule in the molecules dictionary. 
	"""

	# First, for each molecule in molecules
	for molecule_name in tuple(molecules.keys()):

		# Second, get the molecule we will be removing atoms from.
		molecule       = molecules[molecule_name]

		# Third, get the graph of the molecule we will be removing atoms from.
		molecule_graph = molecule_graphs[molecule_name]

		# Fourth, get the components of the molecule. 
		connected_graphs = list(connected_components(molecule_graph))

		# Fifth, make sure that connected_graphs is not 0
		if len(connected_graphs) == 0:
			raise Exception('Error: There are no components of the graph. This is odd, and probably indicates a programming error.')

		# Sixth, if there is only one component, exit this method.
		if len(connected_graphs) == 1:
			continue 

		# --- If at this point, there are multiple components. Separate these into individual molecules. --- 

		# Seventh, sort the atom indices in the graphs
		connected_graphs = [tuple(sorted(connected_graph)) for connected_graph in connected_graphs]

		# Eighth, sort the graphs by the lowest index in each individual component graph.
		connected_graphs.sort(key=lambda x:min(x))

		# Ninth, create the subgraph from the main graph for this (disconnected) molecule.
		individual_graphs = [molecule_graph.subgraph(component).copy() for component in connected_graphs]

		# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - 
		# Tenth, create the individual molecules from the disconnected molecule

		# 10.1: Initialise a list to record the individual molecules
		individual_molecules = []

		# For each connected_graph in connected_graphs
		for index, connected_graph in enumerate(connected_graphs):

			# 10.2: Create a new Atoms object for the molecule
			new_molecule = Atoms(cell=molecule.get_cell(),pbc=molecule.get_pbc())

			# 10.3: Append the atoms in connected_graph to new_molecule.
			for atom_index in sorted(connected_graph):
				new_molecule.append(molecule[atom_index])

			# 10.4: Add new_molecule to individual_molecules
			individual_molecules.append(new_molecule)

			# 10.5: Make a mapping for these new individual molecules
			mapping = {old_atom_index: new_atom_index for new_atom_index, old_atom_index in enumerate(sorted(connected_graph))}

			# 10.6: Convert the atom indices of the individual graph into the new values in new_molecule
			individual_graphs[index] = relabel_nodes(individual_graphs[index], mapping=mapping)

		# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - 

		# Eleventh, update molecule molecule_name with the first molecule in individual_molecules.
		#           * Also do this for the associated molecule graph
		molecules[molecule_name]       = individual_molecules.pop(0)
		molecule_graphs[molecule_name] = individual_graphs.pop(0)

		# Twelfth, add the other molecules in individual_molecules to molecules
		#          * And likewise for the associated molecule graphs
		for individual_molecule, individual_graph in zip(individual_molecules, individual_graphs):

			# 12.1: Get the names of the molecules, and make sure that all the names are integers and do not include the solvent tag
			names_of_molecules = [int(str(mol_name).replace('S','')) for mol_name in molecules.keys()]

			# 12.2: Get the name for the new molecule
			new_molecule_name = max(names_of_molecules) + 1

			# 12.3: Add new molecule to the molecules dictionary.
			molecules[new_molecule_name] = individual_molecule

			# 12.4: Add the associated graph of the new molecule to the molecule_graphs dictionary.
			molecule_graphs[new_molecule_name] = individual_graph

