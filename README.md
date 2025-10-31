# MacroManager

A customizable macro tool designed for automating repetitive actions in games, with a focus on user-friendly interface and configuration. This tool features a modern graphical user interface for easy macro management and configuration.

![MacroManager Interface](https://cdn.ssx.si/u/bnRDeH.png)

## Features

- Modern graphical user interface (GUI)
- Multiple macro support with easy selection
- Detailed macro descriptions and status monitoring

- Customizable start/stop keys
- Clean and informative console interface
- Persistent key bindings configuration
- Real-time status display
- Ability to change key bindings on the fly

## Installation

### Prerequisites

- Windows OS (required for game window interaction)
- Python 3.11 or higher ([Download from python.org](https://www.python.org/downloads/))
  - During installation, check "Add Python to PATH"

### Quick Start (Recommended)

1. Download the repository from [GitHub](https://github.com/panteLx/MacroManager/)
2. Double-click `start_macro.bat`
3. That's it! The script will handle everything automatically

### Manual Installation

If you prefer to set up manually or the quick start doesn't work:

1. **Get the Code**

   ```powershell
   # Either clone the repository
   git clone https://github.com/panteLx/MacroManager.git
   cd MacroManager

   # Or download and extract the ZIP from GitHub
   ```

2. **Set Up Environment**

   ```powershell
   # Create and activate virtual environment
   python -m venv .venv
   .\.venv\Scripts\activate

   # Install dependencies
   pip install -r requirements.txt
   ```

## Usage

1. **Launch the Application**

   ```powershell
   python app.py
   ```

2. **First-Time Setup**

   - On first run, you'll be prompted to set up your hotkeys
   - Choose your preferred START and STOP keys
   - These settings will be saved for future use

3. **Using MacroManager**
   - Make sure your game is running and visible
   - Select a macro from the dropdown menu
   - Read the description to understand what it does
   - Use the buttons or hotkeys to control the macro
   - Monitor the status in real-time
   - Press 'K' or use the button to change key bindings

## Adding New Macros

You can easily add new macros by editing the `macros.py` file:

1. Create a new class inheriting from `Macro`
2. Implement the required methods
3. Add your macro to the `AVAILABLE_MACROS` dictionary

Example:

```python
class MyNewMacro(Macro):
    def __init__(self):
        super().__init__(
            "My Custom Macro",
            "Description of what this macro does"
        )

    def run(self, game_window: Any, running: Any) -> None:
        while running.is_set():
            try:
                # Your macro logic here
                pass
            except Exception as e:
                print(f"Error in macro sequence: {e}")
                time.sleep(1)

# Add to available macros
AVAILABLE_MACROS["my_macro"] = MyNewMacro()
```

### 2. Daily Usage

1. Start the Macro:

   ```powershell
   # Navigate to project folder
   cd path\to\MacroManager

   # Activate virtual environment
   .\.venv\Scripts\activate

   # Run the script
   python app.py
   ```

2. Using the Macro:

   - Make sure your game window is open and visible
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

- Make sure to stop the macro before changing key bindings
- Your key bindings are saved in `macro_config.json` and will be loaded automatically on subsequent runs
- The script must be run with sufficient permissions to send input to the game

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
