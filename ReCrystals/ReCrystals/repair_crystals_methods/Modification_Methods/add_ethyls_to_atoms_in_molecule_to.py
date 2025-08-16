"""
add_ethyls_to_atoms_in_molecule_to.py, Geoffrey Weal, 4/2/24

This method is designed to add ethyls to atoms in the molecule.
"""
import numpy as np
from SUMELF import add_ethyls_to_molecules, remove_node_properties_from_graph

def add_ethyls_to_atoms_in_molecule_to(molecule_name, atoms_to_add_ethyls_to, number_of_ethyls_to_add, identifier, molecules, molecule_graphs, symmetry_operations, cell, crystal, crystal_graph):
	"""
	This method is designed to add ethyls to atoms in the molecule.

	Parameters
	----------
	molecule_name : int.
		This is the molecules to add ethyls to atoms to.
	atoms_to_add_ethyls_to : list of int. 
		These are the indices of the atoms we want to add ethyls to.
	number_of_ethyls_to_add : int of list of ints
		These are the number of ethyls you would like to add to each atom in the molecule of interest. 
	molecules : dict. of ase.Atoms
		These are the molecules in the crystal (Only the structurally unique molecules due to the symmetry of the crystal).
	molecule_graphs : dict. of networkx.Graphs
		These are the graphs associated with each molecule in the molecules dictionary. 
	crystal : ase.Atoms
		This is the ase Atoms object of the crystal of interest we are wanting to repair. 
	crystal_graph : networkx.graph
		This is the graph of the associated graph.
	"""

	# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - 

	# First, get the molecule we want to focus on from the molecules dictionary. 
	molecule = molecules[molecule_name]

	# Second, get the graph associated with molecule we want to add ethyls to.
	molecule_graph = molecule_graphs[molecule_name]

	# Third, create a dictionary that assign each atom index in atoms_to_add_ethyls_to to that in number_of_ethyls_to_add
	no_of_ethyls_to_add_to_each_atom_in_mol = {molecule_name: {atom_index: no_of_ethyl_to_add for atom_index, no_of_ethyl_to_add in sorted(zip(atoms_to_add_ethyls_to, number_of_ethyls_to_add), key=lambda x:x[0])}}

	# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - 

	# Fourth, get the number of atoms in the original molecule.
	original_indices = molecule.get_array('original_indices').tolist()

	# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - 

	# Fifth, Add the ethyls to the molecules in the crystal.
	updated_molecules, updated_molecule_graphs, were_ethyls_added, hydrogens_to_add_to_atoms = add_ethyls_to_molecules(no_of_ethyls_to_add_to_each_atom_in_mol, molecules, molecule_graphs, crystal, crystal_graph, symmetry_operations, cell, add_hydrogens=False, logger=None, identifier=identifier)

	# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - 

	# Sixth, check that the were_ethyls_added boolean is Ture, indicating that one or more ethyls has been added
	#        * If this is False, this is weird, as this means that no ethyls were added during this method where ethyl 
	#          were suppose to be added to the molecule. 
	if not were_ethyls_added:
		to_string  = 'Error: It seems that no ethyls were added during the "atom_ethyls" instruction. Check that you have indicated you are wanting to add ethyls to your crystal.'
		raise Exception(to_string)

	# Seventh, get the number of ethyls that were added to the molecule
	number_of_atoms_from_ethyls_added = len(updated_molecules[molecule_name]) - len(original_indices)

	# Eighth, add -1 as the original index for all the atoms for each added ethyl group. -1 indicates that these atoms do not exist in the original molecule.
	original_indices += [-1]*number_of_atoms_from_ethyls_added

	# Ninth, set the original_indices list to the molecule
	updated_molecules[molecule_name].arrays['original_indices'] = np.array(original_indices)

	# Tenth, add the update molecule and associated graph to molecules and molecule_graphs.
	molecules[molecule_name]       = updated_molecules[molecule_name]
	molecule_graphs[molecule_name] = updated_molecule_graphs[molecule_name]

	# Eleventh, return the indices of the hydrogens that have been added to the molecule when the ethyls were added to the system.
	return hydrogens_to_add_to_atoms


