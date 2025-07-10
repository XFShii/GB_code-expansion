# GB_code-expansion
The code set establishes a workflow to systematically calculate grain boundary energies across a range of sigma values, based on https://github.com/oekosheri/GB_code, by constructing periodic grain boundary structures.


1. Select the target tilt axis for the symmetric grain boundary (e.g., [0 0 1]).
2. Refine the output of GB_code: Use the output io_file and rename it as io_file33-1, where 33-1 denotes the grain boundary plane normal vector.
3. Run GB_code to generate CSLs: Execute python CSLgenerator.py u v w [limit] to generate the list of possible Sigma values and corresponding rotation angles. Save this output as sigma_theta_list.
4. Run sigma_folder.bash: Use this script to create folders for each Sigma value.
5. Run io_file_generator.bash: Generate the io_file for each Sigma using this script.
6. Refine the supercell periodicity: Use python refine_period.py to optimize the periodic numbers for each supercell.

