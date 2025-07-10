#!/bin/bash
# build folder for different sigma
input_file="sigma_theta_list"

# Check if the file exists
if [[ ! -f "$input_file" ]]; then
    echo "Error: File '$input_file' not found!"
    exit 1
fi

while read -r line; do
    sigma=$(echo "$line" | awk '{print $2}')
    if [[ "$line" == Sigma:* ]]; then
        mkdir "Sigma_$sigma"
    fi
done < "$input_ST_file"
