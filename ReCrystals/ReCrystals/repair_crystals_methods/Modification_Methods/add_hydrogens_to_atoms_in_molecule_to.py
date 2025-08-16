"""
add_hydrogens_to_atoms_in_molecule_to.py, Geoffrey Weal, 4/2/24

This method is designed to add hydrogens to atoms in the molecule.
"""
import numpy as np
from SUMELF import add_hydrogens_to_molecules

def add_hydrogens_to_atoms_in_molecule_to(molecule_name, atoms_to_add_hydrogens_to, number_of_hydrogens_to_add, identifier, molecules, molecule_graphs, symmetry_operations, cell, crystal, crystal_graph):
	"""
	This method is designed to add hydrogens to atoms in the molecule.

	Parameters
	----------
	molecule_name : int.
		This is the molecules to add hydrogens to atoms to.
	atoms_to_add_hydrogens_to : list of int. 
		These are the indices of the atoms we want to add hydrogens to.
	number_of_hydrogens_to_add : int of list of ints
		These are the number of hydrogens you would like to add to each atom in the molecule of interest. 
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
	# First, check that each atom in the crystal does not contains an instance of 'no_of_neighbouring_non_cord_H'
	
	# 1.1: Initalise a dictionary that contains which atoms/nodes do not contain an instance of 'no_of_neighbouring_non_cord_H'
	atoms_that_do_not_contain__no_of_neighbouring_non_cord_H = {}

	# 1.2: Determine which atoms do not contain an instance of 'no_of_neighbouring_non_cord_H' in the molecule. 
	for mol_name, molecule_graph in molecule_graphs.items():
		for node_name, node_property in molecule_graph.nodes.items():
			if ('no_of_neighbouring_non_cord_H' in node_property.keys()) and (node_property['no_of_neighbouring_non_cord_H'] != 0):
				atoms_that_do_not_contain__no_of_neighbouring_non_cord_H.setdefault(mol_name,[]).append(node_name)

	# 1.3: If any of the atoms are missing 'no_of_neighbouring_non_cord_H', raise an exception
	if len(atoms_that_do_not_contain__no_of_neighbouring_non_cord_H) > 0:
		to_string  = 'Error: Some of the atoms in the crystal contain  an input for "no_of_neighbouring_non_cord_H" in the graphs for the atoms in the crystal.\n'
		to_string  = 'This should not be the case for using the ReCrystal program.\n'
		to_string += 'These are:\n'
		to_string += '\n'
		to_string += 'molecule name: list of atom indices\n'
		to_string += '-----------------------------------\n'
		for mol_name, list_of_atom_indices in atoms_that_do_not_contain__no_of_neighbouring_non_cord_H.items():
			to_string += f'{mol_name}: {list_of_atom_indices}\n'
		to_string += '\n'
		to_string += 'Check this.\n'
		raise Exception(to_string)

	# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - 

	# Second, get the molecule we want to focus on from the molecules dictionary. 
	molecule = molecules[molecule_name]

	# Third, get the graph associated with molecule we want to add hydrogens to.
	molecule_graph = molecule_graphs[molecule_name]

	# Fourth, create a dictionary that assign each atom index in atoms_to_add_hydrogens_to to that in number_of_hydrogens_to_add
	no_of_hydrogens_to_add_to_each_atom_in_mol = {molecule_name: {atom_index: no_of_hydrogen_to_add for atom_index, no_of_hydrogen_to_add in sorted(zip(atoms_to_add_hydrogens_to, number_of_hydrogens_to_add), key=lambda x:x[0])}}

	# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - 

	# Fifth, get the number of atoms in the original molecule.
	original_indices = molecule.get_array('original_indices').tolist()

	# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - 

	# Sixth, Add the hydrogens to the molecules in the crystal.
	updated_molecules, updated_molecule_graphs, were_hydrogens_added = add_hydrogens_to_molecules(no_of_hydrogens_to_add_to_each_atom_in_mol, molecules, molecule_graphs, crystal, crystal_graph, symmetry_operations, cell, logger=None, identifier=identifier, allow_hydrogen_free_rotation=True)

	# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - 

	# Seventh, check that the were_hydrogens_added boolean is Ture, indicating that one or more hydrogens has been added
	#          * If this is False, this is weird, as this means that no hydrogens were added during this method where hydrogen 
	#            were suppose to be added to the molecule. 
	if not were_hydrogens_added:
		to_string  = 'Error: It seems that no hydrogens were added during the "atom_hydrogens" instruction. Check that you have indicated you are wanting to add hydrogens to your crystal.'
		raise Exception(to_string)

	# Eighth, get the number of hydrogens that were added to the molecule
	number_of_hydrogens_added = len(updated_molecules[molecule_name]) - len(original_indices)

	# Ninth, add -1 as the original index for each added hydrogen. -1 indicates that this atom did not exist in the original molecule.
	original_indices += [-1]*number_of_hydrogens_added

	# Tenth, set the original_indices list to the molecule
	updated_molecules[molecule_name].arrays['original_indices'] = np.array(original_indices)

	# Eleventh, add the update molecule and associated graph to molecules and molecule_graphs.
	molecules[molecule_name]       = updated_molecules[molecule_name]
	molecule_graphs[molecule_name] = updated_molecule_graphs[molecule_name]

	# Twelfth, return None
	return None


