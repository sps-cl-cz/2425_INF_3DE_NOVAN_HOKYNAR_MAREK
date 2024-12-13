# File Hash Tracker 🗂️

## Introduction 🌟

Welcome to the File Hash Tracker! This is a simple Python script that helps you monitor files by calculating their SHA-1 hashes. It allows you to add files for tracking, remove them, and check their status. 

## Features ✨

- **Initialize Tracking**: Create a `.check` file to start tracking files. 📂
- **Add Files**: Add files to the tracking list and compute their SHA-1 hashes. ➕
- **Remove Files**: Remove files from the tracking list if you no longer want to monitor them. ❌
- **Check Status**: View the current status of tracked files, including any changes in their hashes. 🔍

## Requirements 📋

To run this script, you need to have Python installed on your machine. This script has been tested with Python 3.13.0 and Python 3.12.x

### Libraries 📚

This script uses the built-in `hashlib`, `os`, and `sys` libraries, so there are no additional libraries to install. Just make sure you have Python installed.

## Installation ⚙️

1. Clone this repository to your local machine:
   ```bash
   git clone https://github.com/sps-cl-cz/2425_INF_3DE_NOVAN_HOKYNAR_MAREK.git
   cd 2425_INF_3DE_NOVAN_HOKYNAR_MAREK
   ```

2. Make sure you have the necessary permissions to run the script.

## Usage 🛠️

1. **Initialize Tracking**:
   To create a new tracking file, run:
   ```bash
   python check.py init
   ```

2. **Add a File**:
   To add a file for tracking, use:
   ```bash
   python check.py add <path_to_your_file>
   ```
   Replace `<path_to_your_file>` with the actual path of the file you want to track.

3. **Remove a File**:
   To remove a file from tracking, run:
   ```bash
   python check.py remove <path_to_your_file>
   ```

4. **Check Status**:
   To see the status of all tracked files, simply run:
   ```bash
   python check.py status
   ```

5. **Help**:
   If you need help with the commands, you can always run:
   ```bash
   python check.py --help
   ```

## Example 📖

Here’s a quick example of how to use the script:
```bash
# Initialize tracking
python check.py init

# Add a file
python check.py add myfile.txt

# Check status
python check.py status

# Remove a file
python check.py remove myfile.txt
```
## Tests and limitations of the program ⚠️

Runned tests and possible/known limitations that this program has are listed in [TESTS](TESTS.md).

## Conclusion 🎉

This File Hash Tracker is a great way to keep an eye on your important files and ensure they haven't been altered. If you have any questions or suggestions, feel free to reach out.

## License 📜

This project is licensed under the GNU License - see the [LICENSE](LICENSE) file for details.
