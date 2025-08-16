"""
change_charge_of_atoms.py, Geoffrey Weal, 2/4/24

This method is designed to change the charge of the atoms in the molecule.
"""

def change_charges_of_atoms(molecule_name, atoms_to_change_charges_of, list_of_charges, molecules):
	"""
	This method is designed to change the charge of the atoms in the molecule.

	Parameters
	----------
	molecule_name : int
		This is the name of the molecule to change the elements of.
	atoms_to_change_charges_of : list of int
		These are the indices of the atoms in the molecule that you want to change the charges of.
	list_of_charges : list of str.
		These are the charges of the atoms you want to change. 
	molecules : dict. of ase.Atoms
		These are the molecules in the crystal (Only the structurally unique molecules due to the symmetry of the crystal).
	molecule_graphs : dict. of networkx.Graphs
		These are the graphs associated with each molecule in the molecules dictionary.
	"""

	# First, get the graph associated with molecule we want to change the charge of
	molecule = molecules[molecule_name]

	# Second, for each molecule to change the charge of atoms of:
	for atom_index, charge in zip(atoms_to_change_charges_of, list_of_charges):

		# 2.1: Change the charge of the atom in molecule_graph
		molecule[atom_index].charge = charge