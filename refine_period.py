import os
import math
import numpy as np
"""
dimensions: [1, 1, 1] change the periodic number in io_file
The x direction is normal to the grain boundary plane, while y and z are the in-plane directions. 
The total length of the simulation box in each direction can be adjusted by changing these parameters according to the requirements of your task.
author by XFShii and chatgpt 
"""

bg_plane = []

# Get the current directory
current_dir = os.getcwd()
io_file_path = []
# Loop through all items in the current directory
for folder_name in os.listdir(current_dir):
    if folder_name.startswith("io_file"):
        io_file_path.append(os.path.join(current_dir, folder_name))
        # Extract the characters after "io_file" and add to bg_plane
        bg_plane.append(folder_name[len("io_file"):])
print("bg_plane:", bg_plane)

# Find the file that starts with "input_G" + bg_plane[0]
if bg_plane:
    input_file_path = []
    target_prefix = []
    for i in range(len(bg_plane)):
        target_prefix.append("input_G" + bg_plane[i])

    # Loop through all files and directories in the current folder
    for i in range(len(bg_plane)):
        for item in os.listdir(current_dir):
            if item.startswith(target_prefix[i]):
                input_file_path.append(os.path.join(current_dir, item))
                break

    # Output the result
    if input_file_path:
        print(f"Found file: {input_file_path}")
    print(bg_plane, input_file_path, io_file_path)
# Read the first file and extract x, y, z values
for i in range(len(bg_plane)):

    with open(input_file_path[i], "r") as file1:
        lines = file1.readlines()
        x = float(lines[6].split()[1])  # Second float number in line 7 (index 6)
        y = float(lines[7].split()[1])  # Second float number in line 8 (index 7)
        z = float(lines[8].split()[1])  # Second float number in line 9 (index 8)
        print(x,y,z)

    # Calculate periodic_x
    periodic_x = math.ceil(120 / x)

    # Round y and z to nearest integers
    a = round(y)
    b = round(z)
    print(periodic_x, a, b)
    # Find the smallest common multiple of a and b
    # Determine periodic_y and periodic_z based on the condition
    if min(math.ceil(120 / a),math.ceil(120 / b)) > 2:
        periodic_y = int(round(120 / a))
        periodic_z = int(round(120 / b))
    else:
        periodic_y = int(round(240 / a))
        periodic_z = int(round(240 / b))
    print(periodic_x*x,periodic_y*y , periodic_z*z)
    # Read the second file and modify the 27th line
    with open(io_file_path[i], "r") as file2:
        lines = file2.readlines()

    # Update line 27 with the new dimensions
    lines[26] = f"dimensions: [{periodic_x}, {periodic_y}, {periodic_z}]\n"
    print(io_file_path[i], lines[26])
    with open(io_file_path[i], "w") as file2:
        file2.writelines(lines)

