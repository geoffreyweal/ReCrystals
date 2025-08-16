"""
repair_crystal.py, Geoffrey Weal, 20/5/2022

This program will repair crystals that you have indicated need repairing, based on how you have indicated your crystal needs to be repaired.
"""
import os, shutil
import numpy as np
from tqdm import tqdm
from ase.io import write
from copy import deepcopy
from SUMELF import read_crystal, obtain_graph, process_crystal, make_crystal, add_graph_to_ASE_Atoms_object

from ReCrystals.ReCrystals.repair_crystals_methods.check_instructions                         import check_instructions
from ReCrystals.ReCrystals.repair_crystals_methods.add_atom_removal_instructions              import add_atom_removal_instructions
from ReCrystals.ReCrystals.repair_crystals_methods.reorder_instructions                       import reorder_instructions
from ReCrystals.ReCrystals.repair_crystals_methods.perform_instruction                        import perform_instruction
from ReCrystals.ReCrystals.repair_crystals_methods.separate_molecules_into_components         import separate_molecules_into_components
from ReCrystals.ReCrystals.repair_crystals_methods.rename_molecules                           import rename_molecules

from SUMELF.SUMELF.add_atoms.add_hydrogens_to_molecules                                       import add_hydrogens_to_molecules
from SUMELF.SUMELF.add_atoms.Utilities.free_rotation_methods.allow_hydrogens_to_freely_rotate import allow_hydrogens_to_freely_rotate

