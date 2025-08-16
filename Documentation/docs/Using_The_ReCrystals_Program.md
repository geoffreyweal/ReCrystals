# Using the ReCrystals Program

This page will describe the general steps of how to use this program, including how to modify the crystals you would like to modify. 

!!! example

	You can find examples for running the ReCrystals program in [the ``Examples`` folder here](https://github.com/geoffreyweal/ReCrystals/tree/main/Examples).

## Preliminary Step: Check the Quality of your Crystal Structure (``get_molecules``)

To begin, we will want to check what our crystal structure looks like. One of the easiest ways to do this is to look at the molecules in the crystals individually. It is possible to obtain the xyz files of each molecule in the crystal individually using the ``get_molecules`` module in the ``SUMELF`` program to separate the crystal into separate molecules. 

To use the ``get_molecules`` module, type the following into your terminal:

```bash
# First, change directory into the directory contain the folder with your crystal files
cd path_to_crystal_database

# Second, run the get_molecules program:
SUMELF get_molecules crystal_database
```

This will separate the crystal into its individual molecules, and save them as individual ``xyz`` file in folder called crystal_database_molecules. You can view these molecules using your favourite GUI viewer, mine is ``ase gui`` ([click here for more about ``ase gui``](https://wiki.fysik.dtu.dk/ase/ase/gui/basics.html)).

!!! info

	You can also use [Mercury (a CCDC program)](https://www.ccdc.cam.ac.uk/solutions/software/free-mercury/) to view the crystal. However, you will need to use the ``get_molecules`` to get the names of the molecules and the atom indices to make modifications to for the  ``Repair_Crystals`` module in the ReCrystals program


## Main Step: Repair the Crystal

The ``Repair_Crystals`` module allows you to repair the molecules in a crystal before recombining them to form the crystal using a python script. Below is an example of a python script called ``repair_crystals.py`` that contains the instructions given by the user to modify and repair the crystal.  

```python title="repair_crystals.py"
--8<-- "docs/Using_The_ReCrystals_Program/repair_crystals.py"
```

Here, a dictionary called ``repair_crystals_instructions`` contains the names of the crystals you want to repair from the ``ACSD`` or ``xyzCrystal`` programs, along with a list of all the instructions you would like to perform upon the crystal. 

An instruction is itself a dictionary the contains an action, along with options for that action. 

```python
instruction = {'action': 'action here', ...}
```

The actions available are:

* ``remove_edges``: Remove edges that connect atoms together in the crystal. This is used if bonds were given between two atoms that should not exist. 
* ``add_edges``: Add edges to connect atoms together in the crystal. This is used if bonds were not given between atoms in the crystal file.
* ``update_edges``: Update an edges that already exists in the crystal. 

* ``remove_molecules``: Remove selected molecules from the crystal.
* ``remove_atoms``: Remove atoms from a molecule in a crystal.

* ``move_atom_to``: Move an atom in a molecule to a new position.
* ``change_element``: Change the element of an atom in a molecule.
* ``change_hybridisation``: Change the hybridisation of an atom in a molecule.
* ``change_charges``: Change the charge of an atom in a molecule.

* ``add_ethyls``: Add ethyl groups to a molecule.
* ``add_methyls``: Add methyl groups to a molecule.
* ``add_hydrogens``: Add hydrogens to a molecule.

The following describe the settings for each instruction action:

#### Action: ``remove_edges``

This action will remove edges from a molecule from the crystal. This is required if the original crystal structure contains incorrect bonds in a molecule. The parameters for this action are:

* `molecule` (``int``) [*Required*]: This is the molecule you want to add edges to in the crystal. The names of the molecules are given by the ``SUMELF get_molecules`` program. 
* ``edges`` (``list`` of tuples) [*Required*]: This is the list of edges you want to remove from the molecule of interest. 

```python title="Example of the remove_edges action"
repair_crystals_instructions['CAMKEK'] = [{'action': 'remove_edges', 'molecule': 1, 'edges': [(26, 27)]}]
```

#### Action: ``add_edges``

This action will add edges to a molecule from the crystal. This is required if the original crystal structure did not indicate there was a bond between atoms in the molecule. The parameters for this action are:

* `molecule` (``int``) [*Required*]: This is the molecule you want to add edges to in the crystal. The names of the molecules are given by the ``SUMELF get_molecules`` program. 
* ``edges`` (``list`` of tuples) [*Required*]: This is the list of edges to add to the molecule of interest. This is given as a tuple containing the two indices of the atoms you want to connnect, along with the bond information (``bond_info``). If the bond information is not given, this will not be supplied to the edge. This may cause issues by not entering the ``bond_info``, so it is recommended to do so. 

```python title="Example of the add_edges action"
bond_info = {'bond_type': 'Single', 'involved_in_no_of_rings': 0, 'is_conjugated': False, 'is_cyclic': False, 'bond_type_from_sybyl_type': 1}
repair_crystals_instructions['CAMKEK'] = [{'action': 'add_edges', 'molecule': 1, 'edges': [(26, 27, bond_info)]}]
```

#### Action: ``update_edges``

This action will update the bond information (``bond_info``) of the edges of interest in the molecule of interest. 

!!! note

	The edges much exist in the molecule prior to updating them. If these are new edges, use the ``add_edges`` action. 

The parameters for this action are:

* `molecule` (``int``) [*Required*]: This is the molecule you want to update the edges to in the crystal. The names of the molecules are given by the ``SUMELF get_molecules`` program. 
* ``edges`` (``list`` of tuples) [*Required*]: This is the list of edges you want to update. This is given as a tuple containing the two indices of the atoms you want to connnect, along with the bond information (``bond_info``). If the bond information is not given, this will not be supplied to the edge. This may cause issues by not entering the ``bond_info``, so it is recommended to do so. 

```python title="Example of the add_edges action"
bond_info = {'bond_type': 'Single', 'involved_in_no_of_rings': 0, 'is_conjugated': False, 'is_cyclic': False, 'bond_type_from_sybyl_type': 1}
repair_crystals_instructions['CAMKEK'] = [{'action': 'update_edges', 'molecule': 1, 'edges': [(26, 27, bond_info)]}]
```

#### Action: ``remove_molecules``

This action will remove molecules from the crystal. The parameters for this action are:

* `molecules` (int or list) [Required]: These are the names of the molecule you want to remove from the crystal. The names of the molecules are given by the ``SUMELF get_molecules`` program. 

```python title="Example of the remove_molecules action"
repair_crystals_instructions['AFUZIN'] = [{'action': 'remove_molecules', 'molecules': 3}]
```

#### Action: ``remove_atoms``

This action will remove atoms in a molecule from the crystal. The parameters for this action are:

* `molecule` (``int``) [*Required*]: This is the molecule you want to remove atoms from in the crystal. The names of the molecules are given by the ``SUMELF get_molecules`` program. 
* ``atoms`` (``int`` or ``list``) [*Required*]: This is the list of atom indices you want to remove from the molecule of interest. This can be given as an ``int`` or a ``list`` of indices.
* ``remove_attached_hydrogens`` (``bool.``) [*Optional*]: If this is set to ``True``, any hydrogens that are attached to atoms you want to remove will also be removed. If ``False``, attached hydrogen will not be removed automatically. Default: ``True``.
* ``create_new_molecules`` (``bool.``) [*Optional*]: This indicates if you are happy if two molecules are created when you split a molecule into two or more pieces by removing atoms from the molecule. 

```python title="Example of the remove_atoms action"
repair_crystals_instructions['ARUJOP'] = [{'action': 'remove_atoms', 'molecule': 1, 'atoms': [98, 82, 85, 76, 77, 88, 89, 101, 95, 87, 90, 86, 81, 99]}]
```

#### Action: ``move_atom_to``

This action will move atoms in a molecule. The parameters for this action are:

* `molecule` (``int``) [*Required*]: This is the molecule you want to move atoms within. The names of the molecules are given by the ``SUMELF get_molecules`` program. 
* ``atoms`` (``dict.``) [*Required*]: This dictionary contains the atom indices you want to move, along with the positions you want to move the atoms to. 

```python title="Example of the move_atom_to action"
repair_crystals_instructions['ANCTNB'] = [{'action': 'move_atom_to', 'molecule': 2, 'atoms': {12: (-3.7497, 0.0377, 0.5917), 4:  (-0.7413, 0.0377, 4.2583)}}]
```

#### Action: ``change_element``

This action will change the elements of the atoms in a molecule. The parameters for this action are:

* ``atoms`` (``int``, ``list``, or ``dict.``) [*Required*]: This is the list of atom indices you want to change the element of in the molecule of interest. This can be given as an ``int`` or a ``list`` of indices. If given as a ``dict``, the key is the atom index you want to change, and the value is the symbol of the element you want to change the atoms to.
* ``updated_elements`` (``str.``, or ``list`` of ``str.``) [*Optional*]: These are the elements you want to change the atoms in the ``atoms`` variable to. Only give this if your ``atoms`` variable was an ``int`` or ``list``. If only one element is given here, all the atoms in the ``atoms`` variable will be changed to this element.

```python title="Example of the change_element action. All these are valid."
repair_crystals_instructions['CAMKEK'] = [{'action': 'change_element', 'molecule': 1, 'atoms': [25, 26], 'updated_elements': 'C'}]
repair_crystals_instructions['CAMKEK'] = [{'action': 'change_element', 'molecule': 1, 'atoms': [18, 25, 26], 'updated_elements': ['N', 'C', 'C']}]
repair_crystals_instructions['UNIHOP'] = [{'action': 'change_element', 'molecule': 1, 'atoms': {48: 'C'}}]
```

#### Action: ``change_hybridisation``

This action will change the hybridisations of the atoms in a molecule. The parameters for this action are:

* ``atoms`` (``int``, ``list``, or ``dict.``) [*Required*]: This is the list of atom indices you want to change the hybridisation of in the molecule of interest. This can be given as an ``int`` or a ``list`` of indices. If given as a ``dict``, the key is the atom index you want to change, and the value is the hybridisation of the atom you want to change the atoms to.
* ``updated_hybridisations`` (``str.``, or ``list`` of ``str.``) [*Optional*]: These are the hybridisations you want to change the atoms in the ``atoms`` variable to. Only give this if your ``atoms`` variable was an ``int`` or ``list``. If only one element is given here, all the atoms in the ``atoms`` variable will be changed to this element.

```python title="Example of the change_hybridisation action. All these are valid."
repair_crystals_instructions['JITLII'] = [{'action': 'change_hybridisation', 'molecule': 1, 'atoms': [2,4,6,11,12,13,15,16,17,72,71,70,68,67,66,61,59,57], 'updated_hybridisations': 'sp2'}]
repair_crystals_instructions['EBOZEE'] = [{'action': 'change_hybridisation', 'molecule': 2, 'atoms': [98,30], 'updated_hybridisations': ['sp2', 'sp2']}]
repair_crystals_instructions['GUXMIW'] = [{'action': 'change_hybridisation', 'molecule': 1, 'atoms': {10: 'sp2',9: 'sp2'}}]
```

#### Action: ``change_charges``

This action will change the charge of the atoms in a molecule. The parameters for this action are:

* ``atoms`` (``int``, ``list``, or ``dict.``) [*Required*]: This is the list of atom indices you want to change the charge of in the molecule of interest. This can be given as an ``int`` or a ``list`` of indices. If given as a ``dict``, the key is the atom index you want to change, and the value is the charge of the atom you want to change the atoms to.
* ``updated_charges`` (``int.``, or ``list`` of ``int.``) [*Optional*]: These are the charges you want to change the atoms in the ``atoms`` variable to. Only give this if your ``atoms`` variable was an ``int`` or ``list``. If only one element is given here, all the atoms in the ``atoms`` variable will be changed to this element.

```python title="Example of the change_charges action. All these are valid."
repair_crystals_instructions['EGOFEN'] = [{'action': 'change_charges', 'molecule': 1, 'atoms': [36,12], 'updated_charges': 0}]
repair_crystals_instructions['EGOFEN'] = [{'action': 'change_charges', 'molecule': 1, 'atoms': [36,12], 'updated_charges': [0, 0]}]
repair_crystals_instructions['EGOFEN'] = [{'action': 'change_charges', 'molecule': 1, 'atoms': {36: 0, 12: 0}}]
```

#### Action: ``add_ethyls``

This action will attach ethyl groups to atoms in a molecule. The parameters for this action are:

* ``atoms`` (``int``, ``list``, or ``dict.``) [*Required*]: This is the list of atom indices you want to add ethyl groups to in the molecule of interest. This can be given as an ``int`` or a ``list`` of indices. If given as a ``dict``, the key is the atom index you want to change, and the value is the charge of the atom you want to change the atoms to.
* ``number_of_ethyls_to_add`` (``int.``, or ``list`` of ``int.``) [*Optional*]: These are the number of ethyl groups you want to attached the atoms in the ``atoms`` variable to. Only give this if your ``atoms`` variable was an ``int`` or ``list``. If only one element is given here, all the atoms in the ``atoms`` variable will be changed to this element.

```python title="Example of the add_ethyls action. All these are valid."
repair_crystals_instructions['SAZQIX'] = []
repair_crystals_instructions['SAZQIX'].append({'action': 'add_ethyls',    'molecule': 1, 'atoms': [69, 70], 'number_of_ethyls_to_add': 1})
#repair_crystals_instructions['SAZQIX'].append({'action': 'add_ethyls',    'molecule': 1, 'atoms': [69, 70], 'number_of_ethyls_to_add': [1, 1]}) # Another way to write the above
repair_crystals_instructions['SAZQIX'].append({'action': 'add_hydrogens', 'molecule': 1, 'atoms': {71:3,68:3}})
repair_crystals_instructions['SAZQIX'].append({'action': 'add_ethyls',    'molecule': 2, 'atoms': {69:1,68:1}})
repair_crystals_instructions['SAZQIX'].append({'action': 'add_hydrogens', 'molecule': 2, 'atoms': {50:3,70:3}})
```

#### Action: ``add_methyls``

This action will attach methyl groups to atoms in a molecule. This method works in the same way as the ``add_ethyls`` action. The parameters for this action are:

* ``atoms`` (``int``, ``list``, or ``dict.``) [*Required*]: This is the list of atom indices you want to add methyl groups to in the molecule of interest. This can be given as an ``int`` or a ``list`` of indices. If given as a ``dict``, the key is the atom index you want to change, and the value is the charge of the atom you want to change the atoms to.
* ``number_of_methyls_to_add`` (``int.``, or ``list`` of ``int.``) [*Optional*]: These are the number of methyl groups you want to attached the atoms in the ``atoms`` variable to. Only give this if your ``atoms`` variable was an ``int`` or ``list``. If only one element is given here, all the atoms in the ``atoms`` variable will be changed to this element.

```python title="Example of the add_methyls action. All these are valid."
repair_crystals_instructions['SAZQOD'] = []
repair_crystals_instructions['SAZQOD'].append({'action': 'add_methyls', 'molecule': 1, 'atoms': {4:1, 70:1}})
```

#### Action: ``add_hydrogens``

This action will attach hydrogens to atoms in a molecule. The parameters for this action are:

* ``atoms`` (``int``, ``list``, or ``dict.``) [*Required*]: This is the list of atom indices you want to add hydrogens to in the molecule of interest. This can be given as an ``int`` or a ``list`` of indices. If given as a ``dict``, the key is the atom index you want to change, and the value is the charge of the atom you want to change the atoms to.
* ``number_of_methyls_to_add`` (``int.``, or ``list`` of ``int.``) [*Optional*]: These are the number of hydrogens you want to attached the atoms in the ``atoms`` variable to. Only give this if your ``atoms`` variable was an ``int`` or ``list``. If only one element is given here, all the atoms in the ``atoms`` variable will be changed to this element.

```python title="Example of the add_hydrogens action. All these are valid."
repair_crystals_instructions['CUMRUA'] = []

repair_crystals_instructions['CUMRUA'].append({'action': 'remove_atoms',  'molecule': 1, 'atoms': [131, 125, 119, 143, 129] + [135, 133, 137, 79] + [123, 127]})
repair_crystals_instructions['CUMRUA'].append({'action': 'remove_atoms',  'molecule': 2, 'atoms': [138, 118, 116, 109, 126, 146] + [150, 134, 98, 123, 142] + [119, 114, 100, 112, 136, 129, 125], 'remove_attached_hydrogens': True})
repair_crystals_instructions['CUMRUA'].append({'action': 'remove_atoms',  'molecule': 3, 'atoms': [119, 125, 98, 130, 113, 156, 152]+[85]+[143, 147, 140, 146, 150, 151, 159]+[132, 141, 136, 128], 'remove_attached_hydrogens': True})
repair_crystals_instructions['CUMRUA'].append({'action': 'remove_atoms',  'molecule': 4, 'atoms': [132,121,127,130,157,154,160,150]+[81]+[112,102,105,93,79,100,118,136]+[163,124,119,116,145,144,146]+[140,107,82,70,92,64,80,95], 'remove_attached_hydrogens': True})

repair_crystals_instructions['CUMRUA'].append({'action': 'add_hydrogens', 'molecule': 1, 'atoms': [130, 124, 118, 142, 128], 'number_of_hydrogens_to_add': [2, 2, 2, 2, 3]})
repair_crystals_instructions['CUMRUA'].append({'action': 'add_hydrogens', 'molecule': 1, 'atoms': [134, 132, 136, 78], 'number_of_hydrogens_to_add': 2})
repair_crystals_instructions['CUMRUA'].append({'action': 'add_hydrogens', 'molecule': 1, 'atoms': [122, 126], 'number_of_hydrogens_to_add': 2})
repair_crystals_instructions['CUMRUA'].append({'action': 'add_hydrogens', 'molecule': 2, 'atoms': [90, 92]+[93], 'number_of_hydrogens_to_add': [2, 3]+[3]})
repair_crystals_instructions['CUMRUA'].append({'action': 'add_hydrogens', 'molecule': 3, 'atoms': {93: 3, 84: 2, 138: 2, 92: 2}})
repair_crystals_instructions['CUMRUA'].append({'action': 'add_hydrogens', 'molecule': 4, 'atoms': [111]+[75]+[91]+[45], 'number_of_hydrogens_to_add': [3]+[2]+[3]+[3]})
```


## Output from the ReCrystals Program

The ReCrystals program will create a folder called ``repaired_crystal_database`` and save the xyz files of the repaired crystals given in your ``repair_crystals.py`` script, based on the instructions you gave in this ``repair_crystals.py``. 

* Another folder called ``repaired_crystal_database_molecules`` will also be created. This will contain the ``xyz`` files of the individual molecules from your crystal files. This folder is purely created to allow you to check the repair molecules that make up your crystal, and make it easier to double-check that you have repaired the crystal as you desired. 

As well as the  ``repaired_crystal_database`` and ``repaired_crystal_database_molecules`` folders, the ReCrystals program will also create a file called ``ReCrystals_logfile.log`` that will record any warning messages produced while the ReCrystals program. 


## Example Output Files from the ReCrystals Program

[Click here](https://github.com/geoffreyweal/ReCrystals/tree/main/Examples) to find examples of crystals from the CCDC that have been repaired with the instructions from a ``repair_crystals.py`` file. 

