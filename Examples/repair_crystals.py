from ReCrystals import Repair_Crystals

repair_crystals_instructions = {}

# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - 

repair_crystals_instructions['AFUZIN'] = [{'action': 'remove_molecules', 'molecules': 3}]
repair_crystals_instructions['AJUCAK'] = [{'action': 'remove_molecules', 'molecules': 6}]

repair_crystals_instructions['ANCTNB'] = []
repair_crystals_instructions['ANCTNB'].append({'action': 'move_atom_to', 'molecule': 2, 'atoms': {12: (-3.7497, 0.0377, 0.5917), 4:  (-0.7413, 0.0377, 4.2583)}})

repair_crystals_instructions['ARUJOP'] = []
repair_crystals_instructions['ARUJOP'].append({'action': 'add_methyls',   'molecule': 1, 'atoms': {92:1, 100:1}})
repair_crystals_instructions['ARUJOP'].append({'action': 'add_hydrogens', 'molecule': 1, 'atoms': {98:3,82:2,85:2,76:2,77:1,88:2,89:3,65:2, 92:2, 58:2,86:1,81:2,99:3,90:2,87:2,95:2,101:3, 100:2}})
repair_crystals_instructions['ARUJOP'].append({'action': 'add_methyls',   'molecule': 2, 'atoms': {92:1,95:1}})
repair_crystals_instructions['ARUJOP'].append({'action': 'add_hydrogens', 'molecule': 2, 'atoms': {35:2,70:1,84:2,91:2,83:3,75:2,96:3, 92:2, 59:2,80:1,94:2,97:3,85:2,98:3, 95:2}})
repair_crystals_instructions['ARUJOP'].append({'action': 'add_methyls',   'molecule': 3, 'atoms': {93:1, 95:1}})
repair_crystals_instructions['ARUJOP'].append({'action': 'add_hydrogens', 'molecule': 3, 'atoms': {55:2,70:1,88:2,89:3,84:2,96:2,87:2,92:3, 93:2, 65:2,83:2,94:3, 95:2}})
repair_crystals_instructions['ARUJOP'].append({'action': 'add_methyls',   'molecule': 4, 'atoms': {94:1, 93:1}})
repair_crystals_instructions['ARUJOP'].append({'action': 'add_hydrogens', 'molecule': 4, 'atoms': {57:2,78:1,85:2,92:2,90:3,91:3, 94:2, 48:2,88:1,95:3,89:3, 93:2}})

repair_crystals_instructions['ARUJUV'] = []
repair_crystals_instructions['ARUJUV'].append({'action': 'add_hydrogens', 'molecule': 1, 'atoms': {50:2,53:2,51:2,55:2,58:2,59:3, 47:2,44:2,46:2,49:2,54:2,57:3, 108:2,105:2,107:2,110:2,115:2,118:3, 111:2,114:2,112:2,116:2,119:2,120:3,  121:2,113:3, 60:2,52:3}})
repair_crystals_instructions['ARUJUV'].append({'action': 'add_hydrogens', 'molecule': 2, 'atoms': {36:2,38:2,52:2,51:2,57:2,61:3, 56:2,55:2,53:2,54:2,58:2,59:2,60:2,62:3, 120:2,119:2,117:2,118:2,122:2,123:2,124:2,126:3, 100:2,102:2,116:2,115:2,121:2,125:3, 29:2,37:2,63:3, 93:2,101:2,127:3}})

repair_crystals_instructions['ATEHUC01'] = [{'action': 'remove_molecules', 'molecules': 3}]
repair_crystals_instructions['BALLOT']   = [{'action': 'remove_molecules', 'molecules': 2}]
repair_crystals_instructions['BALBUL']   = [{'action': 'add_hydrogens', 'molecule': 1, 'atoms': 23, 'number_of_hydrogens_to_add': 3}]
repair_crystals_instructions['BARXOL']   = [{'action': 'remove_molecules', 'molecules': 1}]
repair_crystals_instructions['BEHRUD']   = [{'action': 'remove_molecules', 'molecules': 1}]
repair_crystals_instructions['BIHNIR']   = [{'action': 'remove_atoms', 'molecule': 1, 'atoms': [70, 71]+[6, 41]}, {'action': 'add_hydrogens', 'molecule': 1, 'atoms': [4, 39], 'number_of_hydrogens_to_add': 1}] # Check
repair_crystals_instructions['BOMXAE']   = [{'action': 'remove_atoms', 'molecule': 2, 'atoms': [3, 5]}]
repair_crystals_instructions['BOWBIA']   = [{'action': 'remove_molecules', 'molecules': 5}]
repair_crystals_instructions['BOWCOH']   = [{'action': 'remove_molecules', 'molecules': 5}]
repair_crystals_instructions['BOWCUN']   = [{'action': 'remove_molecules', 'molecules': 5}]
repair_crystals_instructions['BUKCUH']   = [{'action': 'remove_molecules', 'molecules': 3}]
repair_crystals_instructions['BUKDAO']   = [{'action': 'remove_molecules', 'molecules': 3}]

