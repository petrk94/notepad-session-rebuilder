
## Overview

This repository contains a Python script designed to rebuild the `session.xml` file for Notepad++ from backup files. The script allows sorting the recovered files by date, name, or size, providing flexibility in session restoration. This tool is particularly useful in situations where the original `session.xml` file is lost or corrupted, ensuring that your Notepad++ environment is restored with minimal disruption.

Im using Notepad++ daily and rely on it, the lost of the session.xml for a unknown reason, in the past, I were lost, but with the structure of the session.xml, and the help of ChatGPT, this python script with command line features was possible. I hope it will help anyone who is in need to get the session.xml back.

## Features

- **Automatic Detection of Backup Directory:** The script automatically detects the Notepad++ backup directory based on the current user's environment.
- **Sorting Options:** Users can choose to sort the files in the rebuilt session by the last modification date, file name, or file size.
- **Command Line Interface:** The script is fully operable from the command line, making it easy to integrate into various workflows.

## Prerequisites

- Python 3.x
- Notepad++ with existing backup files

## Usage

To use the script, clone this repository or download the `notepad_plusplus_session_rebuild.py` file. Run the script from your command line interface. The script offers the following command-line arguments:

- `--sort-by-date`: Sorts the files by the last modification date.
- `--sort-by-name`: Sorts the files alphabetically by name.
- `--sort-by-size`: Sorts the files by their size.

Example of running the script:

```bash
python notepad_plusplus_session_rebuild.py --sort-by-name
```
Upon successful execution, the script will output the path of the newly created session.xml file.

## Acknowledgements
This script was developed with the assistance of ChatGPT, an AI language model by OpenAI. It demonstrates the potential of AI-assisted coding and problem-solving.

