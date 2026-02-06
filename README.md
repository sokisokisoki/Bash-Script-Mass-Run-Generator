# Mass Run Script Generator

This script generates a bash script that runs a single executable across all combinations of specified command-line arguments. It is intended for parameter sweeps, batch execution, and exhaustive testing.

## Requirements

- Python 3
- A compiled executable in the current working directory
- A Unix-like system with bash

## Running the Script

Execute the script with:

python3 massRunScript.py

The script runs interactively and prompts for the following inputs:

- **Executable name**  
  Name of the binary to execute. The generated bash script will invoke it using `./<executable>`.

- **Number of fields**  
  The number of positional command-line arguments required by the executable.

- **Options for each field**  
  For each field, provide a comma-separated list of valid argument values. Whitespace is stripped automatically.

- **Bash script name**  
  Name of the output bash script. If the `.sh` extension is not provided, it will be appended automatically.

## Behavior

The script computes the Cartesian product of all provided argument option lists. Each unique combination of arguments produces one command in the output bash script.

Generated commands follow the format:

./executable arg1 arg2 ... argN

The total number of commands generated is the product of the number of options provided for each field.

## Output

The script writes a bash file containing one command per line and prints the total number of commands generated.

Before running the generated script, make it executable:

chmod +x script_name.sh

Run the script with:

./script_name.sh

All commands are executed sequentially in the invoking shell.
