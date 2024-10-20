import ctypes
import time
import winsound
import win32gui
import win32api
import win32con

# Function to make a beep sound
def beep():
    winsound.Beep(1000, 200)  # Frequency: 1000 Hz, Duration: 200 ms

# Function to get the window under the mouse cursor
def get_window_under_cursor():
    pt = win32api.GetCursorPos()  # Get the cursor position (x, y)
    hwnd = win32gui.WindowFromPoint(pt)  # Get the window handle from the cursor position
    if hwnd:
        # Retrieve the window's title
        window_text = win32gui.GetWindowText(hwnd)
        if window_text:
            return hwnd, window_text
    return None, None

# Function to monitor the mouse hover over open windows
def monitor_hover():
    last_window = None
    while True:
        hwnd, window_text = get_window_under_cursor()
        if hwnd and hwnd != last_window:
            print(f"Hovering over window: {window_text}")
            last_window = hwnd
            beep()
        time.sleep(0.1)  # Sleep for a short while to reduce CPU usage

if __name__ == "__main__":
    monitor_hover()
