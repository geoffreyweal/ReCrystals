from ReCrystals import Repair_Crystals

repair_crystals_instructions = {}

repair_crystals_instructions['AFUZIN'] = [{'action': 'remove_molecules', 'molecules': 3}]
repair_crystals_instructions['AJUCAK'] = [{'action': 'remove_molecules', 'molecules': 6}]

repair_crystals_instructions['ARUJOP'] = []
repair_crystals_instructions['ARUJOP'].append({'action': 'remove_atoms', 'molecule': 1, 'atoms': [98, 82, 85, 76, 77, 88, 89, 101, 95, 87, 90, 86, 81, 99]})
repair_crystals_instructions['ARUJOP'].append({'action': 'remove_atoms', 'molecule': 2, 'atoms': [83, 91, 84, 70, 75, 96, 98, 85, 80, 94, 97]})
repair_crystals_instructions['ARUJOP'].append({'action': 'remove_atoms', 'molecule': 3, 'atoms': [89, 88, 70, 84, 96, 87, 92, 94, 83]})
repair_crystals_instructions['ARUJOP'].append({'action': 'remove_atoms', 'molecule': 4, 'atoms': [90, 92, 85, 78, 91, 95, 88, 89]})
repair_crystals_instructions['ARUJOP'].append({'action': 'add_hydrogens', 'molecule': 1, 'atoms': [92, 65, 58, 100], 'number_of_hydrogens_to_add': 3})
repair_crystals_instructions['ARUJOP'].append({'action': 'add_hydrogens', 'molecule': 2, 'atoms': [35, 59, 92, 95], 'number_of_hydrogens_to_add': 3})
repair_crystals_instructions['ARUJOP'].append({'action': 'add_hydrogens', 'molecule': 3, 'atoms': [55, 65, 95, 93], 'number_of_hydrogens_to_add': 3})
repair_crystals_instructions['ARUJOP'].append({'action': 'add_hydrogens', 'molecule': 4, 'atoms': [48, 57, 93, 94], 'number_of_hydrogens_to_add': 3})

repair_crystals_instructions['ANCTNB'] = []
repair_crystals_instructions['ANCTNB'].append({'action': 'move_atom_to', 'molecule': 2, 'atoms': {12: (-3.7497, 0.0377, 0.5917), 4:  (-0.7413, 0.0377, 4.2583)}})

bond_info = {'bond_type': 'Single', 'involved_in_no_of_rings': 0, 'is_conjugated': False, 'is_cyclic': False, 'bond_type_from_sybyl_type': 1}
repair_crystals_instructions['CAMKEK'] = []
repair_crystals_instructions['CAMKEK'].append({'action': 'remove_atoms',   'molecule': 1, 'atoms': [12, 13, 14, 15, 11]+[23, 24]+[31, 30, 29], 'add_edges_after_removing_atoms': [(26, 27, bond_info)]})
repair_crystals_instructions['CAMKEK'].append({'action': 'change_element', 'molecule': 1, 'atoms': [18, 25, 26], 'updated_elements': ['N', 'C', 'C']})
repair_crystals_instructions['CAMKEK'].append({'action': 'add_hydrogens',  'molecule': 1, 'atoms': 28, 'number_of_hydrogens_to_add': 3})

repair_crystals_instructions['EBOZII'] = []
repair_crystals_instructions['EBOZII'].append({'action': 'change_hybridisation', 'molecule': 1, 'atoms': [97,33], 'updated_hybridisations': 'sp3'})
repair_crystals_instructions['EBOZII'].append({'action': 'add_hydrogens', 'molecule': 1, 'atoms': {53:2,49:2,33:2,52:3, 97:2,113:2,117:2,116:3, 109:3,115:3, 45:3,51:3}, 'remove_existing_hydrogens': True})
repair_crystals_instructions['EBOZII'].append({'action': 'add_hydrogens', 'molecule': 2, 'atoms': [107,108,105,106]+[51,50,53,52], 'number_of_hydrogens_to_add': 3})

repair_crystals_instructions['EGOFEN'] = []
repair_crystals_instructions['EGOFEN'].append({'action': 'change_charges', 'molecule': 1, 'atoms': [36,12], 'updated_charges': 0})
repair_crystals_instructions['EGOFEN'].append({'action': 'add_hydrogens',  'molecule': 1, 'atoms': [36,12], 'number_of_hydrogens_to_add': 2, 'remove_existing_hydrogens': True})

repair_crystals_instructions['SAZQIX'] = []
repair_crystals_instructions['SAZQIX'].append({'action': 'add_ethyls',    'molecule': 1, 'atoms': [69, 70], 'number_of_ethyls_to_add': 1})
#repair_crystals_instructions['SAZQIX'].append({'action': 'add_ethyls',    'molecule': 1, 'atoms': [69, 70], 'number_of_ethyls_to_add': [1, 1]}) # Another way to write the above
repair_crystals_instructions['SAZQIX'].append({'action': 'add_hydrogens', 'molecule': 1, 'atoms': {71:3,68:3}})
repair_crystals_instructions['SAZQIX'].append({'action': 'add_ethyls',    'molecule': 2, 'atoms': {69:1,68:1}})
repair_crystals_instructions['SAZQIX'].append({'action': 'add_hydrogens', 'molecule': 2, 'atoms': {50:3,70:3}})

repair_crystals_instructions['SAZQOD'] = []
repair_crystals_instructions['SAZQOD'].append({'action': 'add_methyls',   'molecule': 1, 'atoms': {4:1,70:1}})
repair_crystals_instructions['SAZQOD'].append({'action': 'add_hydrogens', 'molecule': 1, 'atoms': {71:3,68:3}})

# ===================================================================================================================

Repair_Crystals(repair_crystals_instructions)

# ===================================================================================================================



