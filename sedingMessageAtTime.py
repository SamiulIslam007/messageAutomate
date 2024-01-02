import schedule
import time
import pyautogui
import sys
from datetime import datetime

def send_whatsapp_message():
    # Replace this with your code to send the message via WhatsApp
    # Specify the line to be typed
    line_to_type = "Tmi onk besi sundor ree."
    # Type the line
    pyautogui.typewrite(line_to_type)

    # Press Enter
    pyautogui.press('enter')
    sys.exit()

# Set the time for sending the message (4:00 AM)
# If we need to send any parameters in send_whatsapp_message function, we can just uss a comma and then write the perameter of the function.
schedule.every().day.at("01:41").do(send_whatsapp_message)

while True:
    schedule.run_pending()
    time.sleep(1)