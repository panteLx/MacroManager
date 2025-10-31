# Python Game Macro

A customizable macro tool designed for automating repetitive actions in games, with a focus on user-friendly interface and configuration.

## Features

- Customizable start/stop keys
- Clean and informative console interface
- Persistent key bindings configuration
- Real-time status display
- Ability to change key bindings on the fly

## Prerequisites

Before running the script, make sure you have the following installed:

- Python 3.11 or higher
- Windows operating system (required for DirectInput functionality)

## Detailed Setup Guide

### 1. System Setup

1. Install Python:

   - Download Python 3.11 or higher from [python.org](https://www.python.org/downloads/)
   - During installation, make sure to check "Add Python to PATH"
   - Verify installation by opening PowerShell and running:
     ```powershell
     python --version
     ```

2. Download the Project:
   - Download this repository as a ZIP file and extract it, or
   - If you have Git installed, clone the repository:
     ```powershell
     git clone https://github.com/panteLx/python-macro.git
     cd python-macro
     ```

### 2. Project Setup

1. Open PowerShell as Administrator:

   - Right-click on PowerShell in the Start menu
   - Select "Run as administrator"
   - Navigate to your project folder:
     ```powershell
     cd path\to\python-macro
     ```

2. Create and Activate Virtual Environment:

   ```powershell
   # Remove existing venv if any
   if (Test-Path .venv) { Remove-Item -Recurse -Force .venv }

   # Create new virtual environment
   python -m venv .venv

   # Activate it
   .\.venv\Scripts\activate

   # Your prompt should now show (.venv)
   ```

3. Install Required Packages:

   ```powershell
   # Upgrade pip first
   python -m pip install --upgrade pip

   # Install requirements
   pip install -r requirements.txt
   ```

## Running and Using the Macro

### 1. First-Time Setup

1. Start the Script:

   ```powershell
   # Make sure you're in the project directory and venv is activated
   python app.py
   ```

2. Initial Configuration:

   - You'll be prompted to set up your key bindings
   - Press the key you want to use to START the macro
   - Press the key you want to use to STOP the macro
   - These settings will be saved in `macro_config.json`

3. Game Window Detection:
   - The script will look for your game window
   - The game must be running and visible
   - The window title will be displayed when found

### 2. Daily Usage

1. Start the Macro:

   ```powershell
   # Navigate to project folder
   cd path\to\python-macro

   # Activate virtual environment
   .\.venv\Scripts\activate

   # Run the script
   python app.py
   ```

2. Using the Macro:

   - Make sure your game window is open and visible
   - **IMPORTANT**: Click on the game window to focus it before starting the macro
   - Use your configured START key to begin the macro
   - Use your configured STOP key to halt the macro
   - Press 'K' to change key bindings (only while macro is stopped)
   - Press Ctrl+C in the console to exit the program

3. Understanding the Interface:
   - The console shows the current status (Idle/Running/Stopped)
   - Your current key bindings are always displayed
   - Warning messages will appear when important actions are needed
   - The game window title is shown to confirm correct detection

## Important Notes

- The game window must be in focus on first start for the macro to work properly
- Make sure to stop the macro before changing key bindings
- Your key bindings are saved in `macro_config.json` and will be loaded automatically on subsequent runs
- The script must be run with sufficient permissions to send input to the game

## Files Description

- `app.py` - Main script containing the macro logic and UI
- `direct_keys.py` - DirectInput key codes and functions for game input
- `macro_config.json` - Stores your key binding preferences

## Troubleshooting

1. If the macro isn't working:

   - Ensure the game window is in focus
   - Check if you're running the script with the correct permissions
   - Verify the game window is detected (title will be displayed)

2. If keys aren't being detected:
   - Try running the script as administrator
   - Ensure no other programs are blocking keyboard input

## License

This project is open source and available under the MIT License.
