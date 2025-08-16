"""
add_edges_to_molecule_graph.py, Geoffrey Weal, 11/4/24

This method is designed to add edges to a molecule's graph.
"""

def add_edges_to_molecule_graph(molecule_name, edges_to_add, molecule_graphs):
	"""
	This method is designed to add edges to a molecule's graph.

	Parameters
	----------
	molecule_name : int.
		This is the molecules to add edges to in its graph.
	edges_to_add : list of list (int, int, dict) or (int, int)
		This list contain all the information about the graphs to add to the graph.
	molecule_graphs : dict. of networkx.Graphs
		These are the graphs associated with each molecule in the molecules dictionary. 
	"""

	# First, get the graph of the molecule we will be removing atoms from.
	molecule_graph = molecule_graphs[molecule_name]

	# Second, get all the bonds that already exist in the molecule's graph
	original_edges = tuple(molecule_graph.edges)

	# Third, check that all the edges you want to add to the molecule's graph do not already exist. 
	for u_index, v_index, bond_info in edges_to_add:

		# 3.1: Get the atom indices in the bond to check for,
		edge = tuple(sorted([u_index, v_index]))

		# 3.2: Check that the edge does not already exist in the molecule's graph already.
		if edge in original_edges:
			to_string  = f"Error: edge {edge} is already in the molecule's graph\n"
			to_string += f"Edge you are trying to add to the molecule's graph: {edge}\n"
			to_string += f"Edges already in the molecule's graph: {original_edges}\n"
			to_string += 'Check this.'
			raise Exception(to_string)

	# Fourth, add new bond edges to the molecule's graph.
	molecule_graph.add_edges_from(edges_to_add)