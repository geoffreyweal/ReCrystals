"""
reorder_instructions.py, Geoffrey Weal, 5/4/24

This method is designed to reorder the instructions given in the instructions list.

This is so that atoms are removed before new hydrogens and methyls are added to the molecule. 
"""
from copy import deepcopy

# This is the order of actions to be performed in:
actions_to_perform_in_order = ('remove_edges', 'add_edges', 'update_edges', 'remove_molecules', 'remove_atoms', 'move_atom_to', 'change_element', 'change_hybridisation', 'change_charges', 'change_magnetic_moments', 'change_added_or_modified_tags', 'add_methyls', 'add_ethyls', 'add_hydrogens')

def reorder_instructions(unordered_instructions):
	"""
	This is so that atoms are removed before new hydrogens and methyls are added to the molecule. 

	Parameters
	----------
	unordered_instructions : list
		This is the original instructions list that has not been ordered

	Returns
	-------
	ordered_instructions : list
		This is the instructions list that has been ordered so that remove actions are performed first and hydrogen+methyl additions are performed last.
	"""

	# First, categorise the instructions from unordered_instructions into categories based on actions_to_perform_in_order
	categorised_instructions = {action_type : [] for action_type in actions_to_perform_in_order}

	# Second, for each instruction in unordered_instructions:
	for instruction in unordered_instructions:

		# 2.1: Get the action type from instruction['action']
		action = instruction['action']

		# 2.2: Append a copy of instruction to the appropriate action type in categorised_instructions
		categorised_instructions[action].append(instruction)

	# Third, initialise the list of ordered instructions
	ordered_instructions = []

	# Fourth, add all the instructions from categorised_instructions to ordered_instructions in order of actions_to_perform_in_order
	for action_to_perform in actions_to_perform_in_order:
		ordered_instructions += categorised_instructions[action_to_perform]

	# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - 
	# Fifth, check that all the instructions in unordered_instructions have been transferred to ordered_instructions.

	# 5.1: Check that all the instructions in ordered_instructions can be found in unordered_instruction with any extra instructions
	#      or any instructions that have changed during transfer.
	ordered_instructions_to_check = deepcopy(ordered_instructions)
	instruction_not_found_in_ordered_instructions = []
	for unordered_instruction in unordered_instructions:
		if not unordered_instruction in ordered_instructions_to_check:
			instruction_not_found_in_ordered_instructions.append(unordered_instruction)
		else:
			ordered_instructions_to_check.remove(unordered_instruction)

	# 5.2: If there are instructions in ordered_instructions that were not found in unordered_instruction, report this.
	if len(instruction_not_found_in_ordered_instructions) > 0:
		to_string  = 'Error: Some instructions have not been transfered successfully from the unordered list to the ordered list.\n'
		to_string += f'unordered_instructions = {unordered_instructions}\n'
		to_string += f'ordered_instructions = {ordered_instructions}\n'
		to_string += 'Check this.'
		raise Exception(to_string)

	# 5.3: If there are still instructions in ordered_instructions_to_check, then ordered_instructions may have extra instructions is it.
	if len(ordered_instructions_to_check) > 0:
		to_string  = 'Error: ordered_instructions might contain extra instructions compared to unordered_instructions.\n'
		to_string += f'unordered_instructions = {unordered_instructions}\n'
		to_string += f'ordered_instructions = {ordered_instructions}\n'
		to_string += f'extra instruction in ordered_instructions = {ordered_instructions_to_check}\n'
		to_string += 'Check this.'
		raise Exception(to_string)		

	# 5.4: Make sure that ordered_instructions does not contain extra instructions. 
	if not len(ordered_instructions) == len(unordered_instructions):
		to_string  = 'Error: Some instructions have not been transfered successfully from the unordered list to the ordered list.\n'
		to_string += f'unordered_instructions = {unordered_instructions}\n'
		to_string += f'ordered_instructions = {ordered_instructions}\n'
		to_string += 'Check this.'
		raise Exception(to_string)

	# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - 

	# Sixth, return ordered_instructions
	return ordered_instructions
