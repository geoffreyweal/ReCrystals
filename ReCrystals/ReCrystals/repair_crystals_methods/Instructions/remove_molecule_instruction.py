"""
remove_molecule_instruction.py, Geoffrey Weal, 5/4/24

This method is designed to remove molecules based on instruction.
"""
from copy import deepcopy
from ReCrystals.ReCrystals.repair_crystals_methods.Modification_Methods.remove_molecules import remove_molecules

def remove_molecule_instruction(instruction, molecules, molecule_graphs, SolventsList):
	"""
	This method is designed to remove molecules based on instruction.

	Parameters
	----------
	instruction : dict. 
		This is the instruction you would like to perform upon the molecules in the crystal
	molecules : dict. of ase.Atoms
		These are the molecules in the crystal (Only the structurally unique molecules due to the symmetry of the crystal).
	molecule_graphs : dict. of networkx.Graphs
		These are the graphs associated with each molecule in the molecules dictionary. 
	SolventsList : list
		This list contains all the molecules in the molecules dictionary that are solvents. 
	"""

	# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - 
	# PART I: Import input variables from the instruction dictionary.

	# First, obtain the list of molecules to remove
	molecules_to_remove = deepcopy(instruction['molecules'])

	# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - 
	# Part II: Make sure that the variable above have been updated so they are ready for the "remove_molecules" method.

	# Second, if molecules_to_remove is an int, convert to a list
	if isinstance(molecules_to_remove, int):
		molecules_to_remove = [molecules_to_remove]

	# Third, remove the str in the list to ints, and remove the solvent tag "S" from the names if they exist. 
	for index, molecule_to_remove in enumerate(molecules_to_remove):
		if isinstance(molecule_to_remove, str):
			molecules_to_remove[index] = int(molecule_to_remove.replace('S',''))

	# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - 
	# PART III: Run the "remove_molecules" method.

	# Fourth, remove molecules from the molecules dictionaries in the crystal.
	remove_molecules(molecules_to_remove, molecules, molecule_graphs, SolventsList)

	# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - 
