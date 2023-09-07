import sys

# Get the command-line arguments (excluding the script name)
argv = sys.argv[1:]

# Calculate the number of arguments
num_arguments = len(argv)

# Print the number of arguments
if num_arguments == 1:
    print("1 argument:", end="")
else:
    print(f"{num_arguments} arguments:", end="")

# Print a colon (or dot) followed by a new line
if num_arguments > 0:
    print(":")

# Print the list of arguments and their positions
for i, arg in enumerate(argv, start=1):
    print(f"{i}: {arg}")

# Print a new line if no arguments were passed
if num_arguments == 0:
    print(".")
else:
    print()
