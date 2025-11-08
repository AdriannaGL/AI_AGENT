
## Introduction

An experimental local agent that analyzes a codebase, plans changes, and proposes patches with safety rails.

## Features

- Scans repositories and identifies bugs or refactors
- Generates diffs/patches instead of blindly editing
- Swappable LLM providers/models via environment variables

## Usage Examples

- uv run main.py "how does the calculator render results to the console?"
- uv run main.py "what files are in the root?" --verbose
- uv run main.py "get the contents of lorem.txt" --verbose
  
## Functionality
It provides tools for 
- listing files,
- reading file contents,
- executing Python scripts
- writing new files.

### Listing Files

The `get_files_info` function allows you to list files and their sizes within a specified directory. If no directory is provided, it defaults to the working directory. This is constrained to the working directory for security.

### Reading Files

The `get_file_content` function enables you to read the contents of a file. You must provide the file path relative to the working directory.

### Executing Python Files

The `run_python_file` function allows you to execute Python scripts. You can also pass command-line arguments to the script using the `args` parameter.

### Writing Files

The `write_file` function lets you write or overwrite files with text content. Provide the desired file path and content.

## Safety Notes
- This is a toy agent. Use in sandboxes and test repos.
- Commit your target repo before running so you can revert.
- All file operations are constrained to the working directory. This is a security measure to prevent the agent from accessing sensitive files outside of its designated workspace.

## Getting Started

## Tech Stack
- Python 3.11+
- Geminai model
- Optional providers: OpenAI, Anthropic, Google
- CLI app with simple planning loop and tool-calls (filesystem, search, run)


## Installation

```bash
git clone https://github.com/<your-username>/<your-repo>.git
cd <your-repo>
python -m venv .venv && source .venv/bin/activate  # Windows: .venv\Scripts\activate
pip install -r requirements.txt



