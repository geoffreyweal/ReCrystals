"""
remove_edges_to_molecule_graph.py, Geoffrey Weal, 11/4/24

This method is designed to remove edges to a molecule's graph.
"""

def remove_edges_to_molecule_graph(molecule_name, edges_to_remove, molecule_graphs):
	"""
	This method is designed to remove edges to a molecule's graph.

	Parameters
	----------
	molecule_name : int.
		This is the molecules to remove edges to in its graph.
	edges_to_remove : list of list (int, int)
		This list contain all the information about the graphs to remove to the graph.
	molecule_graphs : dict. of networkx.Graphs
		These are the graphs associated with each molecule in the molecules dictionary. 
	"""

	raise Exception('need to try this method out')
	
	# First, get the graph of the molecule we will be removing atoms from.
	molecule_graph = molecule_graphs[molecule_name]

	# Second, get all the bonds that already exist in the molecule's graph
	original_edges = tuple(molecule_graph.edges)

	# Third, check that all the edges you want to remove to the molecule's graph actually currently exist in the molecule's graph
	for u_index, v_index in edges_to_remove:

		# 3.1: Get the atom indices in the bond to check for,
		edge = tuple(sorted([u_index, v_index]))

		# 3.2: Check that the edge does not already exist in the molecule's graph already.
		if edge not in original_edges:
			to_string  = f"Error: edge {edge} is not in the molecule's graph, so you cant remove it from the graph because it is already not in the graph.\n"
			to_string += f"Edge you are trying to remove to the molecule's graph: {edge}\n"
			to_string += f"Edges in the molecule's graph: {original_edges}\n"
			to_string += 'Check this.'
			raise Exception(to_string)

	# Fourth, remove new bond edges to the molecule's graph.
	molecule_graph.remove_edges_from(edges_to_remove)