#repair_crystals_instructions['CAMHOR'] = [{'action': 'remove_atoms', 'molecule': 1, 'atoms': [30,31,32,42,40,41,43,44,39,38,36,37, 27,29,28, 53,45,46,47,48,49,50,51,52,33,34,35], 'remove_attached_hydrogens': False}]

bond_info = {'bond_type': 'Single', 'involved_in_no_of_rings': 0, 'is_conjugated': False, 'is_cyclic': False, 'bond_type_from_sybyl_type': 1}
repair_crystals_instructions['CAMKEK'] = []
repair_crystals_instructions['CAMKEK'].append({'action': 'add_edges',      'molecule': 1, 'edges': [(26, 27, bond_info)]})
repair_crystals_instructions['CAMKEK'].append({'action': 'remove_atoms',   'molecule': 1, 'atoms': [12, 13, 14, 15, 11] + [23, 24] + [31, 30, 29]})
repair_crystals_instructions['CAMKEK'].append({'action': 'change_element', 'molecule': 1, 'atoms': [18, 25, 26], 'updated_elements': ['N', 'C', 'C']})
repair_crystals_instructions['CAMKEK'].append({'action': 'add_hydrogens',  'molecule': 1, 'atoms': 28, 'number_of_hydrogens_to_add': 3}) # Check this molecule's methyl group.

repair_crystals_instructions['CIWCAP']   = [{'action': 'remove_molecules', 'molecules': 2}]

repair_crystals_instructions['CUMRUA'] = []
repair_crystals_instructions['CUMRUA'].append({'action': 'remove_atoms',  'molecule': 1, 'atoms': [131, 125, 119, 143, 129] + [135, 133, 137, 79] + [123, 127]})
repair_crystals_instructions['CUMRUA'].append({'action': 'add_hydrogens', 'molecule': 1, 'atoms': [130, 124, 118, 142, 128], 'number_of_hydrogens_to_add': [2, 2, 2, 2, 3]})
repair_crystals_instructions['CUMRUA'].append({'action': 'add_hydrogens', 'molecule': 1, 'atoms': [134, 132, 136, 78], 'number_of_hydrogens_to_add': 2})
repair_crystals_instructions['CUMRUA'].append({'action': 'add_hydrogens', 'molecule': 1, 'atoms': [122, 126], 'number_of_hydrogens_to_add': 2})
repair_crystals_instructions['CUMRUA'].append({'action': 'remove_atoms',  'molecule': 2, 'atoms': [138, 118, 116, 109, 126, 146] + [150, 134, 98, 123, 142] + [119, 114, 100, 112, 136, 129, 125], 'remove_attached_hydrogens': True})
repair_crystals_instructions['CUMRUA'].append({'action': 'add_hydrogens', 'molecule': 2, 'atoms': [90, 92]+[93], 'number_of_hydrogens_to_add': [2, 3]+[3]})
repair_crystals_instructions['CUMRUA'].append({'action': 'remove_atoms',  'molecule': 3, 'atoms': [119, 125, 98, 130, 113, 156, 152]+[85]+[143, 147, 140, 146, 150, 151, 159]+[132, 141, 136, 128], 'remove_attached_hydrogens': True})
repair_crystals_instructions['CUMRUA'].append({'action': 'add_hydrogens', 'molecule': 3, 'atoms': [93, 84, 138, 92], 'number_of_hydrogens_to_add': [3, 2, 2, 2]})
repair_crystals_instructions['CUMRUA'].append({'action': 'remove_atoms',  'molecule': 4, 'atoms': [132,121,127,130,157,154,160,150]+[81]+[112,102,105,93,79,100,118,136]+[163,124,119,116,145,144,146]+[140,107,82,70,92,64,80,95], 'remove_attached_hydrogens': True})
repair_crystals_instructions['CUMRUA'].append({'action': 'add_hydrogens', 'molecule': 4, 'atoms': [111]+[75]+[91]+[45], 'number_of_hydrogens_to_add': [3]+[2]+[3]+[3]})

repair_crystals_instructions['EBOZEE'] = []
repair_crystals_instructions['EBOZEE'].append({'action': 'add_hydrogens', 'molecule': 1, 'atoms': [43, 114]+[135,141]+[140]+[70,64]+[69], 'number_of_hydrogens_to_add': [2, 2]+[3]*6})
repair_crystals_instructions['EBOZEE'].append({'action': 'remove_atoms',  'molecule': 2, 'atoms': [31,32] + [99,100]})
repair_crystals_instructions['EBOZEE'].append({'action': 'change_hybridisation', 'molecule': 2, 'atoms': [98,30], 'updated_hybridisations': 'sp2'})
repair_crystals_instructions['EBOZEE'].append({'action': 'add_hydrogens', 'molecule': 2, 'atoms': [63, 131]+[124,117,49,56]+[98,30], 'number_of_hydrogens_to_add': [3]*6 + [1,1]})

