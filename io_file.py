import os
import re
"""
Goal is to automatically change the grain plane of symmetry tilt grain boundary in io_file
after command csl_generator.py 1 1 1 diamond 13 thanks to https://github.com/oekosheri/GB_code
get the grain plane vector from CSL_planes* file, and write into io_file
*** keep in mind:
gb1_plane = symmetric_tilt_rows[0] the number 0 here is related to symmetry property of structure!

author by XFShii and chatgpt
"""
# Define the base directory where the Sigma folders are located
base_dir = os.getcwd()  # Current working directory, or specify the path

# Define the name of the io_file to be updated in each folder
io_file_name = "io_file"

# Iterate through each folder in the base directory
for folder in os.listdir(base_dir):
    # Look for directories starting with "Sigma_"
    if folder.startswith("Sigma_") and os.path.isdir(folder):
        sigma_folder = os.path.join(base_dir, folder)
        csl_file_name = f"CSL_planes_sigma{folder.split('_')[-1]}.txt"  # Construct the CSL file name
        csl_file_path = os.path.join(sigma_folder, csl_file_name)

        # Check if the CSL file exists
        if os.path.isfile(csl_file_path):
            print(f"Processing {csl_file_path}...")
            
            # Read the CSL file and extract Symmetric Tilt rows
            with open(csl_file_path, "r") as csl_file:
                lines = csl_file.readlines()

            symmetric_tilt_rows = []
            for line in lines:
                # Match rows where Type = Symmetric Tilt
                if "Symmetric Tilt" in line:
                    # Extract the GB1 plane (first 3 numbers inside square brackets)
                    match = re.search(r"\[([^\]]+)\]", line)  # Regex to find content inside square brackets
                    if match:
                        gb1 = match.group(1).strip()  # Extract GB1 plane as a string
                        symmetric_tilt_rows.append(gb1)

            # Check if Symmetric Tilt rows were found
            if symmetric_tilt_rows:
                print(symmetric_tilt_rows)
                # Get the first Symmetric Tilt GB1 plane (or customize for more rows)
                gb1_plane = symmetric_tilt_rows[0]  # Use the first Symmetric Tilt plane
                gb1_numbers = [int(x) for x in gb1_plane.split()]  # Convert GB1 to a list of integers
                
                print(f"Found Symmetric Tilt GB1: {gb1_numbers} in {folder}")

                # Update the io_file in the current Sigma folder
                io_file_path = os.path.join(sigma_folder, io_file_name)
                if os.path.isfile(io_file_path):
                    # Read the io_file
                    with open(io_file_path, "r") as io_file:
                        io_file_lines = io_file.readlines()
                    io_file_path_w = os.path.join(sigma_folder, io_file_name+f"{int(gb1_numbers[0])}{int(gb1_numbers[1])}{int(gb1_numbers[2])}")
                    # Rewrite the io_file with the updated GB_plane
                    with open(io_file_path_w, "w") as io_file:
                        for line in io_file_lines:
                            if line.strip().startswith("GB_plane:"):
                                # Replace the GB_plane line with the new GB1 plane
                                io_file.write(f"GB_plane: [{', '.join(map(str, gb1_numbers))}]\n")
                            else:
                                # Keep all other lines unchanged
                                io_file.write(line)

                    print(f"Updated {io_file_name} with GB_plane: [{', '.join(map(str, gb1_numbers))}]")
                else:
                    print(f"Warning: io_file not found in {folder}")
            else:
                print(f"No Symmetric Tilt found in {csl_file_name}")
        else:
            print(f"Warning: {csl_file_name} not found in {folder}")
