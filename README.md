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

## Setup Instructions

1. Clone or download this repository to your local machine

2. Create a virtual environment (recommended):

   ```powershell
   python -m venv .venv
   .\.venv\Scripts\activate
   ```

3. Install the required packages:
   ```powershell
   pip install keyboard win32gui
   ```

## Running the Macro

1. Activate the virtual environment (if you created one):

   ```powershell
   .\.venv\Scripts\activate
   ```

2. Run the script:

   ```powershell
   python app.py
   ```

3. First-time Setup:

   - On first run, you'll be prompted to choose your preferred start and stop keys
   - These settings will be saved for future use

4. Using the Macro:
   - Make sure your game window is in focus (clicked) before starting the macro
   - Use your configured keys to start and stop the macro
   - Press 'K' to change key bindings at any time (while macro is not running)
   - Use Ctrl+C to exit the program

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