repair_crystals_instructions['EBOZII'] = []
repair_crystals_instructions['EBOZII'].append({'action': 'change_hybridisation', 'molecule': 1, 'atoms': [97,33], 'updated_hybridisations': 'sp3'})
repair_crystals_instructions['EBOZII'].append({'action': 'add_hydrogens', 'molecule': 1, 'atoms': {53:2,49:2,33:2,52:3, 97:2,113:2,117:2,116:3, 109:3,115:3, 45:3,51:3}, 'remove_existing_hydrogens': True})
repair_crystals_instructions['EBOZII'].append({'action': 'add_hydrogens', 'molecule': 2, 'atoms': [107,108,105,106]+[51,50,53,52], 'number_of_hydrogens_to_add': 3})

repair_crystals_instructions['ECIQUC'] = [{'action': 'remove_molecules', 'molecules': 4}]
repair_crystals_instructions['ECIREN'] = [{'action': 'remove_molecules', 'molecules': 2}]

repair_crystals_instructions['EGOFEN'] = []
repair_crystals_instructions['EGOFEN'].append({'action': 'change_charges', 'molecule': 1, 'atoms': [36,12], 'updated_charges': 0})
repair_crystals_instructions['EGOFEN'].append({'action': 'add_hydrogens',  'molecule': 1, 'atoms': [36,12], 'number_of_hydrogens_to_add': 2, 'remove_existing_hydrogens': True})

repair_crystals_instructions['EHICOO'] = [{'action': 'remove_molecules', 'molecules': 1}] # C60 has been removed, will not be good for KMC

repair_crystals_instructions['ELERAR'] = []
repair_crystals_instructions['ELERAR'].append({'action': 'add_hydrogens', 'molecule': 2, 'atoms': [29,32,40]+[37]+[58,59,66,57]+[19,35,65]+[46,50,47,52], 'number_of_hydrogens_to_add': [1,1,1]+[3]+[2,3,2,3]+[2,2,3]+[1,1,1,1]})
repair_crystals_instructions['ELERAR'].append({'action': 'remove_atoms',  'molecule': 3, 'atoms': [34,65]})
repair_crystals_instructions['ELERAR'].append({'action': 'add_hydrogens', 'molecule': 3, 'atoms': [15,12,4]+[25,81,23]+[28,76,67,19,26]+[46,75,24,77,78,68]+[66]+[62,59,56,57], 'number_of_hydrogens_to_add': [1,1,1]+[2,2,3]+[2,1,3,2,3]+[2,1,2,3,2,3]+[3]+[1,1,1,1]})
repair_crystals_instructions['ELERAR'].append({'action': 'add_hydrogens', 'molecule': 1, 'atoms': 2, 'number_of_hydrogens_to_add': 2})
repair_crystals_instructions['ELERAR'].append({'action': 'add_hydrogens', 'molecule': 4, 'atoms': 2, 'number_of_hydrogens_to_add': 2})
repair_crystals_instructions['ELERAR'].append({'action': 'add_hydrogens', 'molecule': 5, 'atoms': 2, 'number_of_hydrogens_to_add': 2})
repair_crystals_instructions['ELERAR'].append({'action': 'add_hydrogens', 'molecule': 6, 'atoms': 1, 'number_of_hydrogens_to_add': 2})
repair_crystals_instructions['ELERAR'].append({'action': 'remove_molecules', 'molecules': 7})

repair_crystals_instructions['EQEMOF'] = []
repair_crystals_instructions['EQEMOF'].append({'action': 'remove_molecules', 'molecules': 7})
repair_crystals_instructions['EQEMOF'].append({'action': 'remove_molecules', 'molecules': 9})

repair_crystals_instructions['EZETOU'] = []
repair_crystals_instructions['EZETOU'].append({'action': 'remove_atoms',  'molecule': 1, 'atoms': [65,68,58,61], 'remove_attached_hydrogens': True})
repair_crystals_instructions['EZETOU'].append({'action': 'add_hydrogens', 'molecule': 1, 'atoms': 15, 'number_of_hydrogens_to_add': 2})

repair_crystals_instructions['FAPXON'] = []
repair_crystals_instructions['FAPXON'].append({'action': 'change_hybridisation', 'molecule': 2, 'atoms': [67], 'updated_hybridisations': 'sp2'})
repair_crystals_instructions['FAPXON'].append({'action': 'add_hydrogens', 'molecule': 2, 'atoms': [46,61,32]+[92,93,91]+[44,38,50,72,96,97,99,98,88,89,83,94]+[78,77,57,53,37,55,81,95,33]+[90]+[63,67,85], 'number_of_hydrogens_to_add': [1,1,1]+[2,2,3]+[2,1,2,2,2,2,2,3,2,2,2,3]+[3,2,2,2,1,2,2,3,2]+[3]+[1,1,1]})

