#!/bin/bash
# remember to change the tilt axis and basis
input_ST_file="sigma_theta_list"

# Check if the file exists
if [[ ! -f "$input_ST_file" ]]; then
    echo "Error: File '$input_ST_file' not found!"
    exit 1
fi

while read -r line; do
    sigma=$(echo "$line" | awk '{print $2}')
    if [[ "$line" == Sigma:* ]]; then
	echo $sigma
	pwd
	cd Sigma_$sigma
        python csl_generator.py  0 0 1 fcc $sigma
	cd ..
    fi
done < "$input_ST_file"
