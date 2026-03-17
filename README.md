# Python Environment Setup (Mac)

## Python • Anaconda • VS Code • Conda Environments

This guide explains how to set up a clean Python development environment on macOS using:
- Python
- Anaconda
- VS Code
- Conda environments
- Jupyter kernel support

It also contains a terminal command cheat sheet and workflow notes that beginners can follow when starting Python projects.

## Why Python?
Python is one of the most widely used programming languages in the world. It is used for:
- Data science
- Machine learning
- Web development
- Automation
- Cybersecurity
- Backend systems
- AI applications

## Python is beginner-friendly because it has:
- simple syntax
- a massive ecosystem of libraries
- strong community support
- cross-platform compatibility

## Why Environment Setup Matters
A proper Python setup prevents many common problems such as:
- package conflicts
- incorrect Python interpreter usage
- broken environments
- dependency issues between projects

Using Conda environments allows each project to run with its own isolated Python environment.
This means:
- one project can use Python 3.10
- another can use Python 3.11
- packages won't conflict with each other

## Mac Terminal Basics
These commands are frequently used when working with Python environments.
- Home directory
~
- Represents the home directory.

- Switch to home directory
cd ~
- Moves the terminal to the home folder.

- Print current directory
pwd
- Displays the full path of the current working directory.

- Check if Anaconda exists
ls -ld /opt/anaconda*
- Shows whether an Anaconda installation exists in the system.

- Show hidden files in Finder
Press:
COMMAND + SHIFT + .

Hidden files such as .zshrc can affect Python paths and environment variables.
Removing / Cleaning Anaconda
Sometimes an existing Anaconda installation can cause environment conflicts or path issues. Cleaning it ensures a fresh setup.
- Delete Anaconda installation
sudo rm -rf /opt/anaconda3
- Removes the Anaconda directory.

- Remove shell configuration
rm ~/.zshrc
- Removes shell configuration that may contain old environment paths.

- Edit shell configuration manually
nano ~/.zshrc
- Opens the configuration file in the terminal editor.

- Check Conda installation
conda --version
- Verifies that Conda is installed and accessible.

# VS Code Essentials
VS Code is a lightweight and powerful editor widely used for Python development.
- Open VS Code in the current directory
code .
- This launches VS Code with the current folder as the workspace.

- Open integrated terminal
Control + `
- Opens the built-in terminal inside VS Code.

- Install code command in PATH
Open the command palette:
Cmd + Shift + P
- Then run:
Shell Command: Install code command in PATH
- This allows launching VS Code directly from the terminal.


## Example Workflow
- Typical workflow when starting a project:
cd ~/Desktop/data\ science
code .
- This moves to the working directory and opens it in VS Code.
- VS Code Clean Uninstall
If VS Code needs to be removed completely:
rm -rf ~/Library/Application\ Support/Code
rm -rf ~/.vscode
rm -rf ~/Library/Caches/com.microsoft.VSCode
rm -rf ~/Library/Preferences/com.microsoft.VSCode.plist
rm -rf ~/Library/Saved\ Application\ State/com.microsoft.VSCode.savedState
rm -rf ~/Library/Application\ Support/com.microsoft.VSCode.ShipIt
sudo rm -f /usr/local/bin/code

- Checking the Python Interpreter
- To confirm which Python interpreter is currently active:
which python
- This command returns the path to the Python executable currently being used.
- This is useful to verify that the correct environment is active.

## Conda Environments
Conda environments allow you to isolate Python installations and dependencies for each project.
- Creating Conda Environments
Path-based environment
conda create -p ./venv python=3.10

 or

conda create -p venv python=3.10
- Creates an environment inside the current project folder.

- Name-based environment
conda create -n myenv python=3.10
- Creates a globally accessible named environment.

- Activating Environments
- Activate using path
conda activate "/Users/vivekaggarwal/Desktop/data science/python/myenv"

- Activate using name
conda activate myenv

- Deactivate Environment
conda deactivate
- Returns to the base environment.

- Installing Jupyter Kernel Support
pip install ipykernel
- This allows the environment to appear as a selectable kernel in Jupyter notebooks.

- Listing Conda Environments
conda env list

or

conda info --envs
- Shows all available environments.

- Removing Environments
- Path-based environment
conda remove -p ./venv --all

- Named environment
conda remove -n myenv --all

- Manual removal
rm -rf venv

- Handling Paths with Spaces
If a folder path contains spaces, wrap it in quotes.
Example:
conda remove -p "/Users/vivekaggarwal/Desktop/data science/python/venv" --all

- Typical Python Project Workflow
cd ~/Desktop/data\ science
code .

conda create -p ./venv python=3.10
conda activate ./venv

pip install ipykernel

which python

conda deactivate
Important Notes
• Always activate the environment before installing packages.
• ipykernel is required for Jupyter to detect environments.
• Renaming project folders can break kernel paths.
• code . quickly opens VS Code in the current directory.
• Hidden files such as .zshrc can affect PATH configuration.
Who This Guide Is For
This setup guide is useful for:
Python beginners
Data science students
Developers learning Conda environments
Anyone setting up Python on macOS
Users working with VS Code and Jupyter