repair_crystals_instructions['FAPXUT'] = [] # Check
repair_crystals_instructions['FAPXUT'].append({'action': 'change_hybridisation', 'molecule': 4, 'atoms': [14, 21], 'updated_hybridisations': 'sp2'})
repair_crystals_instructions['FAPXUT'].append({'action': 'remove_atoms',  'molecule': 4, 'atoms': [89,90,84,86,85,88,87]+[91,83,82,80,67,79]})
repair_crystals_instructions['FAPXUT'].append({'action': 'add_hydrogens', 'molecule': 4, 'atoms': [70,73,44,21,76]+[65,55]+[81,14,58,50,53]+[14,21], 'number_of_hydrogens_to_add': [1,1,1,1,3]+[3,3]+[3,1,1,1,1]+[1,1]})

repair_crystals_instructions['FEBTEP'] = []
repair_crystals_instructions['FEBTEP'].append({'action': 'remove_atoms',  'molecule': 1, 'atoms': [37,100], 'remove_attached_hydrogens': True})
repair_crystals_instructions['FEBTEP'].append({'action': 'add_hydrogens', 'molecule': 1, 'atoms': [36], 'number_of_hydrogens_to_add': 3})

repair_crystals_instructions['GEGFIJ'] = []
repair_crystals_instructions['GEGFIJ'].append({'action': 'remove_atoms',  'molecule': 3, 'atoms': [132,135,138,141,143,142,70,71,69,66,63,60], 'remove_attached_hydrogens': True, 'create_new_molecules': True})
repair_crystals_instructions['GEGFIJ'].append({'action': 'add_hydrogens', 'molecule': 3, 'atoms': [129,57], 'number_of_hydrogens_to_add': 1})

repair_crystals_instructions['GUXMIW'] = []
repair_crystals_instructions['GUXMIW'].append({'action': 'remove_atoms',  'molecule': 1, 'atoms': [80,81,161,97,99,104,106,110,111]+[78,79,158,95,91,90,86,84,82], 'remove_attached_hydrogens': True})
repair_crystals_instructions['GUXMIW'].append({'action': 'change_hybridisation', 'molecule': 1, 'atoms': [10,9], 'updated_hybridisations': 'sp2'})
repair_crystals_instructions['GUXMIW'].append({'action': 'add_hydrogens', 'molecule': 1, 'atoms': [10,9], 'number_of_hydrogens_to_add': 1})

repair_crystals_instructions['HOCTUR'] = []
repair_crystals_instructions['HOCTUR'].append({'action': 'remove_atoms',  'molecule': 1, 'atoms': [350,349,134,348,53,313,351], 'remove_attached_hydrogens': True})
repair_crystals_instructions['HOCTUR'].append({'action': 'change_hybridisation', 'molecule': 1, 'atoms': [133,52,312], 'updated_hybridisations': 'sp2'})
repair_crystals_instructions['HOCTUR'].append({'action': 'add_hydrogens', 'molecule': 1, 'atoms': [133,52,312], 'number_of_hydrogens_to_add': 1})

repair_crystals_instructions['ICEKEK'] = []
repair_crystals_instructions['ICEKEK'].append({'action': 'add_hydrogens', 'molecule': 6, 'atoms': [97,98,62,22,143,155,175,224,220,236], 'number_of_hydrogens_to_add': [2,3,3,3,3,2,3,3,3,3]})

repair_crystals_instructions['IZAMEE'] = [{'action': 'remove_molecules', 'molecules': 3}]

repair_crystals_instructions['JETQIL'] = []
repair_crystals_instructions['JETQIL'].append({'action': 'remove_atoms', 'molecule': 1, 'atoms': [142], 'remove_attached_hydrogens': True})
repair_crystals_instructions['JETQIL'].append({'action': 'add_methyls',  'molecule': 1, 'atoms': {141: 1}})

repair_crystals_instructions['JITLII'] = []
repair_crystals_instructions['JITLII'].append({'action': 'change_hybridisation', 'molecule':  1, 'atoms': [2,4,6,11,12,13,15,16,17,72,71,70,68,67,66,61,59,57], 'updated_hybridisations': 'sp2'})
repair_crystals_instructions['JITLII'].append({'action': 'remove_atoms',  'molecule': 1, 'atoms': [3,5,14,69,60,58]})
repair_crystals_instructions['JITLII'].append({'action': 'add_hydrogens', 'molecule':  1, 'atoms': [2,4,13,68,59,57], 'number_of_hydrogens_to_add': 1})

repair_crystals_instructions['KUMTAQ'] = []
repair_crystals_instructions['KUMTAQ'].append({'action': 'remove_atoms',  'molecule': 1, 'atoms': [40,41]+[59,44,62,66], 'remove_attached_hydrogens': True})
repair_crystals_instructions['KUMTAQ'].append({'action': 'add_hydrogens', 'molecule': 1, 'atoms': [74,75]+[23], 'number_of_hydrogens_to_add': 2})

