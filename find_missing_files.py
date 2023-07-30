import os

def find_missing_files(directory_path, prefix, suffix):
    # List all files in the directory
    files = os.listdir(directory_path)

    # Extract the sequential numbers from the file names
    numbers = []
    for file_name in files:
        if file_name.startswith(prefix) and file_name.endswith(suffix):
            # Extract the number from the file name
            number_str = file_name[len(prefix): -len(suffix)]
            try:
                number = int(number_str)
                numbers.append(number)
            except ValueError:
                # Ignore the file if the number can't be converted to an integer
                continue

    # Sort the numbers to find the maximum in the sequence
    numbers.sort()

    # Find and print the missing numbers
    if numbers:
        for i in range(1, numbers[-1]):
            if i not in numbers:
                print(f"Missing file: {prefix}{i}{suffix}")

# Example usage
directory_path = 'C:\\path\\to\\your\\directory' # Change to your directory path
prefix = 'file' # Change to your common prefix
suffix = '.txt' # Change to your common suffix
find_missing_files(directory_path, prefix, suffix)
