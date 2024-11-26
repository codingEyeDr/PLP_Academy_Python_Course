# TASK 1

# Function to read a file, modify its content, and write to a new file
def modify_file(input_file, output_file):
    try:
        # Open the input file in read mode
        with open(input_file, 'r') as infile:
            # Read the content of the file
            content = infile.read()

        # Modify the content (for example, convert it to uppercase)
        modified_content = content.upper()

        # Open the output file in write mode
        with open(output_file, 'w') as outfile:
            # Write the modified content to the new file
            outfile.write(modified_content)

        print(f"Modified content has been written to '{output_file}' successfully.")

    except FileNotFoundError:
        print(f"Error: The file '{input_file}' was not found.")
    except Exception as e:
        print(f"An error occurred: {e}")

# Specify the input and output file paths
input_file = 'input.txt'  # Replace with your input file name
output_file = 'output.txt'  # Replace with your desired output file name

# Call the function to modify the file
modify_file(input_file, output_file)


# TASK 2

def read_file():
    try:
        # Prompt the user to enter a filename
        filename = input("Enter the filename: ")
        
        # Attempt to open and read the file
        with open(filename, 'r') as file:
            content = file.read()
            print("\nFile content:")
            print(content)

    except FileNotFoundError:
        print(f"Error: The file '{filename}' does not exist.")
    except PermissionError:
        print(f"Error: You do not have permission to read the file '{filename}'.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

# Call the function
read_file()