repair_crystals_instructions['KUNPOA'] = []
repair_crystals_instructions['KUNPOA'].append({'action': 'add_hydrogens', 'molecule': 1, 'atoms': [60,11], 'number_of_hydrogens_to_add': 1})

repair_crystals_instructions['KUZPOL01'] = []
repair_crystals_instructions['KUZPOL01'].append({'action': 'remove_atoms',  'molecule': 1, 'atoms': [20,23,31,27, 57,54,65,61], 'remove_attached_hydrogens': True})
repair_crystals_instructions['KUZPOL01'].append({'action': 'add_hydrogens', 'molecule': 1, 'atoms': [53,19], 'number_of_hydrogens_to_add': 2})

repair_crystals_instructions['LAGWAV'] = []
repair_crystals_instructions['LAGWAV'].append({'action': 'remove_atoms',  'molecule': 1, 'atoms': [35,36,33]+[96,99,98]})
repair_crystals_instructions['LAGWAV'].append({'action': 'add_hydrogens', 'molecule': 1, 'atoms': [32,34]+[95,97], 'number_of_hydrogens_to_add': [2,3,2,3]})

repair_crystals_instructions['LAHLUF'] = []
repair_crystals_instructions['LAHLUF'].append({'action': 'remove_atoms',  'molecule': 1, 'atoms': [86,89,88]+[52,55,54]})
repair_crystals_instructions['LAHLUF'].append({'action': 'add_hydrogens', 'molecule': 1, 'atoms': [85,87]+[51,53], 'number_of_hydrogens_to_add': [2,3]+[2,3]})

repair_crystals_instructions['LUJYAT'] = []
repair_crystals_instructions['LUJYAT'].append({'action': 'change_hybridisation', 'molecule': 1, 'atoms': [40,47,44,46,39,35,34,52,76,73,78], 'updated_hybridisations': 'sp2'})
repair_crystals_instructions['LUJYAT'].append({'action': 'add_hydrogens',        'molecule': 1, 'atoms': [44,46,47,34]+[38,54,59,85]+[53,57,51,58,62,86,30]+[55,49,50,60,64,41]+[56,61,63]+[52,76,73,78], 'number_of_hydrogens_to_add': [1,1,1,1]+[2,2,2,3]+[3,2,1,2,2,3,2]+[3,2,1,2,3,2]+[2,2,3]+[1,1,1,1]})
repair_crystals_instructions['LUJYAT'].append({'action': 'change_hybridisation', 'molecule': 2, 'atoms': [45,47,51,56,29,42,36,41], 'updated_hybridisations': 'sp2'})
repair_crystals_instructions['LUJYAT'].append({'action': 'add_hydrogens',        'molecule': 2, 'atoms': {48:1,51:1,47:1,56:1,83:3,82:2,81:2,69:2,67:2,38:2,44:1,66:2,70:3,45:2,58:3,25:2,63:2,68:3,39:2,46:2,61:3,29:1,41:1,42:1,36:1}})
repair_crystals_instructions['LUJYAT'].append({'action': 'change_hybridisation', 'molecule': 3, 'atoms': [20,27,24,18,61,58,55,56], 'updated_hybridisations': 'sp2'})
repair_crystals_instructions['LUJYAT'].append({'action': 'remove_atoms',         'molecule': 3, 'atoms': [68,70,69]})
repair_crystals_instructions['LUJYAT'].append({'action': 'add_hydrogens',        'molecule': 3, 'atoms': {20:1,27:1,24:1,18:1,38:2,44:2,67:3, 39:2,42:2,43:2,45:3, 51:2,52:3, 71:3 ,61:1,58:1,55:1,56:1}})
repair_crystals_instructions['LUJYAT'].append({'action': 'change_hybridisation', 'molecule': 4, 'atoms': [46,55,39,22,58,61,62,64], 'updated_hybridisations': 'sp2'})
repair_crystals_instructions['LUJYAT'].append({'action': 'add_hydrogens',        'molecule': 4, 'atoms': {46:1,55:1,39:1,22:1, 44:2,53:2,66:2,86:2,76:3, 36:2,68:1,87:3,71:2,70:3, 37:2,49:1,69:2,73:3,80:2,59:2,83:2,82:3, 67:2,72:2,74:3, 58:1,61:1,62:1,64:1}})
repair_crystals_instructions['LUJYAT'].append({'action': 'change_hybridisation', 'molecule': 5, 'atoms': [51,47,46,29,57,77,74,75], 'updated_hybridisations': 'sp2'})
repair_crystals_instructions['LUJYAT'].append({'action': 'add_hydrogens',        'molecule': 5, 'atoms': {51:1,47:1,46:1,29:1, 39:2,58:2,65:3, 32:2,63:1,68:2,61:3,66:2,69:2,85:3, 53:2,50:1,72:2,67:3,60:2,59:2,86:2,87:3, 62:2,70:2,71:3, 57:1,77:1,74:1,75:1}})
repair_crystals_instructions['LUJYAT'].append({'action': 'change_hybridisation', 'molecule': 6, 'atoms': [54,56,57,60,17,20,22,31], 'updated_hybridisations': 'sp2'})
repair_crystals_instructions['LUJYAT'].append({'action': 'add_hydrogens',        'molecule': 6, 'atoms': {54:1,56:1,57:1, 63:3, 49:3, 34:2,35:2,65:2,37:3, 21:2,36:3, 60:1,17:1,20:1,22:1,31:1}})

