import os
import sys

path = ".check"

def main():
    args = parse_args()

    if args.command == "init":
        init()
    elif args.command == "add":
        add(args)
    elif args.command == "remove":
        remove(args)
    elif args.command == "status":
        status()
    elif args.command in ("-h", "--help") or args.command is None:
        print_help()
    else:
        print(f"Unknown command: {args.command}")
        print_help()
        sys.exit(1)

def parse_args():
    class Args:
        command = None
        path = None 

    args = Args()

    argv = sys.argv[1:] #odebere z argumentu název souboru a do pole hodí pouze command a cestu pokud existují
    if len(argv) > 0:
        args.command = argv[0]
        if len(argv) > 1:
            args.path = argv[1]

    return args

def init():
    if check_if_file_exist() is True:
        print("File already exist in this directory. \n Do you want to recreate a new file? Y/N")
        if input().upper() == "Y":
            create_file()
        else:
            return
    else:
        create_file()

def add(args):
    if not args.path:
        print("Error: No path specified.")
        return

    with open(".check", "a") as f:
        if os.path.isfile(args.path):
            hash = compute_sha1(args.path)
            f.write(f"{args.path} {hash}\n")
            print(f"Added: {args.path} (SHA-1: {hash})")
        else:
            print(f"Error: File not found - {args.path}")

def remove(args):
    print(f"Removing files from tracking: {args.path}")

def status():
    if check_if_file_exist() is False:
        print("File .check doesnt exist. Run 'check.py init' first!")
        return
    else:
        with open(".check", "r") as file:
            lines = file.readlines()

        ok, change, error = 0, 0, 0
        for line in lines:
            file_path, _, saved_hash = line.strip().split(",")
            if not os.path.exists(file_path):
                print(f"[ERROR] Soubor nebyl nalezen: {file_path}")
                error += 1
            else:
                current_hash = "FUNKCE PRO HASH"
                if current_hash == saved_hash:
                    print(f"[OK] {saved_hash} {file_path}")
                    ok += 1
                else:
                    print(f"[CHANGE] {saved_hash} {file_path}")
                    print(f"NEW HASH: {current_hash}")
                    change += 1

        print(f"\nSummary: {ok} OK, {change} CHANGE, {error} ERROR")


def print_help():
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
    if os.path.isfile(path) is True:
        return True
    else:
        return False

def create_file():
    with open(".check", "w") as file:
        file.write("")
    print("File .check was created!")

def compute_sha1():
    return


