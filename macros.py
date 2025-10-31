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

class BF6LibPeakMacro(Macro):
    def __init__(self):
        super().__init__(
            "Battlefield 6 Liberation Peak AFK",
            "Liberation Peak AFK Macro for Battlefield 6 that automates capturing objectives."
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
                print(f"Error in macro sequence: {e}")
                time.sleep(1)

# Add more macro classes here...

# Dictionary of all available macros
AVAILABLE_MACROS: Dict[str, Macro] = {
    "bf6_lib_peak": BF6LibPeakMacro(),
    # Add more macros here...
}