repair_crystals_instructions['MUPMOC'] = []
repair_crystals_instructions['MUPMOC'].append({'action': 'add_hydrogens', 'molecule': 1, 'atoms': {73:2,78:2,82:2,122:3, 37:2,77:2,74:3}})
repair_crystals_instructions['MUPMOC'].append({'action': 'add_hydrogens', 'molecule': 2, 'atoms': {88:3, 43:2,60:2,99:2,102:3}})

repair_crystals_instructions['NAGVOK'] = []
repair_crystals_instructions['NAGVOK'].append({'action': 'remove_atoms',  'molecule': 4, 'atoms': 4})
repair_crystals_instructions['NAGVOK'].append({'action': 'add_hydrogens', 'molecule': 4, 'atoms': {2:1}}) # <-- moving atom, could make a method that allows only the hydrogens in a molecule to move. 

repair_crystals_instructions['NOJPEK'] = []
repair_crystals_instructions['NOJPEK'].append({'action': 'remove_atoms',  'molecule': 2, 'atoms': [37,43,40,36,45,41,44]})
repair_crystals_instructions['NOJPEK'].append({'action': 'add_hydrogens', 'molecule': 2, 'atoms': {4:1,1:1,8:1,14:1,24:1,18:1,11:1,16:1, 27:1, 32:3, 35:1,39:1,42:1,38:1,34:1, 33:3}}) # <-- moving atom, could make a method that allows only the hydrogens in a molecule to move. 

repair_crystals_instructions['NOKSIS'] = []
repair_crystals_instructions['NOKSIS'].append({'action': 'remove_atoms',  'molecule': 1, 'atoms': [77,150,78,152,151,79]})
repair_crystals_instructions['NOKSIS'].append({'action': 'add_hydrogens', 'molecule': 1, 'atoms': {72:3, 25:3}})

repair_crystals_instructions['OVOYOP'] = [] 
atoms_to_modify_OVOYOP = [30,24,37,43, 77,72,88,82, 66,59,54,48]
repair_crystals_instructions['OVOYOP'].append({'action': 'change_hybridisation', 'molecule': 1, 'atoms': [15,20,18,19,17,16] + atoms_to_modify_OVOYOP,  'updated_hybridisations': 'sp2'})
repair_crystals_instructions['OVOYOP'].append({'action': 'add_hydrogens',        'molecule': 1, 'atoms': atoms_to_modify_OVOYOP, 'number_of_hydrogens_to_add': 1})
repair_crystals_instructions['OVOYOP'].append({'action': 'add_methyls',          'molecule': 1, 'atoms': [15,20,18,19,17,16], 'number_of_methyls_to_add': 1})

repair_crystals_instructions['PAZHAD'] = []
repair_crystals_instructions['PAZHAD'].append({'action': 'add_hydrogens', 'molecule': 1, 'atoms': [76,90,83,86,85,84], 'number_of_hydrogens_to_add': 3})
repair_crystals_instructions['PAZHAD'].append({'action': 'add_hydrogens', 'molecule': 1, 'atoms': [54,87,88], 'number_of_hydrogens_to_add': 1})
repair_crystals_instructions['PAZHAD'].append({'action': 'add_hydrogens', 'molecule': 7, 'atoms': [93,77,91,89,79,90], 'number_of_hydrogens_to_add': 3})

repair_crystals_instructions['PUVKEX'] = [{'action': 'remove_molecules', 'molecules': 3}]
repair_crystals_instructions['QALGIW'] = [{'action': 'remove_molecules', 'molecules': [3]}] # check there is a 4.
repair_crystals_instructions['RUMSEA'] = [{'action': 'add_hydrogens', 'molecule': 1, 'atoms': [62,58,121,125], 'number_of_hydrogens_to_add': 3}]

repair_crystals_instructions['RUMSIE'] = []
repair_crystals_instructions['RUMSIE'].append({'action': 'add_hydrogens', 'molecule': 2, 'atoms': [174,175,86,87], 'number_of_hydrogens_to_add': [2,3,2,3]})
repair_crystals_instructions['RUMSIE'].append({'action': 'add_hydrogens', 'molecule': 3, 'atoms': [135,139,124,120], 'number_of_hydrogens_to_add': 3})

