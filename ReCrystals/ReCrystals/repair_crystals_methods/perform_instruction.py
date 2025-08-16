"""
perform_instruction.py, Geoffrey Weal, 2/4/24

This method is designed to execute an instruction upon the molecules in a crystal.
"""
from ReCrystals.ReCrystals.repair_crystals_methods.Instructions.remove_edges_instruction                  import remove_edges_instruction
from ReCrystals.ReCrystals.repair_crystals_methods.Instructions.add_edges_instruction                     import add_edges_instruction
from ReCrystals.ReCrystals.repair_crystals_methods.Instructions.update_edges_instruction                  import update_edges_instruction

from ReCrystals.ReCrystals.repair_crystals_methods.Instructions.remove_molecule_instruction               import remove_molecule_instruction
from ReCrystals.ReCrystals.repair_crystals_methods.Instructions.remove_atoms_instruction                  import remove_atoms_instruction

from ReCrystals.ReCrystals.repair_crystals_methods.Instructions.move_atom_to_instruction                  import move_atom_to_instruction
from ReCrystals.ReCrystals.repair_crystals_methods.Instructions.change_elements_instruction               import change_elements_instruction
from ReCrystals.ReCrystals.repair_crystals_methods.Instructions.change_hybridisations_instruction         import change_hybridisations_instruction
from ReCrystals.ReCrystals.repair_crystals_methods.Instructions.change_charges_instruction                import change_charges_instruction
from ReCrystals.ReCrystals.repair_crystals_methods.Instructions.change_magnetic_moments_instruction       import change_magnetic_moments_instruction
from ReCrystals.ReCrystals.repair_crystals_methods.Instructions.change_added_or_modified_tags_instruction import change_added_or_modified_tags_instruction 

from ReCrystals.ReCrystals.repair_crystals_methods.Instructions.add_ethyls_instruction                    import add_ethyls_instruction
from ReCrystals.ReCrystals.repair_crystals_methods.Instructions.add_methyls_instruction                   import add_methyls_instruction
from ReCrystals.ReCrystals.repair_crystals_methods.Instructions.add_hydrogens_instruction                 import add_hydrogens_instruction

def perform_instruction(instruction, molecules, molecule_graphs, SolventsList, symmetry_operations, cell, identifier, crystal, crystal_graph):
	"""
	This method is designed to execute an instruction upon the molecules in a crystal.

	Parameters
	----------
	instruction : str. 
		This is the instruction you would like to perform upon the molecules in the crystal
	molecules : dict. of ase.Atoms
		These are the molecules in the crystal (Only the structurally unique molecules due to the symmetry of the crystal).
	molecule_graphs : dict. of networkx.Graphs
		These are the graphs associated with each molecule in the molecules dictionary. 
	SolventsList : list
		This list contains all the molecules in the molecules dictionary that are solvents. 
	crystal : ase.Atoms
		This is the ase Atoms object of the crystal of interest we are wanting to repair. 
	crystal_graph : networkx.graph
		This is the graph of the associated graph.
	"""

	# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
	# PART I: Make changes to the bonds (graphs) in the molecule

	# First, if the action is mote atoms to
	if instruction['action'] == 'remove_edges':
		return remove_edges_instruction(instruction, molecules, molecule_graphs)

	# Second, if the action is mote atoms to
	if instruction['action'] == 'add_edges':
		return add_edges_instruction(instruction, molecules, molecule_graphs)

	# Third, if the action is mote atoms to
	if instruction['action'] == 'update_edges':
		return update_edges_instruction(instruction, molecules, molecule_graphs)

	# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
	# PART II: Removing atoms and molecules methods

	# Fourth, if the action is remove molecule
	if instruction['action'] == 'remove_molecules':
		return remove_molecule_instruction(instruction, molecules, molecule_graphs, SolventsList)

	# Fifth, if the action is to remove atoms for a molecule. 
	if instruction['action'] == 'remove_atoms':
		return remove_atoms_instruction(instruction, molecules, molecule_graphs)

	# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
	# PART III: Change components of existing atoms

	# Sixth, if the action is mote atoms to
	if instruction['action'] == 'move_atom_to':
		return move_atom_to_instruction(instruction, molecules)

	# Seventh, Update the element of the atom. 
	if instruction['action'] == 'change_element':
		return change_elements_instruction(instruction, molecules, molecule_graphs)

	# Eighth, Update the hybridisation of the atom. 
	if instruction['action'] == 'change_hybridisation':
		return change_hybridisations_instruction(instruction, molecules, molecule_graphs)

	# Ninth, Update the hybridisation of the atom. 
	if instruction['action'] == 'change_charges':
		return change_charges_instruction(instruction, molecules)

	# Seventh, Update the element of the atom. 
	if instruction['action'] == 'change_magnetic_moments':
		return change_magnetic_moments_instruction(instruction, molecules)

	# Ninth, Update the hybridisation of the atom. 
	if instruction['action'] == 'change_added_or_modified_tags':
		return change_added_or_modified_tags_instruction(instruction, molecules, molecule_graphs)

	# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
	# PART VI: Add atoms to the molecules

	# Tenth, add ethyl group to the system.
	if instruction['action'] == 'add_ethyls':
		return add_ethyls_instruction(instruction, identifier, molecules, molecule_graphs, symmetry_operations, cell, crystal, crystal_graph)

	# Eleventh, add methyl group to the system.
	if instruction['action'] == 'add_methyls':
		return add_methyls_instruction(instruction, identifier, molecules, molecule_graphs, symmetry_operations, cell, crystal, crystal_graph)

	# Twelfth, add hydrogens to the system.
	if instruction['action'] == 'add_hydrogens':
		return add_hydrogens_instruction(instruction, identifier, molecules, molecule_graphs, symmetry_operations, cell, crystal, crystal_graph)

	# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -

	