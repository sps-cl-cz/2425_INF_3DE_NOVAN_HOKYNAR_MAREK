import hashlib
import os
import sys

CHECK_PATH = ".check"  # Path to the file for tracking hashes

def main():
    # Main function for processing command line arguments
    args = parse_args()
    if args.command == "init":
        init()  # Initialize tracking
    elif args.command == "add":
        add(args)  # Add a file to tracking
    elif args.command == "remove":
        remove(args)  # Remove a file from tracking
    elif args.command == "status":
        status()  # Show the status of tracked files
    elif args.command in ("-h", "--help") or args.command is None:
        help()  # Show help
    else:
        print(f"Unknown command: {args.command}")  # Unknown command
        help()

def parse_args():
    # Class to hold command line arguments
    class Args:
        command = None
        path = None

    args = Args()
    argv = sys.argv[1:]  # Arguments without the script name

    if argv:
        args.command = argv[0]  # First argument is the command
        if len(argv) > 1:
            args.path = argv[1]  # Second argument is the file path

    return args

def init():
    # Initialize the tracking file
    if check_if_file_exist():
        if input("File already exists. Recreate? Y/N: ").upper() == "Y":
            create_file()  # Create a new file
    else:
        create_file()  # Create the file if it does not exist

def add(args):
    # Add a file to tracking
    if not args.path:
        print("Error: No path specified.")  # Error if no path is provided
        return

    if os.path.isfile(args.path):
        new_hash = compute_sha1(args.path)  # Compute SHA-1 hash
        if new_hash is None:
            print(f"Error: Unable to compute hash for {args.path}.")  # Error during hash computation
            return
        with open(CHECK_PATH, "a") as f:
            f.write(f"{args.path},{new_hash}\n")  # Save path and hash to the file
        print(f"Added: {args.path} (SHA-1: {new_hash})")  # Confirmation of addition
    else:
        print(f"Error: File not found - {args.path}")  # Error if file does not exist

def remove(args):
    # Remove a file from tracking
    if not args.path:
        print("Error: Path is not specified.")  # Error if no path is provided
        return
    if not check_if_file_exist():
        print("Error: .check file does not exist. Run 'check.py init' first!")  # Error if .check file does not exist
        return

    lines = read_check_file()  # Read lines from the file
    file_found = False

    with open(CHECK_PATH, "w") as file:
        for line in lines:
            file_path, _ = line.strip().split(",")  # Split line into path and hash
            if file_path != args.path:
                file.write(line)  # Write line if path does not match
            else:
                file_found = True  # File was found and marked for removal

    if file_found:
        print(f"Removed: {args.path} from tracking.")  # Confirmation of removal
    else:
        print(f"Error: File not found in tracking: {args.path}")  # Error if file was not found

def status():
    # Show the status of tracked files
    if not os.path.isfile(CHECK_PATH):
        print("Error: .check file does not exist. Run 'check.py init' first!")  # Error if .check file does not exist
        return

    with open(CHECK_PATH, "r") as file:
        lines = file.readlines()  # Read lines from the file

    summary = {"OK": 0, "CHANGE": 0, "ERROR": 0}  # Status summary

    for line in lines:
        line = line.strip()
        if not line:
            continue  # Skip empty lines
        parts = line.split(",")
        if len(parts) != 2:
            print(f"[ERROR] Wrong line format: {line}")  # Error in line format
            summary["ERROR"] += 1
            continue

        file_path, stored_hash = parts
        current_hash = compute_sha1(file_path)  # Compute current hash
        if current_hash is None:
            print(f"[ERROR] File not found: {file_path}")  # Error if file was not found
            summary["ERROR"] += 1
        elif current_hash == stored_hash:
            print(f"[OK] {current_hash} {file_path}")  # Confirmation of hash match
            summary["OK"] += 1
        else:
            print(f"[CHANGE] {file_path}")  # Hash has changed
            print(f"New Hash: {current_hash}")
            summary["CHANGE"] += 1

    print(f"Summary: {summary['OK']} OK, {summary['CHANGE']} CHANGE, {summary['ERROR']} ERROR")  # Display summary

def help():
    # Display help for the user
    bold = "\033[1m"
    reset = "\033[0m"
    green = "\033[32m"
    blue = "\033[34m"
    yellow = "\033[33m"
    cyan = "\033[36m"

    print(f"""
{bold}Monitor files using SHA-1 hashes.{reset}

Usage:
    {green}python check.py [command] [options]{reset}

Commands:
    {blue}init{reset}                Initialize tracking (creates a .check file).
    {blue}add <pathspec>{reset}      Add files for tracking (compute SHA-1 hash).
    {blue}remove <pathspec>{reset}   Remove files from tracking.
    {blue}status{reset}              Show the status of tracked files.

Options:
    {yellow}-h, --help{reset}          Show this help message.

Examples:
    {cyan}python check.py init{reset}
    {cyan}python check.py add "*.txt"{reset}
    {cyan}python check.py status{reset}
""")

def check_if_file_exist():
    # Check if the .check file exists
    return os.path.isfile(CHECK_PATH)

def compute_sha1(file_path):
    # Compute the SHA-1 hash of a file
    sha1 = hashlib.sha1()
    try:
        with open(file_path, "rb") as f:
            while chunk := f.read(8192):
                sha1.update(chunk)  # Update hash in chunks
    except FileNotFoundError:
        return None  # Return None if the file was not found
    return sha1.hexdigest()  # Return the hexadecimal representation of the hash

def create_file():
    # Create the .check file
    with open(CHECK_PATH, "w") as file:
        file.write("")  # Create an empty file
    print("File .check was created!")  # Confirmation of file creation

def read_check_file():
    # Read the contents of the .check file
    with open(CHECK_PATH, "r") as file:
        return file.readlines()  # Return lines from the file

if __name__ == "__main__":
    main()  # Run the main function