repair_crystals_instructions['SAZQIX'] = []
repair_crystals_instructions['SAZQIX'].append({'action': 'change_hybridisation', 'molecule': 1, 'atoms': [69,70], 'updated_hybridisations': 'sp3'})
repair_crystals_instructions['SAZQIX'].append({'action': 'add_ethyls',           'molecule': 1, 'atoms': {69:1,70:1}})
repair_crystals_instructions['SAZQIX'].append({'action': 'add_hydrogens',        'molecule': 1, 'atoms': {71:3,68:3}})
repair_crystals_instructions['SAZQIX'].append({'action': 'change_hybridisation', 'molecule': 2, 'atoms': [68,69], 'updated_hybridisations': 'sp3'})
repair_crystals_instructions['SAZQIX'].append({'action': 'add_ethyls',           'molecule': 2, 'atoms': {69:1,68:1}})
repair_crystals_instructions['SAZQIX'].append({'action': 'add_hydrogens',        'molecule': 2, 'atoms': {50:3,70:3}})

repair_crystals_instructions['SAZQOD'] = []
repair_crystals_instructions['SAZQOD'].append({'action': 'change_hybridisation', 'molecule': 1, 'atoms': [4,70], 'updated_hybridisations': 'sp3'})
repair_crystals_instructions['SAZQOD'].append({'action': 'add_ethyls',           'molecule': 1, 'atoms': {4:1,70:1}})
repair_crystals_instructions['SAZQOD'].append({'action': 'add_hydrogens',        'molecule': 1, 'atoms': {71:3,68:3}})

repair_crystals_instructions['TETTRI03'] = [{'action': 'remove_molecules', 'molecules': 2}]
repair_crystals_instructions['TETTRI04'] = [{'action': 'remove_molecules', 'molecules': 2}]
repair_crystals_instructions['TETTRI05'] = [{'action': 'remove_molecules', 'molecules': 2}]
repair_crystals_instructions['TETTRI07'] = [{'action': 'remove_molecules', 'molecules': 2}]

repair_crystals_instructions['TIVVIF'] = [{'action': 'remove_molecules', 'molecules': 2}]

repair_crystals_instructions['TUGJEN'] = []
repair_crystals_instructions['TUGJEN'].append({'action': 'add_hydrogens', 'molecule': 1, 'atoms': {74:2,99:2,100:2,101:2,102:2,104:3, 85:2,68:1,84:2,89:2,90:2,92:2,95:2,97:3,87:2,91:2,93:2,94:3, 75:2,63:1,73:2,98:2,77:2,80:2,82:3,76:2,78:2,79:2,81:2,88:3, 67:2,83:2,72:2,96:2,86:2,103:3}})
repair_crystals_instructions['TUGJEN'].append({'action': 'add_hydrogens', 'molecule': 2, 'atoms': {68:3, 35:2,73:1,83:2,86:2,88:2,92:3,84:2,94:2,85:2,87:2,89:2,93:3, 65:2,38:1,75:2,77:2,79:2,80:3,74:2,76:2,78:2,81:2,82:2,90:3, 64:3}})

repair_crystals_instructions['UCIJOF'] = []
repair_crystals_instructions['UCIJOF'].append({'action': 'remove_atoms',  'molecule': 1, 'atoms': [45,47]})
repair_crystals_instructions['UCIJOF'].append({'action': 'add_hydrogens', 'molecule': 1, 'atoms': {31:2}})

repair_crystals_instructions['UKOXUQ'] = [{'action': 'remove_atoms', 'molecule': 1, 'atoms': [3,16], 'remove_attached_hydrogens': True}]

repair_crystals_instructions['UNIHOP'] = []
repair_crystals_instructions['UNIHOP'].append({'action': 'remove_atoms',   'molecule': 1, 'atoms': [46,47,45,94]})
repair_crystals_instructions['UNIHOP'].append({'action': 'change_element', 'molecule': 1, 'atoms': {48:'C'}})
repair_crystals_instructions['UNIHOP'].append({'action': 'add_hydrogens',  'molecule': 1, 'atoms': [10,11,13], 'number_of_hydrogens_to_add': 1})

repair_crystals_instructions['USOTII'] = [] # Hydrogen is a bit wonky
repair_crystals_instructions['USOTII'].append({'action': 'remove_atoms',  'molecule': 1, 'atoms': [87,84,0,3]+[13,17,91,21,24], 'remove_attached_hydrogens': True})
repair_crystals_instructions['USOTII'].append({'action': 'add_hydrogens', 'molecule': 1, 'atoms': {82:2,20:3}})
#repair_crystals_instructions['USOTII'].append({'action': 'remove_atoms',  'molecule': 2, 'atoms': [88,85,77,78,81], 'remove_attached_hydrogens': True})
#repair_crystals_instructions['USOTII'].append({'action': 'add_hydrogens', 'molecule': 2, 'atoms': {76:3}})
#repair_crystals_instructions['USOTII'].append({'action': 'remove_atoms',  'molecule': 3, 'atoms': [18,15,14,10,6]+[53], 'remove_attached_hydrogens': True})
#repair_crystals_instructions['USOTII'].append({'action': 'add_hydrogens', 'molecule': 3, 'atoms': {13:3,52:1}})

