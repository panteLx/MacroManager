import time
import sys
from threading import Thread
import keyboard
import win32gui
from os import system
from direct_keys import DIK_W, DIK_S, DIK_SPACE, hold_key, press_key, release_key

def find_game_window():
    def callback(hwnd, windows):
        if win32gui.IsWindowVisible(hwnd):
            title = win32gui.GetWindowText(hwnd).lower()
            # Add more possible window titles if needed
            if any(x in title for x in ["battlefield", "bf2042"]):
                windows.append(hwnd)
        return True
    
    windows = []
    win32gui.EnumWindows(callback, windows)
    return windows[0] if windows else None

def focus_game_window(hwnd):
    """Focus the game window and return the previously focused window"""
    if not hwnd or not win32gui.IsWindow(hwnd):
        return None
        
    # Store the current focused window
    previous_window = win32gui.GetForegroundWindow()
    
    # Only focus if we're not already focused
    if previous_window != hwnd:
        win32gui.SetForegroundWindow(hwnd)
        time.sleep(0.1)  # Small delay to ensure focus is set
        
    return previous_window

def restore_window_focus(hwnd):
    """Restore focus to a specific window"""
    if hwnd and win32gui.IsWindow(hwnd):
        win32gui.SetForegroundWindow(hwnd)
        time.sleep(0.05)  # Small delay to ensure focus is restored

def send_key_to_window(hwnd, key, duration=None):
    if not hwnd or not win32gui.IsWindow(hwnd):
        return

    # Map keys to DirectInput scan codes
    key_map = {
        'w': DIK_W,
        's': DIK_S,
        'space': DIK_SPACE
    }
    
    scan_code = key_map.get(key.lower())
    if not scan_code:
        return

    # Make sure game window is focused
    if win32gui.GetForegroundWindow() != hwnd:
        win32gui.SetForegroundWindow(hwnd)
        time.sleep(0.1)  # Small delay to ensure focus is set

    # Send input
    if duration:
        hold_key(scan_code, duration)
    else:
        press_key(scan_code)
        time.sleep(0.1)
        release_key(scan_code)
    
    time.sleep(0.1)  # Small delay between key presses

def macro_sequence(game_window, running):
    while running.is_set():
        try:
            if not win32gui.IsWindow(game_window):
                print("Game window no longer exists! Stopping macro...")
                running.clear()
                return

            # Press W for 7 seconds
            print("Pressing W for 7 seconds")
            send_key_to_window(game_window, 'w', 7)
            if not running.is_set(): return
            print("Released W")
            
            # Press space 4 times with 30 second intervals
            for i in range(4):
                if not running.is_set(): return
                print(f"Pressing Space ({i+1}/4)")
                send_key_to_window(game_window, 'space')
                print("Released Space")
                time.sleep(3)
            
            # Press S for 7 seconds
            if not running.is_set(): return
            print("Pressing S for 7 seconds")
            send_key_to_window(game_window, 's', 7)
            if not running.is_set(): return
            print("Released S")
            
            # Press space 4 more times with 30 second intervals
            for i in range(4):
                if not running.is_set(): return
                print(f"Pressing Space ({i+1}/4)")
                send_key_to_window(game_window, 'space')
                print("Released Space")
                time.sleep(3)
        except Exception as e:
            print(f"Error in macro sequence: {e}")
            time.sleep(1)

def clear_screen():
    if sys.platform == 'win32':
        _ = system('cls')
    else:
        _ = system('clear')

def print_status(title, status_text, start_key, stop_key, show_focus_warning=False):
    clear_screen()
    print("=" * 50)
    print(f"{title:^50}")
    print("=" * 50)
    print(f"\nStatus: {status_text}")
    
    if show_focus_warning:
        print("\n" + "!" * 50)
        print("IMPORTANT: Make sure the game window is in focus (clicked)")
        print("before starting the macro for the first time!")
        print("!" * 50)
    
    print(f"\nControls:")
    print(f"  Start Macro: {start_key}")
    print(f"  Stop Macro:  {stop_key}")
    print(f"  Change Keys: Press 'K'")
    print(f"  Exit:        Press Ctrl+C")
    print("\n" + "=" * 50)

def get_key_binding(prompt):
    print(f"\n{prompt}")
    print("Press any key (except ESC)...")
    event = keyboard.read_event(suppress=True)
    while event.event_type != 'down':
        event = keyboard.read_event(suppress=True)
    return event.name

def main():
    from threading import Event
    from os import system
    import json
    import os

    # Load or create key bindings
    config_file = 'macro_config.json'
    if os.path.exists(config_file):
        with open(config_file, 'r') as f:
            key_bindings = json.load(f)
    else:
        clear_screen()
        print("First-time setup: Configure your macro keys\n")
        start_key = get_key_binding("Choose the key to START the macro")
        stop_key = get_key_binding("Choose the key to STOP the macro")
        key_bindings = {'start_key': start_key, 'stop_key': stop_key}
        with open(config_file, 'w') as f:
            json.dump(key_bindings, f)

    print("Looking for game window...")
    game_window = find_game_window()
    
    if not game_window:
        print("Game window not found! Please make sure Battlefield is running.")
        sys.exit(1)
        
    window_title = win32gui.GetWindowText(game_window)
    macro_thread = None
    running = Event()
    macro_status = "Idle"
    
    first_start = True
    def start_macro():
        nonlocal macro_thread, macro_status, first_start
        if macro_thread is None or not macro_thread.is_alive():
            macro_status = "Running"
            running.set()
            macro_thread = Thread(target=macro_sequence, args=(game_window, running))
            macro_thread.daemon = True
            macro_thread.start()
            print_status(window_title, macro_status, key_bindings['start_key'], key_bindings['stop_key'], show_focus_warning=first_start)
            first_start = False
    
    def stop_macro():
        nonlocal macro_status
        macro_status = "Stopped"
        running.clear()
        print_status(window_title, macro_status, key_bindings['start_key'], key_bindings['stop_key'], show_focus_warning=False)
    
    def change_keys():
        nonlocal key_bindings
        if running.is_set():
            print("\nPlease stop the macro before changing keys!")
            time.sleep(2)
            return

        clear_screen()
        print("Changing key bindings...\n")
        start_key = get_key_binding("Choose the new START key")
        stop_key = get_key_binding("Choose the new STOP key")
        
        # Remove old bindings
        keyboard.unhook_all()
        
        # Update bindings
        key_bindings = {'start_key': start_key, 'stop_key': stop_key}
        with open(config_file, 'w') as f:
            json.dump(key_bindings, f)
            
        # Set new bindings
        keyboard.on_press_key(key_bindings['start_key'], lambda _: start_macro())
        keyboard.on_press_key(key_bindings['stop_key'], lambda _: stop_macro())
        keyboard.on_press_key('k', lambda _: change_keys())
        
        print_status(window_title, macro_status, key_bindings['start_key'], key_bindings['stop_key'], show_focus_warning=False)

    # Set initial key bindings
    keyboard.on_press_key(key_bindings['start_key'], lambda _: start_macro())
    keyboard.on_press_key(key_bindings['stop_key'], lambda _: stop_macro())
    keyboard.on_press_key('k', lambda _: change_keys())
    
    # Show initial UI
    print_status(window_title, macro_status, key_bindings['start_key'], key_bindings['stop_key'], show_focus_warning=True)
    
    # Keep the main thread alive
    while True:
        time.sleep(0.1)

if __name__ == "__main__":
    main()
