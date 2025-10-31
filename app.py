import time
import sys
from threading import Thread, Event
import keyboard
import win32gui
from os import system
import json
import os
import tkinter as tk
from tkinter import ttk, messagebox
from window_utils import find_game_window
from macros import AVAILABLE_MACROS

def clear_screen():
    if sys.platform == 'win32':
        _ = system('cls')
    else:
        _ = system('clear')

def get_key_binding(prompt):
    print(f"\n{prompt}")
    print("Press any key (except ESC)...")
    event = keyboard.read_event(suppress=True)
    while event.event_type != 'down':
        event = keyboard.read_event(suppress=True)
    return event.name

class MacroUI:
    def __init__(self, root):
        self.root = root
        self.root.title("MacroManager")
        self.root.geometry("600x700")
        
        # Configure root window to be resizable
        self.root.resizable(True, True)
        self.root.minsize(500, 600)
        
        # Configure grid weights
        self.root.grid_rowconfigure(0, weight=1)
        self.root.grid_columnconfigure(0, weight=1)
        
        # Initialize variables
        self.macro_thread = None
        self.running = Event()
        self.game_window = None
        self.current_macro = None
        
        # Load key bindings
        self.load_key_bindings()
        
        # Create UI elements
        self.create_widgets()
        
        # Set key bindings
        self.set_key_bindings()
        
    def load_key_bindings(self):
        config_file = 'macro_config.json'
        if os.path.exists(config_file):
            with open(config_file, 'r') as f:
                self.key_bindings = json.load(f)
        else:
            clear_screen()
            print("First-time setup: Configure your macro keys\n")
            start_key = get_key_binding("Choose the key to START the macro")
            stop_key = get_key_binding("Choose the key to STOP the macro")
            self.key_bindings = {'start_key': start_key, 'stop_key': stop_key}
            with open(config_file, 'w') as f:
                json.dump(self.key_bindings, f)
    
    def create_widgets(self):
        # Create main frame
        main_frame = ttk.Frame(self.root, padding="20")
        main_frame.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))
        
        # Configure main frame grid
        main_frame.grid_columnconfigure(0, weight=1)
        
        # Create title
        title_label = ttk.Label(main_frame, text="MacroManager", font=('Helvetica', 16, 'bold'))
        title_label.grid(row=0, column=0, columnspan=2, pady=(0, 20))
        
        # Macro selection
        ttk.Label(main_frame, text="Select Macro:", font=('Helvetica', 10, 'bold')).grid(row=1, column=0, sticky=tk.W, pady=5)
        self.macro_combo = ttk.Combobox(main_frame, width=50, font=('Helvetica', 10))
        self.macro_combo['values'] = [macro.name for macro in AVAILABLE_MACROS.values()]
        self.macro_combo.grid(row=2, column=0, columnspan=2, sticky=(tk.W, tk.E), pady=5, padx=5)
        if self.macro_combo['values']:
            self.macro_combo.current(0)
        
        # Description
        ttk.Label(main_frame, text="Description:", font=('Helvetica', 10, 'bold')).grid(row=3, column=0, sticky=tk.W, pady=5)
        self.description_text = tk.Text(main_frame, height=6, wrap=tk.WORD, font=('Helvetica', 10))
        self.description_text.grid(row=4, column=0, columnspan=2, sticky=(tk.W, tk.E), pady=5, padx=5)
        self.description_text.config(state=tk.DISABLED)
        
        # Status frame
        status_frame = ttk.LabelFrame(main_frame, text="Status", padding="10")
        status_frame.grid(row=5, column=0, columnspan=2, sticky=(tk.W, tk.E), pady=10, padx=5)
        status_frame.grid_columnconfigure(1, weight=1)
        
        ttk.Label(status_frame, text="Current State:", font=('Helvetica', 10)).grid(row=0, column=0, sticky=tk.W, padx=5)
        self.status_label = ttk.Label(status_frame, text="Idle", font=('Helvetica', 10, 'bold'))
        self.status_label.grid(row=0, column=1, sticky=tk.W, padx=5)
        
        ttk.Label(status_frame, text="Game Window:", font=('Helvetica', 10)).grid(row=1, column=0, sticky=tk.W, padx=5)
        self.window_label = ttk.Label(status_frame, text="Not detected", font=('Helvetica', 10))
        self.window_label.grid(row=1, column=1, sticky=tk.W, padx=5)
        
        # Key bindings
        keys_frame = ttk.LabelFrame(main_frame, text="Controls", padding="10")
        keys_frame.grid(row=6, column=0, columnspan=2, sticky=(tk.W, tk.E), pady=10, padx=5)
        keys_frame.grid_columnconfigure(0, weight=1)
        
        # Add key binding labels with proper padding
        key_style = {'font': ('Helvetica', 10)}
        ttk.Label(keys_frame, text=f"Start Macro: {self.key_bindings['start_key']}", **key_style).grid(row=0, column=0, sticky=tk.W, padx=5, pady=2)
        ttk.Label(keys_frame, text=f"Stop Macro: {self.key_bindings['stop_key']}", **key_style).grid(row=1, column=0, sticky=tk.W, padx=5, pady=2)
        ttk.Label(keys_frame, text="Change Keys: K", **key_style).grid(row=2, column=0, sticky=tk.W, padx=5, pady=2)
        
        # Buttons
        button_frame = ttk.Frame(main_frame)
        button_frame.grid(row=7, column=0, columnspan=2, pady=20)
        button_frame.grid_columnconfigure((0, 1, 2), weight=1)
        
        # Style the buttons
        button_style = {'width': 15}
        start_btn = ttk.Button(button_frame, text="Start", command=self.start_macro, **button_style)
        stop_btn = ttk.Button(button_frame, text="Stop", command=self.stop_macro, **button_style)
        change_btn = ttk.Button(button_frame, text="Change Keys", command=self.change_keys, **button_style)
        
        # Add padding and layout
        start_btn.grid(row=0, column=0, padx=10)
        stop_btn.grid(row=0, column=1, padx=10)
        change_btn.grid(row=0, column=2, padx=10)
        
        # Add footer
        footer_frame = ttk.Frame(main_frame)
        footer_frame.grid(row=8, column=0, columnspan=2, sticky=(tk.W, tk.E), pady=(20, 0))
        footer_frame.grid_columnconfigure(0, weight=1)
        
        # Developer credit
        dev_label = ttk.Label(footer_frame, text="Developed by panteLx", font=('Helvetica', 9))
        dev_label.grid(row=0, column=0, sticky=(tk.W, tk.E))
        
        # Copyright notice
        copyright_label = ttk.Label(footer_frame, text="© 2025 MacroManager - MIT License", font=('Helvetica', 8))
        copyright_label.grid(row=1, column=0, sticky=(tk.W, tk.E), pady=(2, 0))
        
        # Configure text alignment to center for both labels
        dev_label.configure(anchor="center")
        copyright_label.configure(anchor="center")
        
        # Bind macro selection change
        self.macro_combo.bind('<<ComboboxSelected>>', self.update_description)
        self.update_description(None)
    
    def update_description(self, event):
        selected_name = self.macro_combo.get()
        selected_macro = next((m for m in AVAILABLE_MACROS.values() if m.name == selected_name), None)
        
        self.description_text.config(state=tk.NORMAL)
        self.description_text.delete(1.0, tk.END)
        if selected_macro:
            self.description_text.insert(tk.END, selected_macro.description)
        self.description_text.config(state=tk.DISABLED)
    
    def set_key_bindings(self):
        keyboard.on_press_key(self.key_bindings['start_key'], lambda _: self.start_macro())
        keyboard.on_press_key(self.key_bindings['stop_key'], lambda _: self.stop_macro())
        keyboard.on_press_key('k', lambda _: self.change_keys())
    
    def start_macro(self):
        if self.macro_thread and self.macro_thread.is_alive():
            return
            
        if not self.game_window:
            self.game_window = find_game_window()
            if not self.game_window:
                messagebox.showerror("Error", "Game window not found! Please make sure Battlefield is running.")
                self.window_label.config(text="Not detected")
                return
            else:
                window_title = win32gui.GetWindowText(self.game_window)
                self.window_label.config(text=window_title)
        
        selected_name = self.macro_combo.get()
        self.current_macro = next((m for m in AVAILABLE_MACROS.values() if m.name == selected_name), None)
        
        if not self.current_macro:
            messagebox.showerror("Error", "Please select a macro first!")
            return
        
        self.running.set()
        self.macro_thread = Thread(target=self.current_macro.run, args=(self.game_window, self.running))
        self.macro_thread.daemon = True
        self.macro_thread.start()
        self.status_label.config(text="Running")
    
    def stop_macro(self):
        self.running.clear()
        self.status_label.config(text="Stopped")
        if not self.game_window or not win32gui.IsWindow(self.game_window):
            self.game_window = None
            self.window_label.config(text="Not detected")
    
    def change_keys(self):
        if self.running.is_set():
            messagebox.showwarning("Warning", "Please stop the macro before changing keys!")
            return
        
        self.root.withdraw()  # Hide the main window
        clear_screen()
        print("Changing key bindings...\n")
        start_key = get_key_binding("Choose the new START key")
        stop_key = get_key_binding("Choose the new STOP key")
        
        # Remove old bindings
        keyboard.unhook_all()
        
        # Update bindings
        self.key_bindings = {'start_key': start_key, 'stop_key': stop_key}
        with open('macro_config.json', 'w') as f:
            json.dump(self.key_bindings, f)
        
        # Set new bindings
        self.set_key_bindings()
        
        # Update UI
        self.root.deiconify()  # Show the main window again
        self.create_widgets()  # Recreate widgets to update key binding display

def main():
    root = tk.Tk()
    app = MacroUI(root)
    root.mainloop()

if __name__ == "__main__":
    main()
