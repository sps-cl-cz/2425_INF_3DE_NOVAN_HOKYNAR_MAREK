import sys

def main():
    args = parse_args()
    if args.command is None:
        print_help()
        sys.exit(0)

def parse_args():
    class Args:
        command = None
    return Args()


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