import sys
import os
from os.path import isfile


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
    return
def add(args):
    print(f"Adding files for tracking: {args.path}")

def remove(args):
    print(f"Removing files from tracking: {args.path}")

def status():
    print("Showing status of tracked files...")

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

if __name__ == "__main__":
    main()
