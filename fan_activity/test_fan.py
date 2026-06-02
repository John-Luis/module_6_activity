# test_fan.py
import time
import sys
from fan_class import fan


def simulate_fan_rotation(fan_obj, fan_label):
    """Simulates a spinning fan blade in the terminal based on its speed state."""
    print(f"\n[!] ACCESSING CORES FOR {fan_label.upper()}...")
    time.sleep(0.3)

    # Determine rotational animation speed based on fan speed configuration
    if not fan_obj.get_on():
        print(f"[○] STATUS: STATIONARY (POWER OFF)")
        return

    speed_level = fan_obj.get_speed()
    if speed_level == fan.SLOW:
        delay = 0.2
        speed_text = "LOW VELOCITY"
    elif speed_level == fan.MEDIUM:
        delay = 0.1
        speed_text = "BALANCED VELOCITY"
    else:
        delay = 0.03
        speed_text = "MAXIMUM ROTATIONAL VELOCITY"

    print(f"[▶] ENGINE ENGAGED // MODE: {speed_text}")