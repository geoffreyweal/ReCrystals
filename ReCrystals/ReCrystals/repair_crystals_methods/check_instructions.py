"""
check_instructions.py, Geoffrey Weal, 6/4/24

This method is designed to make sure there are no obvious issues with the instructions that have been supplied.
"""

# These are the inputs for each action that are required.
required_inputs = {}

required_inputs['remove_edges']                  = ('action', 'molecule', 'edges')
required_inputs['add_edges']                     = ('action', 'molecule', 'edges')
required_inputs['update_edges']                  = ('action', 'molecule', 'edges')

required_inputs['remove_molecules']              = ('action', 'molecules')
required_inputs['remove_atoms']                  = ('action', 'molecule', 'atoms')

required_inputs['move_atom_to']                  = ('action', 'molecule', 'atoms')
required_inputs['change_element']                = ('action', 'molecule', 'atoms')
required_inputs['change_hybridisation']          = ('action', 'molecule', 'atoms')
required_inputs['change_charges']                = ('action', 'molecule', 'atoms')
required_inputs['change_magnetic_moments']       = ('action', 'molecule', 'atoms')
required_inputs['change_added_or_modified_tags'] = ('action', 'molecule', 'atoms')

required_inputs['add_hydrogens']                 = ('action', 'molecule', 'atoms')
required_inputs['add_methyls']                   = ('action', 'molecule', 'atoms')
required_inputs['add_ethyls']                    = ('action', 'molecule', 'atoms')

# These are the inputs for each action that are optional.
optional_inputs = {}

optional_inputs['remove_molecules']              = tuple([])
optional_inputs['remove_atoms']                  = ('remove_attached_hydrogens', 'create_new_molecules')

optional_inputs['remove_edges']                  = tuple([])
optional_inputs['add_edges']                     = tuple([])
optional_inputs['update_edges']                  = tuple([])

optional_inputs['move_atom_to']                  = tuple([])
optional_inputs['change_element']                = ('updated_elements',)
optional_inputs['change_hybridisation']          = ('updated_hybridisations',)
optional_inputs['change_charges']                = ('updated_charges',)
optional_inputs['change_magnetic_moments']       = ('updated_magnetic_moments',)
optional_inputs['change_added_or_modified_tags'] = ('updated_added_or_modified_tags',)

optional_inputs['add_hydrogens']                 = ('number_of_hydrogens_to_add', 'remove_existing_hydrogens')
optional_inputs['add_methyls']                   = ('number_of_methyls_to_add',)
optional_inputs['add_ethyls']                    = ('number_of_ethyls_to_add',)

# These are the actions to check for.
actions_to_check_for = tuple(required_inputs.keys())

def check_instructions(instructions):
	"""
	This method is designed to make sure there are no obvious issues with the instructions that have been supplied.

	Parameters
	----------
	instructions : list of dicts.
		These are the instructions that you would like to perform.
	"""

	# First, for each instruction in the instructions list
	for counter, instruction in enumerate(instructions,start=1):

		# Second, make sure there is an action input.
		if 'action' not in instruction.keys():
			to_string  = f'Error: You have not given an action in the {counter}-th instruction\n'
			to_string += f'Instruction {counter}: {instruction}\n'
			to_string += f'Check this.'
			raise Exception(to_string)

		# Third, make sure that the action given is valid.
		if instruction['action'] not in actions_to_check_for:
			to_string  = f'Error: The action given in the {counter}-th instruction is not valid\n'
			to_string += f'Action: {instruction["action"]}\n'
			to_string += f'Valid Actions -> {actions_to_check_for}\n'
			to_string += f'Instruction {counter}: {instruction}\n'
			to_string += f'Check this.'
			raise Exception(to_string)

		# Fourth, get the action for the instruction.
		action = instruction['action']

		# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - 
		# Fifth, check that the instruction contains all the required inputs

		# 5.1: Initialise the list to required what required inputs were not found in the instructions dictionary.
		not_found_required_inputs = []

		# 5.2: Determine if every required input can be found in the instruction dictionary. 
		for required_input_name in required_inputs[action]:
			if required_input_name not in instruction.keys():
				not_found_required_inputs.append(required_input_name)

		# 5.3: Raise an exception if there is a missing required input.
		if len(not_found_required_inputs) > 0:
			to_string  = 'Error: Some required inputs were not found in this instruction\n'
			to_string += f'Desired action: {action}\n'
			to_string += f'Required inputs: {required_inputs[action]}\n'
			to_string += f'Missing inputs in your instruction: {not_found_required_inputs}\n'
			to_string += f'Instruction: {instruction}\n'
			to_string += f'Check this.'
			raise Exception(to_string)

		# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - 
		# Sixth, check that all the inputs you have given can be used for the action you are performing. 

		# 6.1: Obtain all the possible accepted inputs for the action of this instruction. 
		all_possible_inputs = tuple(list(required_inputs[action]) + list(optional_inputs[action]))

		# 6.2: Initialise the list to record any inputs that are not valid for this action.
		non_valid_inputs = []

		# 6.3: Check each input in the instruction dictionary, and indicate if any are not valid. 
		for input_name in instruction.keys():
			if input_name not in all_possible_inputs:
				non_valid_inputs.append(input_name)

		# 6.4: Raise an exception if there is an input that is not valid
		if len(non_valid_inputs) > 0:
			to_string  = 'Error: Some of the inputs in this instruction are not valid for this action\n'
			to_string += f'Desired action: {action}\n'
			to_string += f'Valid inputs: {all_possible_inputs}\n'
			to_string += f'Non-valid inputs in your instruction: {non_valid_inputs}\n'
			to_string += f'Instruction: {instruction}\n'
			to_string += f'Check this.'
			raise Exception(to_string)

		# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - 

