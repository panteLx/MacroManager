from typing import Dict, Any
import time
from direct_keys import DIK_W, DIK_S, DIK_SPACE
from window_utils import send_key_to_window

class Macro:
    def __init__(self, name: str, description: str):
        self.name = name
        self.description = description

    def run(self, game_window: Any, running: Any) -> None:
        raise NotImplementedError("Each macro must implement run()")

class BF6SiegeCairoMacro(Macro):
    def __init__(self):
        super().__init__(
            "Battlefield 6 Siege of Cairo AFK",
            "Siege of Cairo AFK Macro for Battlefield 6 that automates capturing objectives. Portal Code: YVNDS"
        )

    def run(self, game_window: Any, running: Any) -> None:
        while running.is_set():
            try:
                # Press W for 15.70 seconds
                print("Pressing W for 15.70 seconds")
                send_key_to_window(game_window, 'w', 15.70)
                if not running.is_set(): return
                print("Released W")
                
                # Sleep for 120 seconds
                if not running.is_set(): return
                print("Sleeping for 120 seconds")
                time.sleep(120)
                
                # Press space and sleep twice
                for i in range(2):
                    if not running.is_set(): return
                    print(f"Pressing Space ({i+1}/2)")
                    send_key_to_window(game_window, 'space')
                    print("Released Space")
                    print("Sleeping for 120 seconds")
                    time.sleep(120)
                
                # Sleep for 30 seconds
                if not running.is_set(): return
                print("Sleeping for 30 seconds")
                time.sleep(30)
                
                # Press S for 16.11 seconds
                if not running.is_set(): return
                print("Pressing S for 16.11 seconds")
                send_key_to_window(game_window, 's', 16.11)
                if not running.is_set(): return
                print("Released S")
                
                # Sleep for 120 seconds
                if not running.is_set(): return
                print("Sleeping for 120 seconds")
                time.sleep(120)
                
                # Press space and sleep twice
                for i in range(2):
                    if not running.is_set(): return
                    print(f"Pressing Space ({i+1}/2)")
                    send_key_to_window(game_window, 'space')
                    print("Released Space")
                    print("Sleeping for 120 seconds")
                    time.sleep(120)
                
                # Final 30 second sleep
                if not running.is_set(): return
                print("Sleeping for 30 seconds")
                time.sleep(30)
                
            except Exception as e:
                print(f"Error in BF6SiegeCairoMacro: {e}")
                time.sleep(1)


class BF6LibPeakMacro(Macro):
    def __init__(self):
        super().__init__(
            "Battlefield 6 Liberation Peak AFK",
            "Liberation Peak AFK Macro for Battlefield 6 that automates capturing objectives. Portal Code: YWVXU"
        )

    def run(self, game_window: Any, running: Any) -> None:
        while running.is_set():
            try:
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
                    time.sleep(30)
                
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
                    time.sleep(30)
            except Exception as e:
                print(f"Error in BF6LibPeakMacro: {e}")
                time.sleep(1)

# Add more macro classes here...

# Dictionary of all available macros
AVAILABLE_MACROS: Dict[str, Macro] = {
    "bf6_lib_peak": BF6LibPeakMacro(),
    "bf6_siege_cairo": BF6SiegeCairoMacro(),
    # Add more macros here...
}
