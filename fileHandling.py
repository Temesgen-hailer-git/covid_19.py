def read_and_modify_file(input_filename, output_filename):
    try:
        with open(input_filename, 'r') as file:
            content = file.read()
        
        # Example modification: Convert content to uppercase
        modified_content = content.upper()
        
        with open(output_filename, 'w') as file:
            file.write(modified_content)
        
        print(f"Modified content has been written to '{output_filename}'.")
    
    except FileNotFoundError:
        print(f"Error: The file '{input_filename}' does not exist.")
    except IOError:
        print(f"Error: Cannot read the file '{input_filename}'.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

def main():
    input_filename = input("Enter the filename to read: ").strip()
    output_filename = input("Enter the filename to write the modified content: ").strip()
    
    read_and_modify_file(input_filename, output_filename)

if __name__ == "__main__":
    main()