def Repair_Crystals(repair_crystals_instructions):
    """
    This method is designed to repair crystals that you have indicated need repairing, based on how you have indicated your crystal needs to be repaired in the "repair_crystals.py" file.

    Parameters
    ----------
    repair_crystals_instructions : dict.
        This is the instructions given for repairing crystals obtained from the ACSD method. 
    """

    # First, indicate the names of important files and folders
    ACSD_crystal_database_foldername   = 'crystal_database'

    # Second, indicate if you have the files and fodlers necessary for running this program
    if not os.path.exists(ACSD_crystal_database_foldername):
        exit('Error: You need a folder called '+str(path_to_repair_crystals_input_file)+' that contains all the crystal files made by the "ACSD run" command.')

    # Third, create the logfile.
    import logging
    Log_Format = "%(levelname)s %(asctime)s - %(message)s"
    logging.basicConfig(filename="ReCrystals_logfile.log",filemode="w",format=Log_Format,level=logging.NOTSET)
    logger = logging.getLogger()

    # Fourth, create the folder for saving repaired crystals to.
    repaired_crystal_database = 'repaired_crystal_database' 
    if os.path.exists(repaired_crystal_database):
        shutil.rmtree(repaired_crystal_database)
    os.mkdir(repaired_crystal_database)

    # Fifth, create a folder that contains all the molecules files for the crystals in crystal_database_foldername
    repaired_crystal_molecules_foldername = 'repaired_crystal_database_molecules'
    if os.path.exists(repaired_crystal_molecules_foldername):
        shutil.rmtree(repaired_crystal_molecules_foldername)
    os.makedirs(repaired_crystal_molecules_foldername)

    # Sixth, repair each crystal.
    pbar = tqdm(sorted(repair_crystals_instructions.items(),key=lambda x:x[0]), unit='crystal')
    for crystal_name, instructions in pbar:

        # 6.1: Write descriptions to logger and to terminal.
        description = 'Repairing '+str(crystal_name)
        pbar.set_description(description)
        logging.info("==========================================================")
        logging.info(description)
        logging.info("==========================================================")

        # 6.1: Perform checks on the instructions to make sure they can all be executed.
        check_instructions(instructions)

        # - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - 

        # 6.2: Obtain the path to the crystal file.
        filepath = ACSD_crystal_database_foldername+'/'+crystal_name+'.xyz'

        # 6.3: Read the crystal file and the graph.
        crystal = read_crystal(filepath)

        # 6.4: Get the graph of the crystal.
        crystal, crystal_graph = obtain_graph(crystal,name=crystal_name)

        # 6.5: Get the molecules and the graphs associated with each molecule in the crystal.
        molecules, molecule_graphs, SolventsList, symmetry_operations, cell = process_crystal(crystal,crystal_graph=crystal_graph,take_shortest_distance=True,return_list=False,logger=logger,print_progress=False)

        # - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - 

        # 6.6: If any instructions include an atom removal sub-instruction, split the instructions into the remocal instruction and the second. 
        instructions = add_atom_removal_instructions(instructions, molecules, molecule_graphs)

        # 6.7: Move the entries in instructions so they are done in an certain order.
        instructions = reorder_instructions(instructions)
        
        # - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - 

        # 6.8: Initialise a list for recording any added hydrogens that you would like to be allowed to freely rotate about the attached atoms in the molecule
        no_of_hydrogens_to_add_to_atoms_in_molecules = {}

        # - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - 

        # 6.9: Add a temporary array to each of the molecules in the crystal that indicates what the original index of the atom was before performing modifications. 
        for mol_name, molecule in molecules.items():
            molecule.arrays['original_indices'] = np.array((range(len(molecule))))

        # 6.10: Perform each instruction in the instructions list. 
        for instruction in instructions:

            # 6.10.1: Perform the desired instruction.
            hydrogens_to_add_to_atoms_to_molecules = perform_instruction(instruction, molecules, molecule_graphs, SolventsList, symmetry_operations, cell, crystal_name, crystal, crystal_graph)

            # 6.10.2: If hydrogens have been added that you would like to allow free rotation of, record this here
            if hydrogens_to_add_to_atoms_to_molecules is not None:
                add_to_AAAIM_dictionary(no_of_hydrogens_to_add_to_atoms_in_molecules, hydrogens_to_add_to_atoms_to_molecules)

        # - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - 

        # 6.11: Add any hydrogens you want to add after performing all instructions now
        if len(no_of_hydrogens_to_add_to_atoms_in_molecules) > 0:
            
            # 6.11.1: Add the hydrogens to the molecules
            updated_molecules, updated_molecule_graphs, were_hydrogens_added = add_hydrogens_to_molecules(no_of_hydrogens_to_add_to_atoms_in_molecules, molecules, molecule_graphs, crystal, crystal_graph, symmetry_operations, cell, logger=logger, identifier=crystal_name, allow_hydrogen_free_rotation=False)
            #molecules[molecule_name] = allow_hydrogens_to_freely_rotate(molecules[molecule_name], molecule_graphs[molecule_name], added_hydrogen_indices_in_molecule, molecule_name=molecule_name, method_type=None)
            
            # 6.11.2: Update the molecules in the molecules dictionary.
            for molecule_name in molecules.keys():
                molecules[molecule_name]       = updated_molecules[molecule_name].copy()
                molecule_graphs[molecule_name] = deepcopy(updated_molecule_graphs[molecule_name])
                
        # - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - 

        # 6.12: Separate molecules into separate components if they have been split by removing atoms. 
        separate_molecules_into_components(molecules, molecule_graphs)

        # 6.13: Rename the molecules so they are in consecutive order is needed
        molecules, molecule_graphs, SolventsList = rename_molecules(molecules, molecule_graphs, SolventsList)

        # 6.14: Create the updated crystal.
        crystal, crystal_graph = make_crystal(molecules, symmetry_operations, cell, wrap=False, solvent_components=SolventsList, remove_solvent=False, molecule_graphs=molecule_graphs, return_all_molecules=False)

        # 6.15: Add the node and edge information from the molecules graph back to the molecule
        add_graph_to_ASE_Atoms_object(crystal, crystal_graph)

        # 6.16: ave the updated crystal as a xyz file to the repaired_crystal_database folder. 
        write(repaired_crystal_database+'/'+crystal_name+'.xyz', crystal)

        # 6.17: Add the node and edge information from the molecules graph back to the molecule
        for molecule_name in molecules.keys():
            add_graph_to_ASE_Atoms_object(molecules[molecule_name], molecule_graphs[molecule_name])

        # 6.18: Create the folder to store molecule xyz data to.
        os.makedirs(repaired_crystal_molecules_foldername+'/'+crystal_name)

        # 6.19: Save each molecule from the crystal to disk
        for molecule_name, molecule in molecules.items():
            solvent_tag = 'S' if molecule_name in SolventsList else ''
            write(repaired_crystal_molecules_foldername+'/'+crystal_name+'/'+str(molecule_name)+str(solvent_tag)+'.xyz', molecule)

    logging.info("==========================================================")

# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - 

def add_to_AAAIM_dictionary(all_added_atoms_in_molecules, added_atoms_to_molecules):
    """
    This method is designed to add information about the atoms that you would like to allow hydrogens to freely rotation about. 

    Parameters
    ----------
    all_added_atoms_in_molecules : dict.
        This dictionary contains the indices of the atoms that you have added to the molecule. 
    added_atoms_to_molecules : dict. 
        These are the indices of the atoms just added to the molecule by the index. 
    """

    # First, for each molecule in the added_atoms_to_molecules dictionary
    for molecule_name, added_atoms in added_atoms_to_molecules.items():

        # Second, if molecule_name is not already in atoms_to_allow_hydrogens_to_freely_rotate_in_molecules, add it.
        if molecule_name not in all_added_atoms_in_molecules:
            all_added_atoms_in_molecules[molecule_name] = {}

        # Third, for each ....
        for atom_index, added_hydrogen_indices_in_molecule in added_atoms.items():

            if atom_index in all_added_atoms_in_molecules[molecule_name]:
                raise Exception('Error: atom_index already in all_added_atoms_in_molecules[molecule_name]')

            all_added_atoms_in_molecules[molecule_name][atom_index] = added_hydrogen_indices_in_molecule


# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - 

