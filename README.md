# GB_code-expansion
The code set establishes a workflow to systematically calculate grain boundary energies across a range of sigma values, based on https://github.com/oekosheri/GB_code, by constructing periodic grain boundary structures.

1. Select the target tilt axis for the symmetric grain boundary (e.g., [0 0 1]).
2. Run GB_code (https://github.com/oekosheri/GB_code) to generate CSLs: Execute python CSLgenerator.py u v w [limit] to generate the list of possible Sigma values and corresponding rotation angles. Save this output as sigma_theta_list.
3. Run sigma_folder.bash: Use this script to create folder for each Sigma value.
4. Run io_file_generator.bash, using the refined GB_code (https://github.com/oekosheri/GB_code). The output io_file is renamed as io_file33-1, where 33-1 is the grain boundary plane normal vector.
5. Refine the supercell periodicity: Use python refine_period.py to optimize the periodic numbers for each supercell.