repair_crystals_instructions['VOGRIU'] = []
repair_crystals_instructions['VOGRIU'].append({'action': 'remove_atoms',  'molecule': 1, 'atoms': 4})
repair_crystals_instructions['VOGRIU'].append({'action': 'add_hydrogens', 'molecule': 1, 'atoms': {3:1}})

repair_crystals_instructions['WEKYAP'] = [{'action': 'remove_molecules', 'molecules': 2}]

repair_crystals_instructions['XASHEH'] = []
repair_crystals_instructions['XASHEH'].append({'action': 'change_hybridisation', 'molecule': 1, 'atoms': [110, 50],  'updated_hybridisations': 'sp2'})
repair_crystals_instructions['XASHEH'].append({'action': 'add_hydrogens',        'molecule': 1, 'atoms': {110:1, 50:1}, 'remove_existing_hydrogens': True})

repair_crystals_instructions['ZOFTUL'] = [{'action': 'remove_atoms',  'molecule': 1, 'atoms': 1, 'remove_attached_hydrogens': True}]

repair_crystals_instructions['ZUQNUX'] = []
repair_crystals_instructions['ZUQNUX'].append({'action': 'remove_atoms',  'molecule': 2, 'atoms': [69,95,86,31], 'remove_attached_hydrogens': True})
repair_crystals_instructions['ZUQNUX'].append({'action': 'add_hydrogens', 'molecule': 2, 'atoms': [67], 'number_of_hydrogens_to_add': 2})

# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - 
'''
repair_crystals_instructions['ADIXIW'] = []
repair_crystals_instructions['ADIXIW'].append({'action': 'change_element', 'molecule': 1, 'atoms': [35,32], 'updated_elements': 'C'})
repair_crystals_instructions['ADIXIW'].append({'action': 'add_hydrogens',  'molecule': 1, 'atoms': [35,32], 'number_of_hydrogens_to_add': 1})

repair_crystals_instructions['AGINEM'] = []
repair_crystals_instructions['AGINEM'].append({'action': 'remove_atoms',  'molecule': 1, 'atoms': [48, 34, 43], 'remove_attached_hydrogens': True, 'create_new_molecules': True})
repair_crystals_instructions['AGINEM'].append({'action': 'add_hydrogens', 'molecule': 1, 'atoms': [29,20], 'number_of_hydrogens_to_add': 1})

repair_crystals_instructions['AGINIQ'] = []
repair_crystals_instructions['AGINIQ'].append({'action': 'remove_atoms',  'molecule': 1, 'atoms': [46, 12, 3], 'remove_attached_hydrogens': True, 'create_new_molecules': True})
repair_crystals_instructions['AGINIQ'].append({'action': 'add_hydrogens', 'molecule': 1, 'atoms': [22,40], 'number_of_hydrogens_to_add': 1})

repair_crystals_instructions['AGINUC'] = []
repair_crystals_instructions['AGINUC'].append({'action': 'remove_atoms',  'molecule': 1, 'atoms': [5], 'remove_attached_hydrogens': True, 'create_new_molecules': True})
repair_crystals_instructions['AGINUC'].append({'action': 'add_hydrogens', 'molecule': 1, 'atoms': [20,28], 'number_of_hydrogens_to_add': 1})
repair_crystals_instructions['AGINUC'].append({'action': 'remove_atoms',  'molecule': 2, 'atoms': [14], 'remove_attached_hydrogens': True, 'create_new_molecules': True})
repair_crystals_instructions['AGINUC'].append({'action': 'add_hydrogens', 'molecule': 2, 'atoms': [4,44], 'number_of_hydrogens_to_add': 1})

repair_crystals_instructions['AGIYIB'] = []
repair_crystals_instructions['AGIYIB'].append({'action': 'remove_atoms',  'molecule': 1, 'atoms': [50, 55], 'remove_attached_hydrogens': True, 'create_new_molecules': True})
repair_crystals_instructions['AGIYIB'].append({'action': 'add_hydrogens', 'molecule': 1, 'atoms': [22,32], 'number_of_hydrogens_to_add': 1})

repair_crystals_instructions['AGIYOH'] = []
repair_crystals_instructions['AGIYOH'].append({'action': 'remove_atoms',  'molecule': 1, 'atoms': [21, 51], 'remove_attached_hydrogens': True, 'create_new_molecules': True})
repair_crystals_instructions['AGIYOH'].append({'action': 'add_hydrogens', 'molecule': 1, 'atoms': [56,35], 'number_of_hydrogens_to_add': 1})
'''
# ===================================================================================================================

Repair_Crystals(repair_crystals_instructions)

# ===================================================================================================================



