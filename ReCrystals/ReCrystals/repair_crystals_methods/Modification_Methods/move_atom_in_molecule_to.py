"""
move_atom_in_molecule_to.py, Geoffrey Weal, 2/4/24

This method is designed to move an atom in a molecule to a new position.
"""
import numpy as np

def move_atom_in_molecule_to(molecule_to_move, atom_to_move, position_to_move_atom_to, molecules):
	"""
	This method is designed to move an atom in a molecule to a new position.

	Parameters
	----------
	molecule_to_move : int. 
		This is the molecule to move an atom in.
	atom_to_move : int. 
		This is the atom in a molecule to move.
	position_to_move_atom_to : tuple
		This is the position to move the atom in the molecule to.
	molecules : dict. of ase.Atoms
		These are the molecules in the crystal (Only the structurally unique molecules due to the symmetry of the crystal).
	"""

	# First, for each atom in atom_to_move, position_to_move_atom_to
	for atom_to_move, updated_position in zip(atom_to_move, position_to_move_atom_to):

		# Second, move the atom in the molecule to the new position. 
		molecules[molecule_to_move][atom_to_move].position = np.array(updated_position)