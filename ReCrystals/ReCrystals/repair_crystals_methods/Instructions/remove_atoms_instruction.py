"""
remove_atoms_instruction.py, Geoffrey Weal, 5/4/24

This method is designed to remove atoms from a molecule based on instruction.
"""
from copy import deepcopy
from ReCrystals.ReCrystals.repair_crystals_methods.Utilities.get_original_to_modified_atom_indices_for_mol import get_original_to_modified_atom_indices_for_mol
from ReCrystals.ReCrystals.repair_crystals_methods.Modification_Methods.remove_atoms_from_molecule         import remove_atoms_from_molecule

def remove_atoms_instruction(instruction, molecules, molecule_graphs):
	"""
	This method is designed to remove atoms from a molecule based on instruction.

	Parameters
	----------
	instruction : dict. 
		This is the instruction you would like to perform upon the molecules in the crystal
	molecules : dict. of ase.Atoms
		These are the molecules in the crystal (Only the structurally unique molecules due to the symmetry of the crystal).
	molecule_graphs : dict. of networkx.Graphs
		These are the graphs associated with each molecule in the molecules dictionary. 
	"""

	# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - 
	# PART I: Import input variables from the instruction dictionary.

	# First, obtain the molecule to remove atoms from.
	molecule_name = deepcopy(instruction['molecule'])

	# Second, obtain the atoms to remove. 
	atoms_to_remove = deepcopy(instruction['atoms'])

	# Third, indicate if you want to remove any hydrogens that are attached to the atoms you are wanting to remove. 
	remove_attached_hydrogens = deepcopy(instruction['remove_attached_hydrogens']) if 'remove_attached_hydrogens' in instruction else True

	# Fourth, obtain the bonds to add just in case there is an issue that causes fragmentations when removing an atom.
	add_edges_after_removing_atoms = deepcopy(instruction['add_edges_after_removing_atoms']) if ('add_edges_after_removing_atoms' in instruction) else []

	# Fifth, determine if you want to create new molecules if you create multiple components by removing one or more atoms. 
	create_new_molecules = deepcopy(instruction['create_new_molecules']) if 'create_new_molecules' in instruction else False

	# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - 
	# Part II: Make sure that the variable above have been updated so they are ready for the "remove_atoms_from_molecule" method.

	# Sixth, remove any solvent tags in the molecule name. 
	if isinstance(molecule_name, str):
		molecule_name = int(molecule_name.replace('S',''))

	# Seventh, if atoms_to_remove is an interger, convert it into a list 
	if isinstance(atoms_to_remove, int):
		atoms_to_remove = [atoms_to_remove]

	# Eighth, obtain the original_to_modified_atom_indices_for_mol dictionary for molecules[molecule_name]
	original_to_modified_atom_indices_for_mol = get_original_to_modified_atom_indices_for_mol(molecules[molecule_name])

	# Ninth, update the atoms to remove list.
	atoms_to_remove = [original_to_modified_atom_indices_for_mol[atom_to_remove] for atom_to_remove in atoms_to_remove]

	# Tenth, update the atoms to add_edges_after_removing_atoms list.
	add_edges_after_removing_atoms = [(original_to_modified_atom_indices_for_mol[uu], original_to_modified_atom_indices_for_mol[vv], edge_properties) for uu, vv, edge_properties in add_edges_after_removing_atoms]

	# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - 
	# PART III: Run the "remove_atoms_from_molecule" method.

	# Eleventh, remove the atoms from the molecule of interest
	remove_atoms_from_molecule(molecule_name, atoms_to_remove, remove_attached_hydrogens, molecules, molecule_graphs, add_edges_after_removing_atoms=add_edges_after_removing_atoms, create_new_molecules=create_new_molecules)

	# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - 
